import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

DB_NAME = 'movies4.db'

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS languages (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS countries (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS genres (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS directors (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS movies (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    """)
    conn.commit()
    conn.close()

def get_all(table):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, name FROM {table} ORDER BY name")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_value_to_table(table, name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"INSERT OR IGNORE INTO {table} (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_name_by_id(table, id_):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM {table} WHERE id=?", (id_,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else ""

def get_id_by_name(table, name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"SELECT id FROM {table} WHERE name=?", (name,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def load_movies(search=None):
    for item in tree.get_children():
        tree.delete(item)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    query = """
    SELECT
        movies.id,
        movies.title,
        directors.name,
        movies.release_year,
        genres.name,
        movies.duration,
        movies.rating,
        languages.name,
        countries.name,
        movies.description
    FROM movies
    LEFT JOIN directors ON movies.director_id = directors.id
    LEFT JOIN genres ON movies.genre_id = genres.id
    LEFT JOIN languages ON movies.language_id = languages.id
    LEFT JOIN countries ON movies.country_id = countries.id
    """
    params = ()
    if search:
        query += " WHERE movies.title LIKE ?"
        params = (f"%{search}%",)
    cursor.execute(query, params)
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    conn.close()

def add_edit_movie(movie=None):
    form = tk.Toplevel(root)
    form.title("Muuda filmi" if movie else "Lisa uus film")

    labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
    widgets = {}

    # Загрузка всех значений для выпадающих списков
    directors = [x[1] for x in get_all("directors")]
    genres = [x[1] for x in get_all("genres")]
    languages = [x[1] for x in get_all("languages")]
    countries = [x[1] for x in get_all("countries")]

    def open_add_window(table, refresh_func):
        def save_new():
            val = entry.get().strip()
            if val:
                add_value_to_table(table, val)
                refresh_func()
                add_win.destroy()

        add_win = tk.Toplevel(form)
        add_win.title(f"Lisa uus {table[:-1]}")
        tk.Label(add_win, text=f"Uus {table[:-1]}:").pack(padx=10, pady=5)
        entry = tk.Entry(add_win)
        entry.pack(padx=10, pady=5)
        tk.Button(add_win, text="Salvesta", command=save_new).pack(pady=10)

    def refresh_combobox(combo, table):
        vals = [x[1] for x in get_all(table)]
        combo['values'] = vals

    for i, label in enumerate(labels):
        tk.Label(form, text=label).grid(row=i, column=0, sticky='e', padx=5, pady=5)
        if label == "Režissöör":
            combo = ttk.Combobox(form, values=directors, state='readonly')
            combo.grid(row=i, column=1, sticky='we', padx=5, pady=5)
            widgets[label] = combo
            btn = tk.Button(form, text="+", width=2,
                            command=lambda c=combo: [open_add_window("directors", lambda: refresh_combobox(c, "directors"))])
            btn.grid(row=i, column=2, sticky='w')
        elif label == "Žanr":
            combo = ttk.Combobox(form, values=genres, state='readonly')
            combo.grid(row=i, column=1, sticky='we', padx=5, pady=5)
            widgets[label] = combo
            btn = tk.Button(form, text="+", width=2,
                            command=lambda c=combo: [open_add_window("genres", lambda: refresh_combobox(c, "genres"))])
            btn.grid(row=i, column=2, sticky='w')
        elif label == "Keel":
            combo = ttk.Combobox(form, values=languages, state='readonly')
            combo.grid(row=i, column=1, sticky='we', padx=5, pady=5)
            widgets[label] = combo
            btn = tk.Button(form, text="+", width=2,
                            command=lambda c=combo: [open_add_window("languages", lambda: refresh_combobox(c, "languages"))])
            btn.grid(row=i, column=2, sticky='w')
        elif label == "Riik":
            combo = ttk.Combobox(form, values=countries, state='readonly')
            combo.grid(row=i, column=1, sticky='we', padx=5, pady=5)
            widgets[label] = combo
            btn = tk.Button(form, text="+", width=2,
                            command=lambda c=combo: [open_add_window("countries", lambda: refresh_combobox(c, "countries"))])
            btn.grid(row=i, column=2, sticky='w')
        else:
            ent = tk.Entry(form)
            ent.grid(row=i, column=1, sticky='we', padx=5, pady=5)
            widgets[label] = ent

    # Заполнение формы если редактирование
    if movie:
        widgets["Pealkiri"].insert(0, movie[1])
        widgets["Režissöör"].set(movie[2] if movie[2] else "")
        widgets["Aasta"].insert(0, movie[3] if movie[3] else "")
        widgets["Žanr"].set(movie[4] if movie[4] else "")
        widgets["Kestus"].insert(0, movie[5] if movie[5] else "")
        widgets["Reiting"].insert(0, movie[6] if movie[6] else "")
        widgets["Keel"].set(movie[7] if movie[7] else "")
        widgets["Riik"].set(movie[8] if movie[8] else "")
        widgets["Kirjeldus"].insert(0, movie[9] if movie[9] else "")

    def save_movie():
        title = widgets["Pealkiri"].get().strip()
        if not title:
            messagebox.showerror("Viga", "Pealkiri on kohustuslik!")
            return
        director = widgets["Režissöör"].get()
        year = widgets["Aasta"].get()
        genre = widgets["Žanr"].get()
        duration = widgets["Kestus"].get()
        rating = widgets["Reiting"].get()
        language = widgets["Keel"].get()
        country = widgets["Riik"].get()
        description = widgets["Kirjeldus"].get()

        director_id = get_id_by_name("directors", director)
        genre_id = get_id_by_name("genres", genre)
        language_id = get_id_by_name("languages", language)
        country_id = get_id_by_name("countries", country)

        try:
            year = int(year) if year else None
        except ValueError:
            messagebox.showerror("Viga", "Aasta peab olema täisarv")
            return
        try:
            duration = int(duration) if duration else None
        except ValueError:
            messagebox.showerror("Viga", "Kestus peab olema täisarv")
            return
        try:
            rating = float(rating) if rating else None
        except ValueError:
            messagebox.showerror("Viga", "Reiting peab olema arv")
            return

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        if movie:
            cursor.execute("""
                UPDATE movies SET title=?, director_id=?, release_year=?, genre_id=?, duration=?, rating=?, language_id=?, country_id=?, description=?
                WHERE id=?
            """, (title, director_id, year, genre_id, duration, rating, language_id, country_id, description, movie[0]))
        else:
            cursor.execute("""
                INSERT INTO movies (title, director_id, release_year, genre_id, duration, rating, language_id, country_id, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (title, director_id, year, genre_id, duration, rating, language_id, country_id, description))
        conn.commit()
        conn.close()
        load_movies()
        form.destroy()

    tk.Button(form, text="Salvesta", command=save_movie).grid(row=len(labels), column=0, columnspan=3, pady=10)

def delete_selected_movie():
    sel = tree.selection()
    if not sel:
        messagebox.showerror("Viga", "Vali film, mida kustutada!")
        return
    movie_id = tree.item(sel[0])['values'][0]
    if messagebox.askyesno("Kustuta?", "Kas oled kindel?"):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM movies WHERE id=?", (movie_id,))
        conn.commit()
        conn.close()
        load_movies()

def search_movies():
    q = search_var.get().strip()
    if q == "":
        load_movies()
    else:
        load_movies(search=q)

root = tk.Tk()
root.title("Filmi andmete haldamine")

search_var = tk.StringVar()

frame_search = tk.Frame(root)
frame_search.pack(fill='x', padx=10, pady=5)

tk.Label(frame_search, text="Otsi pealkirja:").pack(side='left')
search_entry = tk.Entry(frame_search, textvariable=search_var)
search_entry.pack(side='left', fill='x', expand=True, padx=5)
search_entry.bind("<Return>", lambda e: search_movies())
tk.Button(frame_search, text="Otsi", command=search_movies).pack(side='left', padx=5)
tk.Button(frame_search, text="Näita kõik", command=lambda: load_movies()).pack(side='left', padx=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack(fill='x', padx=10, pady=5)

tk.Button(frame_buttons, text="Lisa uus film", command=lambda: add_edit_movie()).pack(side='left', padx=5)
tk.Button(frame_buttons, text="Muuda valitud", command=lambda: (
    add_edit_movie(tree.item(tree.selection()[0])['values']) if tree.selection() else messagebox.showerror("Viga", "Vali film!"))).pack(side='left', padx=5)
tk.Button(frame_buttons, text="Kustuta valitud", command=delete_selected_movie).pack(side='left', padx=5)

columns = ("id", "Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus")
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor='center')
tree.column("Pealkiri", width=200, anchor='w')
tree.column("Kirjeldus", width=250, anchor='w')
tree.pack(fill='both', expand=True, padx=10, pady=5)

create_tables()
load_movies()

root.mainloop()
