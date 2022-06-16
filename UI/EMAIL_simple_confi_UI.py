from Helpers.EMAIL_simple_confi import *
from Helpers.EMAIL_ERROR import *
#alages sto showframe
#clear ta textbox
class EMAIL_simple_confi_UI(tk.Frame):
    def __init__(self, parent, controller):
        ##arxikopoihsi tou tk frame gia to simple_email
        self.EMAIL_simple_confi = EMAIL_simple_confi()
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="white")
        controller.config(bg='white', highlightcolor='#DAE3F3', highlightthickness=8)

        self.label = tk.Label(self, text="Απλή ρύθμισή Email",height=3, width=44, font=("Lucida", "16", "bold"), fg='#335BA3', bg='white')

        self.save_but = tk.Button(self, text="Αποθήκευση", height=1, width=30, font=("Lucida", "10", "bold"),
                              fg='white', bg='#335BA3', command= lambda:  EMAIL_simple_confi_UI.save(self))

        self.EMAIL_CONFI_but = tk.Button(self, text="Επιστροφή στις Ρυθμίσεις Email",height=1, width=30, font=("Lucida", "10", "bold"),
                                fg='white', bg='#335BA3', command= lambda: EMAIL_simple_confi_UI.reload_and_return(self,self.controller))

        self.email_adr_frame = tk.Frame(self, bg='white')
        self.email_adr_label = tk.Label(self.email_adr_frame, text="address mail", width=15,
                                font=("Lucida", "10", "bold"), fg='#335BA3', bg='white')
        self.email_adr = tk.Entry(self.email_adr_frame, bd =5, width=100, fg = "black")

        self.email_password_frame = tk.Frame(self, bg='white')
        self.email_password_label = tk.Label(self.email_password_frame, text="password", width=15,
                                    font=("Lucida", "10", "bold"), fg='#335BA3', bg='white')
        self.email_password = tk.Entry(self.email_password_frame, bd =5, width=100, fg = "black")

        self.success = tk.Label(self, bg='white')


        self.option_menu_frame = tk.Frame(self, bg='white')
        self.option_menu_label = tk.Label(self.option_menu_frame, text="Διακομιστής", width=15,
                                font=("Lucida", "10", "bold"), fg='#335BA3', bg='white')
        self.menu_items = ["gmail","yahoo"]
        self.option_menu_init = tk.StringVar()
        self.option_menu_init.set(self.menu_items[0])
        self.option_menu = tk.OptionMenu(self.option_menu_frame, self.option_menu_init, *self.menu_items)

        #framepack

        self.save_but.pack(padx=10,pady=10)
        self.EMAIL_CONFI_but.pack( padx=10,pady=10)
        self.label.pack(padx=10,pady=5)
        self.option_menu_frame.pack(padx=10,pady=5)
        self.email_adr_frame.pack(padx=10,pady=5)
        self.email_password_frame.pack(padx=10,pady=5)

        #pack
        self.option_menu_label.pack(side = "left", padx=10)
        self.option_menu.pack(side = "right",padx=265)
        self.email_adr_label.pack(side = "left", padx=10)
        self.email_adr.pack(side = "right")
        self.email_password_label.pack(side = "left", padx=10)
        self.email_password.pack(side = "right")
        self.success.pack(padx=10,pady=10)
#pack


        EMAIL_simple_confi_UI.load_mail(self)


    def load_mail(self):

        self.pickle_email_adr, self.pickle_email_password =self.EMAIL_simple_confi.load_mail_confi()
        self.email_adr.insert(tk.END, self.pickle_email_adr)
        self.email_password.insert(tk.END, self.pickle_email_password)

    def save(self):
        #den tin ekteli gia kapoio logo
        self.success.config(text = "Σύνδεση με το διακομιστεί", fg = "blue")
        #ean to balo apeu8ias stin if dimiourgi bugs
        state = self.EMAIL_simple_confi.save_value(self.menu_items,self.option_menu_init.get(),self.email_adr.get(), self.email_password.get())
        if  state :
            self.success.config(text = "Όλες οι αλλαγές αποθηκευτήκανε με επιτυχία", fg = "green")
        else:
            self.success.config(text = "Οι αλλαγές δεν αποθηκεύτηκαν με επιτυχία", fg = "red")



    def del_rec(self):
            self.email_adr.delete(0, tk.END)
            self.email_password.delete(0, tk.END)

    def reload_and_return(self, controller):
        EMAIL_simple_confi_UI.del_rec(self)
        EMAIL_simple_confi_UI.load_mail(self)

        controller.show_frame("EMAIL_CONFI")
