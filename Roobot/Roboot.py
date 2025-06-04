import tkinter as tk
from tkinter import ttk, messagebox
import os
from PIL import Image, ImageTk
import time

BASE_PATH = r"C:\Users\opilane.TTHK\source\repos\TARpv24-EldarAliev\PythonApplication1\assets"

def part_coords(part):
    return {
        "naovorm": (368, 368),
        "brows": (368, 360),
        "nose": (368, 390),
        "mouth": (368, 420),
        "ears": (366, 380),
    }[part]

def get_part_image_path(part, variant_num):
    index = int(variant_num) - 1

    if part == "brows":
        if 0 <= index < len(brows_files):
            return os.path.join(BASE_PATH, "brows", brows_files[index])
    elif part == "nose":
        return os.path.join(BASE_PATH, "nose", f"NOS{variant_num}.png")
    elif part == "mouth":
        return os.path.join(BASE_PATH, "mouth", f"ROT{variant_num}.png")
    elif part == "ears":
        if 0 <= index < len(ears_files):
            return os.path.join(BASE_PATH, "ears", ears_files[index])
    return None

def draw_part(part, image_dict, variable, var_check):
    canvas.delete(part)
    if var_check.get():
        if part == "naovorm":
            path = os.path.join(BASE_PATH, "base", "conor.jpg")
        else:
            path = get_part_image_path(part, variable.get())

        if path and os.path.exists(path):
            pil_image = Image.open(path)
            image = ImageTk.PhotoImage(pil_image)
            images[part] = image
            x, y = part_coords(part)
            canvas.create_image(x, y, image=image, tags=part)

def update_all():
    canvas.delete("all")
    draw_part("naovorm", images, None, naovorm_check)
    draw_part("brows", images, brows_var, brows_check)
    draw_part("nose", images, nose_var, nose_check)
    draw_part("mouth", images, mouth_var, mouth_check)
    draw_part("ears", images, ears_var, ears_check)

def save_robot():
    data = []
    for part, check_var, combo_var in [
        ("brows", brows_check, brows_var),
        ("nose", nose_check, nose_var),
        ("mouth", mouth_check, mouth_var),
        ("ears", ears_check, ears_var),
    ]:
        if check_var.get():
            data.append(f"{part}:{combo_var.get()}")
    with open("fotorobotid.txt", "a") as f:
        f.write(",".join(data) + "\n")

    save_image_composite()
    messagebox.showinfo("Сохранено", "Фоторобот сохранён и изображение экспортировано!")

def save_image_composite():
    final_img = Image.new("RGBA", (736, 736), (0, 0, 0, 0))
    parts_order = ["naovorm", "ears", "brows", "nose", "mouth"]

    for part in parts_order:
        var_check = {
            "naovorm": naovorm_check,
            "brows": brows_check,
            "nose": nose_check,
            "mouth": mouth_check,
            "ears": ears_check,
        }[part]
        var_value = {
            "naovorm": None,
            "brows": brows_var,
            "nose": nose_var,
            "mouth": mouth_var,
            "ears": ears_var,
        }[part]

        if var_check.get():
            if part == "naovorm":
                path = os.path.join(BASE_PATH, "base", "conor.jpg")
            else:
                path = get_part_image_path(part, var_value.get())

            if path and os.path.exists(path):
                part_img = Image.open(path).convert("RGBA")
                x, y = part_coords(part)
                paste_x = x - part_img.width // 2
                paste_y = y - part_img.height // 2
                final_img.paste(part_img, (paste_x, paste_y), part_img)

    save_dir = os.path.join(BASE_PATH, "saves")
    os.makedirs(save_dir, exist_ok=True)
    filename = f"photofit_{int(time.time())}.png"
    save_path = os.path.join(save_dir, filename)
    final_img.save(save_path)
    print(f"Сохранено изображение: {save_path}")

def load_last_robot():
    try:
        with open("fotorobotid.txt", "r") as f:
            lines = f.readlines()
        if not lines:
            raise FileNotFoundError
        last = lines[-1].strip().split(",")

        for var in [brows_check, nose_check, mouth_check, ears_check]:
            var.set(False)
        for var in [brows_var, nose_var, mouth_var, ears_var]:
            var.set("1")

        for part_data in last:
            part, variant = part_data.split(":")
            if part == "brows":
                brows_check.set(True)
                brows_var.set(variant)
            elif part == "nose":
                nose_check.set(True)
                nose_var.set(variant)
            elif part == "mouth":
                mouth_check.set(True)
                mouth_var.set(variant)
            elif part == "ears":
                ears_check.set(True)
                ears_var.set(variant)
        update_all()
    except FileNotFoundError:
        messagebox.showwarning("Внимание", "Файл с фотороботами не найден!")

# === GUI ===

root = tk.Tk()
root.title("Фоторобот")
root.configure(bg="black")

left = tk.Frame(root, bg="black")
left.pack(side="left", padx=10, pady=10)

right = tk.Frame(root, bg="black")
right.pack(side="right", padx=10, pady=10)

canvas = tk.Canvas(right, width=736, height=736, bg="black", highlightthickness=0)
canvas.pack()

images = {}

# Переменные
naovorm_check = tk.BooleanVar(value=True)
brows_check = tk.BooleanVar(value=True)
nose_check = tk.BooleanVar(value=True)
mouth_check = tk.BooleanVar(value=True)
ears_check = tk.BooleanVar(value=True)

brows_var = tk.StringVar()
nose_var = tk.StringVar(value="1")
mouth_var = tk.StringVar(value="1")
ears_var = tk.StringVar()

# Файлы
brows_files = ["BROVI1.png", "BROVI2.png", "BROVI3.png", "BROVI4.png"]
ears_files = ["YSHI.png", "YSHI2.png", "YSH13.png", "YSHI4.png"]

def add_selector_numeric(label_text, check_var, combo_var, max_val):
    tk.Checkbutton(left, text=label_text, variable=check_var, command=update_all,
                   bg="black", fg="lightgreen", selectcolor="black").pack(anchor="w")
    tk.Label(left, text=f"{label_text} (номер):", bg="black", fg="lightgreen").pack(anchor="w")
    combo = ttk.Combobox(left, textvariable=combo_var, values=[str(i) for i in range(1, max_val + 1)], width=10)
    combo.bind("<<ComboboxSelected>>", lambda e: update_all())
    combo.pack(anchor="w", pady=(0, 5))

add_selector_numeric("Брови", brows_check, brows_var, len(brows_files))
add_selector_numeric("Нос", nose_check, nose_var, 4)
add_selector_numeric("Рот", mouth_check, mouth_var, 4)
add_selector_numeric("Уши", ears_check, ears_var, len(ears_files))

brows_var.set("1")
ears_var.set("1")

def style_button(btn):
    btn.configure(
        bg="#004d00",
        fg="#b3ffb3",
        activebackground="#006600",
        activeforeground="#e6ffe6",
        relief="raised",
        bd=3,
        font=("Arial", 10, "bold")
    )

btn_save = tk.Button(left, text="Сохранить фоторобот", command=save_robot)
style_button(btn_save)
btn_save.pack(pady=5)

btn_load = tk.Button(left, text="Загрузить последний", command=load_last_robot)
style_button(btn_load)
btn_load.pack()

update_all()
root.mainloop()
