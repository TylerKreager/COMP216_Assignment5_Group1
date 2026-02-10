import tkinter as tk
from tkinter import Tk , font, messagebox
from tkinter import ttk
from tkinter.ttk import Label, Button, Style, Frame


class MainWindow(Tk):
    
    fullName = "Nerendra Pershad"
    Residency = ["Domestic", "International"]
    program = ["AI", "Gaming", "Health", "Software"]
    courses = {"COMP100":"Programming 1", 
               "COMP213": "Web Page Design", 
               "COMP120": "Software Engineering"}
    
    def __init__(self):
        super().__init__()
        self.title("Assignment 5 - Part 2")
        self.geometry("500x500")  # Adjust me after you add your widgets
        self.configure(bg="lightgreen")  # Set background color
        self.create_widgets()
        
    def create_widgets(self):
        style = Style()
        style.configure("Green.TFrame", background="lightgreen")
        style.configure("TLabel", background="lightgreen")
        style.configure("TRadiobutton", background="lightgreen")
        
        # Main Frame
        self.main_frame = Frame(self, style="Green.TFrame")
        self.main_frame.pack(expand=True, fill='both', pady=20)
        
        #Title
        title_font = font.Font(family="Arial", size=24, weight="bold", slant="italic")
        self.label = Label(self.main_frame, text="ICET Student Survey", font=title_font, style="TLabel")
        self.label.pack(pady=20)
        
        #Name Row
        name_row = Frame(self.main_frame, style="Green.TFrame")
        name_row.pack( pady=5, fill='x')
        
        name_row.columnconfigure(0, weight=1)
        name_row.columnconfigure(1, weight=1)
        name_row.columnconfigure(2, weight=1)
        
        name_label = Label(name_row, text="Full Name:", style="TLabel")
        name_label.grid(row=0, column=0, sticky="w")
        
        self.name_textbox = ttk.Entry(name_row, width=30)
        self.name_textbox.grid(row=0, column=1, sticky="w")
        
        
        #Residency Row
        residency_row = Frame(self.main_frame, style="Green.TFrame")
        residency_row.pack(pady=5, fill='x')
        
        residency_row.columnconfigure(0, weight=1)
        residency_row.columnconfigure(1, weight=1)
        residency_row.columnconfigure(2, weight=1)
        
        residency_label = Label(residency_row, text="Residency:", style="TLabel")
        residency_label.grid(row=0, column=0, sticky="w")
        self.residency_choice = tk.StringVar()
        
        for i, option in enumerate(self.Residency):
            radio_button = ttk.Radiobutton(residency_row, text=option, value=option, style="TRadiobutton", variable=self.residency_choice)
            radio_button.grid(row=i, column=1, sticky="w")
        
        
        #Program Row
        program_row = Frame(self.main_frame, style="Green.TFrame")
        program_row.pack(pady=10, fill='x')
        
        program_row.columnconfigure(0, weight=1)
        program_row.columnconfigure(1, weight=1)
        program_row.columnconfigure(2, weight=1)
        
        program_label = Label(program_row, text="Program:", style="TLabel")
        program_label.grid(row=0, column=0, sticky="w")
        
        self.combobox = ttk.Combobox(program_row, values=self.program, state="readonly")
        self.combobox.grid(row=0, column=1, sticky="w")
        
        #Courses Row
        courses_row = Frame(self.main_frame, style="Green.TFrame")
        courses_row.pack(pady=10, fill='x')
        
        courses_row.columnconfigure(0, weight=1)
        courses_row.columnconfigure(1, weight=1)
        courses_row.columnconfigure(2, weight=1)
        
        courses_label = Label(courses_row, text="Courses:", style="TLabel")
        courses_label.grid(row=0, column=0, sticky="w")
        
        self.course_values = []
        for i, course in enumerate(self.courses.values()):
            var = tk.BooleanVar()
            self.checkbox = tk.Checkbutton(courses_row, text=course, variable=var, bg="lightgreen")
            self.checkbox.grid(row=i, column=1, sticky="w")
            
            self.course_values.append(var)
            
        #Buttons Row
        buttons_row = Frame(self.main_frame, style="Green.TFrame")
        buttons_row.pack(pady=20, fill='x')
        
        self.reset_btn = Button(buttons_row, text="Reset", command=self.reset)
        self.reset_btn.grid(row=0, column=0, padx=10)
        
        self.ok_btn = Button(buttons_row, text="OK", command=self.on_button_click)
        self.ok_btn.grid(row=0, column=1, padx=10)
        
        self.exit_btn = Button(buttons_row, text="Exit", command=self.exit)
        self.exit_btn.grid(row=0, column=2, padx=10)
        
        #set default values
        self.setDefaultValues()
        
    def setDefaultValues(self):
        self.name_textbox.insert(0, self.fullName)
        self.residency_choice.set(self.Residency[0])
        self.combobox.current(2)
        self.course_values[0].set(True)
        
    def on_button_click(self):
        popup_text = f"{self.name_textbox.get()}\n{self.combobox.get()}\n{self.residency_choice.get()[0:3].lower()}"
        popup_text += "\n("
        course_keys = list(self.courses.keys())
        for i, box in enumerate(self.course_values):
            if (box.get()):
                if (i > 0):
                    popup_text += ",\n"
                popup_text += (course_keys[i])
        popup_text += " )"

        messagebox.showinfo("Information", popup_text)


    def exit(self):
        self.destroy()

    def reset(self):
        self.name_textbox.delete(0, tk.END)
        for box in self.course_values:
            box.set(False)
        self.fullName = "Nerendra Pershad"
        self.setDefaultValues()
        
        
        
app = MainWindow()
app.mainloop()


