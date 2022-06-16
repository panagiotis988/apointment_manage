import tkinter as tk
from tkinter import ttk
import webbrowser
import picklel_helper as picklel_helper
from os import path
from Helpers.EMAIL_ERROR import *
from tkinter.filedialog import askopenfilename
from datetime import*


class HTML_ADVANCE_CONFI():
    #2 leitouries 8a pros8eso 1) ean epei8imeis na iparxei koumpi open from pou na mporeis na dialegeis opio html 8es, kai ena koumpi na emfanizi to trexon apo8ikeumeno EmailNotification.html
    #pros8iki keimenou text sxetka me teis metableites pou einai dinamikes dld pios metablites blepei to kirios programa kai tis antikatasta me imerominia ranteuou ktlp

    def pickle_html():

        email_state,html_state =picklel_helper.picklel_helper.load_confi()
        html_state = True
        picklel_helper.picklel_helper.save_confi(email_state,html_state)

    def open_html(text):
        #dimiourgia enos temp.html gia na dokimaseis ean o kodikas html leitourgi opos 8eleis
        filepath = path.relpath("templates/temp.html")
        try:
            with open(filepath,"w", encoding="utf-8") as j:
                j.write(text)
            webbrowser.open(filepath)
        except IOError:
            print("html adv error not tested")

    def open_file():
            #template apo ton panagioti
        smtp_link, smtp_port_tls, email_adr, email_password= picklel_helper.picklel_helper.load_mail_confi()
        with open("templates/EmailNotification.html",'r', encoding="utf-8") as file:
            text = file.read()
        return(text)

    def open_file_path():
    #Open a file for editing

        filepath = askopenfilename(
            filetypes=[('html files', '*.html'),("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return("","")
        with open(filepath, mode="r", encoding="utf-8") as input_file:
            text = input_file.read()
        return(text,filepath)

    def open_file_in_use():
        try:
            with open("templates/In_use/EmailNotification.html",'r', encoding="utf-8") as file:
                text = file.read()
            return(text,"templates/In_use/EmailNotification.html")
        except:
            return("","")



    def save_file(text):#apo8ikeusi arxeiou se path , kai backup toi prigoumeno me datetime

        email_state,html_state =picklel_helper.picklel_helper.load_confi()
        if html_state:
            try:
                with open("templates/In_use/EmailNotification.html",'r', encoding="utf-8") as file:
                    old_file = file.read()
                now = datetime.now()
                date_time= now.strftime("%d_%m_%Y_%H-%M-%S")
                print(date_time)
                filepath = f"templates/backup/EmailNotification_Backup_{date_time}.html"
                filepath = path.relpath(filepath)
                with open(filepath,"w",encoding="utf-8") as backup:
                    backup.write(old_file)

            except:
                picklel_helper.picklel_helper.start_pickle()
                html_state = False
                picklel_helper.picklel_helper.save_confi(email_state,html_state)
                HTML_ADVANCE_CONFI.save_file(text)

            finally:
                with open("templates/In_use/EmailNotification.html","w",encoding="utf-8") as file:
                    file.write(text)
                    HTML_ADVANCE_CONFI.pickle_html()
        else:
            with open("templates/In_use/EmailNotification.html","w",encoding="utf-8") as file:
                file.write(text)
                HTML_ADVANCE_CONFI.pickle_html()
        return(True)
