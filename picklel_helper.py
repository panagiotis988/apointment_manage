import pickle
import os
from Helpers.EMAIL_ERROR import *
#to do path tou trexon html se xrisi

#conf_state.pkl exei 2 metablites email_state,html_state einai True otan exoun ri8mistei to email,html
#email_state.pkl exei 4 metablites smtp_link, smtp_port_tls, email_adr, email_password me ta dedomena gia to mail
class picklel_helper:
    def start_pickle():
        smtp_link, smtp_port_tls, email_adr, email_password =picklel_helper.load_mail_confi()
        email_state,html_state=picklel_helper.load_confi()
        picklel_helper.create_directory("","log")
        picklel_helper.create_directory("backup","templates")
        picklel_helper.create_directory("In_use","templates")
        picklel_helper.create_html()
        if email_state == True:
            state = EMAIL_ERROR.login(smtp_link,smtp_port_tls, email_adr, email_password) == False
            if  state:
                email_state = False
                picklel_helper.picklel_helper.save_confi(email_state, html_state)


    def create_directory(directory, parent_dir):
        #sinartisi pou dimiourgi kapio directory
        path = os.path.join(parent_dir, directory)
        try:
            os.makedirs(path)

        except:
            return()

    def load_confi():
        #den ein olokliromenei dimiourgia h elengos tis katastaseis email kai html
        #ean einai False simenei pos den exei ri8misti sosta
        try:
            with open('conf_state.pkl','rb') as file:
                email_state, html_state = pickle.load(file)

            return(email_state,html_state)
        except IOError:
            email_state = True
            html_state = False
            with open('conf_state.pkl','wb') as file:
                pickle.dump([email_state,html_state],file)
            return(email_state,html_state)

    def load_mail_confi():
        # den 8eoro sosto to programa na exei arxiko email alla ean den iparxei to file conf_state.pkl tote eisagei kai arxiko mail

        try:
            with open('email_state.pkl','rb') as file:
                smtp_link, smtp_port_tls, email_adr, email_password=pickle.load(file)
            return(smtp_link, smtp_port_tls, email_adr, email_password)
        except IOError:
            smtp_link = "smtp.mail.yahoo.com"
            smtp_port_tls = "587"
            email_adr="apointmentmanager@yahoo.com"
            email_password = "mihnphgrfwzbebby"

            with open('conf_state.pkl','rb') as file:
                email_state,html_state=pickle.load(file)
                email_state = True

            with open('email_state.pkl','wb') as file:
                pickle.dump([smtp_link, smtp_port_tls, email_adr, email_password],file)

            with open('conf_state.pkl','wb') as file:
                pickle.dump([email_state,html_state],file)
            return(smtp_link, smtp_port_tls, email_adr, email_password)



    def save_confi(email_state = False, html_state = False):
        #apo8ikeusi pickle conf_state.pkl
        with open('conf_state.pkl','wb') as file:
            pickle.dump([email_state,html_state],file)



    def save_mail_confi(smtp_link = "", smtp_port_tls = "", email_adr = "", email_password= ""):
        #apo8ikeusi email_state.pkl
        with open('email_state.pkl','wb') as file:
            pickle.dump([smtp_link, smtp_port_tls, email_adr, email_password],file)

    def create_html():
        txt="""<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> Υπενθύμιση ραντεβού </title>
</head>
<body>
<table class="wrapper" width="375px" align="center" width="100%" border="0" cellspacing="0" cellpadding="0">
    <tr align="center">
        <td>
            <br/>
            <h1>Γεια σας {first_name:} {last_name:}</h1>

            <p>Αυτό το μήνυμα είναι μία υπενθύμιση για το ραντεβού σας στις {date:}</p>
            <br/>

            <p>Η ώρα έναρξης του ραντεβού σας είναι <b>{start_time:}</b></p>
        </td>
    </tr>
    <tr height="100px">
        <td align="center" style="vertical-align:bottom; padding-top: 50px">
            <img style="width: 200px" src="https://www.eap.gr/wp-content/uploads/2020/09/logo.png"/>
        </td>
    </tr>
    <tr align="center">
        <td>
            <p>Θέλετε να ακυρώσετε ή να αλλάξετε το ραντεβού σας;</p>
            <a href="mailto:appointmentmanagerproject@gmail.com"> Επικοινωνήστε μαζί μας </a>
        </td>
    </tr>
</table>
</body>
</html>"""

        try:
            with open("templates/EmailNotification.html",'r', encoding="utf-8") as file:
                html_format = file.read()
                if html_format == txt:
                    return()
                else:
                    with open("templates/EmailNotification.html",'w', encoding="utf-8") as file:
                        file.write(txt)
                    return()

        except IOError:
            with open("templates/EmailNotification.html",'w', encoding="utf-8") as file:
                file.write(txt)
            return()
