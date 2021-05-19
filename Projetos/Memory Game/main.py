from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random

root = Tk()
root.title("Memory Game")

picked = []


#functions
def verifyNames():
    global e0,e1
    t0 = e0.get()
    t1 = e1.get()
    if len(t0) == 0 or len(t1) == 0:
        messagebox.showerror("ERRO","Um dos nomes não foi inserido! Tente novamente.")
    else:
        startGame(t0,t1)


ok=''
def selectCards():
    global ok
    global images
    global positions
    for i in range(0,20):
        atual = []
        while True:
            choiceImage = random.choice(images)
            if i != 1:
                for el in picked:
                    if choiceImage == el[0]:
                        ok = 'N'
                    else:
                        ok = 'S'
                        break
                if ok == 'S':
                    atual.append(choiceImage)
                    break
            else:
                atual.append(choiceImage)
        while True:
            choicePosition1 = random.choice(positions)
            choicePosition2 = random.choice(positions)
            if i != 1:
                while choicePosition2 == choicePosition1:
                    choicePosition2 = random.choice(positions)
                for el in picked:
                    if choicePosition1 == el[1]:
                        ok1 = 'N'
                    else:
                        ok1 = 'S'
                    if choicePosition2 == el[2]:
                        ok2 = 'N'
                    else:
                        ok2 = 'S'
                    if ok1 == ok2 == 'S':
                        break
        atual.append(choicePosition1)
        atual.append(choicePosition2)
        picked.append(atual[:])
                
clk = 0
def onClick(event,plc,val):
    global picked
    global clk
    if clk == 0:
        plc['image'] = picked[0][0]
        clk += 1
    else:
        plc['image'] = logoImage


def startGame(name1,name2):
    global label1
    global label0
    global e1
    global e0
    global bframe
    label0.destroy()
    label1.destroy()
    e0.destroy()
    e1.destroy()
    bframe.destroy()
    
    canvas = Canvas(root, bg="#ee0000", height=655, width=820, highlightthickness=3, highlightbackground="#000000")
    canvas.place(x=250,y=20)

    #first column
    canvas.create_rectangle(20,20,160,160,)
    canvas.create_rectangle(20,180,160,320,)
    canvas.create_rectangle(20,340,160,480,)
    canvas.create_rectangle(20,500,160,640,)

    canvasImage1 = canvas.create_image(90,90,image=logoImage)
    canvasImage2 = canvas.create_image(90,250,image=logoImage)
    canvasImage3 = canvas.create_image(90,410,image=logoImage)
    canvasImage4 = canvas.create_image(90,570,image=logoImage)

    #second column
    canvas.create_rectangle(180,20,320,160,)
    canvas.create_rectangle(180,180,320,320,)
    canvas.create_rectangle(180,340,320,480,)
    canvas.create_rectangle(180,500,320,640,)

    canvasImage5 = canvas.create_image(250,90,image=logoImage)
    canvasImage6 = canvas.create_image(250,250,image=logoImage)
    canvasImage7 = canvas.create_image(250,410,image=logoImage)
    canvasImage8 = canvas.create_image(250,570,image=logoImage)

    #third column
    canvas.create_rectangle(340,20,480,160,)
    canvas.create_rectangle(340,180,480,320,)
    canvas.create_rectangle(340,340,480,480,)
    canvas.create_rectangle(340,500,480,640,)

    canvasImage9 = canvas.create_image(410,90,image=logoImage)
    canvasImage10 = canvas.create_image(410,250,image=logoImage)
    canvasImage11 = canvas.create_image(410,410,image=logoImage)
    canvasImage12 = canvas.create_image(410,570,image=logoImage)

    #fourth column
    canvas.create_rectangle(500,20,640,160,)
    canvas.create_rectangle(500,180,640,320,)
    canvas.create_rectangle(500,340,640,480,)
    canvas.create_rectangle(500,500,640,640,)

    canvasImage13 = canvas.create_image(570,90,image=logoImage)
    canvasImage14 = canvas.create_image(570,250,image=logoImage)
    canvasImage15 = canvas.create_image(570,410,image=logoImage)
    canvasImage16 = canvas.create_image(570,570,image=logoImage)

    #fifth column
    canvas.create_rectangle(660,20,800,160,)
    canvas.create_rectangle(660,180,800,320,)
    canvas.create_rectangle(660,340,800,480,)
    canvas.create_rectangle(660,500,800,640,)
    
    canvasImage17 = canvas.create_image(730,90,image=logoImage)
    canvasImage18 = canvas.create_image(730,250,image=logoImage)
    canvasImage19 = canvas.create_image(730,410,image=logoImage)
    canvasImage20 = canvas.create_image(730,570,image=logoImage)

    selectCards()


#images directories
img0 = Image.open("C:\\Users\\rozia\\Desktop\\César\\Curso Python\\Python GUI\\Exercícios Adaptados\\Projetos\\Projetos\\Memory Game\\_images\\img0.png")
rimg0 = img0.resize((120,100), Image.ANTIALIAS)
cimg0 = ImageTk.PhotoImage(rimg0)

img1 = Image.open("C:\\Users\\rozia\\Desktop\\César\\Curso Python\\Python GUI\\Exercícios Adaptados\\Projetos\\Projetos\\Memory Game\\_images\\img1.png")
rimg1 = img1.resize((120,100), Image.ANTIALIAS)
cimg1 = ImageTk.PhotoImage(rimg1)

img2 = Image.open("C:\\Users\\rozia\\Desktop\\César\\Curso Python\\Python GUI\\Exercícios Adaptados\\Projetos\\Projetos\\Memory Game\\_images\\img2.png")
rimg2 = img2.resize((120,100), Image.ANTIALIAS)
cimg2 = ImageTk.PhotoImage(rimg2)

img3 = Image.open("C:\\Users\\rozia\\Desktop\\César\\Curso Python\\Python GUI\\Exercícios Adaptados\\Projetos\\Projetos\\Memory Game\\_images\\img3.png")
rimg3 = img3.resize((120,100), Image.ANTIALIAS)
cimg3 = ImageTk.PhotoImage(rimg3)

img4 = Image.open("C:\\Users\\rozia\\Desktop\\César\\Curso Python\\Python GUI\\Exercícios Adaptados\\Projetos\\Projetos\\Memory Game\\_images\\img4.png")
rimg4 = img4.resize((120,100), Image.ANTIALIAS)
cimg4 = ImageTk.PhotoImage(rimg4)

img5 = Image.open("C:\\Users\\rozia\\Desktop\\César\\Curso Python\\Python GUI\\Exercícios Adaptados\\Projetos\\Projetos\\Memory Game\\_images\\img5.png")
rimg5 = img5.resize((120,100), Image.ANTIALIAS)
cimg5 = ImageTk.PhotoImage(rimg5)

img6 = Image.open("C:\\Users\\rozia\\Desktop\\César\\Curso Python\\Python GUI\\Exercícios Adaptados\\Projetos\\Projetos\\Memory Game\\_images\\img6.png")
rimg6 = img6.resize((120,100), Image.ANTIALIAS)
cimg6 = ImageTk.PhotoImage(rimg6)

img7 = Image.open("C:\\Users\\rozia\\Desktop\\César\\Curso Python\\Python GUI\\Exercícios Adaptados\\Projetos\\Projetos\\Memory Game\\_images\\img7.png")
rimg7 = img7.resize((120,100), Image.ANTIALIAS)
cimg7 = ImageTk.PhotoImage(rimg7)

img8 = Image.open("C:\\Users\\rozia\\Desktop\\César\\Curso Python\\Python GUI\\Exercícios Adaptados\\Projetos\\Projetos\\Memory Game\\_images\\img8.png")
rimg8 = img8.resize((120,100), Image.ANTIALIAS)
cimg8 = ImageTk.PhotoImage(rimg8)

img9 = Image.open("C:\\Users\\rozia\\Desktop\\César\\Curso Python\\Python GUI\\Exercícios Adaptados\\Projetos\\Projetos\\Memory Game\\_images\\img9.png")
rimg9 = img9.resize((120,100), Image.ANTIALIAS)
cimg9 = ImageTk.PhotoImage(rimg9)

logo = Image.open("C:\\Users\\rozia\\Desktop\\César\\Curso Python\\Python GUI\\Exercícios Adaptados\\Projetos\\Projetos\\Memory Game\\_images\\logo.jpeg")
rlogo = logo.resize((140,140), Image.ANTIALIAS)
logoImage = ImageTk.PhotoImage(rlogo)

images = [cimg0,cimg1,cimg2,cimg3,cimg4,cimg5,cimg6,cimg7,cimg8,cimg9]
positions = [(90,90),(90,250),(90,410),(90,570),(250,90),(250,250),(250,410),(250,570),(410,90),(410,250),(410,410),(410,570),(570,90),(570,250),(570,410),(570,570),(730,90),(730,250),(730,410),(730,570)]

#creating login screen
label0 = Label(root, text="Jogador 1:", bg="#ee0000", fg="#000000", font=("Segoe UI", 11))
e0 = Entry(root, width=40, font=("Segoe UI",11))
label0.place(x=420,y=250)
e0.place(x=505, y=252)

label1 = Label(root, text="Jogador 2:", bg="#ee0000", fg="#000000", font=("Segoe UI", 11))
e1 = Entry(root, width=40,font=("Segoe UI",11))
label1.place(x=420,y=300)
e1.place(x=505,y=302)

bframe = LabelFrame(root, highlightthickness=3, highlightbackground="#000000")
startBtn = Button(bframe, text="Começar", bg="#ffffff", fg="#000000", font=("Segoe UI",12), bd=0, command=verifyNames)
startBtn.pack()
bframe.place(x=600,y=355)


#root sheets
root.resizable(0,0)
root["bg"] = "#ee0000"
root.state('zoomed')
root.mainloop()
