from tkinter import *
from tkinter import messagebox
import datetime
import random
import time
global low_r
global hi_r
global cnvs
global id_text
global id_needle

def update_gauge():
    global hi_r
    global low_r
    global cnvs
    global id_text
    global id_needle
    newvalue = random.randint(low_r,hi_r)
    cnvs.itemconfig(id_text,text = str(newvalue) + "°C")
    # Rescale value to angle range (0%=120deg, 100%=30 deg)
    angle = 120 * (hi_r - newvalue)/(hi_r - low_r) + 30
    cnvs.itemconfig(id_needle,start = angle)
    login.after(300, update_gauge)  
def humidity_indcator():
	global hi_r
	global low_r
	global cnvs
	global id_text
	global id_needle
	canvas_width = 400
	canvas_height =300
 
	hum_root = Tk()
 
	cnvs = Canvas(hum_root, width=canvas_width, height=canvas_height)
	cnvs.grid(row=2, column=1)
 
	coord = 10, 50, 350, 350 #define the size of the gauge
	low_r = 0 # chart low range
	hi_r = 100 # chart hi range
 
	# Create a background arc with a number of range lines
	numpies = 8
	for i in range(numpies):
		cnvs.create_arc(coord, start=(i*(120/numpies) +30), extent=(120/numpies), fill="white",  width=1)    
 
	# add hi/low bands
	cnvs.create_arc(coord, start=30, extent=120, outline="green", style= "arc", width=40)
	cnvs.create_arc(coord, start=30, extent=20, outline="red", style= "arc", width=40)
	cnvs.create_arc(coord, start=50, extent=20, outline="yellow", style= "arc", width=40)
	# add needle/value pointer
	id_needle = cnvs.create_arc(coord, start= 119, extent=1, width=7)
 
	# Add some labels
	cnvs.create_text(180,15,font="Times 20 italic bold", text="Humidity")
	cnvs.create_text(25,140,font="Times 12 bold", text=low_r)
	cnvs.create_text(330,140,font="Times 12 bold", text=hi_r)
	id_text = cnvs.create_text(170,210,font="Times 15 bold")
 
	hum_root.after(3000, update_gauge)
 
	hum_root.mainloop()

def temp_indcator():
    global hi_r
    global low_r
    global cnvs
    global id_text
    global id_needle
    canvas_width = 400
    canvas_height =300
   

    temp_root = Toplevel()
 
    cnvs = Canvas(temp_root, width=canvas_width, height=canvas_height)
    cnvs.grid(row=2, column=1)
 
    coord = 10, 50, 350, 350 #define the size of the gauge
    low_r =500 # chart low range
    hi_r = 950 # chart hi range
 
    # Create a background arc with a number of range lines
    numpies = 8
    for i in range(numpies):
        cnvs.create_arc(coord, start=(i*(120/numpies) +30), extent=(120/numpies), fill="white",  width=1)    
 
    # add hi/low bands
    cnvs.create_arc(coord, start=30, extent=120, outline="green", style= "arc", width=40)
    cnvs.create_arc(coord, start=30, extent=20, outline="red", style= "arc", width=40)
    cnvs.create_arc(coord, start=50, extent=20, outline="yellow", style= "arc", width=40)
    # add needle/value pointer
    id_needle = cnvs.create_arc(coord, start= 119, extent=1, width=7)
 
    # Add some labels
    cnvs.create_text(180,15,font="Times 20 italic bold", text="Temerature")
    cnvs.create_text(25,140,font="Times 12 bold", text=low_r)
    cnvs.create_text(330,140,font="Times 12 bold", text=hi_r)
    id_text = cnvs.create_text(170,210,font="Times 15 bold")
 
    temp_root.after(300, update_gauge)
 
    temp_root.mainloop()
def time_indicator():
	
	time_root=Toplevel()
	time_root.title("Time")
	time_root.geometry("700x500")
	time_root.resizable(False,False)
	photo_3=PhotoImage(file="earth.png")
	photo_3=photo_3.subsample(2,2)
	label_4=Label(time_root,image=photo_3,height=500,width=700)
	label_4.place(x=0,y=0)
	day_label=Label(time_root,background="black",fg="white",bd=1,font=('Helvetica bold', 20))
	day_label.place(x=300,y=200)
	now = datetime.datetime.now()
	hour_var=now.hour
	if hour_var>=12:
		day_label.config(text="  Night  ")
	elif hour_var<12:
		day_label.config(text="   Day   ")
	
	time_root.mainloop()
	

def Ok():
	uname = e1.get()
	password = e2.get()

	if(uname == "" and password == "") :
		messagebox.showinfo("", "Blank Not allowed")


	elif(uname == "admin" and password == "123"):
		messagebox.showinfo("","Login Success")
		
		screen = Toplevel(login)
		screen.title("Home Page")
		screen.geometry("700x500")
		screen.resizable(False,False)
		photo_1=PhotoImage(file="nrs.png")
		photo_1=photo_1.subsample(4,4)
		label_1=Label(screen,image=photo_1,bg="black",height=500,width=700)
		label_1.place(x=0,y=0)
		b1= Button(screen, text="Day",height = 3, width = 13,bg="yellow",fg="black",bd='10',command=time_indicator).place(x=300, y=40)
		b2= Button(screen, text="Tempurature",height = 3, width = 13,bg="yellow",fg="black",bd='10',command=temp_indcator).place(x=480, y=200)
		b3= Button(screen, text="Humidity",height = 3, width = 13,bg="yellow",fg="black",bd='10',command=humidity_indcator).place(x=100, y=200)
		screen.mainloop()
		

	else :
		messagebox.showinfo("","Incorrent Username and Password")


login = Tk()
login.title("Login")
login.geometry("700x500")
login.resizable(False,False)
global e1
global e2

photo_2=PhotoImage(file="m.png")
photo_2=photo_2.subsample(1,1)
label_1=Label(login,image=photo_2,bg="white",height=500,width=700)
label_1.place(x=0,y=0)

Label(login, text="UserName", bg="black",fg="white").place(x=200, y=160)
Label(login, text="Password", bg="black",fg="white").place(x=200, y=200)

e1 = Entry(login)
e1.place(x=340, y=160)

e2 = Entry(login)
e2.place(x=340, y=200)
e2.config(show="*")


Button(login, text="Login", command=Ok ,height = 3, width = 13,bg="black",fg="white",bd='10').place(x=200, y=250)

login.mainloop()