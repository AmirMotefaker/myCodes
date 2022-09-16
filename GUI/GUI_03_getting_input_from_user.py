# Code by AmirMotefaker

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



# # Solution 2 - connect Entry and Label
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



# # Solution 3 - .pack(side=tk.LEFT)
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

user_input.pack(side=tk.LEFT)
text.pack(side=tk.LEFT)


window.mainloop()



# # Solution 4 - .pack()
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

name_text = tk.Label(
    master=window,
    text='First Name: ',
)

name_text.pack(side=tk.LEFT)
user_input.pack(side=tk.LEFT)
text.pack(side=tk.LEFT)


window.mainloop()



# Solution 5 - from tkinter import LEFT, BOTTOM
import tkinter as tk
from tkinter import LEFT, BOTTOM

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

name_text = tk.Label(
    master=window,
    text='First Name: ',
)

name_text.pack(side=LEFT)
user_input.pack(side=LEFT)
text.pack(side=LEFT)


window.mainloop()
