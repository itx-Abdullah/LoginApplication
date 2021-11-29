# import tkinter
from tkinter import *
from tkinter import messagebox, ttk


    

# create instance / window
window = Tk()

# set window on device screen
x = int((window.winfo_screenwidth() / 2) - 500)
y = int((window.winfo_screenheight() / 2) - 400)
window.geometry(f"1000x700+{x}+{y}")

# set window title
window.title("Login Application")

# set window background color 
window['bg'] = "#8db1ab"

# set resizeable false
window.resizable(False,False)

# Text Variables
username_input = StringVar()
password_input = StringVar()

def login():
    global username
    if username_input.get() == "" or password_input.get() == "":
        messagebox.showerror("Empty Credentials", "All fields are required!")
        username.focus()   
    elif username_input.get() != "python" or password_input.get() != "python":
        messagebox.showerror("Invalid Credentials", "Wrong username or password!")
        username.focus()   
    else:
        messagebox.showinfo("Login Succcessfully", f"Welcome {username_input.get()}")
        username_input.set("")
        password_input.set("")
        username.focus()    
        

# Login Frame
login_frame = Frame(window, bg = "#cee397", pady = 30 )
login_frame.place(x = 300, y = 150, w = 400, h = 400)

# Login Title
login_title = Label(login_frame, text = "Login", bg  = "#cee397", fg = "#587792", font = ("Cooper Black", 28, "bold"))
login_title.pack()



# Username Label 
username_label = Label(login_frame, text = "Username:", bg  = "#cee397", fg = "#587792", font = ("Courier", 18, "bold"), anchor = "w")
username_label.pack(fill = X, pady = (20, 0), padx = 35)

# Style TEntry 
ttk.Style().configure("TEntry", padding = "4 4 0 4", forground = "#000")
username = ttk.Entry(login_frame, font = ("Courier", 20, "bold"), textvariable = username_input)
username.pack()
# set autofoucus on username input
username.focus()


# Password Label and input
password_label = Label(login_frame, text = "Password:", bg  = "#cee397", fg = "#587792", font = ("Courier", 18, "bold"), anchor = "w")
password_label.pack(fill = X, pady = (20, 0), padx = 35)
password = ttk.Entry(login_frame, font = ("Courier", 20, "bold"), textvariable = password_input,  show = "*")
password.pack()

# Login Button
login_btn = Button(login_frame, text = "Login", bg = "#587792", activebackground = "#587792", fg = "#cee397", activeforeground = "#cee397" , bd = 0, font = ("Courier", 18, "bold"), cursor = "hand2", command  = login)
login_btn.pack(fill = X, padx = 38, pady = 25)

# run window
window.mainloop()