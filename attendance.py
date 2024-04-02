from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox
import mysql.connector
import cv2

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")

        # Title label
        title_lbl = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=15, y=80, width=1500, height=700)

        # Left frame
        Left_frame = LabelFrame(main_frame, bd=3, relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 16, "bold"), bg="white", fg="black")
        Left_frame.place(x=10, y=10, width=760, height=670)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=15, y=80, width=720, height=500)

        # Label and entry
        Attendance_label = Label(left_inside_frame, text="Attendance Id", font=("times new roman", 14, "bold"),
                                 bg="white", fg="black")
        Attendance_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        Attendance_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 14, "bold"),
                                     background="white", foreground="black")
        Attendance_entry.grid(row=0, column=1)

        # Roll
        roll_label = Label(left_inside_frame, text="Roll:", font=("times new roman", 14, "bold"), bg="white", fg="black")
        roll_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 14, "bold"), background="white",
                              foreground="black")
        roll_entry.grid(row=0, column=3)

        # Name
        Name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 14, "bold"), bg="white", fg="black")
        Name_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        Name_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 14, "bold"), background="white",
                               foreground="black")
        Name_entry.grid(row=1, column=1)

        # Department
        Dep_label = Label(left_inside_frame, text="Department:", font=("times new roman", 14, "bold"), bg="white",
                          fg="black")
        Dep_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        Dep_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 14, "bold"), background="white",
                              foreground="black")
        Dep_entry.grid(row=1, column=3)

        # Time
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 14, "bold"), bg="white", fg="black")
        time_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 14, "bold"), background="white",
                               foreground="black")
        time_entry.grid(row=2, column=1)

        # Date
        Date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 14, "bold"), bg="white", fg="black")
        Date_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        Date_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 14, "bold"), background="white",
                               foreground="black")
        Date_entry.grid(row=2, column=3)

        # Attendance
        attendance_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 14, "bold"),
                                  bg="white", fg="black")
        attendance_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, width=20, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=50, y=410, width=627, height=50)

        save_btn = Button(btn_frame, text="Import csv", height=2, width=12, font=("times new roman", 14, "bold"),
                          bg="black", fg="red")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv", height=2, width=12, font=("times new roman", 14, "bold"),
                            bg="black", fg="red")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update ", height=2, width=12, font=("times new roman", 14, "bold"),
                            bg="black", fg="red")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", height=2, width=12, font=("times new roman", 14, "bold"),
                           bg="black", fg="red")
        reset_btn.grid(row=0, column=3)

        # Right frame
        Right_frame = LabelFrame(main_frame, bd=3, relief=RIDGE, text="Attendance Details",
                                 font=("times new roman", 16, "bold"), bg="white", fg="black")
        Right_frame.place(x=780, y=10, width=700, height=670)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=20, y=30, width=657, height=445)

        # Scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("id", "roll", "Name", "dep", "time", "date", "Attendance"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("Name", text="Name")
        self.AttendanceReportTable.heading("dep", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("Attendance", text="Attendance")

        self.AttendanceReportTable['show'] = 'headings'

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("Name", width=150)
        self.AttendanceReportTable.column("dep", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("Attendance", width=100)
        self.AttendanceReportTable["show"]="headings"


        self.AttendanceReportTable.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = Tk()
    app = Attendance(root)
    root.mainloop()
