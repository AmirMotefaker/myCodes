# Code by @AmirMotefaker

# GUI - Display text in window

# # Solution 1
import tkinter as tk

window = tk.Tk()

# label - .pack()
text = tk.Label(text='Hello World!')
text.pack()

window.mainloop()



# # Solution 2
import tkinter as tk

window = tk.Tk()

# label - .pack()
text1 = tk.Label(text='Hello World1!')
text1.pack()

text2 = tk.Label(text='Hello World2!')
text2.pack()

window.mainloop()



# Solution 3
import tkinter as tk

window = tk.Tk()

# label - .pack()
text1 = tk.Label(text='Hello World1!')
text2 = tk.Label(text='Hello World2!')

text2.pack()
text1.pack()

window.mainloop()
