from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk #pip install pillow
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from student import Student
import train
import face_recognition

class Face_Recongnition:
    def __init__(self,root):
        self.root=root
        self.root.title("face Recognition System")
        self.root.geometry("1530x790+0+0")

        title_lbl=Label(self.root, text="FACE RECOGNITION", font=("time new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #no images 

        #button
        b1_1=Button (self.root, text="Face Recognition", cursor="hand2", font=("time new roman", 35, "bold"))
        b1_1.place( x = 0, y=380, width=1530,height=60)


    #face recognition   
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image=cv2.cvtColor(img, cv2.COLOR_BGRGRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor, minNeighbors)

            coord = [ ]

            for (x,y,w,h) in features: 
                cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="facial_Recignition_Prj")
                my_cursor=conn.cursor()

                my_cursor.execute("select Student Name from student WHERE SAP ID= " + str(id))
                n = my_cursor.fetchone()
                n="+".join(n) #concatnate 

                my_cursor.execute("select Roll No from student WHERE SAP ID= " + str(id))
                r = my_cursor.fetchone()
                r="+".join(r)  

                my_cursor.execute("select Program from student WHERE SAP ID= " + str(id))
                p = my_cursor.fetchone()
                p="+".join(p)   

                my_cursor.execute("select department from student WHERE SAP ID= " + str(id))
                d = my_cursor.fetchone()
                d="+".join(d)  

                if confidence>77: 
                    cv2.putText(img, f"Roll:{r} ", (x,y-70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                    cv2.putText(img, f"Student Name:{n} ", (x,y-60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                    cv2.putText(img, f"Program:{p} ", (x,y-50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                    cv2.putText(img, f"department:{d} ", (x,y-40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h), (0,0,255),3)
                    cv2.putText(img, "Unknown Face ", (x,y-40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)

                coord=[x,y,w,h]   
            return coord 
        
        def recognize(img,clf,faceCascade):
            coord= draw_boundary(img, faceCascade, 1.1,10,(255,25,255), "Face", clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("xyz.xml") #to copy xml file -> we get in train data 
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img, clf, faceCascade)
            cv2.imshow("WELCOME TO FACE RECOGNITION", img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()







if __name__ == "__main__":
    root=Tk()
    app=Face_Recongnition(root)
    root.mainloop()