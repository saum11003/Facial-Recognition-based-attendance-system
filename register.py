from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk #pip install pillow
from tkinter import messagebox

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #background
        self.bg=ImageTk.PhotoImage(file=r"/Users/saumyapandey/Desktop/FacialRecognitionProject.py/bg.jpeg")
        lbl_bg=Label(self.root, image=self.bg)
        lbl_bg.place(x=0,y=0, relwidth=1, relheight=1)

        #left image
        self.bg1=ImageTk.PhotoImage(file=r"/Users/saumyapandey/Desktop/FacialRecognitionProject.py/register.png")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        #main frame
        frame=Frame(self.root, bg="white")
        frame.place(x=520,y=100, width=800,height=550)

        register_lbl=Label (frame, text="REGISTER HERE", font=("times new roman", 28, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20,y=20)

        #label and entry
        fname=Label(frame, text="First Name", font=("times new roman", 15, "bold"),bg="white", fg="black")
        fname.place(x=50,y=100) 

        fname_entry=ttk.Entry (frame, font=("times new roman", 15, "bold")) 
        fname_entry.place(x=50,y=130, width=250, height= 30)

    

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white", fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk. Entry (frame, font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #row 2
        contact=Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black") 
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame, font=("times new roman",15))
        self.txt_contact.place(x=50,y=200, width=250)

        email=Label(frame,text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370,y=170)
        self.txt_email=ttk.Entry(frame, font=("times new roman",15))
        self.txt_email.place(x=370,y=200, width=250)

        #row3

        security_Q=Label(frame, text="Select Security Quetions", font=("times new roman", 15, "bold"), bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_securiy_Q=ttk.Combobox (frame, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_securiy_Q["values"]=("Select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
        self.combo_securiy_Q.place(x=50,y=270, width=250)
        self.combo_securiy_Q.current(0)

        security_A=Label(frame, text="Security Answer", font=("times new roman", 15, "bold"),bg="white", fg="black") 
        security_A.place(x=370,y=240)
        self.txt_security=ttk.Entry(frame, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        #row4

        pswd=Label(frame,text="Password", font=("times new roman", 15, "bold"), bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame, font=("times new roman", 15))
        self.txt_pswd.place (x=50,y=340, width=258)

        confirm_pswd=Label (frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",fg="black") 
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk. Entry (frame, font=("times new roman", 15)) 
        self.txt_confirm_pswd.place(x=370,y=340, width=258)

        checkbtn=Checkbutton(frame, text="I Agree The Terms & Conditions", font=("times new roman", 12, "bold"), onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #buttons
        img=Image.open("/Users/saumyapandey/Desktop/FacialRecognitionProject.py/registernow.jpeg")
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage, borderwidth=0, cursor="hand2", font=("times new roman",15,"bold"))
        b1.place(x=10,y=420, width=300)

        img1=Image.open("/Users/saumyapandey/Desktop/FacialRecognitionProject.py/loginnow.jpeg")
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=330,y=420, width=300)





        





if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()

