# Code by AmirMotefaker

# GUI - Button making

# # Solution 1 - Create Button
import tkinter as tk

window = tk.Tk()

button = tk.Button(
    master=window,
    text='Click me!',
)

button.pack()

window.mainloop()



# # Solution 2 - def button_clicked()
import tkinter as tk

window = tk.Tk()

def button_clicked():
    print('Clicked!')

button = tk.Button(
    master=window,
    text='Click me!',
    command=button_clicked,
)

button.pack()

window.mainloop()

# Output:
# Clicked!



# Solution 3 - lambda Instead of def button_clicked()
import tkinter as tk

window = tk.Tk()

button = tk.Button(
    master=window,
    text='Click me!',
    command=lambda: print('Clicked!'),
)

button.pack()

window.mainloop()

# Output:
# Clicked!
# Clicked!
# Clicked!
