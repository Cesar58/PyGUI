from tkinter import *
import random
import time
import threading


root = Tk()


def starting():
	global tentativas
	global colorLabel
	global stop_bool
	global currentColor
	global e
	global bstart
	global breset
	global cont
	bstart["state"] = DISABLED
	breset["state"] = NORMAL
	e["state"] = NORMAL
	e.focus()
	stop_bool = False
	cont += 1
	tentativas[cont].start()
	randomText = random.choice(colorText)
	randomColor = random.choice(colorFG)
	currentColor = randomColor
	colorLabel["text"] = randomText
	colorLabel["fg"] = randomColor


def reseting():
	global tentativas
	global timerLabel
	global colorLabel
	global stop_bool
	global currentColor
	global score
	global e
	global bstart
	global breset
	global scoreLabel
	global cont
	global tempo
	if tentativas[cont].is_alive():
		stop_bool = True
	currentColor = ''
	score = 0
	tempo = 60
	bstart["state"] = NORMAL
	breset["state"] = DISABLED
	e["state"] = DISABLED
	timerLabel["text"] = "Game ends in: -"
	colorLabel["text"] = ' '
	scoreLabel["text"] = f'Sua pontuação: {score}'


def general(event):
	global e
	global currentColor
	global score
	if event.keysym == 'Return':
		it = e.get()
		inputText = it.upper()
		if colorDict[currentColor] == inputText:
			score += 1
		randomText = random.choice(colorText)
		randomColor = random.choice(colorFG)
		currentColor = randomColor
		colorLabel["text"] = randomText
		colorLabel["fg"] = randomColor
		scoreLabel["text"] = f'Sua pontuação: {score}'
		e.delete(0, END)





def endGame():
	global e
	e.delete(0,END)
	e["state"] = DISABLED


def countdown():
	global tempo
	global stop_bool
	for i in range(0,61):
		timerLabel["text"] = f'Game ends in: {tempo}'
		time.sleep(1)
		tempo -= 1
		if tempo == 0:
			endGame()
		if stop_bool:
			break


score = 0
currentColor = ""

tempo = 60
stop_bool = False

colorText = ("ROXO", "AZUL", "VERMELHO", "LARANJA", "MARROM", "VERDE", "PRETO", "AMARELO")
colorFG = ("purple", "blue", "red", "orange", "brown", "green", "black", "yellow")

colorDict = {"purple":"ROXO", 
			 "blue":"AZUL",
			 "red":"VERMELHO",
			 "orange":"LARANJA",
			 "brown":"MARROM",
			 "green":"VERDE",
			 "black":"PRETO",
			 "yellow":"AMARELO"}


instructionLabel = Label(root, text="Instruções de Jogo: Você deve escrever a cor das palavras geradas \nna tela no local indicado, e não a cor descrita nas palavras", font=("Segoe UI", 15), fg="#444444", bg="#dddddd")
instructionLabel.place(x=60, y=40)

colorLabel = Label(root, text=' ', font=("Segoe UI", 17), bg="#dddddd", fg="#000000")
colorLabel.place(x=310, y=205)

timerLabel = Label(root, text="Game ends in: -", font=("Segoe UI", 15), bg="#dddddd", fg="#22aa22")
timerLabel.place(x=280, y=250)

cont = -1

t1 = threading.Thread(target=countdown)
t2 = threading.Thread(target=countdown)
t3 = threading.Thread(target=countdown)
t4 = threading.Thread(target=countdown)
t5 = threading.Thread(target=countdown)
t6 = threading.Thread(target=countdown)
t7 = threading.Thread(target=countdown)
t8 = threading.Thread(target=countdown)
t9 = threading.Thread(target=countdown)
t10 = threading.Thread(target=countdown)
t11 = threading.Thread(target=countdown)
t12 = threading.Thread(target=countdown)
t13 = threading.Thread(target=countdown)
t14 = threading.Thread(target=countdown)
t15 = threading.Thread(target=countdown)
t16 = threading.Thread(target=countdown)
t17 = threading.Thread(target=countdown)
t18 = threading.Thread(target=countdown)
t19 = threading.Thread(target=countdown)
t20 = threading.Thread(target=countdown)

tentativas = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20]

e = Entry(root, width=40, state=DISABLED)
e.bind("<Key>", general)
e.place(x=230, y=290)

scoreLabel = Label(root, text=f'Sua pontuação: {score}', font=("Segoe UI", 15), bg="#dddddd", fg="#000000")
scoreLabel.place(x=270,y=320)



bstart = Button(root, text="Começar", bg="#ffaaaa", fg="#ffffff", font=("Segoe UI",13), bd=0, padx=100, pady=8, command=starting)
bstart.place(x=75, y=400)

breset = Button(root, text="Resetar", bg="#aaaaff", fg="#ffffff", font=("Segoe UI",13), bd=0, padx=100, pady=8, state=DISABLED, command=reseting)
breset.place(x=353, y=400)

root.resizable(0,0)
root["bg"] = "#dddddd"
root.geometry("700x500")
root.mainloop()
