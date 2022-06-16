from Helpers.HTML_SIMPLE_CONFI import *
#alages sto showframe
#alages file path to pickle, backup to prigoumeno html
#dimiourgia path
#first_name=appointment[6], last_name=appointment[7],date=appointment[2], start_time=appointment[3], mail = email_adr

class HTML_SIMPLE_CONFI_UI(tk.Frame):
         # tris  leitouries 8a pros8eso 1) ean epei8imeis na iparxei koumpi open from pou na mporeis na dialegeis opio html 8es, kai ena koumpi na emfanizi to trexon apo8ikeumeno EmailNotification.html
        #2)pros8iki keimenou text sxetka me teis metableites pou einai dinamikes dld pios metablites blepei to kirios programa kai tis antikatasta me imerominia ranteuou ktlp
        #3) otan to email ein keno na bazei automata to email pou ein stis ri8miseis , kai ena koumpi gia na simplironei automata to email
    def __init__(self, parent, controller):
        #arxikopoihsi tou tk frame gia to simple_html
        self.HTML_SIMPLE_CONFI = HTML_SIMPLE_CONFI()
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="white")
        controller.config(bg='white', highlightcolor='#DAE3F3', highlightthickness=8)

        self.label = tk.Label(self, text="Απλή ρύθμισή HTML",height=3, width=44, font=("Lucida", "16", "bold"), fg='#335BA3', bg='white')

        self.save=tk.Button(self, text="Αποθήκευση ",font=("Lucida", "10", "bold"),fg='white', bg='#335BA3',height=1, width=30,
            command = lambda: HTML_SIMPLE_CONFI_UI.save(self, self.txt_edit_title.get(), self.txt_edit_body.get("1.0", tk.END), self.txt_edit_mail.get(), self.txt_edit_link.get()))


        self.loadtemp =tk.Button(self, text="template", font=("Lucida", "10", "bold"),fg='white', bg='#335BA3',height=1, width=30,
                        command = lambda: HTML_SIMPLE_CONFI_UI.load_template(self))

        self.load_default=tk.Button(self, text="default template", font=("Lucida", "10", "bold"),fg='white', bg='#335BA3',height=1, width=30,
                        command = lambda: HTML_SIMPLE_CONFI_UI.load_default_template(self))

        self.test=tk.Button(self, text="test", font=("Lucida", "10", "bold"),fg='white', bg='#335BA3',height=1, width=30,
            command = lambda: self.HTML_SIMPLE_CONFI.open_html(self.txt_edit_title.get(), self.txt_edit_body.get("1.0", tk.END),self.txt_edit_mail.get(), self.txt_edit_link.get()))

        self.HTML_CONFI_but = tk.Button(self, text="Επιστροφή μενού HTML", font=("Lucida", "10", "bold"),fg='white', bg='#335BA3',height=1, width=30,
                                command = lambda: (controller.show_frame("HTML_CONFI") ))

        self.success = tk.Label(self, bg='white')

        #frame tou label_title kai txt_edit_title
        self.label_title_frame = tk.Frame(self, bg='white')
        self.label_title = tk.Label(self.label_title_frame, text="link", width=15,
                                font=("Lucida", "10", "bold"), fg='#335BA3', bg='white')
        self.txt_edit_title = tk.Entry(self.label_title_frame, bd =5, width=100, fg = "black")

        #frame label_mail_frame tou label_mail kai txt_edit_mail
        self.label_mail_frame = tk.Frame(self, bg='white')
        self.label_mail = tk.Label(self.label_mail_frame, text="email", width=15,
                                font=("Lucida", "10", "bold"), fg='#335BA3', bg='white')
        self.txt_edit_mail = tk.Entry(self.label_mail_frame, bd =5, width=100, fg = "black")

        #frame label_link_frame tou label_link kai txt_edit_link
        self.label_link_frame = tk.Frame(self, bg='white')
        self.label_link = tk.Label(self.label_link_frame, text="logo link", width=15,
                                font=("Lucida", "10", "bold"), fg='#335BA3', bg='white')
        self.txt_edit_link = tk.Entry(self.label_link_frame, bd =5, width=100, fg = "black")

        #frame label_body_frame tou label_body kai txt_edit_body
        self.label_body_frame = tk.Frame(self, bg='white')
        self.label_body  = tk.Label(self.label_body_frame, text="body", width=15,
                                font=("Lucida", "10", "bold"), fg='#335BA3', bg='white')
        self.txt_edit_body = tk.Text(self.label_body_frame, wrap=tk.NONE,bd =5)

        #scrolbar pou elengous to textbox orizontia kai ka8eta (anagkasteika prepei na kano import to ttk dioti to tk den exei tetia leitourgia )
        self.yscrollbary = ttk.Scrollbar(self.label_body_frame, orient='vertical', command=self.txt_edit_body.yview)
        self.txt_edit_body['yscrollcommand'] = self.yscrollbary.set

        self.xscrollbary = ttk.Scrollbar(self.label_body_frame, orient='horizontal', command=self.txt_edit_body.xview)
        self.txt_edit_body['xscrollcommand'] = self.xscrollbary.set

        self.frm_buttons = tk.Frame(self, bg='white')
        self.first_name = tk.Button(self.frm_buttons, text="first_name", command=lambda: HTML_SIMPLE_CONFI_UI.insert_txt(self,"{first_name:}"))
        self.last_name = tk.Button(self.frm_buttons, text="last_name", command=lambda: HTML_SIMPLE_CONFI_UI.insert_txt(self,"{last_name:}"))
        self.date = tk.Button(self.frm_buttons, text="date", command=lambda: HTML_SIMPLE_CONFI_UI.insert_txt(self,"{date:}"))
        self.start_time = tk.Button(self.frm_buttons, text="start_time",command=lambda: HTML_SIMPLE_CONFI_UI.insert_txt(self,"{start_time:}"))
        self.mail = tk.Button(self.frm_buttons, text="mail", command=lambda: HTML_SIMPLE_CONFI_UI.insert_txt(self,"{mail}"))


        #framepack
        self.label.pack(pady=10)
        self.save.pack(pady=5)
        self.loadtemp.pack(pady=5)
        self.load_default.pack(pady=5)
        self.test.pack(pady=5)
        self.HTML_CONFI_but.pack(pady=5)
        self.success.pack(pady=5)

        self.label_title_frame.pack(pady=5)
        self.label_mail_frame.pack(pady=5)
        self.label_link_frame.pack(pady=5)
        self.frm_buttons.pack(pady=5)
        self.label_body_frame.pack(pady=5)




#pack


        self.label_title.pack(side = "left", padx=10)
        self.txt_edit_title.pack(side = "right")

        self.label_mail.pack(side = "left", padx=10)
        self.txt_edit_mail.pack(side = "right")

        self.label_link.pack(side = "left", padx=10)
        self.txt_edit_link.pack(side = "right")

        #grid
        self.label_body.grid(row=0, column=0, padx=10)
        self.txt_edit_body.grid(row=0, column=1)
        self.xscrollbary.grid(row=1, column=1,sticky = "nsew")
        self.yscrollbary.grid(row=0, column=2,sticky = "nsew")


        self.first_name.pack(side = "left", padx=10)
        self.last_name.pack(side = "right", padx=10)
        self.date.pack(side = "right", padx=10)
        self.start_time.pack(side = "right", padx=10)
        self.mail.pack(side = "right", padx=10)

    def load_template(self):
        #fortosi tou template sta textbox
        self.clear_text()

        self.title, self.body, self.mail, self.link =self.HTML_SIMPLE_CONFI.load_template()
        self.txt_edit_title.insert(tk.END,self.title)
        self.txt_edit_body.insert(tk.END,self.body)
        self.txt_edit_mail.insert(tk.END,self.mail)
        self.txt_edit_link.insert(tk.END,self.link)


    def load_default_template(self):
        self.HTML_SIMPLE_CONFI.load_default_template()
        self.clear_text()

    def insert_txt(self,text):
        #eisagogi gia tin automati eisagogi dedomenon kata tin apostoli tou email
        self.txt_edit_body.insert(tk.END,f" {text} ")

    def clear_text(self):
        #ka8arismos ton textbox tou frame
        self.txt_edit_title.delete(0, tk.END)
        self.txt_edit_body.delete("1.0", tk.END)
        self.txt_edit_mail.delete(0, tk.END)
        self.txt_edit_link.delete(0, tk.END)

    def save(self,txt_edit_title, txt_edit_body, txt_edit_mail, txt_edit_link):
        #apo8ikeush tou html
        if txt_edit_title != "" and txt_edit_body != "" and txt_edit_mail != "" :
            self.HTML_SIMPLE_CONFI.create_html(txt_edit_title, txt_edit_body, txt_edit_mail, txt_edit_link)
            self.success.config(text = "Το Template αποθηκεύτηκε με επιτυχία", fg = "green")
        else:
            self.success.config(text = "Το Template δεν αποθηκεύτηκε με επιτυχία", fg = "red")
