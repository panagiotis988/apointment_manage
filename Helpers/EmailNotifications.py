import codecs
import os
import smtplib
from smtplib import *
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import picklel_helper as picklel_helper
from Helpers.EMAIL_ERROR import *
"""
tropopihsi apo github gia na dexete smtp_link, smtp_port_tls, email_adr, email_password
gia na iparxei i dinatotita alagis tou email
"""
#to do import pickle,mailtest


class EmailNotifications:
    @staticmethod
    def sendEmail(appointments, subject, template):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        email_state, html_state=picklel_helper.picklel_helper.load_confi()
        if html_state :
            try:
                with open("templates/In_use/EmailNotification.html",'r', encoding="utf-8") as file:
                    template = os.path.join(base_path, "templates/In_use/" + template + ".html")
            except:
                template = os.path.join(base_path, "templates/" + template + ".html")
                html_state = False
                picklel_helper.picklel_helper.save_confi(email_state, html_state)
                error = "html not found "
                Email_Error_log. general_mail_error(error)
        else:
            template = os.path.join(base_path, "templates/" + template + ".html")
        smtp_link, smtp_port_tls, email_adr, email_password=picklel_helper.picklel_helper.load_mail_confi()

        state = False
        for appointment in appointments:

            msg = MIMEMultipart()
            msg['From'] = email_adr
            msg['To'] = appointment[10]
            msg['Subject'] = subject

            html_file = codecs.open(template, "r", "utf-8")

            html_format = html_file.read().format(first_name=appointment[6], last_name=appointment[7],
                                                  date=appointment[2], start_time=appointment[3], mail = email_adr)

            html_content = MIMEText(html_format, 'html')
            msg.attach(html_content)
            try:
                with smtplib.SMTP(smtp_link, smtp_port_tls) as smtp:
                    try:
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.login(email_adr, email_password)
                        try:
                            smtp.send_message(msg)
                            smtp.quit()

                        except SMTPResponseException as e:
                            error_list = [e.smtp_code, e.smtp_error]
                            #customer_info [first_name, last_name, date tou ranteuou, start_time tou ranteuou, mail tou pelati, tilefono tou pelati]
                            customer_info = [appointment[6], appointment[7],appointment[2], appointment[3], appointment[10], appointment[8]]
                            state=Email_Error_log.current_error_log(state, customer_info,error_list)
                            smtp.quit()

                    except SMTPResponseException as e:
                        #login prob
                        error_list = [e.smtp_code, e.smtp_error]
                        email_state, html_state =picklel_helper.picklel_helper.load_confi()
                        email_state = False
                        picklel_helper.picklel_helper.save_confi(email_state, html_state)
                        state=Email_Error_log.error_login_log(error_list,state)
                        smtp.quit()
                        break
            except:
                email_state, html_state =picklel_helper.picklel_helper.load_confi()
                email_state = False
                picklel_helper.picklel_helper.save_confi(email_state, html_state)
                error = "Δεν μπόρεσε να επικοινωνήσει με το διακομιστεί\nΔεν στάλθηκε κανένα Email, ελέγξετε της ρύθμισης του Email "
                Email_Error_log. general_mail_error(error)
                state = True

        if state :
            filepath = path.relpath("log/Current_Log.txt")
            Email_Error_log.open_Current_Log(filepath)
