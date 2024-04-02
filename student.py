from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk #pip install pillow
from tkinter import messagebox
import mysql.connector
import cv2
import subprocess

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("face Recognition System")
        self.root.geometry("1530x790+0+0")

        #variables
        self.var_dept=StringVar()
        self.var_Sbj=StringVar()
        self.var_Pgm=StringVar()
        self.var_Sem=StringVar()
        self.var_SAP=StringVar()
        self.var_Roll=StringVar()
        self.var_SName=StringVar()
        self.var_Pname=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"/Users/saumyapandey/Desktop/FacialRecognitionProject.py/bg.jpeg")
        lbl_bg=Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        title_lbl=Label(lbl_bg, text="STUDENT MANAGEMENT SYSTEM", font=("time new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame=Frame(self.root, bd=2, bg="white")
        main_frame.place(x=15, y=80, width=1500, height=700)

        #left frame

        Left_frame=LabelFrame(main_frame, bd=3,relief=RIDGE, text="Student Details",font=("times new roman", 16, "bold",), bg="white", fg="black")
        Left_frame.place(x=10,y=10,width=720,height=670)

        CurrentCourse_frame=LabelFrame(Left_frame, bd=3,relief=RIDGE, text="Current Course Information",font=("times new roman", 16, "bold",), bg="white", fg="black")
        CurrentCourse_frame.place(x=10,y=10,width=700,height=170)

        #Department
        dept_label=Label(CurrentCourse_frame,text="Department", font=("time new roman", 14, "bold"),bg="white",fg="black")
        dept_label.grid(row=0,column=0)

        dept_combo=ttk.Combobox(CurrentCourse_frame,textvariable=self.var_dept,font=("time new roman", 14, "bold"), width=20, state="readonly", background="white")
        dept_combo["values"]=("Select Department","Computer Science","Electronics","Mechanical","Civil")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=10, sticky=W) 

        #Program
        Pgm_label=Label(CurrentCourse_frame,text="Program", font=("time new roman", 14, "bold"),bg="white",fg="black")
        Pgm_label.grid(row=0,column=2)

        Pgm_combo=ttk.Combobox(CurrentCourse_frame,textvariable=self.var_Pgm,font=("time new roman", 14, "bold"), width=20, state="readonly", background="white")
        Pgm_combo["values"]=("Select Program","MBATech","BTech")
        Pgm_combo.current(0)
        Pgm_combo.grid(row=0,column=3,padx=10, pady=10, sticky=W) 

        #Subject
        Sbj_label=Label(CurrentCourse_frame,text="Subject", font=("time new roman", 14, "bold"),bg="white",fg="black")
        Sbj_label.grid(row=1,column=0, padx=10, pady=10, sticky=W)

        Sbj_combo=ttk.Combobox(CurrentCourse_frame,textvariable=self.var_Sbj, font=("time new roman", 14, "bold"), width=20, state="readonly", background="white")
        Sbj_combo["values"]=("Select Subject","Software Engineering","Artifical Intelligence","AWP")
        Sbj_combo.current(0)
        Sbj_combo.grid(row=1,column=1,padx=10, pady=10, sticky=W) 

        #Semester
        Sem_label=Label(CurrentCourse_frame,text="Semester", font=("time new roman", 14, "bold"),bg="white",fg="black")
        Sem_label.grid(row=1,column=2, padx=10, pady=10, sticky=W)

        Sem_combo=ttk.Combobox(CurrentCourse_frame,textvariable=self.var_Sem, font=("time new roman", 14, "bold"), width=20, state="readonly", background="white")
        Sem_combo["values"]=("Select Sem","I","II","III","IV","V","VI","VII","VIII","IX","X")
        Sem_combo.current(0)
        Sem_combo.grid(row=1,column=3,padx=10, pady=10, sticky=W) 

        #TeacherName
        Teacher_label=Label(CurrentCourse_frame,text="Proffessor:", font=("time new roman", 14, "bold"),bg="white",fg="black")
        Teacher_label.grid(row=2,column=0, padx=10, pady=10, sticky=W)

        Teacher_entry=ttk.Entry(CurrentCourse_frame,width=20,textvariable=self.var_Pname,font=("time new roman", 14, "bold"),background="white",foreground="black")
        Teacher_entry.grid(row=2,column=1)

        #Class Student Information
        Class_frame=LabelFrame(Left_frame, bd=3,relief=RIDGE, text="Class Student Information",font=("times new roman", 16, "bold",), bg="white", fg="black")
        Class_frame.place(x=10,y=190,width=700,height=400)

        #SAP
        SAP_label=Label(Class_frame,text="SAP ID:", font=("time new roman", 14, "bold"),bg="white",fg="black")
        SAP_label.grid(row=0,column=0, padx=10, pady=10, sticky=W)

        SAP_entry=ttk.Entry(Class_frame,width=20,textvariable=self.var_SAP,font=("time new roman", 14, "bold"),background="white",foreground="black")
        SAP_entry.grid(row=0,column=1)

        #Name
        Name_label=Label(Class_frame,text="Name:", font=("time new roman", 14, "bold"),bg="white",fg="black")
        Name_label.grid(row=0,column=2, padx=10, pady=10, sticky=W)

        Name_entry=ttk.Entry(Class_frame,width=20, textvariable=self.var_SName,font=("time new roman", 14, "bold"),background="white",foreground="black")
        Name_entry.grid(row=0,column=3)

        #RollNo
        RollNO_label=Label(Class_frame,text="Roll No:", font=("time new roman", 14, "bold"),bg="white",fg="black")
        RollNO_label.grid(row=1,column=0, padx=10, pady=10, sticky=W)

        RollNO_entry=ttk.Entry(Class_frame,width=20,textvariable=self.var_Roll,font=("time new roman", 14, "bold"),background="white",foreground="black")
        RollNO_entry.grid(row=1,column=1)

        #Radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_frame,variable=self.var_radio1,text="Click Sample Photo", value="Yes")
        radiobtn1.grid(row=6,column=1)
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(Class_frame,variable=self.var_radio2,text="No Photo Sample", value="Yes")
        radiobtn2.grid(row=6,column=2)

        #Button Frame
        btn_frame=Frame(Class_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=25,y=150, width= 627, height=50)

        save_btn=Button(btn_frame,text="Save", command=self.add_data, height=2,width=12,font=("time new roman", 14, "bold"), bg="black", fg="red")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update", command=self.update_data,height=2, width=12,font=("time new roman", 14, "bold"), bg="black", fg="red")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete", command= self.delete_data,height=2, width=12,font=("time new roman", 14, "bold"), bg="black", fg="red")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,height=2, width=12,font=("time new roman", 14, "bold"), bg="black", fg="red")
        reset_btn.grid(row=0,column=3)

        pic_frame=Frame(Class_frame, bd=2, relief=RIDGE, bg="white")
        pic_frame.place(x=65,y=310, width= 555, height=50)

        take_btn=Button(pic_frame ,text="Take a photo Sample", width=24,height=2,command=self.generate_dataset,font=("time new roman", 14, "bold"), bg="black", fg="red")
        take_btn.grid(row=0,column=0)



        Update_btn=Button(pic_frame,text="Update Photo Sample", width=24,height=2,font=("time new roman", 14, "bold"), bg="black", fg="red")
        Update_btn.grid(row=0,column=1)


            
        #right frame

        Right_frame=LabelFrame(main_frame, bd=3,relief=RIDGE, text="Concurrent Details",font=("times new roman", 16, "bold",), bg="white", fg="black")
        Right_frame.place(x=780,y=10,width=700,height=670)

        #Search System

        Search_frame=LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search System",font=("times new roman", 16, "bold",), bg="white", fg="black")
        Search_frame.place(x=5,y=5, width= 680, height=160)

        Search_label=Label(Search_frame,text="Search By:", font=("time new roman", 14, "bold"),bg="white",fg="black")
        Search_label.grid(row=0,column=0, padx=10, pady=2, sticky=W)

        Search_combo=ttk.Combobox(Search_frame,font=("time new roman", 14, "bold"), width=20, state="readonly", background="white")
        Search_combo["values"]=("Select","SAPID","Roll No","Name")
        Search_combo.current(0)
        Search_combo.grid(row=1,column=0,padx=10, pady=5, sticky=W)

        Search_entry=ttk.Entry(Search_frame,width=20,font=("time new roman", 14, "bold"),background="white",foreground="black")
        Search_entry.grid(row=1,column=1)

        Search_btn=Button(Search_frame,text="Search", width=24,height=2,font=("time new roman", 14, "bold"), bg="black", fg="red")
        Search_btn.grid(row=2,column=0, pady=10)

        ShowAll_btn=Button(Search_frame,text="Show All", width=24,height=2,font=("time new roman", 14, "bold"), bg="black", fg="red")
        ShowAll_btn.grid(row=2,column=1, pady=10)

        table_frame=Frame(Right_frame, bd=2, relief=RIDGE,bg="white")
        table_frame.place(x=5,y=180, width= 680, height=400)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

 #table content view        
        self.student_table=ttk.Treeview(table_frame,columns=("Roll No","Pgm","Sbj","dep","Sem","Teacher Name","Name","SAP"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Roll No", text="Roll No.")
        self.student_table.heading("Pgm", text="Program")
        self.student_table.heading("Sbj", text="Subject")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Teacher Name", text="Professor Name")
        self.student_table.heading("Name", text="Student Name")
        self.student_table.heading("SAP", text="SAP ID")
        self.student_table["show"] = "headings"

        self.student_table.column("Roll No", width=100)
        self.student_table.column("Pgm", width=100)
        self.student_table.column("Sbj", width=100)
        self.student_table.column("dep", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("Teacher Name", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("SAP", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()  

#function declare
    def add_data(self):
        if self.var_dept.get() == "Select Department" or self.var_SName.get() == "" or self.var_SAP.get() == "":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="facial_Recignition_Prj")
                my_cursor=conn.cursor()
                roll_no = int(self.var_Roll.get())
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_Roll.get(),
                                                                            self.var_Pgm.get(),
                                                                            self.var_Sbj.get(),
                                                                            self.var_dept.get(),
                                                                            self.var_Sem.get(),
                                                                            self.var_Pname.get(),
                                                                            self.var_SName.get(),
                                                                            self.var_SAP.get(),
                                                                            self.var_radio1.get()
                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root) 

#funtion fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="facial_Recignition_Prj")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#fetch data 
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        if len(data) >= 8:

                self.var_Roll.set(data[0]),
                self.var_Pgm.set(data[1]),
                self.var_Sbj.set(data[2]),
                self.var_dept.set(data[3]),
                self.var_Sem.set(data[4]),
                self.var_Pname.set(data[5]),
                self.var_SName.set(data[6]),
                self.var_SAP.set(data[7]),

#update data
    def update_data(self):
        if self.var_dept.get() == "Select Department" or self.var_SName.get() == "" or self.var_SAP.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update the student details", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                database="facial_Recignition_Prj")
                    my_cursor = conn.cursor()
                    # Use placeholders for values in the SQL query
                    sql = "UPDATE student SET `Roll No`=%s, Program=%s, Subject=%s, department=%s, Semester=%s, `Professor Name`=%s, `Student Name`=%s WHERE `SAP ID`=%s"
                    val = (self.var_Roll.get(),
                        self.var_Pgm.get(),
                        self.var_Sbj.get(),
                        self.var_dept.get(),
                        self.var_Sem.get(),
                        self.var_Pname.get(),
                        self.var_SName.get(),
                        self.var_SAP.get()
                        )
                    my_cursor.execute(sql, val)
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
            except mysql.connector.errors.ProgrammingError as es:
                    messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


    
#delete data
    def delete_data(self):
        if self.var_SAP.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student data?", parent=self.root)
                if delete:
                    conn = mysql.connector.connect(host="localhost", username="root", password="1234",
                                               database="facial_Recignition_Prj")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE `SAP ID`=%s"
                    val = (self.var_SAP.get(),)
                    my_cursor.execute(sql, val)
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo("Delete", "Successfully Deleted", parent=self.root)
                else:
                    if not delete:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

#reset data
    def reset_data(self):
        self.var_Roll.set("")       # Default value for Roll No
        self.var_Pgm.set("Select Program")  # Default value for Program
        self.var_Sbj.set("Select Subject")  # Default value for Subject
        self.var_dept.set("Select Department")  # Default value for Department
        self.var_Sem.set("Select Sem")  # Default value for Semester
        self.var_Pname.set("")       # Default value for Professor Name
        self.var_SName.set("")       # Default value for Student Name
        self.var_SAP.set("")        # Default value for SAP ID
    
    #genrate dataset or take photo sample
    def generate_dataset(self):
        if self.var_dept.get() == "Select Department" or self.var_SName.get() == "" or self.var_SAP.get() == "":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="facial_Recignition_Prj")
                my_cursor=conn.cursor()  
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1      
                my_cursor.execute("UPDATE student SET `Roll No`=%s, Program=%s, Subject=%s, department=%s, Semester=%s, `Professor Name`=%s, `Student Name`=%s WHERE `SAP ID`=%s",(
                                                                                    self.var_Roll.get(),
                                                                                    self.var_Pgm.get(),
                                                                                    self.var_Sbj.get(),
                                                                                    self.var_dept.get(),
                                                                                    self.var_Sem.get(),
                                                                                    self.var_Pname.get(),
                                                                                    self.var_SName.get(),
                                                                                    self.var_SAP.get()==id+1
                                                                                    
                                                                                ))
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close() 

                #load predefined data on face frontals from opencv

                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                print(cv2.CascadeClassifier.empty(face_classifier))

                
                def face_cropped(img):
                    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray, 1.3,5)
                    #scaling factor=1.3 and min neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h, x:x+w] #face cropped 
                        return face_cropped
                    
                cap = cv2.VideoCapture(1)
                
                img_id=0
                while True: 
                    ret, my_frame=cap.read()
                    if not ret:
                        break
                    detected_face = face_cropped(my_frame)

                    if detected_face is not None: 
                        img_id+=1
                        x,y,w,h = detected_face
                        face=cv2.resize(my_frame[y:y+h,x:x+w],(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(my_frame,str(img_id),(x,y,-10),cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0),2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey (1) == 13 or int(img_id)==5:
                        break 
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result" , "Generating data sets completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

                
            




                    
                                
if __name__ == "__main__":
    root=Tk()
    root.title("Camera App")
    app=Student(root)
    root.mainloop()
