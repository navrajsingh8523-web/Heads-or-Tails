import tkinter as tk
import random

#Creating a window
window = tk.Tk()
window.title('Choosing Heads or Tails')
window.geometry('400x300')

label = tk.Label(window, 
                 text='Heads or Tails ?')
label.pack()

result = tk.Label(window, 
                  text="")
result.pack()

def toss():
    choice = random.choice(['Heads','Tails'])
    result.config(text=choice)

button = tk.Button(window, 
                   text="toss", 
                   command=toss)
button.pack()

#Execute the main window
window.mainloop()