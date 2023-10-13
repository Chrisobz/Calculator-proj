import tkinter as tk

calculation = ""

def add_to_calculation():
    pass

def evaluate_calculation():
    pass

def clear_field():
    pass

root = tk.Tk()
root.geometry("300x375")

#text field 

text_result = tk.Text(root, height=2, width=16, font=("Arial" , 25))
text_result.grid(columnspan=5)
root.mainloop()