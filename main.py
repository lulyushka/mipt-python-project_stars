import tkinter as tk
from classes import Latitude
from tk_functions import errorWindow
from tk_functions import startStarGame


def start_action():
    lat_min = entry_min.get()
    lat_max = entry_max.get()
    rad = radius.get()
    
    latitude_min = Latitude(lat_min)
    latitude_max = Latitude(lat_max)

    if not(latitude_min.check()) or not(latitude_max.check()):
        errorWindow("Ошибка", "Неверно введены данные", "Широта должна быть числом и находиться в диапазоне от -90 до 90", root)
    elif latitude_min.value > latitude_max.value:
        errorWindow("Ошибка", "Неверно введены данные", "Минимальная широка больше максимальной, читай Математика 2 класс", root)
    else:
        startStarGame(latitude_min.value, latitude_max.value, rad, root)


root = tk.Tk()
root.title("Диапазон широт")

label = tk.Label(root, text="Введите диапазон широт", font=("Arial", 16))
label.pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=10)

entry_min = tk.Entry(frame, width=10)
entry_min.grid(row=0, column=0, padx=5)
label_min = tk.Label(frame, text="Минимальная широта")
label_min.grid(row=0, column=1)

entry_max = tk.Entry(frame, width=10)
entry_max.grid(row=1, column=0, padx=5)
label_max = tk.Label(frame, text="Максимальная широта")
label_max.grid(row=1, column=1)

radius = tk.Entry(frame, width=10)
radius.grid(row=2, column=0, padx=5)
label_rad = tk.Label(frame, text="Радиус (рекомендую 400-450)")
label_rad.grid(row=2, column=1)

start_button = tk.Button(root, text="Начать!", command=start_action)
start_button.pack(pady=25)

root.mainloop()