from tkinter import *
from tkinter import messagebox
import random
import time
import threading

root = Tk()
root.title('Genius')

#defining
sequel = []
userSequel = []
colors = ('red','yellow','blue','green')
gameRound = 0
counter = 0
score = 0
enable = 0
stop_timer = False

def startGame():
    global startGame_btn
    global newGame_btn
    startGame_btn['state'] = DISABLED
    newGame_btn['state'] = NORMAL
    roundCounter()

def restartGame():
    global startGame_btn
    global newGame_btn
    global sequel
    global gameRound
    global counter
    global score
    global enable
    global stop_timer
    startGame_btn['state'] = NORMAL
    newGame_btn['state'] = DISABLED
    sequel.clear()
    gameRound = 0
    counter = 0
    score = 0
    enable = 0
    stop_timer = True
    updateRound()
    updateScore()
    updateTime()


def roundCounter(s=False):
    global sequel
    global colors
    global gameRound
    global canvas
    global counter
    global enable
    global userSequel
    global score
    if s:
        score += 1
    userSequel.clear()
    updateTime(v=0)
    counter = 0
    gameRound += 1
    updateRound()
    updateScore()
    choosedColor = random.choice(colors)
    sequel.append(choosedColor)
    time_wait = len(sequel)*1150
    root.after(300,lambda: blink(sequel[0]))
    root.after(time_wait, onEnable)
            

def blink(color):
    global canvas
    global root
    global counter
    counter += 1
    if color == 'red':
        canvas.itemconfigure(redSquare, fill='#FF0000')
        canvas.after(1000,lambda: canvas.itemconfigure(redSquare, fill='#BB3333'))
    elif color == 'yellow':
        canvas.itemconfigure(yellowSquare, fill='#FFFF00')
        canvas.after(1000,lambda: canvas.itemconfigure(yellowSquare, fill='#BBBB33'))
    elif color == 'green':
        canvas.itemconfigure(greenSquare, fill='#00FF00')
        canvas.after(1000,lambda: canvas.itemconfigure(greenSquare, fill='#33BB33'))
    else:
        canvas.itemconfigure(blueSquare, fill='#0000FF')
        canvas.after(1000,lambda: canvas.itemconfigure(blueSquare, fill='#000033'))
    if counter == gameRound:
        pass
    else:
        root.after(1150,lambda: blink(sequel[counter]))
        

def timer():
    global enable
    global stop_timer
    while True:
        time.sleep(1)
        if enable == 0:
            pass
        else:
            countdownTimer = 20
            stop_timer = False
            for i in range(0,21):
                updateTime(v=countdownTimer)
                countdownTimer -= 1
                time.sleep(1)
                if countdownTimer == 0:
                    endGame('T')
                    break
                if stop_timer:
                    updateTime(v=0)
                    break


def sequelEntry(event,color):
    global userSequel
    global enable
    global stop_timer
    userSequel.append(color)
    nextRound = sequelMatch()
    if nextRound == 'Correct':
        enable = 0
        stop_timer = True
        roundCounter(s=True)
    elif nextRound == 'Incorrect':
        endGame()
    else:
        pass


def sequelMatch():
    global userSequel
    global sequel
    ok = ''
    for c in range(0,len(userSequel)):
        if userSequel[c] != sequel[c]:
            ok = 'Incorrect'
            break
        else:
            if len(sequel) > len(userSequel):
                ok = 'Ongoing'
            else:
                ok = 'Correct'
    return ok


def updateScore():
    global score
    global score_display
    score_display['text'] = f'Score: {score} points'


def onEnable():
    global enable
    enable = 1


def updateRound():
    global gameRound
    global round_display
    round_display['text'] = f'Round: {gameRound}'


def updateTime(v=0):
    global time_display
    time_display['text'] = f'Time: {v}'
    

def endGame(v='M'):
    global score
    global stop_timer
    global enable
    stop_timer = True
    enable = 0
    if v == 'M':
        messagebox.showinfo('Whooops... You missed it!','END GAME! You insert the wrong sequel.\nFinal Score: ' + str(score) + ' points')
    else:
        messagebox.showinfo('Whooops... You missed it!','END GAME! Time is over.\nFinal Score: ' + str(score) + ' points')
    restartGame()

#canvas
canvas = Canvas(root, bg='#222222', width=500, height=400, highlightthickness=0)
redSquare = canvas.create_rectangle(1,1,241,191,fill='#BB3333',outline='#FFFFFF')
yellowSquare = canvas.create_rectangle(259,1,499,191,fill='#BBBB33',outline='#FFFFFF')
greenSquare = canvas.create_rectangle(1,209,241,399,fill='#33BB33',outline='#FFFFFF')
blueSquare = canvas.create_rectangle(259,209,499,399,fill='#000033',outline='#FFFFFF')

#binding
canvas.tag_bind(redSquare,'<Button-1>',lambda event: sequelEntry(event,'red'))
canvas.tag_bind(yellowSquare,'<Button-1>',lambda event: sequelEntry(event,'yellow'))
canvas.tag_bind(greenSquare,'<Button-1>',lambda event: sequelEntry(event,'green'))
canvas.tag_bind(blueSquare,'<Button-1>',lambda event: sequelEntry(event,'blue'))


#control game
frame_b1 = Frame(root,highlightthickness=2,highlightbackground='#EFFF08',highlightcolor='#EFFF08')
frame_b2 = Frame(root,highlightthickness=2,highlightbackground='#EFFF08',highlightcolor='#EFFF08')

startGame_btn = Button(frame_b1,text='Start Game',bg='#333333',fg='#EFFF08',bd=0,font=('Segoe UI', 15, 'bold'),command=startGame)
startGame_btn.pack()

newGame_btn = Button(frame_b2,text='New Game',bg='#333333',fg='#EFFF08',bd=0,font=('Segoe UI', 15, 'bold'),state=DISABLED,command=restartGame)
newGame_btn.pack()

#dislays
score_display = Label(root,text='Score: 0 points',bg='#222222',fg='#EFFF08',font=('Segoe UI', 15, 'bold'))
time_display = Label(root, text='Time: 0',bg='#222222',fg='#EFFF08',font=('Segoe UI', 15, 'bold'))
round_display = Label(root, text='Round: 0',bg='#222222',fg='#EFFF08',font=('Segoe UI', 15, 'bold'))

countdown = threading.Thread(target=timer)
countdown.start()

#screen
canvas.place(x=170,y=40)
frame_b1.place(x=15,y=70)
frame_b2.place(x=15,y=140)
time_display.place(x=15,y=210)
round_display.place(x=15,y=240)
score_display.place(x=15,y=270)


root['bg'] = '#222222'
root.geometry('720x480')
root.resizable(0,0)
root.mainloop()
