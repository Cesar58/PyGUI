from tkinter import *
from tkinter.font import  Font
from tkinter import messagebox
import random
import time
import threading


root = Tk()

#defining
score = 0
enable = 0
stop_bool = False

currentColor = ""
colorText = ("PURPLE", "BLUE", "RED", "ORANGE", "BROWN", "GREEN", "WHITE", "YELLOW")
colorFG = ("purple", "blue", "red", "orange", "brown", "green", "white", "yellow")

colorDict = {"purple":"PURPLE", 
			 "blue":"BLUE",
			 "red":"RED",
			 "orange":"ORANGE",
			 "brown":"BROWN",
			 "green":"GREEN",
			 "white":"WHITE",
			 "yellow":"YELLOW"}


def starting():
	global colorLabel
	global stop_bool
	global currentColor
	global userInput
	global bstart
	global breset
	global enable
	bstart["state"] = DISABLED
	breset["state"] = NORMAL
	userInput["state"] = NORMAL
	userInput.focus()
	randomText = random.choice(colorText)
	randomColor = random.choice(colorFG)
	currentColor = randomColor
	colorLabel["text"] = randomText
	colorLabel["fg"] = randomColor
	stop_bool = False
	enable = 1


def reseting():
	global timerLabel
	global colorLabel
	global stop_bool
	global currentColor
	global score
	global userInput
	global bstart
	global breset
	global scoreLabel
	global enable
	stop_bool = True
	enable = 0
	currentColor = ''
	score = 0
	bstart["state"] = NORMAL
	breset["state"] = DISABLED
	userInput["state"] = DISABLED
	timerLabel["text"] = "Game ends in: -"
	colorLabel["text"] = ' '
	scoreLabel["text"] = f'Your score: {score}'


def general(event):
	global userInput
	global currentColor
	global score
	if event.keysym == 'Return':
		it = userInput.get()
		inputText = it.upper()
		if colorDict[currentColor] == inputText:
			score += 1
		randomText = random.choice(colorText)
		randomColor = random.choice(colorFG)
		currentColor = randomColor
		colorLabel["text"] = randomText
		colorLabel["fg"] = randomColor
		scoreLabel["text"] = f'Your score: {score}'
		userInput.delete(0, END)


def endGame():
	global userInput
	global score
	global stop_bool
	global enable
	stop_bool = True
	enable = 0
	userInput.delete(0,END)
	userInput["state"] = DISABLED
	messagebox.showinfo('End Game', 'Final score: '+str(score))
	reseting()


def timer():
	global enable
	global stop_bool
	while True:
		time.sleep(1)
		if enable == 0:
			pass
		else:
			countdownTimer = 60
			for i in range(0,61):
				timerLabel["text"] = f'Game ends in: {countdownTimer}'
				time.sleep(1)
				countdownTimer -= 1
				if countdownTimer == 0:
					endGame()
					break
				if stop_bool:
					break


timerThread = threading.Thread(target=timer)
timerThread.start()


#fonts
helv13bold = Font(family='Helvetica', size=13, weight='bold')
helv15bold = Font(family='Helvetica', size=15, weight='bold')
helv17bold = Font(family='Helvetica', size=17, weight='bold')
helv20bold = Font(family='Helvetica', size=20, weight='bold')


#instruction text
instructionLabel = Label(root, text="Game Description: Enter the color of the words displayed below\nAnd keep in mind not to enter the text itself", bg='#000022', fg='#DDDDDD', font=helv13bold)

#score label
scoreLabel = Label(root, text=f'Your score: {score}', bg='#000022', fg='#BBFF05', font=helv17bold)

#words label
colorLabel = Label(root, text=' ',bg='#000022', fg='#BBFF05', font=helv17bold)

#timer label
timerLabel = Label(root, text="Game ends in: -", bg='#000022', fg='#BBFF05', font=helv13bold)

#user input
user_frame = Frame(root, highlightthickness=1, highlightbackground='#BBFF05', highlightcolor='#BBFF05')
userInput = Entry(user_frame, bd=0, bg='#000011', fg='#FFFFFF', insertbackground='#FFFFFF',width=40, font=helv15bold, borderwidth=2, state=DISABLED, disabledbackground='#222222')
userInput.bind("<Key>", general)
userInput.pack()

#control buttons
bstart = Button(root, text="Start", bg="#AA2222", fg="#FFFFFF", font=helv13bold, cursor='hand2' ,bd=0, padx=116, pady=8, command=starting)
breset = Button(root, text="Reset", bg="#2222AA", fg="#FFFFFF", font=helv13bold, cursor='hand2' ,bd=0, padx=116, pady=8, state=DISABLED, command=reseting)

#placing
instructionLabel.place(x=90, y=10)
scoreLabel.place(x=270,y=60)
colorLabel.place(x=310, y=205)
timerLabel.place(x=290, y=250)
user_frame.place(x=140, y=290)
bstart.place(x=80, y=400)
breset.place(x=360, y=400)

#root sheets
root.resizable(0,0)
root["bg"] = "#000022"
root.geometry("720x480")
root.mainloop()
