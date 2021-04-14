from tkinter import *


root = Tk()

def newClient(event):
	root.geometry("500x400")
	nameLabel = Label(root, text="Nome completo", bg="#dddddd")
	nameEntry = Entry(root, width=40)
	usernameLabel = Label(root, text="Nome de usuário", bg="#dddddd")
	usernameEntry = Entry(root, width=40)
	emailLabel = Label(root, text="E-mail", bg="#dddddd")
	emailEntry = Entry(root, width=40)
	passwordLabel2 = Label(root, text="Senha", bg="#dddddd")
	passwordEntry2 = Entry(root, width=40)
	verifyPassLabel = Label(root, text="Confirme sua Senha", bg="#dddddd")
	verifyPassEntry = Entry(root, width=40)
	submitButton = Button(root, text="Cadastrar")

	nameLabel.place(x=10,y=160)
	nameEntry.place(x=190,y=160)
	usernameLabel.place(x=10,y=200)
	usernameEntry.place(x=190,y=200)
	emailLabel.place(x=10,y=240)
	emailEntry.place(x=190,y=240)
	passwordLabel2.place(x=10,y=280)
	passwordEntry2.place(x=190,y=280)
	verifyPassLabel.place(x=10,y=320)
	verifyPassEntry.place(x=190,y=320)
	submitButton.place(x=210,y=360)



def verifyLogin(event):
	if event.keysym == 'Return':
		alertLabel["text"] = "Deu enter!"


logLabel = Label(root, text="Nome de usuário ou e-mail", bg="#dddddd")
logEntry = Entry(root, width=40)

passwordLabel = Label(root, text="Senha", bg="#dddddd")
passwordEntry = Entry(root, width=40)
passwordEntry.bind('<Key>', verifyLogin)

logLabel.place(x=10,y=20)
logEntry.place(x=190,y=20)
passwordLabel.place(x=10,y=60)
passwordEntry.place(x=190,y=60)

registerInf = Label(root, text="Não tem conta? Faça seu cadastro", fg="#0000ff", bg="#dddddd")
registerInf.place(x=150,y=110)

registerInf.bind('<Button-1>', newClient)

alertLabel = Label(root, text=' ', justify=CENTER, bg="#dddddd")
alertLabel.place(x=180,y=140)

root["bg"] = "#dddddd"
root.resizable(0,0)
root.geometry("500x190")
root.mainloop()