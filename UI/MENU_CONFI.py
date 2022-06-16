import tkinter as tk
import picklel_helper as picklel_helper
#to do check state kai emfanisi antistixo minima # alagi sto xroma




class MENU_CONFI(tk.Frame):

    def __init__(self, parent, controller):
        #arxikopoihsi tou tk frame gia to menu
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="white")
        controller.config(bg='white', highlightcolor='#DAE3F3', highlightthickness=8)

        self.label = tk.Label(self, text="Ρυθμίσεις Email και Html",height=3, width=44, font=("Lucida", "16", "bold"), fg='#335BA3', bg='white')

        self.EMAIL_CONFI_frame = tk.LabelFrame(self, bd=2, bg='#335BA3')
        self.EMAIL_CONFI_but = tk.Button(self.EMAIL_CONFI_frame, text="Μενού ρυθμίσεων Email", font=("Lucida", "14", "bold"),
                                  fg='#335BA3', bg='white', height=3, width=44, command= lambda: controller.show_frame("EMAIL_CONFI"))

        self.HTML_CONFI_frame = tk.LabelFrame(self, bd=2, bg='#335BA3')
        self.HTML_CONFI_but = tk.Button(self.HTML_CONFI_frame, text="Μενού ρυθμίσεων Template", font=("Lucida", "14", "bold"),
                                  fg='#335BA3', bg='white', height=3, width=44, command= lambda: controller.show_frame("HTML_CONFI"))

        self.menu_frame = tk.LabelFrame(self, bd=2, bg='#335BA3')
        self.menu_but = tk.Button(self.menu_frame, text="Επιστροφή στο Αρχικό Μενού", font=("Lucida", "14", "bold"),
                                  fg='#335BA3', bg='white', height=3, width=44, command= lambda: controller.show_frame("Menu"))


        self.label_status = tk.Label(self)

        #pack
        self.label.pack()
        self.EMAIL_CONFI_frame.pack(padx=10,pady=10)
        self.EMAIL_CONFI_but.pack(padx=10, pady=10)
        self.HTML_CONFI_frame.pack(padx=10, pady=10)
        self.HTML_CONFI_but.pack(padx=10, pady=10)
        self.menu_frame.pack(padx=10,pady=10)
        self.menu_but.pack(padx=10, pady=10)
        self.label_status.pack(padx=10,pady=10)

        MENU_CONFI.show_fr(self)





    def show_fr(self):
        smtp_link, smtp_port_tls, email_adr, email_password= picklel_helper.picklel_helper.load_mail_confi()
        email_state,html_state =picklel_helper.picklel_helper.load_confi()

        if email_state == True  and email_adr == "apointmentmanager@yahoo.com" and html_state == True:
            self.label_status.config(text= "Χρησιμοποιείτε το προ-εγκαταστημένο Email (apointmentmanager@yahoo.com)",bg = "white", fg = "red")
        elif email_state == True and html_state == False and email_adr == "apointmentmanager@yahoo.com":
            self.label_status.config(text= "Default Email (apointmentmanager@yahoo.com) και το Default template είναι σε χρήση",bg = "white", fg = "red")
        elif email_state == True and html_state == False:
            self.label_status.config(text= "Το Default template είναι σε χρήση",bg = "white", fg = "orange")
        elif email_state == True and html_state == True:
            self.label_status.config(text= "Όλα είναι ρυθμισμένα", bg='white', fg = "green")
        else :
            self.label_status.config(text= "Δεν ήταν δυνατή η σύνδεση στο Email, το Default template είναι σε χρήση ",bg = "white", fg = "red")
        self.after(5000, self.show_fr)
