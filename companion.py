from tkinter import *
import os
from tkinter import messagebox
from tkinter import filedialog
import pytesseract
from PIL import Image
from gtts import gTTS
from playsound import playsound
from google_trans_new import google_translator
import urllib.request

pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x730+0+0")
        self.root.title("My Companion App")
        bg_color = "#074463"
        title = Label(self.root, text="My Companion App", bd=12, relief=GROOVE, bg=bg_color, fg="white",font=("times new roman", 30, "bold")).pack(fill=X)
        # ----------------VARIABLES------------------------
        self.c_name = StringVar()
        self.c_text = StringVar()
        # ----------------Uploading Image---------------------
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Uploading Image", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Image Path", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=30, textvariable=self.c_name, font="arial 10", bd=7, relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        cbrowse_btn = Button(F1, text="Browse", command=self.find_image, width=10, bd=7, font="arial 12 bold").grid(row=0, column=6, padx=50, pady=5)

        # ----------------------Translated Text----------------------
        F2 = Frame(self.root, bd=10, relief=GROOVE)
        F2.place(x=440, y=175, width=480, height=550)
        bill_title = Label(F2, text="Translated Text", font=("times new roman", 16, "bold"), relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F2, orient=VERTICAL)
        self.texttrans = self.txtarea = Text(F2)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.texttrans.yview)
        self.texttrans.pack(fill=BOTH, expand=1)

        # ---------------Extracted Text----------------
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=5, y=175, width=435, height=550)
        bill_title = Label(F5, text="Extracted Text", font=("times new roman", 16, "bold"), relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ----------------------Voice Operation----------------------
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Speech in required language",font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F4.place(x=917, y=175, width=433, height=270)
        cenglish_btn = Button(F4, text="English", command=self.convert_audio_english, width=10, bd=7,font="arial 12 bold").grid(row=0, column=0, padx=15, pady=15)
        chindi_btn = Button(F4, text="Hindi", command=self.convert_audio_hindi, width=10, bd=7,font="arial 12 bold").grid(row=1, column=0, padx=15, pady=15)
        ckannada_btn = Button(F4, text="Kannada", command=self.convert_audio_kannada, width=10, bd=7,font="arial 12 bold").grid(row=2, column=0, padx=15, pady=15)
        cmarathi_btn = Button(F4, text="Marathi", command=self.convert_audio_marathi, width=10, bd=7,font="arial 12 bold").grid(row=0, column=1, padx=50, pady=15)
        ctamil_btn = Button(F4, text="Tamil", command=self.convert_audio_tamil, width=10, bd=7,font="arial 12 bold").grid(row=1, column=1, padx=50, pady=15)
        ctelgu_btn = Button(F4, text="Telugu", command=self.convert_audio_telgu, width=10, bd=7,font="arial 12 bold").grid(row=2, column=1, padx=50, pady=15)

        # --------------------------Text to be Read-------------------------------------
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Text to be Read", font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F6.place(x=917, y=450, width=433, height=270)
        cname_txt = Entry(F6, width=35, textvariable=self.c_text, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,column=0,pady=5,padx=10)
        cclear2 = Button(F6, text="Clear Text to Read", command=self.clear_normal, width=20, bd=7,font="arial 12 bold").grid(row=1, column=0, padx=89, pady=10)
        cclear1 = Button(F6, text="Clear Translated Text", command=self.clear_translated, width=20, bd=7,font="arial 12 bold").grid(row=3, column=0, padx=90, pady=10)
        cexit = Button(F6, text="Exit", command=self.Exit_app, width=10, bd=7, font="arial 12 bold").grid(row=4,column=0,padx=90,pady=10)

    def convert_audio_kannada(self):
        text_info = self.c_text.get()
        if (text_info == ""):
            messagebox.showerror("Error", "Text Not Found")
        else:
            host = 'http://google.com'
            try:
                urllib.request.urlopen(host)
                text_info = text_info.lower()
                translator = google_translator()
                translation = translator.translate(text_info, lang_src='en', lang_tgt='kn')
                self.texttrans.delete('1.0', END)
                self.texttrans.insert(INSERT, translation)
                myObj = gTTS(text=translation, lang='kn', slow=False)
                myObj.save("TRANS.mp3")
                playsound("TRANS.mp3")
                os.remove("TRANS.mp3")
            except:
                messagebox.showerror("Error", "No Internet Connection")

    def convert_audio_marathi(self):
        text_info = self.c_text.get()
        if (text_info == ""):
            messagebox.showerror("Error", "Text Not Found")
        else:
            host = 'http://google.com'
            try:
                urllib.request.urlopen(host)
                text_info = text_info.lower()
                translator = google_translator()
                translation = translator.translate(text_info, lang_src='en', lang_tgt='mr')
                self.texttrans.delete('1.0', END)
                self.texttrans.insert(INSERT, translation)
                myObj = gTTS(text=translation, lang='mr', slow=False)
                myObj.save("TRANS.mp3")
                playsound("TRANS.mp3")
                os.remove("TRANS.mp3")
            except:
                messagebox.showerror("Error", "No Internet Connection")

    def convert_audio_tamil(self):
        text_info = self.c_text.get()
        if (text_info == ""):
            messagebox.showerror("Error", "Text Not Found")
        else:
            host = 'http://google.com'
            try:
                urllib.request.urlopen(host)
                text_info = text_info.lower()
                translator = google_translator()
                translation = translator.translate(text_info, lang_src='en', lang_tgt='mr')
                self.texttrans.delete('1.0', END)
                self.texttrans.insert(INSERT, translation)
                myObj = gTTS(text=translation, lang='ta', slow=False)
                myObj.save("TRANS.mp3")
                playsound("TRANS.mp3")
                os.remove("TRANS.mp3")
            except:
                messagebox.showerror("Error", "No Internet Connection")

    def convert_audio_telgu(self):
        text_info = self.c_text.get()
        if (text_info == ""):
            messagebox.showerror("Error", "Text Not Found")
        else:
            host = 'http://google.com'
            try:
                urllib.request.urlopen(host)
                text_info = text_info.lower()
                translator = google_translator()
                translation = translator.translate(text_info, lang_src='en', lang_tgt='te')
                self.texttrans.delete('1.0', END)
                self.texttrans.insert(INSERT, translation)
                myObj = gTTS(text=translation, lang='te', slow=False)
                myObj.save("TRANS.mp3")
                playsound("TRANS.mp3")
                os.remove("TRANS.mp3")
            except:
                messagebox.showerror("Error", "No Internet Connection")

    def convert_audio_hindi(self):
        text_info = self.c_text.get()
        if (text_info == ""):
            messagebox.showerror("Error", "Text Not Found")
        else:
            host = 'http://google.com'
            try:
                urllib.request.urlopen(host)
                text_info = text_info.lower()
                translator = google_translator()
                translation = translator.translate(text_info, lang_src='en', lang_tgt='hi')
                self.texttrans.delete('1.0', END)
                self.texttrans.insert(INSERT, translation)
                myObj = gTTS(text=translation, lang='hi', slow=False)
                myObj.save("TRANS.mp3")
                playsound("TRANS.mp3")
                os.remove("TRANS.mp3")
            except:
                messagebox.showerror("Error", "No Internet Connection")

    def find_image(self):
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="select image file",filetypes=(("Jpg file", "*.jpg"), ("PNG file", ".png"), ("All files", "*.*")))
        self.c_name.set(fln)
        self.txtarea.insert(INSERT, pytesseract.image_to_string(Image.open(fln)))

    def convert_audio_english(self):
        text_info = self.c_text.get()
        if (text_info == ""):
            messagebox.showerror("Error", "Text Not Found")
        else:
            host = 'http://google.com'
            try:
                urllib.request.urlopen(host)
                text_info = text_info.lower()
                self.texttrans.delete('1.0', END)
                self.texttrans.insert(INSERT, text_info)
                myObj = gTTS(text=text_info, lang='en', slow=False)
                myObj.save("audio.mp3")
                playsound("audio.mp3")
                os.remove("audio.mp3")
            except:
                messagebox.showerror("Error", "No Internet Connection")



    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

    def clear_normal(self):
        temp = self.c_text.get()
        if (temp == ""):
            messagebox.showerror("Error", "Text Not Found")
        else:
            op = messagebox.askyesno("Exit", "Do you really want to clear Text?")
            if op > 0:
                self.c_text.set("")

    def clear_translated(self):
        temp = self.texttrans.get('1.0', "end-1c")
        if (temp == ""):
            messagebox.showerror("Error", "Text Not Found")
        else:
            op = messagebox.askyesno("Exit", "Do you really want to clear Translated Text?")
            if op > 0:
                self.texttrans.delete('1.0', END)


root = Tk()
obj = App(root)
root.mainloop()