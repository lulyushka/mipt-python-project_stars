import tkinter as tk
from tkinter import Toplevel
from classes import sphericalCoordinates
from classes import cartesianCoordinates
import random as rd
import math

def errorWindow (title: str, label: str, text: str, root):
    '''
    Данная функция создает окно ошибки
    args:
        title - название окна ошибки
        label - строка с названием ошибки
        text - строка, поясняющая, в чем ошибка
        root - корень родительского окна
    '''
    new_window = Toplevel(root)
    new_window.title(title)

    label_new = tk.Label(new_window, text=label, font=("Arial", 16))
    label_new.pack(pady=20)

    label_info = tk.Label(new_window, text=text)
    label_info.pack(pady=10)

    back_button = tk.Button(new_window, text="Назад", command=new_window.destroy)
    back_button.pack(pady=25)

    new_window.mainloop()


def startStarGame (n: str, m: str, rad: str, root):

    global rootgame
    rootgame = Toplevel(root)
    rootgame.title("StarGame")
    global diam
    diam = str(2*(int(rad)+50))
    global radi
    radi = rad

    global canvas
    canvas = tk.Canvas(rootgame, width=int(diam), height=int(diam), bg='black')
    canvas.pack()
    canvas.create_rectangle(0, 0, int(diam), int(diam), fill = 'black', outline = '', tag = 'key0')
    canvas.tag_bind("key0", '<Button-1>', lambda event: klick(0))

    back_button = tk.Button(rootgame, text="Назад", command=rootgame.destroy)
    back_button.pack(pady=15)

    global label_new
    label_new = tk.Label(rootgame, text="Кликни, чтобы начать", font=("Arial", 16))
    label_new.pack(pady = 10)

    global attemps
    global score
    score = 0
    attemps = -1

    global label_score
    label_score = tk.Label(rootgame, text=f"Очков: {score} из {attemps}", font=("Arial", 16))
    label_score.pack(pady = 10)

    global alpha0 
    alpha0 = rd.randint(0,360)
    global theta0
    theta0 = rd.uniform(90-float(n), 90-float(m))

    with open("/home/lulyu/ipynb proj/StarlettePr/stars_catalog.txt", "r") as starfile:
        for star in starfile:
            starlist = list(map(float, star.split()))
            starlist[1] = 90 - starlist[1]
            cords = starCoordinates(starlist, alpha0, theta0)
            if cords[0] > math.pi/2: continue
            radius = int(rad)*math.degrees(cords[0])/90
            xstar = int(diam)/2 + radius*cords[1]
            ystar = int(diam)/2.1 - radius*cords[2]
            rad_star = starlist[2]/2 * int(rad)/450
            canvas.create_oval(xstar - rad_star, ystar - rad_star, xstar + rad_star, ystar + rad_star, fill='white', outline='', tag = 'key1')
            canvas.tag_bind("key1", '<Button-1>', lambda event: klick(0))

    rootgame.mainloop()  


def klick(score_up):

    global label_new
    global label_score
    label_new.destroy()
    label_score.destroy()

    global score
    global attemps

    score += score_up
    attemps += 1
    with open("/home/lulyu/ipynb proj/StarlettePr/Stardict.txt", "r") as keyfile:
        breaker = 0
        all_keys = keyfile.readlines()
        while breaker == 0:
            num = rd.randint(0, len(all_keys)-1)
            key_str_list = list(all_keys[num].split())
            keylist = list(map(float, key_str_list[1:]))
            cords = starCoordinates(keylist, alpha0, theta0)
            if cords[0] > 8*math.pi/18: continue
            else: breaker +=1
            radius = int(radi)*math.degrees(cords[0])/90
            xstar = int(diam)/2 + radius*cords[1]
            ystar = int(diam)/2.1 - radius*cords[2]
            rad_star = keylist[2]/2 * int(radi)/450

            canvas.create_oval(xstar - rad_star, ystar - rad_star, xstar + rad_star, ystar + rad_star, fill='white', outline='', tag = 'key3')
            canvas.tag_bind("key3", '<Button-1>', lambda event: klick(1))

            label_new = tk.Label(rootgame, text="Найди звезду "+key_str_list[0], font=("Arial", 16))
            label_new.pack(pady = 10)

            label_score = tk.Label(rootgame, text=f"Очков: {score} из {attemps}", font=("Arial", 16))
            label_score.pack(pady = 10)
 

def starCoordinates(star: list, alpha0: float, theta0: float):
    spher_coords0 = sphericalCoordinates([star[0], star[1]])
    cart_list = spher_coords0.toCartesian()
    cart_coords = cartesianCoordinates(cart_list)
    cart_coords.spinZ(alpha0)
    cart_coords.spinY(theta0)
    return cart_coords.toSpherical()