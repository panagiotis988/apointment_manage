import tkinter as tk
from tkinter import ttk
import webbrowser
import picklel_helper as picklel_helper
from os import path
from datetime import *


# to do path
class HTML_SIMPLE_CONFI():

    def to_html2(text=""):
        # e3agogi se html

        email_state, html_state = picklel_helper.picklel_helper.load_confi()
        if html_state == True:
            try:
                with open("templates/In_use/EmailNotification.html", 'r', encoding="utf-8") as file:
                    print("open")
                    old_file = file.read()
                now = datetime.now()
                date_time = now.strftime("%d_%m_%Y_%H-%M-%S")
                print(date_time)
                filepath = f"templates/backup/EmailNotification_Backup_{date_time}.html"
                filepath = path.relpath(filepath)
                with open(filepath, "w", encoding="utf-8") as backup:
                    backup.write(old_file)
            except:
                picklel_helper.picklel_helper.start_pickle()
                html_state = False
                picklel_helper.picklel_helper.save_confi(email_state, html_state)
            finally:
                with open("templates/In_use/EmailNotification.html", "w", encoding="utf-8") as file:
                    file.write(text)
                    HTML_SIMPLE_CONFI.pickle_html()
        else:
            with open("templates/In_use/EmailNotification.html", "w", encoding="utf-8") as file:
                file.write(text)
                HTML_SIMPLE_CONFI.pickle_html()

    def html_logo(link=None):
        # dimiourgia antistixou kodika html gia na emfanizei kapia eikona meso apo kopio link pou periexei fotografia
        txt = ""
        if link != "":
            txt = f"""<tr height="100px">
    <td align="center" style="vertical-align:bottom; padding-top: 50px">
        <img style="width: 200px" src="{link}"/>
    </td>
</tr>"""
        return (txt)

    def splt(txt):
        # metatropi to body dld to ka8e enter kirios minima se antistixi grami html
        text = ""
        for a_word in txt.split("\n"):
            text += (2 * "\t") + "<p>" + a_word + "</p>" + "\n"
        return (text)

    def html_contact(mail):
        # mail stoixia epikoinonias
        txt = ""
        if mail != "":
            txt = f"""<tr align="center">
    <td>
        <p>Θέλετε να ακυρώσετε ή να αλλάξετε το ραντεβού σας;</p>
        <a href={mail}> Επικοινωνήστε μαζί μας </a> <p>{mail}</p>
    </td>
</tr>"""
        txt += """</table>
</body>
</html>"""
        if mail == "":
            txt = """<tr align="center">
    <td>
        <p>Θέλετε να ακυρώσετε ή να αλλάξετε το ραντεβού σας;</p>
        <a href={mail}> Επικοινωνήστε μαζί μας </a> <p>{mail}</p>
    </td>
</tr>"""
        txt += """</table>
</body>
</html>"""
        return (txt)

    def html_body(body=""):
        # metatropi to txt se html body dld to kirios minima se html morfi me ti boi8ia tis sinartisis splt
        txt = ""
        if body != "":
            body = HTML_SIMPLE_CONFI.splt(body)
            txt += f"""<tr align="center">
<td>
    {body}
</td>
</tr> """

        return (txt)

    def create_html(self, title, body, mail, link):
        # sinartisi gia dimiourgia EmailNotification.html
        self.txt_part1 = f"""<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> {title} </title>
</head>
<body>
<table class="wrapper" width="375px" align="center" width="100%" border="0" cellspacing="0" cellpadding="0">
        """

        self.txt_logo = HTML_SIMPLE_CONFI.html_logo(link)
        self.txt_body = HTML_SIMPLE_CONFI.html_body(title + "\n" + body)
        self.txt_html_contact = HTML_SIMPLE_CONFI.html_contact(mail)
        HTML_SIMPLE_CONFI.to_html2(self.txt_part1 + self.txt_body + self.txt_logo + self.txt_html_contact)

    def open_html(self, title, body, mail, link):
        # sinartisi gia dimiourgia temp.html kai anoigi sto broswer to arxeio temp
        self.txt_part1 = f"""<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> {title} </title>
</head>
<body>
<table class="wrapper" width="375px" align="center" width="100%" border="0" cellspacing="0" cellpadding="0">
        """
        self.txt_logo = HTML_SIMPLE_CONFI.html_logo(link)
        self.txt_body = HTML_SIMPLE_CONFI.html_body(title + "\n" + body)
        self.txt_html_contact = HTML_SIMPLE_CONFI.html_contact(mail)

        filepath = path.relpath("templates/temp.html")
        text = self.txt_part1 + self.txt_body + self.txt_logo + self.txt_html_contact
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text)
        webbrowser.open(filepath)

    def load_template(self):
        # template tou panagioti i moni diafora ein to Γεια σας {first_name:} {last_name:} den ein se bolt
        smtp_link, smtp_port_tls, email_adr, email_password = picklel_helper.picklel_helper.load_mail_confi()

        self.title = """Υπενθύμιση ραντεβού """
        self.body = """Γεια σας {first_name:} {last_name:}
Αυτό το μήνυμα είναι μία υπενθύμιση για το ραντεβού σας στις {date:}
Η ώρα έναρξης του ραντεβού σας είναι <b>{start_time:}"""

        self.mail = email_adr
        self.link = "https://www.eap.gr/wp-content/uploads/2020/09/logo.png"
        return (self.title, self.body, self.mail, self.link)

    def load_default_template(self):
        self.email_state, self.html_state = picklel_helper.picklel_helper.load_confi()
        self.html_state = False
        picklel_helper.picklel_helper.save_confi(self.email_state, self.html_state)
        filepath = path.relpath("templates/EmailNotification.html")
        webbrowser.open(filepath)

    def pickle_html():
        # alazi ti katastasi tou confi_state tou html se True
        email_state, html_state = picklel_helper.picklel_helper.load_confi()
        html_state = True
        picklel_helper.picklel_helper.save_confi(email_state, html_state)
