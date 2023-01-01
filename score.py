from tkinter import*
import time
def ButtonPressTracker():
	ButtonPressTracker.counter +=1 
	print(ButtonPressTracker.counter)
	label_5=Label(score,text=str(ButtonPressTracker.counter),bd='10')
	label_5.place(x=130,y=270)
	
ButtonPressTracker.counter =0
def ButtonPressTracker1():
	ButtonPressTracker1.counter1 +=1 
	print(ButtonPressTracker1.counter1)
	label_6=Label(score,text=str(ButtonPressTracker1.counter1),bd='10')
	label_6.place(x=340,y=270)
	
ButtonPressTracker1.counter1 =0

def timesnow():
    currentime = time.strftime ("%H:%M:%S")
    timelabel.config (text=currentime)

    timelabel.after(1000, timesnow)
	
score = Tk()
score.geometry('500x500')
photo_1= PhotoImage(file='morocco.png')
photo_2 = PhotoImage(file='croatia.png')
photo_1=photo_1.subsample(10,10)
photo_2=photo_2.subsample(16,16)
label_1=Label(score,image=photo_1)
label_1.place(x=100,y=100)
label_2=Label(score,image=photo_2)
label_2.place(x=300,y=100)
label_3=Label(score,text="MAR",bd='10')
label_3.place(x=120,y=170)
label_4=Label(score,text="CRO",bd='10')
label_4.place(x=330,y=170)
b1=Button(score,bg="red",height = 2,width = 5,command = ButtonPressTracker)
b1.place(x=123,y=220)
b2=Button(score,bg="red",height = 2,width = 5,command = ButtonPressTracker1)
b2.place(x=333,y=220)

timelabel = Label(score, font=("Courier", 44))
timelabel.place(x=100,y=300)
timesnow()

score.mainloop()