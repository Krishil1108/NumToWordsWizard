import num2words as n2w
from tkinter import *

def num_to_words():
    try:
        # Get the input number and convert it to a float
        given_num = float(num.get())
        # Convert the number to words
        num_in_word = n2w.num2words(given_num)
        # Display the result in capitalized form
        display.config(text=str(num_in_word).capitalize())
    except ValueError:
        # Handle invalid input
        display.config(text="Invalid input. Please enter a valid number.")

# Initialize the Tkinter root window
root = Tk()
root.title("Numbers to Words")
root.geometry("650x400")

num = StringVar()

# Add title
title = Label(root, text="Number to Words Converter",
               fg="Blue", font=("Arial", 20, 'bold')).place(x=180, y=10)

# Add supported formats description
formats_label = Label(root, text="Formats supported:", fg="green", font=("Arial", 10, 'bold')).place(x=100, y=70)
Label(root, text="1. Positives", fg="green", font=("Arial", 10)).place(x=200, y=90)
Label(root, text="2. Negatives", fg="green", font=("Arial", 10)).place(x=200, y=110)
Label(root, text="3. Zeros", fg="green", font=("Arial", 10)).place(x=200, y=130)
Label(root, text="4. Floating points/decimals", fg="green", font=("Arial", 10)).place(x=200, y=150)

# Add entry field for user input
num_entry_label = Label(root, text="Enter a number:", fg="Blue", font=("Arial", 15, 'bold')).place(x=50, y=200)
num_entry = Entry(root, textvariable=num, width=30).place(x=220, y=200)

# Add calculate button
btn = Button(root, text="Calculate", fg="green", font=("Arial", 10, 'bold'),
             command=num_to_words).place(x=280, y=230)

# Add label to display the result
display = Label(root, text="", fg="black", font=("Arial", 12, 'bold'), wraplength=600, justify="left")
display.place(x=10, y=300)

# Run the main event loop
root.mainloop()
