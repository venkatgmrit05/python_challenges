import tkinter as tk

# create the main window
root = tk.Tk()
root.title("Adder")

# create the input fields
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

# create the "Add" button


def add():
    # get the user inputs and convert them to integers
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    # add the numbers and display the result
    result = num1 + num2
    tk.Label(root, text=result).pack()


button = tk.Button(root, text="Add", command=add)

# place the input fields and button in the window
entry1.pack()
entry2.pack()
button.pack()

# run the main loop
root.mainloop()
