from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3   #python text to speech
import os  # for download the mp3 file
from tkinter.messagebox import showinfo
# pip install speechrecognition
import speech_recognition as sr

root=Tk()
root.title("TTS and STT")
root.geometry("900x500+200+200")
root.resizable(False,False)
root.configure(bg="#5D5D6E")

# initializing the pyttsx3 module
engine=pyttsx3.init()


def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:    
                text1 = r.recognize_google(audio,language="en-IN")
            except:
                pass
            return text1

def SpeechToText():
    recordbutton = Button(root, text='Record',font="arial 10 bold", bg='#5F9EA0', command=lambda: text_area2.insert(END, recordvoice()))
    recordbutton.place(x=640, y=360)


# speak function
def speaknow():
    text= text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if(gender=="MALE"):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if(speed=="FAST"):
            engine.setProperty("rate",250)
            setvoice()
        elif(speed=="NORMAL"):
            engine.setProperty("rate",150)
            setvoice()
        else:
            engine.setProperty("rate",60)
            setvoice()

# donwload function
def download():
    text= text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if(gender=="MALE"):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,"text.mp3")
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,"text.mp3")
            engine.runAndWait()
    if(text):
        if(speed=="FAST"):
            engine.setProperty("rate",250)
            setvoice()
        elif(speed=="NORMAL"):
            engine.setProperty("rate",150)
            setvoice()
        else:
            engine.setProperty("rate",60)
            setvoice()


# ttle icon
img=PhotoImage(file="D:\\miniproject\\tkinter t-t-s\\speak.png")
root.iconphoto(False,img)

# top frame
top=Frame(root,bg="white",width=900,height=90)
top.place(x=0,y=0)
logo=PhotoImage(file="D:\\miniproject\\tkinter t-t-s\\logo.png")
Label(top,image=logo,bg="white").place(x=10)
Label(top,text="CONVERTER",font="TimesNewRoman 16 bold",bg="white",fg="black").place(x=110,y=32)

# label 1
Label(root, text="TEXT-TO-SPEECH", font=("Times New Roman", 15),bg="#5D5D6E").place(x=60,y=115)
# text area
text_area=Text(root,font="Robote 13",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=20,y=150,width=450,height=100)
text_area.insert(INSERT, "Enter here..")


Label(root,text="VOICE",font="arial 12 bold",bg="#5D5D6E",fg="white").place(x=570,y=120)
Label(root,text="SPEED",font="arial 12 bold",bg="#5D5D6E",fg="white").place(x=740,y=120)

# label2
Label(root, text="SPEECH-TO-TEXT", font=("Times New Roman", 15),bg="#5D5D6E").place(x=60,y=285)
# text area 2
text_area2=Text(root,font="Robote 13",bg="white",relief=GROOVE,wrap=WORD)
text_area2.place(x=20,y=320,width=450,height=100)

# gender
gender_combobox=Combobox(root,values=["MALE","FEMALE"],font="arial 11",state="r",width=10)
gender_combobox.place(x=550,y=150)
gender_combobox.set("MALE")


# speed
speed_combobox=Combobox(root,values=["FAST","NORMAL","SLOW"],font="arial 11",state="r",width=10)
speed_combobox.place(x=730,y=150)
speed_combobox.set("NORMAL")


# button for speak
image_icon=PhotoImage(file="D:\\miniproject\\tkinter t-t-s\\speak.png")
btn=Button(root,text="SPEAK",compound=LEFT,image=image_icon,width=125,font="arial 11 bold",command=speaknow)
btn.place(x=540,y=190)


# button for download
image_icon1=PhotoImage(file="D:\\miniproject\\tkinter t-t-s\\download.png")
save=Button(root,text="DOWNLOAD",compound=LEFT,image=image_icon1,width=145,bg="#5F9EA0",font="arial 11 bold",command=download)
save.place(x=710,y=190)


# speech to text
speechtotextbutton = Button(root, text='Click here to Speech-To-Text', font=('Times New Roman', 14), bg="white",command=SpeechToText)
speechtotextbutton.place(x=560, y=315)



#execute 
root.update()
root.mainloop()
