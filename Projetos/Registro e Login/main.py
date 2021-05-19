from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Login & Registration')
titleLabel = Label(root, text="Login & Registration", bg="#dddddd", font=('Segoe UI',11))
titleLabel.place(x=185,y=10)

clicked = 0

#functions
def newAccount(event):
    global clicked
    global root
    if clicked == 0:
        root.geometry("500x490")
        clicked = 1
    else:
        root.geometry("500x220")
        clicked = 0


def login():
    global username_input
    global password_input
    ok = False
    un = username_input.get()
    pw = password_input.get()
    users_file = open('users.txt','r')
    uv = users_file.read().split('\n')
    users = []
    for i in range(0,len(uv)-1):
        current = uv[i].split('  ')
        users.append(current[:])
        current.clear()
    for sl in users:
        if sl[2] == un and sl[3] == pw:
            ok = True
            break
        else:
            ok = False
    if ok:
        newWindow()
    else:
        messagebox.showerror("ERROR","Incorrect username or password!")
    users_file.close()
    users.clear()


def newWindow():
    topRoot = Toplevel()
    topRoot.geometry('500x230')
    topRoot['bg'] = "#dddddd"
    topRoot.resizable(0,0)
    mesLabel = Label(topRoot, text='Sucessful login!', bg='#dddddd', font=('Segoe UI', 11))
    mesLabel.place(x=190,y=100)


def registration(name,email,username,password,cpassword):
    global root
    global name_input
    global email_input
    global new_username_input
    global new_password_input
    global confirm_password_input
    if password == cpassword:
        users_file = open("users.txt",'a+')
        regTetx = f'{name}  {email}  {username}  {password}\n'
        users_file.write(regTetx)
        users_file.close()
        messagebox.showinfo('Finished','User sucessfully registered!')
        root.geometry('500x220')
        name_input.insert(2,'')
        email_input.insert(3,'')
        new_username_input.insert(4,'')
        new_password_input.insert(5, '')
        confirm_password_input.insert(6,'')
    else:
        messagebox.showerror('ERROR','Passwords are differents!')



#creating
username = Label(root, text="Username:",bg="#dddddd",font=('Segoe UI',11))
username_input = Entry(root, width=40,font=('Segoe UI',11))
password = Label(root, text="Password:",bg="#dddddd",font=('Segoe UI',11))
password_input = Entry(root, width=40,font=('Segoe UI',11))
login_button = Button(root, text="Login", bg="#bbbbbb", font=('Segoe UI', 11), command=login)
new_user = Label(root, text="Create Account", bg="#dddddd", fg="#0000ff", font=('Segoe UI', 11))
new_user.bind("<Button-1>",newAccount)
name_label = Label(root, text="Name:", bg="#dddddd", font=('Segoe UI', 11))
name_input = Entry(root, width=40, font=('Segoe UI', 11))
email_label = Label(root, text="E-mail:", bg="#dddddd", font=('Segoe UI', 11))
email_input = Entry(root, width=40, font=('Segoe UI', 11))
new_username_label = Label(root, text="Username:", bg="#dddddd", font=('Segoe UI', 11))
new_username_input = Entry(root, width=40, font=('Segoe UI', 11))
new_password_label = Label(root, text="Password:", bg="#dddddd", font=('Segoe UI', 11))
new_password_input = Entry(root, width=40, font=('Segoe UI', 11))
confirm_password_label = Label(root, text='Confirm Password:', bg="#dddddd", font=('Segoe UI', 11))
confirm_password_input = Entry(root, width=40, font=('Segoe UI',11))
reg_button = Button(root, text="Register new account", bg="#bbbbbb", font=('Segoe UI',11), command= lambda: registration(name_input.get(),email_input.get(),new_username_input.get(),new_password_input.get(),confirm_password_input.get()))

#place on screen
username.place(x=20,y=60)
username_input.place(x=150,y=60)
password.place(x=20,y=100)
password_input.place(x=150,y=100)
login_button.place(x=230,y=140)
new_user.place(x=200,y=190)
name_label.place(x=20,y=220)
name_input.place(x=150,y=220)
email_label.place(x=20, y=260)
email_input.place(x=150,y=260)
new_username_label.place(x=20,y=300)
new_username_input.place(x=150,y=300)
new_password_label.place(x=20,y=340)
new_password_input.place(x=150,y=340)
confirm_password_label.place(x=20,y=380)
confirm_password_input.place(x=150,y=380)
reg_button.place(x=170,y=420)

#root sheets
root["bg"] = "#dddddd"
root.resizable(0,0)
root.geometry("500x220")
root.mainloop()