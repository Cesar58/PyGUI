from tkinter import *
from tkinter.font import Font
import random


root = Tk()
root.title('WPM Game')

#defining
words = ['sight', 'defendant', 'thrust', 'stay', 'pupil', 'eavesdrop', 'chew', 'drown', 'clarify', 'uncertainty', 'scream', 'similar', 'missile', 'direct', 'salon', 'nuance', 'soar', 'donor', 'duty', 'brake', 'charismatic', 'balance', 'cabinet', 'yard', 'throat', 'distant', 'integration', 'prefer', 'excess', 'consumer', 'tough', 'soup', 'insist', 'memorandum', 'flavor', 'spare', 'chance', 'hiccup', 'flower', 'station', 'absorb', 'last', 'state', 'elapse', 'tension', 'snow', 'rational', 'sentence', 'joke', 'deteriorate','core', 'publicity', 'complication', 'heal', 'far', 'functional', 'printer', 'fair', 'sweater', 'relax', 'gallery', 'discriminate', 'college', 'pride', 'sheep', 'back', 'apathy', 'alive', 'traction', 'ice', 'ego', 'variety', 'inspire', 'commerce', 'switch', 'likely', 'active', 'forget', 'contrast', 'error', 'inquiry', 'race', 'truck', 'parameter', 'architecture', 'corruption', 'response', 'tumour', 'swear', 'captivate', 'potential', 'killer', 'credibility', 'formulate', 'kneel', 'variable', 'hammer', 'conference', 'insure', 'finger','bronze', 'mechanism', 'member', 'biography', 'outlet', 'bar', 'color', 'offspring', 'spirit', 'salmon', 'separate', 'he', 'junior', 'empire', 'clinic', 'dose', 'sow', 'equal', 'see', 'adjust', 'gun', 'presidency', 'mother', 'office', 'convince', 'breakfast', 'sit', 'bleed', 'plane', 'scholar', 'incongruous', 'eye', 'emotion', 'information', 'handy', 'way', 'hostile', 'overcharge', 'face', 'witness', 'iron', 'likely', 'favour', 'net', 'restrict', 'anniversary', 'influence', 'weed', 'fee', 'store', 'needle', 'reaction', 'pedestrian', 'switch', 'heavy', 'powder', 'argument', 'clarify', 'bland', 'collar', 'warn', 'brainstorm', 'white', 'pneumonia', 'threshold', 'inflation', 'gear', 'an', 'shot', 'mourning', 'border', 'achievement', 'exploit', 'quiet', 'old', 'girlfriend', 'spokesperson', 'fair', 'comment', 'court', 'bottom', 'principle', 'quote', 'layer', 'feeling', 'collection', 'direction', 'default', 'rib', 'raise', 'business', 'matter', 'cylinder', 'professor', 'decide', 'fabricate', 'case', 'promotion', 'permission', 'nominate']
onScreen = []

def levelSelector(event,number):
    global level20
    global level50
    global level100
    global level150
    global level200
    global words
    global frameWords
    global onScreen
    if number == 20:
        level20['font'] = helvBoldUnder
        level50['font'] = helvBold
        level100['font'] = helvBold
        level150['font'] = helvBold
        level200['font'] = helvBold
    elif number == 50:
        level20['font'] = helvBold
        level50['font'] = helvBoldUnder
        level100['font'] = helvBold
        level150['font'] = helvBold
        level200['font'] = helvBold
    elif number == 100:
        level20['font'] = helvBold
        level50['font'] = helvBold
        level100['font'] = helvBoldUnder
        level150['font'] = helvBold
        level200['font'] = helvBold
    elif number == 150:
        level20['font'] = helvBold
        level50['font'] = helvBold
        level100['font'] = helvBold
        level150['font'] = helvBoldUnder
        level200['font'] = helvBold
    else:
        level20['font'] = helvBold
        level50['font'] = helvBold
        level100['font'] = helvBold
        level150['font'] = helvBold
        level200['font'] = helvBoldUnder
    if len(onScreen) > 0:
        for el in onScreen:
            el.destroy()
        onScreen.clear()
    column_counter = 0
    row_counter = 0
    for w in range(0,number):
        toLabel = random.choice(words)
        wd = Label(frameWords, text=toLabel, bg='#3F2D54', fg='#EFFF08', font=helvWord)
        wd.grid(row=row_counter,column=column_counter)
        onScreen.append(wd)
        if column_counter == 7:
            column_counter = 0
            row_counter += 1
        else:
            column_counter += 1

    

#fonts
helvBold = Font(family='Helvetica',size=14,weight="bold")
helvBoldUnder = Font(family='Helvetica',size=14,weight="bold",underline=1)
helvWord = Font(family='Helvetica',size=13)
helv = Font(family='Helvetica',size=15)


#top menu
topFrame = Frame(root, bg='#1D0B32',width=701,height=35)

level20 = Label(topFrame, text='20', bg='#1D0B32', fg='#EFFF08', font=helvBold)
level20.place(x=10,y=2)
Label(topFrame, text='|', bg='#1D0B32', fg='#EFFF08', font=helvBold).place(x=40,y=2)

level50 = Label(topFrame, text='50', bg='#1D0B32', fg='#EFFF08', font=helvBold)
level50.place(x=50,y=2)
Label(topFrame, text='|', bg='#1D0B32', fg='#EFFF08', font=helvBold).place(x=80,y=2)

level100 = Label(topFrame, text='100', bg='#1D0B32', fg='#EFFF08', font=helvBold)
level100.place(x=90,y=2)
Label(topFrame, text='|', bg='#1D0B32', fg='#EFFF08', font=helvBold).place(x=130,y=2)

level150 = Label(topFrame, text='150', bg='#1D0B32', fg='#EFFF08', font=helvBold)
level150.place(x=140,y=2)
Label(topFrame, text='|', bg='#1D0B32', fg='#EFFF08', font=helvBold).place(x=180,y=2)

level200 = Label(topFrame, text='200', bg='#1D0B32', fg='#EFFF08', font=helvBold)
level200.place(x=190,y=2)


wpmLabel = Label(topFrame, text='WPM:        ', bg='#1D0B32', fg='#EFFF08', font=helvBold)
wpmLabel.place(x=500,y=2)
Label(topFrame, text='|', bg='#1D0B32', fg='#EFFF08', font=helvBold).place(x=600,y=1)

accLabel = Label(topFrame, text='ACC:        ', bg='#1D0B32', fg='#EFFF08', font=helvBold)
accLabel.place(x=610,y=2)

#binding
level20.bind('<Button-1>',lambda event: levelSelector(event,20))
level50.bind('<Button-1>',lambda event: levelSelector(event,50))
level100.bind('<Button-1>',lambda event: levelSelector(event,100))
level150.bind('<Button-1>',lambda event: levelSelector(event,150))
level200.bind('<Button-1>',lambda event: levelSelector(event,200))

#principal screen
frameWords = Frame(root, highlightthickness=1, bg='#3F2D54',width=650,height=320)


frameUser = Frame(root,highlightthickness=2,highlightcolor='#EFFF08',highlightbackground='#EFFF08')
userInput = Entry(frameUser, bd=0,bg='#1D0B32',fg="#FFFFFF",width=45,font=helv)
userInput.pack()

frameButton = Frame(root,highlightthickness=2,highlightcolor='#EFFF08',highlightbackground='#EFFF08')
btnRedo = Button(frameButton, text='Redo', bd=0, bg='#3F2D54', fg='#EFFF08', font=helvBold, padx=5, pady=5)
btnRedo.pack()


#placing on screen
topFrame.place(x=0,y=0)
frameWords.place(x=25,y=60)
frameUser.place(x=55,y=400)
frameButton.place(x=580,y=390)


#root sheets
root.geometry("700x480")
root.resizable(0,0)
root['bg'] = '#3F2D54'
root.mainloop()
