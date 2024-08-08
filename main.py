import tkinter
from tkinter import *
window = tkinter.Tk()
window.title("BMI Calculator")
window.wm_minsize(300,300)

w_label = tkinter.Label(text="Enter Your Weight (kg)")
w_label.config(pady=10)
w_label.pack()

enter_weight = tkinter.Entry(width=20)
enter_weight.pack()

h_label = tkinter.Label(text="Enter your height (cm)")
h_label.config(pady=10)
h_label.pack()

enter_height = tkinter.Entry(width=20)

enter_height.pack()

def getvalue():
    user_height = enter_height.get()
    user_weight = enter_weight.get()
    if user_height=="" or user_weight=="":
        result_label.config(text="Enter your height and weight!")
    else:
        try:
            bmi = float(user_weight) / (float(user_height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Just numbers!")








c_button = Button(text="Calculate", width=15, command=getvalue)

c_button.pack()

result_label = tkinter.Label(text="")
result_label.config(pady=10)
result_label.pack()

def write_result(bmi):
    result_string= f"Your BMI is: {round(bmi,2)}. You are "
    if bmi <=16:
        result_string += "Severe Thinness"
    elif bmi > 16 and bmi <=17:
        result_string += "Moderate Thinness"
    elif bmi >17 and bmi <=18.5:
        result_string += "Mild Thinness"
    elif  bmi >18.5 and bmi <=25:
        result_string += "Normal"
    elif  bmi >25 and bmi <=30:
        result_string += "Pre-obese"
    elif  bmi >30 and bmi <=35:
        result_string += "Obese class1"
    elif  bmi >35 and bmi <=40:
        result_string += "Obese class2"
    else:
        result_string += "Obese class3"
    return result_string

window.mainloop()
