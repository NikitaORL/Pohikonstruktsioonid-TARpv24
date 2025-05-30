import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

DB = 'movies4.db'
FIELDS = [
    ("Pealkiri", tk.Entry),
    ("Režissöör", ttk.Combobox, "directors"),
    ("Aasta", tk.Entry),
    ("Žanr", ttk.Combobox, "genres"),
    ("Kestus", tk.Entry),
    ("Reiting", tk.Entry),
    ("Keel", ttk.Combobox, "languages"),
    ("Riik", ttk.Combobox, "countries"),
    ("Kirjeldus", tk.Entry)
]


def db(query, params=(), fetch=False, script=False):
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        if script:
            cursor.executescript(query)
        else:
            cursor.execute(query, params)
            return cursor.fetchall() if fetch else None


def create_tables():
    db("""
    CREATE TABLE IF NOT EXISTS languages (id INTEGER PRIMARY KEY, name TEXT UNIQUE NOT NULL);
    CREATE TABLE IF NOT EXISTS countries (id INTEGER PRIMARY KEY, name TEXT UNIQUE NOT NULL);
    CREATE TABLE IF NOT EXISTS genres (id INTEGER PRIMARY KEY, name TEXT UNIQUE NOT NULL);
    CREATE TABLE IF NOT EXISTS directors (id INTEGER PRIMARY KEY, name TEXT UNIQUE NOT NULL);
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        director_id INTEGER,
        release_year INTEGER,
        genre_id INTEGER,
        duration INTEGER,
        rating REAL,
        language_id INTEGER,
        country_id INTEGER,
        description TEXT,
        FOREIGN KEY (director_id) REFERENCES directors(id),
        FOREIGN KEY (genre_id) REFERENCES genres(id),
        FOREIGN KEY (language_id) REFERENCES languages(id),
        FOREIGN KEY (country_id) REFERENCES countries(id)
    );
    """, script=True)


def get_values(table):
    return [x[0] for x in db(f"SELECT name FROM {table} ORDER BY name", fetch=True)]


def get_id(table, name):
    row = db(f"SELECT id FROM {table} WHERE name=?", (name,), fetch=True)
    return row[0][0] if row else None


def insert_value(table, name):
    db(f"INSERT OR IGNORE INTO {table} (name) VALUES (?)", (name,))


def refresh_tree(search=None):
    for row in tree.get_children():
        tree.delete(row)
    q = """
    SELECT m.id, m.title, d.name, m.release_year, g.name, m.duration,
           m.rating, l.name, c.name, m.description
    FROM movies m
    LEFT JOIN directors d ON m.director_id = d.id
    LEFT JOIN genres g ON m.genre_id = g.id
    LEFT JOIN languages l ON m.language_id = l.id
    LEFT JOIN countries c ON m.country_id = c.id
    """
    if search:
        q += " WHERE m.title LIKE ?"
        rows = db(q, (f"%{search}%",), fetch=True)
    else:
        rows = db(q, fetch=True)
    for r in rows:
        tree.insert('', 'end', values=r)


def add_edit_window(movie=None):
    win = tk.Toplevel(root)
    win.title("Muuda filmi" if movie else "Lisa film")
    widgets = {}

    for i, (label, widget_type, *tbl) in enumerate(FIELDS):
        tk.Label(win, text=label).grid(row=i, column=0, sticky='e')
        w = widget_type(win)
        w.grid(row=i, column=1, sticky='we')
        widgets[label] = w

        if widget_type == ttk.Combobox:
            table = tbl[0]
            w['values'] = get_values(table)
            w['state'] = 'readonly'
            btn = tk.Button(win, text='+', width=2, command=lambda t=table, c=w: add_to_dict(t, c))
            btn.grid(row=i, column=2)

    if movie:
        for idx, (label, _, *tbl) in enumerate(FIELDS):
            val = movie[idx + 1]
            widgets[label].insert(0, val) if isinstance(widgets[label], tk.Entry) else widgets[label].set(val or "")

    def save():
        values = {}
        for label, widget in widgets.items():
            values[label] = widget.get().strip()
        if not values['Pealkiri']:
            return messagebox.showerror("Viga", "Pealkiri on kohustuslik!")
        try:
            year = int(values['Aasta']) if values['Aasta'] else None
            duration = int(values['Kestus']) if values['Kestus'] else None
            rating = float(values['Reiting']) if values['Reiting'] else None
        except ValueError:
            return messagebox.showerror("Viga", "Aasta, kestus ja reiting peavad olema arvud")

        data = (
            values['Pealkiri'],
            get_id("directors", values['Režissöör']),
            year,
            get_id("genres", values['Žanr']),
            duration,
            rating,
            get_id("languages", values['Keel']),
            get_id("countries", values['Riik']),
            values['Kirjeldus']
        )
        if movie:
            db("""
            UPDATE movies SET title=?, director_id=?, release_year=?, genre_id=?,
            duration=?, rating=?, language_id=?, country_id=?, description=? WHERE id=?
            """, data + (movie[0],))
        else:
            db("""
            INSERT INTO movies (title, director_id, release_year, genre_id, duration,
                                rating, language_id, country_id, description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, data)
        win.destroy()
        refresh_tree()

    tk.Button(win, text="Salvesta", command=save).grid(row=len(FIELDS), column=0, columnspan=3, pady=10)


def add_to_dict(table, combo):
    win = tk.Toplevel(root)
    win.title(f"Lisa {table}")
    tk.Label(win, text=f"Uus {table[:-1]}").pack()
    e = tk.Entry(win)
    e.pack(pady=5)
    tk.Button(win, text="Salvesta", command=lambda: save_new_value(e.get(), table, combo, win)).pack(pady=5)


def save_new_value(name, table, combo, win):
    if name:
        insert_value(table, name)
        combo['values'] = get_values(table)
        win.destroy()


def delete_movie():
    sel = tree.selection()
    if not sel:
        return messagebox.showerror("Viga", "Vali film!")
    id_ = tree.item(sel[0])['values'][0]
    if messagebox.askyesno("Kustuta", "Oled kindel?"):
        db("DELETE FROM movies WHERE id=?", (id_,))
        refresh_tree()


def search():
    refresh_tree(search_var.get().strip())


root = tk.Tk()
root.title("Filmid")

search_var = tk.StringVar()
tk.Frame(root).pack()
tk.Label(root, text="Otsi pealkirja:").pack(side='left')
tk.Entry(root, textvariable=search_var).pack(side='left', fill='x', expand=True)
tk.Button(root, text="Otsi", command=search).pack(side='left')
tk.Button(root, text="Kõik", command=refresh_tree).pack(side='left')

frame = tk.Frame(root)
frame.pack(pady=5)
tk.Button(frame, text="Lisa", command=lambda: add_edit_window()).pack(side='left')
tk.Button(frame, text="Muuda", command=lambda: add_edit_window(tree.item(tree.selection()[0])['values']) if tree.selection() else messagebox.showerror("Viga", "Vali film")).pack(side='left')
tk.Button(frame, text="Kustuta", command=delete_movie).pack(side='left')

cols = ["id"] + [f[0] for f in FIELDS]
tree = ttk.Treeview(root, columns=cols, show='headings')
for c in cols:
    tree.heading(c, text=c)
    tree.column(c, width=100)
tree.column("Pealkiri", width=200)
tree.column("Kirjeldus", width=250)
tree.pack(fill='both', expand=True)

create_tables()
refresh_tree()
root.mainloop()
