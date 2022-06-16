import tkinter as tk
from tkinter import ttk
import webbrowser
import pickle
import UI.HTML_ADVANCE_CONFI_UI as HTML_ADVANCE_CONFI

#to do html select default temp, if html not found messege box asking for default template or configuration


class HTML_CONFI(tk.Frame):

    def __init__(self, parent, controller):
        ##arxikopoihsi tou tk frame gia to html
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="white")
        controller.config(bg='white', highlightcolor='#DAE3F3', highlightthickness=8)

        self.label = tk.Label(self, text="Ρυθμίσης HTML",height=3, width=44, font=("Lucida", "16", "bold"), fg='#335BA3', bg='white')

        self.HTML_SIMPLE_CONFI_frame = tk.LabelFrame(self, bd=2, bg='#335BA3')
        self.HTML_SIMPLE_CONFI_but = tk.Button(self.HTML_SIMPLE_CONFI_frame, text="Απλή ρύθμισή HTML", font=("Lucida", "14", "bold"),
                                  fg='#335BA3', bg='white', height=3, width=44, command= lambda: controller.show_frame("HTML_SIMPLE_CONFI"))

        self.HTML_ADVANCE_CONFI_frame = tk.LabelFrame(self, bd=2, bg='#335BA3')
        self.HTML_ADVANCE_CONFI_but = tk.Button(self.HTML_ADVANCE_CONFI_frame, text="Ρύθμισης Html για προχωρημένους", font=("Lucida", "14", "bold"),
                                  fg='#335BA3', bg='white', height=3, width=44, command= lambda: HTML_ADVANCE_CONFI.HTML_ADVANCE_CONFI_UI.edit(self))

        self.return_to_menu_confi_frame = tk.LabelFrame(self, bd=2, bg='#335BA3')
        self.return_to_menu_confi_but = tk.Button(self.return_to_menu_confi_frame, text="Επιστροφή στις Ρυθμίσεις Email και Html", font=("Lucida", "14", "bold"),
                                  fg='#335BA3', bg='white', height=3, width=44, command= lambda: controller.show_frame("MENU_CONFI"))


        #pack
        self.label.pack()
        self.HTML_SIMPLE_CONFI_frame.pack(padx=10,pady=10)
        self.HTML_SIMPLE_CONFI_but.pack(padx=10, pady=10)
        self.HTML_ADVANCE_CONFI_frame.pack(padx=10, pady=10)
        self.HTML_ADVANCE_CONFI_but.pack(padx=10, pady=10)
        self.return_to_menu_confi_frame.pack(padx=10,pady=10)
        self.return_to_menu_confi_but.pack(padx=10, pady=10)
