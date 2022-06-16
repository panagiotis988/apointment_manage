
import tkinter as tk
import picklel_helper as picklel_helper
from Helpers.EMAIL_ERROR import *

class EMAIL_advance_confi_UI(tk.Frame):
    def __init__(self, parent, controller):
        #self.EMAIL_advance_confi = EMAIL_advance_confi()
##arxikopoihsi tou tk frame gia to advance_email
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="white")
        controller.config(bg='white', highlightcolor='#DAE3F3', highlightthickness=8)

        self.label = tk.Label(self, text="Ρύθμισης Email για προχωρημένους",height=3, width=44, font=("Lucida", "16", "bold"), fg='#335BA3', bg='white')

        self.save_but = tk.Button(self, text="Αποθήκευση", height=1, width=30, font=("Lucida", "10", "bold"),
                              fg='white', bg='#335BA3', command= lambda: EMAIL_advance_confi_UI.save_value(self))

        self.EMAIL_CONFI_but = tk.Button(self, text="Επιστροφή στις Ρυθμίσεις Email",height=1, width=30, font=("Lucida", "10", "bold"),
                                fg='white', bg='#335BA3', command= lambda: controller.show_frame("EMAIL_CONFI")) #todo


        self.smtp_link_frame = tk.Frame(self, bg='white')
        self.smtp_link_label = tk.Label(self.smtp_link_frame, text="link", width=15,
                                font=("Lucida", "10", "bold"), fg='#335BA3', bg='white')
        self.smtp_link = tk.Entry(self.smtp_link_frame, bd =5, width=100, fg = "black")

        self.smtp_port_tls_frame = tk.Frame(self, bg='white')
        self.smtp_port_tls_label =tk.Label(self.smtp_port_tls_frame, text="port tls", width=15,
                                    font=("Lucida", "10", "bold"), fg='#335BA3', bg='white')
        self.smtp_port_tls = tk.Entry(self.smtp_port_tls_frame, bd =5,  width=100,fg = "black")

        self.email_adr_frame = tk.Frame(self, bg='white')
        self.email_adr_label = tk.Label(self.email_adr_frame, text="address mail", width=15,
                                font=("Lucida", "10", "bold"), fg='#335BA3', bg='white')
        self.email_adr = tk.Entry(self.email_adr_frame, bd =5, width=100, fg = "black")

        self.email_password_frame = tk.Frame(self, bg='white')
        self.email_password_label = tk.Label(self.email_password_frame, text="password", width=15,
                                    font=("Lucida", "10", "bold"), fg='#335BA3', bg='white')
        self.email_password = tk.Entry(self.email_password_frame, bd =5, width=100, fg = "black")

        self.success = tk.Label(self, bg='white')



        #framepack
        self.save_but.pack(padx=10,pady=10)
        self.EMAIL_CONFI_but.pack( padx=10,pady=10)

        self.label.pack(padx=10,pady=5)
        self.smtp_link_frame.pack(padx=10,pady=5)
        self.smtp_port_tls_frame.pack(padx=10,pady=5)
        self.email_adr_frame.pack(padx=10,pady=5)
        self.email_password_frame.pack(padx=10,pady=5)

        #pack

        self.smtp_link_label.pack(side = "left", padx=10)
        self.smtp_link.pack(side = "right")

        self.smtp_port_tls_label.pack(side = "left", padx=10)
        self.smtp_port_tls.pack(side = "right")

        self.email_adr_label.pack(side = "left", padx=10)
        self.email_adr.pack(side = "right")

        self.email_password_label.pack(side = "left", padx=10)
        self.email_password.pack(side = "right")

        self.success.pack(padx=10,pady=10)

        self.load_mail_confi()



    def load_mail_confi(self):
        #fortosi stoixion tou pickle kai dimiourgia ean den iparxei to arxeo pickle email_state.pkl, 8etei kai to state tou email_state se False molis emfanisti to frame dioti ean den patisei save
        #sto Appointment Managment opos anoi3eis to programa na paei sto Appointment Managment Configurator gia na ri8misi to eimail

        smtp_link, smtp_port_tls, email_adr, email_password= picklel_helper.picklel_helper.load_mail_confi()
        self.smtp_link.insert(tk.END, smtp_link)
        self.smtp_port_tls.insert(tk.END, smtp_port_tls)
        self.email_adr.insert(tk.END, email_adr)
        self.email_password.insert(tk.END, email_password)



    def save_value(self):
        #den tin ekteli gia kapoio logo
        self.success.config(text = "Σύνδεση με το διακομιστεί", fg = "blue")
        #apo8ikeusei ton stoixoion tou email sto arxeio pickle email_state.pkl kai to eimail_state to 8eti se True
        state = EMAIL_ERROR.login(self.smtp_link.get(), self.smtp_port_tls.get(), self.email_adr.get(), self.email_password.get())
        if state :
            email_state,html_state =picklel_helper.picklel_helper.load_confi()
            email_state = True
            picklel_helper.picklel_helper.save_mail_confi(self.smtp_link.get(), self.smtp_port_tls.get(), self.email_adr.get(), self.email_password.get())
            picklel_helper.picklel_helper.save_confi(email_state,html_state)
            self.success.config(text = "Όλες οι αλλαγές αποθηκευτήκανε με επιτυχία", fg = "green")
        else:
            email_state,html_state =picklel_helper.picklel_helper.load_confi()
            email_state = False
            picklel_helper.picklel_helper.save_confi(email_state,html_state)
            self.success.config(text = "Οι αλλαγές δεν αποθηκεύτηκαν με επιτυχία", fg  = "red")
