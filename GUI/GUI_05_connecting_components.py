# Code by @AmirMotefaker

# GUI - Connecting components to each other - submit

# # Solution 1
import tkinter as tk

window = tk.Tk()

def button_clicked():
    print('Clicked!')

name_entry = tk.Entry(
    window,
)

submit_button = tk.Button(
    window,
    text = 'Submit',
    command=button_clicked,
)

show_name_label = tk.Label(
    window,
    text = 'Test',
)

name_entry.pack()
submit_button.pack()
show_name_label.pack()

window.mainloop()



# # Solution 2 - name_entry.get()
import tkinter as tk

window = tk.Tk()

name_entry = tk.Entry(
    window,
)
show_name_label = tk.Label(
    window,
    text = 'Test',
)

def button_clicked():
    print(name_entry.get())

submit_button = tk.Button(
    window,
    text = 'Submit',
    command=button_clicked,
)

name_entry.pack()
submit_button.pack()
show_name_label.pack()

window.mainloop()



# Solution 3 - name_entry.get()
import tkinter as tk

window = tk.Tk()

name_entry = tk.Entry(
    window,
)
show_name_label = tk.Label(
    window,
    text = 'Test',
)

def button_clicked():
    show_name_label['text'] = name_entry.get()

submit_button = tk.Button(
    window,
    text = 'Submit',
    command=button_clicked,
)

name_entry.pack()
submit_button.pack()
show_name_label.pack()

window.mainloop()
