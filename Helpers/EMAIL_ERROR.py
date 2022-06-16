import smtplib
from smtplib import *
from os import path
import webbrowser
from datetime import*
#create  directory
class EMAIL_ERROR:


    def login(smtp_link = "", smtp_port_tls = "", email_adr = "", email_password= ""):
        #sunartisi pou dokimazei me ta stoixia tou email ean mporei na epikoinonisi me to diakomisti
        state = False
        try:
            with smtplib.SMTP(smtp_link, smtp_port_tls) as smtp:
                try:
                    smtp.ehlo()
                    smtp.starttls()

                    smtp.login(email_adr, email_password)
                    smtp.quit()
                    state = True
                    return(state)
                except SMTPResponseException as e:
                    error_code = e.smtp_code
                    error_message = e.smtp_error
                    error_list = [error_code,error_message]
                    Email_Error_log.error_login_log(error_list)
                    smtp.quit()
                    return(state)
        except:
            txt = "Δεν μπόρεσε να επικοινωνήσει με το διακομιστή "

            Email_Error_log.general_mail_error(txt)

class Email_Error_log:
    #kalsi pou dimiourgi log gia problimata pou sxetizonte me ta email

    def error_message_template(text, date_time):
        #template gia ta log
        txt = f"""
{date_time}
------------------------------------------------------------
{text}
------------------------------------------------------------

            """
        return(txt)

    def current_error_log(state, customer_info, error_list):
        #sti lista exei ta akolou8a dedomena customer_info [first_name, last_name, date tou ranteuou, start_time tou ranteuou, mail tou pelati, tilefono tou pelati]
        #error_list= [smtp code , smtp_error]
        now = datetime.now()
        date_time= now.strftime("%d/%m/%Y %H:%M:%S")
        filepath = path.relpath("log/Current_Log.txt")
        txt = f"""
    Το email υπενθυμίσεις του  tou {customer_info[0]} {customer_info[1]}  και έχει ραντεβού στις  {customer_info[2]}, ώρα {customer_info[3]}
    δεν μπόρεσε να σταλθεί στο {customer_info[4]}
    Επικοινωνήστε με το πελάτη στο τηλέφωνο: {customer_info[5]}
    Κωδικός σφάλματος SMTP: {error_list[0]}
    {error_list[1]}
    """
        txt = Email_Error_log.error_message_template(txt, date_time)
        if state == True:
            with open(filepath,"r", encoding="utf-8") as j:
                file_txt = j.read()

            with open(filepath,"w", encoding="utf-8") as j:
                j.write(file_txt+txt)
            Email_Error_log.all_error_log(txt,"log/All_Log.txt")
            return(state)

        if state == False:
            with open(filepath,"w", encoding="utf-8") as j:
                j.write(txt)
            Email_Error_log.all_error_log(txt,"log/All_Log.txt")
            state=True
            return(state)


    def all_error_log(txt,traget_path):
        #ta genika log tou programatos opiodipote log dimiourgite iparxei kai sto log/All_Log.txt kai einai ta3inomimeno se apo to pio prosfato sto pio palio
        filepath = path.relpath(traget_path)
        if traget_path == "log/All_Log.txt":
            try:
                with open(filepath,"r", encoding="utf-8") as j:
                    file_txt = j.read()
                with open(filepath,"w", encoding="utf-8") as j:
                    j.write(txt+file_txt)

            except IOError:
                with open(filepath,"w", encoding="utf-8") as j:
                    j.write(txt)
            return()
        if traget_path == "log/Current_Log.txt":
            with open(filepath,"w", encoding="utf-8") as j:
                j.write(txt)
            return()

    def error_login_log(error_list,state = False):
        now = datetime.now()
        date_time= now.strftime("%d/%m/%Y %H:%M:%S")
        txt =f"Κωδικός σφάλματος SMTP: {error_list[0]} \n{error_list[1]}"

        txt = Email_Error_log.error_message_template(txt, date_time)

        filepath = path.relpath("log/Current_Log.txt")

        if state == True:
            with open(filepath,"r", encoding="utf-8") as j:
                file_txt = j.read()

            with open(filepath,"w", encoding="utf-8") as j:
                j.write(file_txt+txt)
            Email_Error_log.all_error_log(txt,"log/All_Log.txt")
            return(state)

        if state == False:
            with open(filepath,"w", encoding="utf-8") as j:
                j.write(txt)
            Email_Error_log.all_error_log(txt,"log/All_Log.txt")
            state=True
            return(state)


    def open_Current_Log(filepath):
        #sinartisi pou anoigi ta torina log (log/Current_Log.txt)
        try:
            webbrowser.open(filepath)
        except:
            return()

    def general_mail_error(*text):
        #gia genika problimata sxetika me ta email dexete ena keimeno kai to pros8eti sta log
        txt=""
        for text_string in text:
            txt+=text_string+"\n"
        now = datetime.now()
        date_time= now.strftime("%d/%m/%Y %H:%M:%S")
        txt = Email_Error_log.error_message_template(txt, date_time)
        Email_Error_log.all_error_log(txt,"log/All_Log.txt")
        Email_Error_log.all_error_log(txt,"log/Current_Log.txt")
