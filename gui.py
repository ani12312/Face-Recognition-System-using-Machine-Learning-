import os
import time
import tkinter as tk
from tkinter import *
import cv2 
from test import *
from attendance import *
import csv
import time
import datetime
import shutil
global today

today=datetime.date.today()

from datetime import datetime
now=datetime.now()
global current_time
from exit__out import *
current_time=now.strftime("%H:%M:%S")

charecter_folder = "yourdata"+os.sep+"character"
sample_folder = "newsample"
character = 0
if not os.path.exists(charecter_folder):
    os.makedirs(charecter_folder)

if not os.path.exists(sample_folder):
    os.makedirs(sample_folder)

face_capture = False
def login():
    startTime=time.time()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    i=0
    while True:
        crop_image = None
        face_capture = False

        ret, cv2frame = cap.read()
        faces = face_cascade.detectMultiScale(cv2frame,1.3,5)
        for (x, y, w, h) in faces:
            crop_image = cv2frame[y:y+h, x:x+w].copy()
            cv2.rectangle(cv2frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_color = cv2frame[y:y + h, x:x + w]
        cv2.imshow("Login",cv2frame)

        k=cv2.waitKey(10)
        if k == 27:
            break
        elif k == 32:
            if len(faces) == 1:
                cv2.imwrite(charecter_folder+os.sep+"tmp.jpg", crop_image)
                character = test_my_model()[0]
                face_capture = True
                break
    cap.release()
    cv2.destroyAllWindows()
    if face_capture:
        global login_screen
        login_screen = Toplevel(main_screen) 
        login_screen.title("Login")
        login_screen.geometry("300x250")
        Label(login_screen, text="Please enter details below", bg="blue").pack()
        Label(login_screen, text="Are your employe ID is : "+ str(character) +" ?", fg="green", font=("calibri", 11)).pack()
        Button(login_screen, text="Yes", width=10, height=1, bg="blue",command=lambda: attendance(character)).pack()
        Button(login_screen, text="No", width=10, height=1, bg="blue",command=login_screen.destroy).pack()
    else:
        main_screen.destroy()


def attendance(character):
    Label(login_screen, text="Successfull,You may enter", fg="green", font=("calibri", 11)).pack()
    attendance_here(str(character), today, current_time)
def exitout():
    exit()

def exitattendance():
    exit_here(character,today,current_time)
    Label(login_screen, text="Successfull,You may out", fg="green", font=("calibri", 11)).pack()

def register():
    global username
    global register_screen
    register_screen = Toplevel(main_screen) 
    register_screen.title("Register")
    register_screen.geometry("300x250")

    username = StringVar()
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    
    username_lable = Label(register_screen, text="ID No. * ")
    username_lable.pack()
 
    global username_entry
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Button(register_screen, text="Register Now", width=10, height=1, bg="blue",command=save_user).pack()
    

def save_user():
    try:
        os.rename(sample_folder, "trainparent"+os.sep+username.get())
    except:
        pass
    register_screen.destroy() 
def facecrop(image):
    facedata = "haarcascade_frontalface_default.xml"
    cascade = cv2.CascadeClassifier(facedata)

    img = cv2.imread(image)

    minisize = (img.shape[1],img.shape[0])
    miniframe = cv2.resize(img, minisize)

    faces = cascade.detectMultiScale(miniframe)

    for f in faces:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))

        sub_face = img[y:y+h, x:x+w]
        fname, ext = os.path.splitext(image)
        cv2.imwrite(fname+ext, sub_face)
    return

def train_model():
    if today.weekday()==5 or today.weekday()==6:
        train_my_model()
        #Label(text="Training Success", fg="green", font=("calibri", 11)).pack()
        attendance_path="attendance.csv"
        exit_path="exit.csv"
        n=os.listdir("trainparent")
        with open (attendance_path,'w',newline='') as csvfile:
            filewriter=csv.writer((csvfile))
            filewriter.writerow(n)
        with open (exit_path,'w',newline='') as csvfile:
            filewriter=csv.writer((csvfile))
            filewriter.writerow(n)
        main_screen.destroy()
    else:
        Label(text="Training can be done only on saturday/sunday", fg="green", font=("calibri", 11)).pack()

def register_admin():
    try:
        shutil.rmtree(sample_folder)
    except:
        pass

    if not os.path.exists(sample_folder):
        os.makedirs(sample_folder)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    i = 0
    while True:
        ret, cv2frame = cap.read()
        faces = face_cascade.detectMultiScale(cv2frame, 1.3, 5)
        for (x, y, w, h) in faces:
            crop_image = cv2frame[y:y+h, x:x+w].copy()
            filename = sample_folder+os.sep+str(i)+".jpg"
            cv2.imwrite(filename, crop_image)
            i = i + 1
            cv2.rectangle(cv2frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_color = cv2frame[y:y + h, x:x + w]

        cv2.imshow("Register",cv2frame)
        k=cv2.waitKey(10)
        if k==27:
            break
    cap.release()
    cv2.destroyAllWindows()
    register()
def train_model_admin():
    import Train

global main_screen
main_screen = tk.Tk()   # create a GUI window 
main_screen.geometry("400x300") # set the configuration of GUI window 
main_screen.title("Account Login") # set the title of GUI window
 
# create a Form label 
Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack() 
 
# create Login Button 
Button(text="Login", height="2", width="30",command=login).pack() 
Label(text="").pack() 
Button(text="Exit", height="2", width="30",command=exitout).pack() 
Label(text="").pack()
# create a register button
Button(text="Register", height="2", width="30",command=register_admin).pack()
Button(text="Train", height="2", width="30",command=train_model_admin).pack()
main_screen.mainloop() # start the GUI