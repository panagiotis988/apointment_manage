import tkinter as tk
import pickle
from tkinter import ttk
#to do import



class EMAIL_CONFI(tk.Frame):
##arxikopoihsi tou tk frame gia to email
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="white")
        controller.config(bg='white', highlightcolor='#DAE3F3', highlightthickness=8)

        self.label = tk.Label(self, text="Ρυθμίσης Email",height=3, width=44, font=("Lucida", "16", "bold"), fg='#335BA3', bg='white')

        self.EMAIL_simple_confi_frame = tk.LabelFrame(self, bd=2, bg='#335BA3')
        self.EMAIL_simple_confi_but = tk.Button(self.EMAIL_simple_confi_frame, text="Απλή ρύθμισή Email", font=("Lucida", "14", "bold"),
                                  fg='#335BA3', bg='white', height=3, width=44, command= lambda: controller.show_frame("EMAIL_simple_confi"))

        self.EMAIL_advance_confi_frame = tk.LabelFrame(self, bd=2, bg='#335BA3')
        self.EMAIL_advance_confi_but = tk.Button(self.EMAIL_advance_confi_frame, text="Ρύθμισης Email για προχωρημένους", font=("Lucida", "14", "bold"),
                                  fg='#335BA3', bg='white', height=3, width=44, command= lambda: controller.show_frame("EMAIL_advance_confi"))

        self.return_to_menu_confi_frame = tk.LabelFrame(self, bd=2, bg='#335BA3')
        self.return_to_menu_confi_but = tk.Button(self.return_to_menu_confi_frame, text="Επιστροφή στις Ρυθμίσεις Email και Html", font=("Lucida", "14", "bold"),
                                  fg='#335BA3', bg='white', height=3, width=44, command= lambda: controller.show_frame("MENU_CONFI"))



        #pack
        self.label.pack()
        self.EMAIL_simple_confi_frame.pack(padx=10,pady=10)
        self.EMAIL_simple_confi_but.pack(padx=10, pady=10)
        self.EMAIL_advance_confi_frame.pack(padx=10, pady=10)
        self.EMAIL_advance_confi_but.pack(padx=10, pady=10)
        self.return_to_menu_confi_frame.pack(padx=10,pady=10)
        self.return_to_menu_confi_but.pack(padx=10, pady=10)
