from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk #pip install pillow
from train import Train
from student import Student
from attendance import Attendance
from face_recognition import Face_Recongnition
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Facial Recognition Attendance System")
        self.root.geometry("1530x790+0+0")

        #bg img
        self.bg=ImageTk.PhotoImage(file=r"/Users/saumyapandey/Desktop/FacialRecognitionProject.py/bg.jpeg")
        lbl_bg=Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0, relwidth=1, relheight=1)

        title_lbl=Label(lbl_bg,text="Facial Recognition Attendance System",font=("time new roman", 35,"bold"), bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img2=Image.open("/Users/saumyapandey/Desktop/FacialRecognitionProject.py/student.png")
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(lbl_bg, image=self.photoimg2, command=self.student_details, cursor="hand2")
        b1.place(x=200,y=100,width=220, height=220)

        b1_1=Button (lbl_bg, text="Student Details", command=self.student_details,cursor="hand2")
        b1_1.place( x = 200, y=300, width=220,height=40)

        #detect face button
        img3=Image.open("/Users/saumyapandey/Desktop/FacialRecognitionProject.py/facedetector.png")
        self.photoimg3=ImageTk.PhotoImage(img3)

        b1=Button(lbl_bg, image=self.photoimg3,command=self.face_data, cursor="hand2")
        b1.place(x=500,y=100,width=220, height=220)

        b1_1=Button (lbl_bg, text="Face Detector", command=self.face_data,cursor="hand2")
        b1_1.place( x = 500, y=300, width=220,height=40)

        #attendance button
        img4=Image.open("/Users/saumyapandey/Desktop/FacialRecognitionProject.py/attendance.png")
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(lbl_bg, image=self.photoimg4,command=self.attendance_data, cursor="hand2")
        b1.place(x=800,y=100,width=220, height=220)

        b1_1=Button (lbl_bg, text="Attendance", command=self.attendance_data,cursor="hand2")
        b1_1.place( x = 800, y=300, width=220,height=40)

        #train data button
        img5=Image.open("/Users/saumyapandey/Desktop/FacialRecognitionProject.py/trainface.png")
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(lbl_bg, image=self.photoimg5,command=self.train_data, cursor="hand2")
        b1.place(x=200,y=400,width=220, height=220)

        b1_1=Button (lbl_bg, text="Train Face", command=self.train_data,cursor="hand2")
        b1_1.place( x = 200, y=600, width=220,height=40)

        #photos button
        img6=Image.open("/Users/saumyapandey/Desktop/FacialRecognitionProject.py/photos.jpeg")
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(lbl_bg, image=self.photoimg6,cursor="hand2")
        b1.place(x=500,y=400,width=220, height=220)

        b1_1=Button (lbl_bg, text="Photos",cursor="hand2")
        b1_1.place( x = 500, y=600, width=220,height=40)

#function button 
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)

    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recongnition(self.new_window)

    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)





if __name__ == "__main__":
    root=Tk()
    app=Face_Recognition_System(root)
    root.mainloop()