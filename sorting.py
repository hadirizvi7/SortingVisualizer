from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

root = Tk()
root.title('Sorting Algorithms')
root.maxsize(900, 600)
root.config(bg='black')

selected_alg = StringVar()
data = []

def start():
	global data

	if not data:
		return

	if algMenu.get() == 'Quick Sort':
		quick_sort(data, 0, len(data) - 1, drawData, speedScale.get())

	elif algMenu.get() == 'Bubble Sort':
		bubble_sort(data, drawData, speedScale.get())

	elif algMenu.get() == 'Merge Sort':
		merge_sort(data, drawData, speedScale.get())

	colorArray = ['green'] *len(data)
	drawData(data, colorArray)

def Generate():
	global data
	print('Algorithm selected: ' + selected_alg.get())
	try:
		minVal = int(minEntry.get())

	except:
		minVal = 1

	try:
		maxVal = int(maxEntry.get())

	except:
		maxVal = 10

	try:
		size = int(sizeEntry.get())

	except:
		size = 10

	if minVal < 0:
		minVal = 0

	if maxVal > 100:
		maxVal = 100

	if size > 30 or size < 3:
		size = 25

	if minVal > maxVal:
		minVal, maxVal = maxVal, minVal

	data = []
	for value in range(size):
		data.append(random.randrange(minVal, maxVal+1))

	colorArray = ['red']*len(data)
	drawData(data, colorArray)

def drawData(data, colorArray):
	canvas.delete("all")
	Cheight = 380
	Cwidth = 600
	width = Cwidth/(len(data)+1)

	offset = 30
	spacing = 10
	normalized = [i/max(data) for i in data]

	for i, height in enumerate(normalized):
		x0 = (i*width) + offset + spacing
		y0 = Cheight - (height*340)

		x1 = ((i+1)*width)+offset
		y1 = Cheight

		canvas.create_rectangle(x0, y0, x1, y1, fill = "red")
		canvas.create_text(x0+2, y0, anchor=SW,  text=str(data[i]))
		

	root.update_idletasks()


UI_frame = Frame(root, width= 600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=start, bg='red').grid(row=0, column=3, padx=5, pady=5)

sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
