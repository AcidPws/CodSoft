
import tkinter as tk

#constant variables for colors
BLACK = "#000000"
HONEYDEW = "#E0EEE0"
WHITE = "#FFFFFF"
MINT = "#BDFCC9"
SLATE_GREY = "#2F4F4F"
GREY = "#F2F2F2"

#constant variables for font
SMALL_FONT = ('Arial',18)
LARGE_FONT = ('Arial',30,"bold")
DIGIT_FONT = ('Arial',24,"bold")
DEFAULT_FONT = ('Arial',20)

class calculator:
    def __init__(self):
        #creating the basic window for the calculator
        self.root = tk.Tk()
        self.root.geometry("320x500")
        self.root.title("Calculator")

        self.total_exp = ""
        self.current_exp = ""

        self.displayframe = self.create_displayframe()
        self.total_label, self.label = self.create_displaylabels()

        #creating 2 dictionaries for storing digits and operations
        self.digits = {
            7: (1,1), 8: (1,2), 9: (1,3),
            4:(2,1), 5:(2,2), 6: (2,3),
            1: (3,1), 2: (3,2), 3: (3,3),
            0: (4,2), '.': (4,1)
            }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        #making a buttonframe for the buttons in calculator
        self.buttonframe = self.create_buttonframe()
        
        self.buttonframe.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttonframe.rowconfigure(x, weight=1)
            self.buttonframe.columnconfigure(x, weight=1)

        #calling the button functions
        self.create_digitbuttons()
        self.create_operatorbuttons()
        self.create_equalsbutton()
        self.create_clearbutton()
        self.create_allclearbutton()

        self.root.mainloop()
    
    #funtion to show display of caculator operations
    def create_displaylabels(self):
        total_label = tk.Label(self.displayframe, text=self.total_exp, anchor=tk.E, bg=SLATE_GREY,
                               fg=HONEYDEW, font= SMALL_FONT, padx=24)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.displayframe, text=self.current_exp, anchor=tk.E, bg=SLATE_GREY,
                               fg=WHITE, font= LARGE_FONT, padx=24)
        label.pack(expand=True, fill="both")

        return total_label,label

    def create_displayframe(self):
        frame = tk.Frame(self.root, height=200, bg=SLATE_GREY)
        frame.pack(expand=True, fill="both")
        return frame
    
    #function to add expressions into the display pannel
    def add_to_exp(self,value):
        self.current_exp += str(value)
        self.update_label()

    def create_digitbuttons(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttonframe, text=str(digit), bg=GREY, fg=BLACK, 
                               font=DIGIT_FONT, borderwidth=0, command=lambda x= digit: self.add_to_exp(x))
            button.grid(row=grid_value[0], column=grid_value[1],sticky=tk.NSEW)
    
    def join_operator(self,operator):
        self.current_exp += operator
        self.total_exp += self.current_exp
        self.current_exp = ""
        self.update_total_label()
        self.update_label()

    def create_operatorbuttons(self):
        i = 0
        for operator,symbol in self.operations.items():
            button = tk.Button(self.buttonframe, text=symbol, bg=HONEYDEW, fg=BLACK,
                               font=DEFAULT_FONT, borderwidth=0, command=lambda x=operator: self.join_operator(x))
            button.grid(row=i ,column=4,sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_exp = ""
        self.update_label()

    def create_clearbutton(self):
        button = tk.Button(self.buttonframe, text="C", bg=HONEYDEW, fg=BLACK,
                               font=DEFAULT_FONT, borderwidth=0, command=self.clear)
        button.grid(row=0 ,column=2,columnspan=2, sticky=tk.NSEW)

    def allclear(self):
        self.current_exp = ""
        self.total_exp = ""
        self.update_label()
        self.update_total_label()

    def create_allclearbutton(self):
        button = tk.Button(self.buttonframe, text="AC", bg=HONEYDEW, fg=BLACK,
                               font=DEFAULT_FONT, borderwidth=0, command=self.allclear)
        button.grid(row=0 ,column=1, sticky=tk.NSEW)

    #function for performing the actual calculations
    def evaluate(self):
        self.total_exp += self.current_exp
        self.update_total_label()
        try: 
            self.current_exp = str(eval(self.total_exp))
            self.total_exp = ""
        except Exception as e:
            self.current_exp = "Error"
        finally:
            self.update_label()
        if self.current_exp == "Error" or (self.total_exp != self.current_exp):
            self.current_exp = ""
            self.total_exp = ""
    
    def create_equalsbutton(self):
        button = tk.Button(self.buttonframe, text="=", bg=MINT, fg=BLACK,
                               font=DEFAULT_FONT, borderwidth=0, command=self.evaluate)
        button.grid(row=4 ,column=3,columnspan=2, sticky=tk.NSEW)

    def create_buttonframe(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame
    
    def update_total_label(self):
        exp = self.total_exp
        for operator,symbol in self.operations.items():
            exp = exp.replace(operator,f"{symbol}")
        self.total_label.config(text=exp)

    def update_label(self):
        self.label.config(text=self.current_exp[:11])

calculator() #calling the class calculator
