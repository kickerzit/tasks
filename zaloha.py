from tkinter import *

# Okno
window = Tk()
window.title("Tasks")
window.minsize(400, 400)
window.iconbitmap("icon.ico")
window.resizable(False, False)

# Definujeme fonty a barvy
main_font = ("Times New Roman", 12)
main_color = "#432d99"
button_color = "#20164a"
window.config(bg=main_color)

# Funkce
def add_task():
    #přidání úkolu
    list_box.insert(END, user_input.get()) # bacha na zavorky za .get()
    user_input.delete(0, END)

def remove_text_item():
    # odstraní jednu položku seznamu
    list_box.delete(ANCHOR) # ANCHOR: odstranit OZNAČENOU položku

def clear_all_list():
    # odstraní všechny položky ze seznamu
    list_box.delete(0, END)

def save_tasks():
    # uloží úkoly do textového souboru
    with open("tasks.txt", "w") as file:
        my_tasks = list_box.get(0, END)
        for one_task in my_tasks:
            if one_task.endswith("\n"):
                file.write(f"{one_task}")
            else:
                file.write(f"{one_task}\n")

def open_tasks():
    # potřebujeme, aby se to podívalo do tasks.txt, vytáhne to úkoly a napíše je do listboxu
    try:
        with open("tasks.txt", "r") as file: # "r" = read
            for one_line in file:
                list_box.insert(END, one_line)
    except:
        print("Chyba ve funkci na otevírání souboru tasks.txt") 

# Framy
# Pack, grid, place nejdou použít zároveň, proto se okno rozděluje tzv. framy, kde v každém framu si určíme, jaký budeme používat
input_frame = Frame(window, bg=main_color)
text_frame = Frame(window, bg=main_color)
button_frame = Frame(window, bg=main_color)
input_frame.pack()
text_frame.pack()
button_frame.pack()

# Input frame - obsah
user_input = Entry(input_frame, width=30, borderwidth=3, font=main_font)
user_input.grid(row=0, column=0, padx=5, pady=5)
add_button = Button(input_frame, text="Add task", borderwidth=2, font=main_font, bg=button_color, fg="white", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=10)

# Scrollbar
text_scrollbar = Scrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, sticky=N+S) # sticky nám roztáhne scrollbar od severu k jihu

# Text frame - obsah
list_box = Listbox(text_frame, width=45, height=15, font=main_font, borderwidth=3, yscrollcommand=text_scrollbar.set)
list_box.grid(row=0, column=0)
# Propojíme scrollbar s list_box 
text_scrollbar.config(command=list_box.yview)


# Button frame - obsah
remove_button = Button(button_frame, text="Remove task", borderwidth=2, font=main_font, bg=button_color, fg="white", command=remove_text_item)
clear_button = Button(button_frame, text="Clear list", borderwidth=2, font=main_font, bg=button_color, fg="white", command=clear_all_list)
save_button = Button(button_frame, text="Save", borderwidth=2, font=main_font, bg=button_color, fg="white", command=save_tasks)
quit_button = Button(button_frame, text="Quit", borderwidth=2, font=main_font, bg=button_color, fg="white", command=window.destroy)

remove_button.grid(row=0, column=0, padx=4, pady=10)
clear_button.grid(row=0, column=1, padx=4, pady=10)
save_button.grid(row=0, column=2, padx=4, pady=10, ipadx=8)
quit_button.grid(row=0, column=3, padx=4, pady=10, ipadx=8)

# Výuková zóna
# test_label = Label(button_frame, text="testovaci", bg="red", fg="white")
# test_label.grid(row=1, column=0, sticky=W+E) # sticky: světové strany - N, S, E, W

# try:
#     print(x)
# except:
#     print("Byla zjištěna chyba, proměnná x neexistuje")

# Načteme seznam úkolů do listboxu
open_tasks()

# Hlavní cyklus
window.mainloop()