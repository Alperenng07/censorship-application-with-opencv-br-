# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 16:35:23 2022

@author: alper
"""

from tkinter import *
import cv2,time



tk = Tk()
tk.title("NORMAL CEKIM | SANSURLU CEKIM")
tk.geometry("400x150")
 #**************************************************************************
def buton():


    cam=cv2.VideoCapture(0)
    
    while True:
        ret,frame=cam.read()
        
        if not ret:
            print("kameradan görüntü alınamadı")
            break
        
        cv2.imshow("kamera",frame)
        
        if cv2.waitKey(1) & 0xFF == ord("e"):
            
            break
        
    cam.release()
    cv2.destroyAllWindows()    
   
#**************************************************************************
def buton2():
 face_cascade = cv2.CascadeClassifier(r'C:/Users/alper/anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
 video=cv2.VideoCapture(0)



 while True:
     check,frame=video.read()
     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
     for x,y,w,h in face:
         img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
         img[y:y+h,x:x+w]=cv2.medianBlur(img[y:y+h,x:x+w],35)
         
         
       #esc ile cik
     cv2.imshow('Video', frame)
     if cv2.waitKey(1) & 0xFF == ord('e'):
         break

 # Fonksiyonları çalıştırıyorum
 video.release()
 cv2.destroyAllWindows()
#**************************************************************************

btn = Button(tk,
            text="NORMAL CEKIM",font="Times 12 bold",
            padx="30",pady="5",
            bg="red", fg="white", cursor="hand2",
            command=buton)
btn.pack()
#**************************************************************************
btn2 = Button(tk,
            text = "SANSURLU CEKIM", font="Times 12 bold",
            padx="20", pady="5", 
            bg="red", fg="white", cursor="hand2",
            activeforeground="green", activebackground="black",
            command=buton2)
btn2.pack()
#**************************************************************************




lbl = Label(tk)
lbl.pack()
 
tk.mainloop()