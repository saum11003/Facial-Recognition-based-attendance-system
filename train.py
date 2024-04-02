from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk #pip install pillow
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2
from student import Student
# train.py
import train

class Train:
    def __init__(self,root):
        self.root=root
        self.root.title("face Recognition System")
        self.root.geometry("1530x790+0+0")

        title_lbl=Label(self.root, text="TRAIN DATA", font=("time new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #image nono

        #button
        b1_1=Button (self.root, text="Train Data", command= self.train_classifier, cursor="hand2", font=("time new roman", 35, "bold"))
        b1_1.place( x = 0, y=380, width=1530,height=60)

        #lbph algorithm- local binary pattern histogram algorithm 


    def train_classifier(self):
        data_dir=("data")
        path= [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = [ ]
        ids = [ ]

        for image in path:
            img=Image.open(image).convert('L') #grayscale image convert
            imageNp=np.array(img, 'uint8')  #to download numpy= pip install numpy
            id=int(os.path.split(image)[1].split(',')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training" , imageNp)
            cv2.waitKey(1) == 13
        ids=np.array(ids)

        #train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed") #output: classifier.xml file in folder 


if __name__ == "__main__":
    root=Tk()
    app=train(root)
    root.mainloop()