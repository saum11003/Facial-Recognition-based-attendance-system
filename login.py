from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from main import Face_Recognition_System
from register import Register

import subprocess


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"/Users/saumyapandey/Desktop/FacialRecognitionProject.py/background.jpeg")
        lbl_bg=Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0, relwidth=1, relheight=1)

        frame=Frame(self.root, bg="black")
        frame.place(x=550,y=170, width=420,height=480)

        img1=Image.open(r"/Users/saumyapandey/Desktop/FacialRecognitionProject.py/logo.png")
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=615,y=175, width=300, height=100)

        get_str=Label(frame, text="Get Started", font=("times new roman", 28, "bold"), fg= "white",bg="black")
        get_str.place(x=140,y=115) 


        # label
        username=lbl=Label(frame, text="Username", font=("times new roman",15,"bold"), fg="white", bg="black")
        username.place(x=15,y=155)
        self.txtuser=ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=15, y=188,width=380)
        password=lbl=Label(frame, text="Password", font=("times new roman",15,"bold"), fg="white", bg="black")
        password.place(x=15,y=225)
        self.txtpass=ttk.Entry(frame,font=("times new roman", 15, "bold"))
        self.txtpass.place(x=15,y=258,width=380)


        # LoginButton
        loginbtn=Button(frame,command=self.login,text="Login", font=("times new roman", 15, "bold"),bd=3, relief=RIDGE, fg="red",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=145,y=330,width=120,height=35)

        # Register button
        registerbtn=Button(frame, text="New Register User", command= self.new_register, font=("times new roman", 15, "bold"),bd=3, relief=RIDGE, borderwidth=0, bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=130,y=380,width=150,height=35)

    def new_register(self):
            self.new_window=Toplevel(self.root)
            self.app=Register(self.new_window)


       

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("Success", "Welcome")

            # Create an instance of Face_Recognition_System and open its window
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognition_System(self.new_window)

        else:
            messagebox.showerror("Invalid", "Invalid Username & Password")

    


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
