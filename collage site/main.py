import tkinter as tkr
from tkinter import *
from tkinter import ttk
import os
from PIL import ImageTk,Image
import webbrowser as wb
from tkinter import messagebox
def b20():
    wb.open_new('https://drive.google.com/file/d/1n0pfCp93KhQlYOyfjUFDRUcbA4aCf3_1/view')  
def b21():
    wb.open_new('https://www.jecrcfoundation.com/faculty-corner')  

def infom():
    app5 =tkr.Tk(__name__)
    app5.title('Info Student')
    app5.geometry('700x600')
    app5.iconbitmap('icon.ico')
    app5.configure(background='#ECECEC')
    # img_info = Image.open('image1.jpg')
    # img_resized_info = img_info.resize((100,100))
    # img7_info = ImageTk.PhotoImage(img_resized_info)
    # tkr.Label(app5, image=img7_info).place(x=20,y=30)
    tkr.Label(app5,text='Student Info',font=('Arial',20),fg='black',bg='#ECECEC').pack()
    tkr.Label(app5,text='Name- ',font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=140)
    tkr.Label(app5,text='Aryan arya',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=140)
    tkr.Label(app5,text='Branch- ',font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=170)
    tkr.Label(app5,text='IT',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=170)
    tkr.Label(app5,text="Father's Name- ",font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=200)
    tkr.Label(app5,text='Narendra arya ',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=200)
    tkr.Label(app5,text="Adderss- ",font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=230)
    tkr.Label(app5,text='2/105 sech no 10 b',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=230)
    tkr.Label(app5,text="Percentage(10th)-",font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=260)
    tkr.Label(app5,text='90%',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=260)
    tkr.Label(app5,text="Percentage(12th)-",font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=290)
    tkr.Label(app5,text='95%',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=290)
    tkr.Label(app5,text="REAP Rank-",font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=320)
    tkr.Label(app5,text='1500',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=320)
    tkr.Label(app5,text="Mobile No.-",font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=350)
    tkr.Label(app5,text='9275709852',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=350)
    tkr.Label(app5,text="Email-",font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=380)
    tkr.Label(app5,text='aryan@gmail.com',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=380)
    tkr.Button(app5,width=10,text='Go To Home',font=('Arial',10),bg='gray').place(x=560,y=550)
    app5.mainloop()

def b23():
    wb.open_new_tab('https://www.jecrcfoundation.com/faculty-corner')
def b24():
    app9 =tkr.Tk(__name__)
    app9.title('Info Teacher')
    app9.geometry('700x600')
    app9.iconbitmap('icon.ico')
    app9.configure(background='#ECECEC')
    # img = Image.open('image1.jpeg')
    # img_resized = img.resize((100,100))
    # img2 = ImageTk.PhotoImage(img_resized)
    # tkr.Label(app9, image=img2).place(x=20,y=30)
    tkr.Label(app9,text='Teacher Info',font=('Arial',20),fg='black',bg='#ECECEC').pack()
    tkr.Label(app9,text='Name- ',font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=140)
    tkr.Label(app9,text='Atishay Jain',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=140)
    tkr.Label(app9,text='Branch Head- ',font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=170)
    tkr.Label(app9,text='IT',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=170)
    tkr.Label(app9,text="Subject- ",font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=200)
    tkr.Label(app9,text='Object Oriented Programing',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=200)
    tkr.Label(app9,text="Adderss- ",font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=230)
    tkr.Label(app9,text='4A,sector3 rajnaghar',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=230)
    tkr.Label(app9,text="Mobile No.-",font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=260)
    tkr.Label(app9,text='92754569852',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=260)
    tkr.Label(app9,text="Email-",font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=290)
    tkr.Label(app9,text='atishay@gmail.com',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=290)
    tkr.Label(app9,text="Collage Rank-",font=('Arial',12),fg='black',bg='#ECECEC').place(x=20,y=320)
    tkr.Label(app9,text='8',font=('Arial',12),fg='black',bg='#ECECEC').place(x=155,y=320)
    tkr.Button(app9,width=10,text='Go To Home',font=('Arial',10),bg='gray').place(x=560,y=550)
    app9.mainloop()

def teacher_info():
    app6 =tkr.Tk(__name__)
    app6.title('Teacher Login')
    app6.geometry('400x600')
    app6.iconbitmap('icon.ico')
    app6.configure(background='#ECECEC')

    # img = Image.open('picture.webp')
    # img_resized = img.resize((100,100))
    # img2 = ImageTk.PhotoImage(img_resized)
    # tkr.Label(app6, image=img2).place(x=147,y=10)
    fv=tkr.Variable(app6)
    sv=tkr.Variable(app6)
    def cred1():
        email=fv.get()
        pasw=sv.get()

        if email =='atishay@gmail.com'and pasw=='123':
            app7 =tkr.Tk(__name__)
            app7.title("Teacher's Page")
            app7.geometry('400x300')
            app7.iconbitmap('icon.ico')
            app7.configure(background='#ECECEC')
            tkr.Label(app7,text='Welcome Student',font=('Arial',15),fg='black',bg='#ECECEC').pack()
            tkr.Button(app7,width=20,text='Info',command=b24,font=('Arial',12),bg='gray').place(x=105,y=60)
            tkr.Button(app7,width=20,text='Time Table',command=b20,font=('Arial',12),bg='gray').place(x=105,y=100)
            tkr.Button(app7,width=20,text='Teacher Corner',command=b23,font=('Arial',12),bg='gray').place(x=105,y=140)

            
        else:
            messagebox.showerror('Invalid Password','Login Failed')
    tkr.Label(app6,text='Welcome To JECRC',font=('Arial',20),fg='black',bg='#ECECEC').place(x=75,y=120)
    tkr.Label(app6,text='Enter Your Gmail',font=('Arial',14),fg='black',bg='#ECECEC').place(x=125,y=170)
    tkr.Label(app6,text='Enter Your Password',font=('Arial',14),fg='black',bg='#ECECEC').place(x=108,y=240)


    tkr.Entry(app6,width=20,textvariable=fv,font=('Arial',12)).place(x=106,y=200)
    tkr.Entry(app6,width=20,textvariable=sv,font=('Arial',12)).place(x=106,y=270)

    tkr.Button(app6,width=15,text='Login',command=cred1,font=('Arial',12),bg='gray').place(x=125,y=330)

    app6.mainloop()



counter=0
def next_pic():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter +=1

def form():
    wb.open_new_tab('https://forms.gle/j6Ro4vXJrEz1CbRHA')

def b2():
    wb.open_new_tab('https://www.jecrcfoundation.com/principal-message')
def b1():
    wb.open_new_tab('https://www.jecrcfoundation.com/computer-science-engineering')
def b3():
    wb.open_new_tab('https://www.jecrcfoundation.com/mechanical-engineering')
def b4():
    wb.open_new_tab('https://www.jecrcfoundation.com/mechanical-engineering')
def b5():
    wb.open_new_tab('https://www.jecrcfoundation.com/information-technology')
def b6():
    wb.open_new_tab('https://www.jecrcfoundation.com/civil-engineering')
def b7():
    wb.open_new_tab('https://www.jecrcfoundation.com/electric-engineering')
def b8():
    wb.open_new_tab('https://www.jecrcfoundation.com/ai')
def b9():
    wb.open_new_tab('https://www.jecrcfoundation.com/about-us')
def b10():
    wb.open_new_tab('https://www.jecrcfoundation.com/chairperson-message')
def b11():
    wb.open_new_tab('https://www.jecrcfoundation.com/registrar-message')    
def b12():
    wb.open_new_tab('https://www.jecrcfoundation.com/pdf/5.1.5(1).pdf')    
def b13():
    wb.open_new_tab('https://www.jecrcfoundation.com/alumni')    
def b14():
    wb.open_new_tab('https://www.jecrcfoundation.com/placement-stats/')    
def b15():
    wb.open_new_tab('https://www.jecrcfoundation.com/internships-and-industrial-visits')    
def b16():
    wb.open_new_tab('https://www.jecrcfoundation.com/placement-recruiters')    
def b17():
    wb.open_new_tab('https://www.jecrcfoundation.com/departmental-tpo')    
def b18():
    wb.open_new_tab('https://www.jecrcfoundation.com/pdf/Campus%20Drive.pdf')  
def b19():
    wb.open_new('https://www.jecrcfoundation.com/')  

def b21():
    wb.open_new('https://www.jecrcfoundation.com/fee')  





def timetable():
    app4 =tkr.Tk(__name__)
    app4.title('Time Table')
    app4.geometry('1100x630')
    app4.iconbitmap('icon.ico')
    app4.configure(background='#ECECEC')
    # img45 = Image.open('time_table.jpeg')
    # img_resized = img45.resize((1050,550))
    # img4 = ImageTk.PhotoImage(img_resized)
    # tkr.Label(app4, image=img4).place(x=20,y=30)
    tkr.Label(app4,text='Time Table',font=('Arial',15),fg='black',bg='#ECECEC').pack()
    tkr.Button(app4,width=10,text='Go To Home',font=('Arial',10),bg='gray').place(x=510,y=590)
    app4.mainloop()



def logins():
    app1 =tkr.Tk(__name__)
    app1.title('Student Login')
    app1.geometry('400x600')
    # app.iconbitmap('icon.ico')
    app1.configure(background='#ECECEC')

    # img = Image.open('picture.jpg')
    # # # img_resized = img.resize((100,100))
    # # # img2 = ImageTk.PhotoImage(img_resized)
    # tkr.Label(app, image=img2).place(x=147,y=10)
    fv=tkr.Variable(app1)
    sv=tkr.Variable(app1)
    def cred():
        email=fv.get()
        pasw=sv.get()

        if email =='aryan@gmail.com'and pasw=='123':
            app3 =tkr.Tk(__name__)
            app3.title('Student Page')
            app3.geometry('400x300')
            # app.iconbitmap('icon.ico')
            app3.configure(background='#ECECEC')
            tkr.Label(app3,text='Welcome Student',font=('Arial',15),fg='black',bg='#ECECEC').pack()
            tkr.Button(app3,width=20,text='Time Table',command=b20,font=('Arial',12),bg='gray').place(x=105,y=60)
            tkr.Button(app3,width=20,text='Info',command=infom,font=('Arial',12),bg='gray').place(x=105,y=100)
            tkr.Button(app3,width=20,text='PayFees',command=b21,font=('Arial',12),bg='gray').place(x=105,y=140)
            

        else:
            messagebox.showerror('Invalid Password','Login Failed')
    tkr.Label(app1,text='Welcome To JECRC',font=('Arial',20),fg='black',bg='#ECECEC').place(x=75,y=120)
    tkr.Label(app1,text='Enter Your Gmail',font=('Arial',14),fg='black',bg='#ECECEC').place(x=125,y=170)
    tkr.Label(app1,text='Enter Your Password',font=('Arial',14),fg='black',bg='#ECECEC').place(x=108,y=240)


    tkr.Entry(app1,width=20,textvariable=fv,font=('Arial',12)).place(x=106,y=200)
    tkr.Entry(app1,width=20,textvariable=sv,font=('Arial',12)).place(x=106,y=270)

    tkr.Button(app1,width=15,text='Login',command=cred,font=('Arial',12),bg='gray').place(x=125,y=330)

    app1.mainloop()


app=tkr.Tk(__name__)
app.title('Welcome Site')
app.geometry('3840x2160')
#app.iconbitmap('sorry.png.ico')
app.configure(background='#FFFFFF')

img=Image.open('jecrc.jpg')
img_resize=img.resize((300,150))
img2=ImageTk.PhotoImage(img_resize)


mb=  Menubutton ( app, text="Department",width=9,font=(10), relief=RAISED )
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label="Computer Science",command=b1,variable=mayoVar )
mb.menu.add_checkbutton ( label="Artifical Intellegance",command=b8,variable=mayoVar )
mb.menu.add_checkbutton ( label="Information Technology",command=b5,variable=mayoVar )
mb.menu.add_checkbutton ( label="Electronic & Communication",command=b4,variable=mayoVar )
mb.menu.add_checkbutton ( label="Mechanical Engineering",command=b3,variable=mayoVar )
mb.menu.add_checkbutton ( label="Civil Engineering",command=b6,variable=mayoVar )
mb.menu.add_checkbutton ( label="Electrical Engineering",command=b7,variable=mayoVar )



mb.place(x=900,y=270)



mb=  Menubutton ( app, text="AboutUs",width=9,font=(10), relief=RAISED )
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu
mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton ( label="About JECRC Foundation",command=b9,variable=mayoVar )
mb.menu.add_checkbutton ( label="Chairperson Message",command=b10,variable=mayoVar )
mb.menu.add_checkbutton ( label="Principal Message",command=b2,variable=mayoVar )
mb.menu.add_checkbutton ( label="Registar Message",command=b11,variable=mayoVar )
mb.menu.add_checkbutton ( label="Policy & Planning",command=b12,variable=mayoVar )
mb.menu.add_checkbutton ( label="Alumnis",command=b13,variable=mayoVar )
mb.place(x=1200,y=270)

mb=  Menubutton ( app, text="Placement",width=9,font=(10), relief=RAISED )
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu
mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton ( label="Placement Statistics",command=b14,variable=mayoVar )
mb.menu.add_checkbutton ( label="Intership",command=b15,variable=mayoVar )
mb.menu.add_checkbutton ( label="On Campus Company",command=b16,variable=mayoVar )
mb.menu.add_checkbutton ( label="Departmental TPO",command=b17,variable=mayoVar )
mb.menu.add_checkbutton ( label="Placement Gallery",command=b18,variable=mayoVar )
mb.place(x=600,y=270)



files=os.listdir('wallpaper')
img_array=[]
for file in files:
    img=Image.open(os.path.join('wallpaper',file))
    resized_image=img.resize((700,500))
    img_array.append(ImageTk.PhotoImage(resized_image))

img_label=Label(app,image=img_array[0])
img_label.place(x=600,y=350)



next_butn=Button(app,text='Next',width=10,fg='white',bg='grey',command=next_pic).place(x=920,y=900)
tkr.Label(app,image=img2).place(x=800,y=10)
tkr.Label(app, text="EMail:info@jecrcmail.com",font=(10)).place(x=1660,y=10)
tkr.Label(app, text="Contact:0141-277032",font=(10)).place(x=1680,y=40)
tkr.Button(app,text='Home',command=b19,width=14,font=(8)).place(x=10,y=10)
tkr.Button(app,text='Login(Student)',command=logins,width=14,font=(8)).place(x=1700,y=100)
tkr.Button(app,text='Login(Faculty)',command=teacher_info,width=14,font=(8)).place(x=1700,y=150)
tkr.Button(app,text='Admission',command=form,width=14,font=(10)).place(x=1700,y=200)
# tkr.Menubutton(app,text='Department',*option).place()


app.mainloop()
