import tkinter as tk
from tkinter import StringVar
import random, string

root = tk.Tk()
root.geometry("200x200")
root.title("Password Generator")

def generate():
  password_len = int(password_len_input.get())
  small_letter = string.ascii_lowercase
  caps_letter = string.ascii_uppercase
  digits = string.digits
  special_char = string.punctuation
  all_list = []
  all_list.extend(list(small_letter))
  all_list.extend(list(caps_letter))
  all_list.extend(list(digits))
  all_list.extend(list(special_char))
  random.shuffle(all_list)
  password.set("".join(all_list[:password_len]))

length = tk.Label(root, text="Enter desired length of password")
length.pack()

password_len_input = tk.Entry(root, width=20)
password_len_input.pack()

generate_btn = tk.Button(root, text="Generate", command=generate)
generate_btn.pack()

password = StringVar()
display_password = tk.Entry(root, textvariable=password)
display_password.pack()

root.mainloop()