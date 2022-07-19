# Code by @AmirMotefaker

# GUI - Getting input from the user - Entry

# # Solution 1 - Entry
import tkinter as tk

window = tk.Tk()

text = tk.Label(
    master=window,
    text='Hello World!',
)

# Entry
user_input = tk.Entry(window)

text.pack()
user_input.pack()

window.mainloop()



# Solution 2 - connect Entry and Label
import tkinter as tk

window = tk.Tk()

text_var = tk.StringVar()

# Label
text = tk.Label(
    master=window,
    textvariable=text_var,
)

# Entry
user_input = tk.Entry(
    window,
    textvariable=text_var,
)

text.pack()
user_input.pack()

window.mainloop()


# 
