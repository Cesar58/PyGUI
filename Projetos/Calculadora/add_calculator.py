from tkinter import *

root = Tk()

def buttonClear():
	e0.delete(0, END)


n1 = 0
def add():
	global n1
	fn = e0.get()
	n1 = int(fn)
	e0.delete(0, END)



def onClick(num):
	current = e0.get()
	e0.delete(0, END)
	e0.insert(0, str(current) + str(num))


def equal(n):
	sn = e0.get()
	n2 = int(sn)
	result = n + n2
	strRes = f'{result}'
	e0.delete(0, END)
	e0.insert(0, strRes)



e0 = Entry(root, width=40, borderwidth=5)
e0.insert(0, "")
e0.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


b0 = Button(root, text="0", padx=42, pady=20, command=lambda: onClick(0))
b1 = Button(root, text="1", padx=42, pady=20, command=lambda: onClick(1))
b2 = Button(root, text="2", padx=42, pady=20, command=lambda: onClick(2))
b3 = Button(root, text="3", padx=42, pady=20, command=lambda: onClick(3))
b4 = Button(root, text="4", padx=42, pady=20, command=lambda: onClick(4))
b5 = Button(root, text="5", padx=42, pady=20, command=lambda: onClick(5))
b6 = Button(root, text="6", padx=42, pady=20, command=lambda: onClick(6))
b7 = Button(root, text="7", padx=42, pady=20, command=lambda: onClick(7))
b8 = Button(root, text="8", padx=42, pady=20, command=lambda: onClick(8))
b9 = Button(root, text="9", padx=42, pady=20, command=lambda: onClick(9))
badd = Button(root, text="+", padx=41, pady=20, command=add)
bequal = Button(root, text="=", padx=90, pady=20, command=lambda: equal(n1))
bclear = Button(root, text="Clear", padx=81, pady=20, command=buttonClear)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)
bclear.grid(row=4, column=1, columnspan=2)
badd.grid(row=5, column=0)
bequal.grid(row=5, column=1, columnspan=2)



root["bg"] = "#dddddd"
root.mainloop()