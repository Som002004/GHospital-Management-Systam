from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

win = Tk()
win.state('zoomed')
win.config(bg = 'Black')
#-----------------------------------
def pd():
    if e1.get() == "" or e2.get() == "" :
     messagebox.showerror('Error','All field are required')
    else:
       con = mysql.connector.connect(host = 'localhost',username='root',password='som@2004',database='hospitalmanagementsystam') 
       my_cursor = con.cursor()
       my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
          nameoftablets.get(),
          referenceno.get(),
          dose.get(),
          NoTablets.get(),
          issuedate.get(),
          expdate.get(),
          dailydose.get(),
          sideeffect.get(),
          nameofpatient.get(),
          Dob.get(),
          patientaddress.get()
       ))
       con.commit()
       fetch_data()
       con.close()
       messagebox.showinfo('Succesful','Your Response has been inserted')

def fetch_data():
    con = mysql.connector.connect(host = 'localhost',username='root',password='som@2004',database='hospitalmanagementsystam') 
    my_cursor = con.cursor()
    my_cursor.execute( 'select * from hospital')
    rows = my_cursor.fetchall()
    if len(rows)!=0:
       table.delete(* table.get_children())
       for items in rows:
          table.insert('',END,values=items)
          con.commit()
    con.close()
def get_data(event=''):
       
       cursor_row = table.focus()
       data = table.item(cursor_row)
       row = data['values']
       nameoftablets.set(row[0])
       referenceno.set(row[1])
       dose.set(row[2])
       NoTablets.set(row[3])
       issuedate.set(row[4])
       expdate.set(row[5])
       dailydose.set(row[6])
       sideeffect.set(row[7])
       nameofpatient.set(row[8])
       Dob.set(row[9])
       patientaddress.set(row[10])

def pre():
  t_box.insert(END, 'Name of Tablet: \t\t\t' + nameoftablets.get() + '\n')

           

def delete():
   con = mysql.connector.connect(host = 'localhost',username='root',password='som@2004',database='hospitalmanagementsystam') 
   my_cursor = con.cursor()
   querry = ('delete from  hospital where `Name of Tablets` = %s')
   value = (nameoftablets.get(), )
   my_cursor.execute(querry,value)
   con.commit()
   con.close()
   fetch_data()
   messagebox.showinfo('Deleted','Patient data has been deleted')
    
def clear():
    nameoftablets.set("")
    referenceno.set("")
    dose.set("")
    NoTablets.set("")
    issuedate.set("")
    expdate.set("")
    dailydose.set("")
    sideeffect.set("")
    nameofpatient.set("")
    Dob.set("")
    patientaddress.set("")

def exit():
    confirm = messagebox.askyesno('Confirmation','Are you sure')  
    if  confirm>0:
        win.destroy()
        return
#Heading
Label(win,text='Hospital Management System',font = 'Impack 31 bold',bg = 'Blue',fg = 'White').pack(fill = X)
#frame1
frame1 = Frame(win,bd = 15,relief =RIDGE)
frame1.place(x = 0 ,y = 54,width =1535 ,height =310 )
#Label Frame1
lf1 = LabelFrame(frame1,text = 'Patient Information',font = 'ariel 10 bold',bd=10 ,bg ='pink')
lf1.place(x=10,y=0,width=750,height=280)
#Label for patient information
Label(lf1,text = 'Name of Tablets',bg='pink').place(x=5,y=10)
Label(lf1,text = 'Reference No.',bg='pink').place(x=5,y=40)
Label(lf1,text = 'Dose',bg='pink').place(x=5,y=70)
Label(lf1,text = 'No.Tablets',bg='pink').place(x=5,y=100)
Label(lf1,text = 'Issue Date',bg='pink').place(x=5,y=130)
Label(lf1,text = 'Exp.Date',bg='pink').place(x=5,y=160)
Label(lf1,text = 'Daily Dose',bg='pink').place(x=5,y=190)
Label(lf1,text = 'Side Effect',bg='pink').place(x=5,y=220)
Label(lf1,text = 'Blood Pressure',bg='pink').place(x=370,y=10)
Label(lf1,text = 'Storege Device',bg='pink').place(x=370,y=40)
Label(lf1,text = 'Medication',bg='pink').place(x=370,y=70)
Label(lf1,text = 'Patient Id',bg='pink').place(x=370,y=100)
Label(lf1,text = 'Name of Patient',bg='pink').place(x=370,y=130)
Label(lf1,text = 'DOB',bg='pink').place(x=370,y=160)
Label(lf1,text = 'Patient Adress',bg='pink').place(x=370,y=190)
#Text Variables
nameoftablets = StringVar()
referenceno = StringVar()
dose = StringVar()
NoTablets = StringVar()
issuedate = StringVar()
expdate = StringVar()
dailydose= StringVar()
sideeffect = StringVar()
bloodpressure = StringVar()
storagedevice = StringVar()
medication = StringVar()
patientid = StringVar()
nameofpatient = StringVar()
Dob = StringVar()
patientaddress = StringVar()

#Entry field for labels
e1 = Entry(lf1,bd = 4,textvariable = nameoftablets)
e1.place(x=130,y=10,width =200)
e2 = Entry(lf1,bd = 4,textvariable =referenceno )
e2.place(x=130,y=40,width =200)
e3 = Entry(lf1,bd = 4,textvariable =dose )
e3.place(x=130,y=70,width =200)
e4 = Entry(lf1,bd = 4,textvariable = NoTablets)
e4.place(x=130,y=100,width =200)
e5 = Entry(lf1,bd = 4,textvariable = issuedate)
e5.place(x=130,y=130,width =200)
e6 = Entry(lf1,bd = 4,textvariable = expdate)
e6.place(x=130,y=160,width =200)
e7 = Entry(lf1,bd = 4,textvariable =dailydose )
e7.place(x=130,y=190,width =200)
e8 = Entry(lf1,bd = 4,textvariable = sideeffect)
e8.place(x=130,y=220,width =200)
e9 = Entry(lf1,bd = 4,textvariable = bloodpressure)
e9.place(x=500,y=10,width =200)
e10 = Entry(lf1,bd = 4,textvariable = storagedevice)
e10.place(x=500,y=40,width =200)
e11 = Entry(lf1,bd = 4,textvariable =medication )
e11.place(x=500,y=70,width =200)
e12 = Entry(lf1,bd = 4,textvariable = patientid)
e12.place(x=500,y=100,width =200)
e13 = Entry(lf1,bd = 4,textvariable = nameofpatient)
e13.place(x=500,y=130,width =200)
e14 = Entry(lf1,bd = 4,textvariable =Dob )
e14.place(x=500,y=160,width =200)
e15 = Entry(lf1,bd = 4,textvariable =patientaddress )
e15.place(x=500,y=190,width =200)

#Label Frame2 Pescribtion
lf2 = LabelFrame(frame1,text = 'Pescribtion',font = 'ariel 10 bold',bd=10 ,bg ='pink')
lf2.place(x=770,y=0,width=750,height=280)
#Text box for pescribtion
t_box = Text(lf2,font = 'ariel 10 bold',width = 400,bg = 'yellow',height = 30)
t_box.pack()


#frame2
frame2 = Frame(win,bd = 15,relief =RIDGE)
frame2.place(x = 0 ,y = 360,width =1535 ,height =310 )
# Scroll Bar Prescribtion Data
scroll_x = ttk.Scrollbar(frame2,orient = HORIZONTAL)
scroll_x.pack(side = 'bottom',fill=X)
scroll_y = ttk.Scrollbar(frame2,orient = VERTICAL)
scroll_y.pack(side = 'right',fill=Y)
table = ttk.Treeview(frame2,columns = ('not','ref','dose','nots','issdt','issd','expd','dd','se','pn','dob','pa'),xscrollcommand =scroll_y.set,yscrollcommand = scroll_x.set)
scroll_x = ttk.Scrollbar(command = table.xview)
scroll_y = ttk.Scrollbar(command = table.yview)
#Heading for Pescribtion Data
table.heading('not',text = 'Name of Tablets')
table.heading('ref',text = 'Reference No.')
table.heading('dose',text = 'Dose')
table.heading('nots',text = 'No.Tablets')
table.heading('issdt',text = 'Issue Date')
table.heading('expd',text = 'Exp.Date')
table.heading('dd',text = 'Daily Dose')
table.heading('se',text = 'Side Effect')
table.heading('pn',text = 'Name of Patient')
table.heading('dob',text = 'DOB')
table.heading('pa',text = 'Patient Adress')

table.column('not',width=100)
table.column('ref',width=100)
table.column('dose',width=100)
table.column('nots',width=100)
table.column('issdt',width=100)
table.column('expd',width=100)
table.column('dd',width=100)
table.column('se',width=100)
table.column('pn',width=100)
table.column('dob',width=100)
table.column('pa',width=100)

table.pack(fill = BOTH,expand =1)

#Delete Button
d_button = Button(text = 'Delete',font = 'ariel 15 bold',bg ='brown' ,fg = 'white',bd = 6,cursor = 'hand2',command=delete )
d_button.place(x = 0,y = 670,width = 330)
#Pescribtion Button
p_button = Button(text = 'Pescribtion',font = 'ariel 15 bold',bg ='purple' ,fg = 'white',bd = 6,cursor = 'hand2',command=pre )
p_button.place(x = 330,y = 670,width = 330)
#Save Pescribtion Button
s_button = Button(text = 'Save Pescribtion Data',font = 'ariel 15 bold',bg ='green' ,fg = 'white',bd = 6,cursor = 'hand2' ,command = pd)
s_button.place(x = 660,y = 670,width = 330)
#Clear Button
c_button = Button(text = 'Clear ',font = 'ariel 15 bold',bg ='blue' ,fg = 'white',bd = 6,cursor = 'hand2' ,command = clear)
c_button.place(x = 990,y = 670,width = 330)
#Exit Button
e_button = Button(text = 'Exit',font = 'ariel 15 bold',bg ='red' ,fg = 'white',bd = 6,cursor = 'hand2',command = exit )
e_button.place(x = 1320,y = 670,width = 220)
table.bind('<ButtonRelease-1>',get_data)
fetch_data()
mainloop()