from tkinter import *

root = Tk()
root.title('Guess the Output')

def darkBG():
    global currentColor
    global darkBtn
    if currentColor == '#FFEEEE':
        root['bg'] = '#222222'
        darkBtn['text'] = 'Light Mode'
        darkBtn['fg'] = '#222222'
        darkBtn['bg'] = '#FFEEEE'
        currentColor = "#222222"
    else:
        root['bg'] = '#FFEEEE'
        darkBtn['text'] = 'Dark Mode'
        darkBtn['fg'] = '#FFEEEE'
        darkBtn['bg'] = '#222222'
        currentColor = "#FFEEEE"

currentColor = "#FFEEEE"
darkBtn = Button(root, text='Dark Mode', fg='#FFEEEE', bg='#222222', command=darkBG)
darkBtn.place(x=320,y=10)






root.geometry('400x600')
root.resizable(0,0)
root['bg'] = '#FFEEEE'
root.mainloop()
