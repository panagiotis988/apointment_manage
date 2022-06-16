import tkinter as tk
import picklel_helper as picklel_helper
from tkinter import ttk
from Helpers.EMAIL_ERROR import *
#to do check mail, print error
#add providers
class EMAIL_simple_confi():
    def mail_provider_dict(self):
        #dedomena gia smtp,port apo to paroxo
        #to do epistrofi ton keys gia to self.menu_items
        self.providerdict = {"gmail":["smtp.gmail.com","587"],
                             "yahoo":["smtp.mail.yahoo.com", 587]}
        return(self.providerdict)

    def load_mail_confi(self):
#fortosi stoixion tou pickle kai dimiourgia ean den iparxei to arxeo pickle email_state.pkl, 8etei kai to state tou email_state se False molis emfanisti to frame dioti ean den patisei save
#sto Appointment Managment opos anoi3eis to programa na paei sto Appointment Managment Configurator gia na ri8misi to eimail

        smtp_link, smtp_port_tls, self.pickle_email_adr, self.pickle_email_password = picklel_helper.picklel_helper.load_mail_confi()
        return(self.pickle_email_adr,self.pickle_email_password)
        #self.email_adr.insert(tk.END, self.pickle_email_adr)
        #self.email_password.insert(tk.END, self.pickle_email_password)

    def save_value(self, menu_items,option_get, email_adr, email_password):
        #apo8ikeusei ton stoixoion tou email sto arxeio pickle email_state.pkl kai to eimail_state to 8eti se True

        dict = EMAIL_simple_confi.mail_provider_dict(self)
        smtp_link, smtp_port_tls = dict[option_get]
        self.email_adr=email_adr
        self.email_password =email_password

        self.email_state,self.html_state =picklel_helper.picklel_helper.load_confi()
        self.email_state = True


        if EMAIL_ERROR.login(smtp_link,smtp_port_tls, self.email_adr, self.email_password) :
            picklel_helper.picklel_helper.save_mail_confi(smtp_link, smtp_port_tls, self.email_adr, self.email_password)
            picklel_helper.picklel_helper.save_confi(self.email_state,self.html_state)
            return(True)
        else:
            self.email_state,self.html_state =picklel_helper.picklel_helper.load_confi()
            self.email_state = False
            picklel_helper.picklel_helper.save_confi(self.email_state,self.html_state)
            return(False)
