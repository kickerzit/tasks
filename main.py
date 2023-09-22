from tkinter import *
import customtkinter
customtkinter.set_appearance_mode("dark")

# Okno
window = customtkinter.CTk()
window.title("Tasks")
window.geometry("600x430")
window.iconbitmap("icon.ico")
window.resizable(False, False)

# Definujeme fonty a barvy
main_font = ("Times New Roman", 12)
#main_color = "#432d99"
button_color = "#20164a"

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
input_frame = customtkinter.CTkFrame(window)
text_frame = customtkinter.CTkFrame(window)
button_frame = customtkinter.CTkFrame(window)
input_frame.pack(pady=5)
text_frame.pack(pady=5)
button_frame.pack()

# Input frame - obsah
user_input = customtkinter.CTkEntry(input_frame, width=380, border_width=3, font=main_font)
user_input.grid(row=0, column=0, padx=12, pady=5)
add_button = customtkinter.CTkButton(input_frame, text="Add task", border_width=2, font=main_font, bg_color=button_color, fg_color=button_color, command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=10)

# Scrollbar
text_scrollbar = customtkinter.CTkScrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, sticky="ns") # sticky nám roztáhne scrollbar od severu k jihu

# Text frame - obsah
list_box = Listbox(text_frame, width=85, height=19, font=main_font, yscrollcommand=text_scrollbar.set)
list_box.grid(row=0, column=0, padx = 5, pady = 5)

# Propojíme scrollbar s list_box 
text_scrollbar = customtkinter.CTkScrollbar(text_frame, command=list_box.yview)
text_scrollbar.grid(row=0, column=1, sticky="ns")
# connect textbox scroll event to CTk scrollbar
list_box.configure(yscrollcommand=text_scrollbar.set)

# Button frame - obsah
remove_button = customtkinter.CTkButton(button_frame, text="Remove task", border_width=2, bg_color=button_color, fg_color=button_color, command=remove_text_item)
clear_button = customtkinter.CTkButton(button_frame, text="Clear list", border_width=2, bg_color=button_color, fg_color=button_color, command=clear_all_list)
save_button = customtkinter.CTkButton(button_frame, text="Save", border_width=2, bg_color=button_color, fg_color=button_color, command=save_tasks)
quit_button = customtkinter.CTkButton(button_frame, text="Quit", border_width=2, bg_color=button_color, fg_color=button_color, command=window.destroy)

remove_button.grid(row=1, column=0, padx=1, pady=5)
clear_button.grid(row=1, column=1, padx=1, pady=5)
save_button.grid(row=1, column=2, padx=1, pady=5)
quit_button.grid(row=1, column=3, padx=1, pady=5)

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