from Helpers.HTML_ADVANCE_CONFI import *
import tkinter as tk
from tkinter import ttk

#alages file path to pickle, backup to prigoumeno html
#dimiourgia path

class HTML_ADVANCE_CONFI_UI():
#dimiourgia enos toplevel para8iro sto tk gia to html_edit
    def edit(self):
        self.window = tk.Toplevel()
        self.window.title("Html Editor")
        #mege8os para8iro me Tk.rowconfigure kai Tk.columnconfigure
        self.window.rowconfigure(0, minsize=600, weight=1)
        self.window.columnconfigure(1, minsize=1366, weight=1)


        self.frm_buttons_frame = tk.Frame(self.window, relief=tk.RAISED, bd=2) #geniko frame gia ta menu

        #ta button tou frm_buttons_frame_sub1
        self.frm_buttons_frame_sub1=tk.Frame(self.frm_buttons_frame) #frame gia tin automati simplirosi
        self.label_title = tk.Label(self.frm_buttons_frame_sub1, height=3, width=30, text="Αυτόματη εισαγωγή δεδομένων\nκατά τη διάρκεια\nτης αποστολής του Email ")
        self.first_name = tk.Button(self.frm_buttons_frame_sub1,height=1, width=22,  text="Όνομα του πελάτη ", command=lambda: HTML_ADVANCE_CONFI_UI.insert_txt(self,"{first_name:}"))
        self.last_name = tk.Button(self.frm_buttons_frame_sub1, height=1, width=22, text="Επίθετο του πελάτη ", command=lambda: HTML_ADVANCE_CONFI_UI.insert_txt(self,"{last_name:}"))
        self.date = tk.Button(self.frm_buttons_frame_sub1, height=1, width=22, text="Ημερομηνία του ραντεβού ", command=lambda: HTML_ADVANCE_CONFI_UI.insert_txt(self,"{date:}"))
        self.start_time = tk.Button(self.frm_buttons_frame_sub1, height=1, width=22, text="Ώρα του ραντεβού ",command=lambda: HTML_ADVANCE_CONFI_UI.insert_txt(self,"{start_time:}"))
        self.mail = tk.Button(self.frm_buttons_frame_sub1, height=1, width=22, text="Email επικοινωνίας ", command=lambda: HTML_ADVANCE_CONFI_UI.insert_txt(self,"{mail}"))

        #ta button tou frm_buttons_frame_sub2
        self.frm_buttons_frame_sub2=tk.Frame(self.frm_buttons_frame)
        self.label_title2 = tk.Label(self.frm_buttons_frame_sub2, height=2, width=22, text="ΜΕΝΟΥ")
        self.btn_template = tk.Button(self.frm_buttons_frame_sub2, height=1, width=22, text="default template", command=lambda: HTML_ADVANCE_CONFI_UI.open_file(self))
        self.btn_open = tk.Button(self.frm_buttons_frame_sub2, height=1, width=22, text="Άνοιγμα από...", command=lambda: HTML_ADVANCE_CONFI_UI.open_file_from(self))
        self.btn_open_in_use = tk.Button(self.frm_buttons_frame_sub2, height=1, width=22, text="template in use", command=lambda: HTML_ADVANCE_CONFI_UI.open_file_in_use(self))
        self.btn_save = tk.Button(self.frm_buttons_frame_sub2, height=1, width=22, text="Αποθήκευση και επιστροφή ", command=lambda: HTML_ADVANCE_CONFI_UI.save_file(self))
        self.btn_test = tk.Button(self.frm_buttons_frame_sub2, height=1, width=22, text="test", command = lambda: HTML_ADVANCE_CONFI_UI.open_html(self))

        #wrap=tk.NONE einai gia to textbox otan ftanei sto aristero akro na min piganei sti apo kato seira
        self.txt_edit = tk.Text(self.window, wrap=tk.NONE)

        #scrolbar pou elengous to textbox orizontia kai ka8eta (anagkasteika prepei na kano import to ttk dioti to tk den exei tetia leitourgia )
        self.yscrollbary = ttk.Scrollbar(self.window, orient='vertical', command=self.txt_edit.yview)
        self.yscrollbary.grid(row=0, column=2, sticky='nsew')
        self.txt_edit['yscrollcommand'] = self.yscrollbary.set

        self.xscrollbary = ttk.Scrollbar(self.window, orient='horizontal', command=self.txt_edit.xview)
        self.xscrollbary.grid(row=1, column=1, sticky='nsew')
        self.txt_edit['xscrollcommand'] = self.xscrollbary.set

        #main grid tou programatos
        self.frm_buttons_frame.grid(row=0, column=0, sticky="ns")
        self.txt_edit.grid(row=0, column=1, sticky="nsew")

        #framepack ton frm_buttons_frame_sub1,2
        self.frm_buttons_frame_sub1.pack()
        self.frm_buttons_frame_sub2.pack(pady=50)

        #pack tou frm_buttons_frame_sub1
        self.label_title.pack(pady=20)
        self.first_name.pack(pady=5)
        self.last_name.pack(pady=5)
        self.date.pack(pady=5)
        self.start_time.pack(pady=5)
        self.mail.pack(pady=5)

        #pack tou frm_buttons_frame_sub2
        self.label_title2.pack(pady=10)
        self.btn_template.pack(pady=5)
        self.btn_open.pack(pady=5)
        self.btn_open_in_use.pack(pady=5)
        self.btn_save.pack(pady=5)
        self.btn_test.pack(pady=5)






        self.window.mainloop()

    def open_file(self):
        HTML_ADVANCE_CONFI_UI.clear_text(self)
        self.txt_edit.insert(tk.END, HTML_ADVANCE_CONFI.open_file())
        self.window.title("Html Editor - Template")

    def open_file_from(self):

        text,filepath = HTML_ADVANCE_CONFI.open_file_path()
        if text!= "" and filepath!="":
            HTML_ADVANCE_CONFI_UI.clear_text(self)
            self.txt_edit.insert(tk.END, text)
            self.window.title(f"Html Editor - {filepath}")

    def save_file(self):
        if HTML_ADVANCE_CONFI.save_file(self.txt_edit.get("1.0", tk.END)) :
            self.window.destroy()

    def open_html(self):
         HTML_ADVANCE_CONFI.open_html(self.txt_edit.get("1.0", tk.END))

    def clear_text(self):
        self.txt_edit.delete("1.0", tk.END)

    def open_file_in_use(self):
        text,filepath = HTML_ADVANCE_CONFI.open_file_in_use()
        if text!= "" and filepath!="":
            HTML_ADVANCE_CONFI_UI.clear_text(self)
            self.txt_edit.insert(tk.END, text)
            self.window.title(f"Html Editor - {filepath}")


    def insert_txt(self,text):
            self.txt_edit.insert(tk.END,f" {text} ")
