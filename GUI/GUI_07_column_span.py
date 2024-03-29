# Code by @AmirMotefaker

# GUI - ColumnSpan

# # Solution 1 - ColumnSpan
import tkinter as tk

window = tk.Tk()

label_title = tk.Label(
    window,
    text='Enter you data',
)
label_title.grid(row=0, column=0, columnspan=2)

label_input_name = tk.Label(
    window,
    text = 'First Name: ',
)
entry_name = tk.Entry(
    window,
)


label_input_name.grid(row=1, column=0)
entry_name.grid(row=1, column=1)

label_input_last_name = tk.Label(
    window,
    text = 'Last Name: ',
)
entry_last_name = tk.Entry(
    window,
)

label_input_last_name.grid(row=2, column=0)
entry_last_name.grid(row=2, column=1)

label_input_age = tk.Label(
    window,
    text='Age: ',
)
entry_age = tk.Entry(
    window,
)


label_input_age.grid(row=3, column=0)
entry_age.grid(row=3, column=1)

window.mainloop()



# Solution 2 - ColumnSpan
import tkinter as tk

window = tk.Tk()

label_title = tk.Label(
    window,
    text='Enter you data',
)
label_title.grid(row=0, column=0, columnspan=2)

label_input_name = tk.Label(
    window,
    text = 'First Name: ',
)
entry_name = tk.Entry(
    window,
)


label_input_name.grid(row=1, column=0)
entry_name.grid(row=1, column=1)

label_input_last_name = tk.Label(
    window,
    text = 'Last Name: ',
)
entry_last_name = tk.Entry(
    window,
)

label_input_last_name.grid(row=2, column=0)
entry_last_name.grid(row=2, column=1)

label_input_age = tk.Label(
    window,
    text='Age: ',
)
entry_age = tk.Entry(
    window,
)


label_input_age.grid(row=3, column=0)
entry_age.grid(row=3, column=1)


submit_button = tk.Button(
    window,
    text='Submit'
)
submit_button.grid(row=4, column=0, columnspan=2)

window.mainloop()
