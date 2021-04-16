from tkinter import *
from tkinter import messagebox
import random

root = Tk()

def zerar():
	for elem in elements:
		canvas.itemconfigure(elem, text=' ')
	Xbutton["state"] = NORMAL
	Obutton["state"] = NORMAL
	global escolha
	escolha = ''
	global jogadas
	jogadas = 1


def onClick(n, labelName1, labelName2):
	global escolha
	labelName1["state"] = DISABLED
	labelName2["state"] = DISABLED
	alertLabel["fg"] = "#ffffff"
	alertLabel["bg"] = "#aa0000"
	if n == 1:
		escolha = 'X'
	else:
		escolha = 'O'


def randomChoice():
	global elements
	return random.choice(elements)


def randomFill():
	global escolha
	cont = 0
	if escolha == 'X':
		randomEscolha = 'O'
	else:
		randomEscolha = 'X'
	for el in elements:
		canvText = canvas.itemcget(el, 'text')
		if canvText == ' ':
			cont += 1
	if cont > 1:
		rw = randomChoice()
		ctext = canvas.itemcget(rw, 'text')
		while ctext != ' ':
			rw = randomChoice()
			ctext = canvas.itemcget(rw, 'text')
		else:
			canvas.itemconfigure(rw, text=randomEscolha)
	else:
		pass


def winlos():
	global jogadas
	linha1 = [canvas.itemcget(spc11, 'text'), canvas.itemcget(spc12, 'text'), canvas.itemcget(spc13, 'text')]
	linha2 = [canvas.itemcget(spc21, 'text'), canvas.itemcget(spc22, 'text'), canvas.itemcget(spc23, 'text')]
	linha3 = [canvas.itemcget(spc31, 'text'), canvas.itemcget(spc32, 'text'), canvas.itemcget(spc33, 'text')]

	coluna1 = [canvas.itemcget(spc11,'text'), canvas.itemcget(spc21,'text'), canvas.itemcget(spc31,'text')]
	coluna2 = [canvas.itemcget(spc12,'text'), canvas.itemcget(spc22,'text'), canvas.itemcget(spc32,'text')]
	coluna3 = [canvas.itemcget(spc13,'text'), canvas.itemcget(spc23,'text'), canvas.itemcget(spc33,'text')]

	diagonal1 = [canvas.itemcget(spc11,'text'), canvas.itemcget(spc22,'text'), canvas.itemcget(spc33,'text')]
	diagonal2 = [canvas.itemcget(spc13,'text'), canvas.itemcget(spc22,'text'), canvas.itemcget(spc31,'text')]
	ok = False
	valor = 0
	if linha1[0] != ' ' or linha1[1] != ' ' or linha1[2] != ' ':
		if linha1[0] == linha1[1] == linha1[2]:
			ok = True
			valor = linha1[0]
	if linha2[0] != ' ' or linha2[1] != ' ' or linha2[2] != ' ':
		if linha2[0] == linha2[1] == linha2[2]:
			ok = True
			valor = linha2[0]
	if linha3[0] != ' ' or linha3[1] != ' ' or linha3[2] != ' ':
		if linha3[0] == linha3[1] == linha3[2]:
			ok = True
			valor = linha3[0]
	if coluna1[0] != ' ' or coluna1[1] != ' ' or coluna1[2] != ' ':
		if coluna1[0] == coluna1[1] == coluna1[2]:
			ok = True
			valor = coluna1[0]
	if coluna2[0] != ' ' or coluna2[1] != ' ' or coluna2[2] != ' ':
		if coluna2[0] == coluna2[1] == coluna2[2]:
			ok = True
			valor = coluna2[0]
	if coluna3[0] != ' ' or coluna3[1] != ' ' or coluna3[2] != ' ':
		if coluna3[0] == coluna3[1] == coluna3[2]:
			ok = True
			valor = coluna3[0]
	if diagonal1[0] != ' ' or diagonal1[1] != ' ' or diagonal1[2] != ' ':
		if diagonal1[0] == diagonal1[1] == diagonal1[2]:
			ok = True
			valor = diagonal1[0]
	if diagonal2[0] != ' ' or diagonal2[1] != ' ' or diagonal2[2] != ' ':
		if diagonal2[0] == diagonal2[1] == diagonal2[2]:
			ok = True
			valor = diagonal2[0]
	if jogadas == 5 and ok == False:
		ok = True
		valor = 'V'
	else:
		jogadas += 1
	linha1.clear()
	linha2.clear()
	linha3.clear()
	coluna1.clear()
	coluna2.clear()
	coluna3.clear()
	diagonal1.clear()
	diagonal2.clear()
	return ok,valor


def vencedor(e):
	if e == 'X' or e == 'O':
		restart = messagebox.askyesno("Resultado",f'{e} venceu!!! Jogar novamente?')
	else:
		restart = messagebox.askyesno("Resultado", "Deu VELHA!!! Jogar novamente?")
	if restart == 1:
		zerar()
	else:
		quit()

def fillSpace(event, element):
	global escolha
	if escolha == '':
		alertLabel["bg"] = "#ffffff"
		alertLabel["fg"] = "#aa0000"
	else:
		ctext = canvas.itemcget(element, 'text')
		if ctext == ' ':
			canvas.itemconfigure(element, text=escolha)
			randomFill()
			venceu,quem = winlos()
			if venceu:
				vencedor(quem)		
		else:
			pass


escolha = ''
jogadas = 1

canvas = Canvas(root, bg="#aa0000", highlightthickness=0, highlightbackground="#ffffff", height=300, width=300)
canvas.place(x=50,y=30)

horiz1 = canvas.create_line(0,100,305,100, fill="#ffffff", width=3)
horiz2 = canvas.create_line(0,200,305,200, fill="#ffffff", width=3)

vert1 = canvas.create_line(100,0,100,305, fill="#ffffff", width=3)
vert2 = canvas.create_line(200,0,200,305, fill="#ffffff", width=3)

var = StringVar()
var.set("Escolha sua opção")

alertLabel = Label(root, textvariable=var, bg="#aa0000", fg="#ffffff", font=("Segoe UI", 15))
alertLabel.place(x=120,y=350)

Xbutton = Button(root, text="X", font=("Segoe UI", 20), padx=5, bd=1, bg="#aa0000", fg="#ffffff", command=lambda: onClick(1,Xbutton,Obutton))
Xbutton.place(x=130, y=400)

Obutton = Button(root, text="O", font=("Segoe UI", 20), padx=4, bd=1, bg="#aa0000", fg="#ffffff", command=lambda: onClick(0,Xbutton,Obutton))
Obutton.place(x=230, y=400)

spc11 = canvas.create_text(50,50,text=" ", fill="#ffffff", font=("Segoe UI", 50))
spc12 = canvas.create_text(150,50, text=" ", fill="#ffffff", font=("Segoe UI", 50))
spc13 = canvas.create_text(250,50, text=" ", fill="#ffffff", font=("Segoe UI", 50))
spc21 = canvas.create_text(50,150, text=" ", fill="#ffffff", font=("Segoe UI", 50))
spc22 = canvas.create_text(150,150, text=" ", fill="#ffffff", font=("Segoe UI", 50))
spc23 = canvas.create_text(250,150, text=" ", fill="#ffffff", font=("Segoe UI", 50))
spc31 = canvas.create_text(50,250, text=" ", fill="#ffffff", font=("Segoe UI", 50))
spc32 = canvas.create_text(150,250, text=" ", fill="#ffffff", font=("Segoe UI", 50))
spc33 = canvas.create_text(250,250, text=" ", fill="#ffffff", font=("Segoe UI", 50))


canvas.tag_bind(spc11, "<Button-1>", lambda event: fillSpace(event, spc11))
canvas.tag_bind(spc12, "<Button-1>", lambda event: fillSpace(event, spc12))
canvas.tag_bind(spc13, "<Button-1>", lambda event: fillSpace(event, spc13))
canvas.tag_bind(spc21, "<Button-1>", lambda event: fillSpace(event, spc21))
canvas.tag_bind(spc22, "<Button-1>", lambda event: fillSpace(event, spc22))
canvas.tag_bind(spc23, "<Button-1>", lambda event: fillSpace(event, spc23))
canvas.tag_bind(spc31, "<Button-1>", lambda event: fillSpace(event, spc31))
canvas.tag_bind(spc32, "<Button-1>", lambda event: fillSpace(event, spc32))
canvas.tag_bind(spc33, "<Button-1>", lambda event: fillSpace(event, spc33))


elements = [spc11, spc12, spc13, spc21, spc22, spc23, spc31, spc32, spc33]



root["bg"] = "#aa0000"
root.resizable(0, 0)
root.geometry("400x500")
root.mainloop()
