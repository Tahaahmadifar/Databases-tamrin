import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import * 
from tkinter import messagebox
from PIL import Image,ImageTk,ImageFile
import psycopg2
from psycopg2 import connect

root = ttk.Window(themename="cosmo")
root.title("register")
root.geometry("800x600")
root.resizable(width=False, height=False)

#Style
style = ttk.Style()
style.configure("Custom.TButton", background="cadetblue", highlightthickness=0, relief=tk.FLAT, focuscolor="transparent", bordercolor=LIGHT)
style.configure("Custom2.TButton", background="white", highlightthickness=0, relief=tk.FLAT, focuscolor="transparent", bordercolor=LIGHT)
style.configure("Custom.Label", font=("calibri",30,"bold"))
style.configure('Custom.TEntry', bordercolor="cadetblue")

#command
def checkfill_register():
   text1 = e1.get() 
   text2 = e2.get() 
   text3 = e3.get()  
   if text1 == "" or text2 == "" or text3 == "":
        messagebox.showerror(message='Fill In Your Information Completely')
   else:
       e1.delete(0,'end')
       e2.delete(0,'end')
       e3.delete(0,'end')
       connection_to_db = psycopg2.connect(host="Localhost", database='taha1', user='postgres', password='ta0509ha')
       connection = connection_to_db.cursor()
       connection.execute("insert into db(id, name, family) values(%s, %s, %s)", (text1,text2,text3))
       connection_to_db.commit()
       


def check_number(new_value): 
    if new_value.isdigit() or new_value == "": 
        return True 
    else: 
        messagebox.showerror(message='Only Numbers') 
        return False
    
def checkfill_search():
    text4 = e4.get()
    text5 = e5.get()
    text6 = e6.get()
    if text4 == "" or text5 == "" or text6 == "":
        messagebox.showerror(message='Fill In Your Information Completely')
    else:
        e4.delete(0,'end')
        e5.delete(0,'end')
        e6.delete(0,'end')
        connection_to_db = psycopg2.connect(host="Localhost", database='taha1', user='postgres', password='ta0509ha')
        connection = connection_to_db.cursor()
        connection.execute("select * from db")
        connection_to_db.commit()
        var_search = connection.fetchall()
        found = False
        for i in var_search:
            if int(text4) == i[0] and text5 == i[1] and text6 == i[2]:
                found = True
    if found:
        messagebox.showinfo(message="User with these characteristice exists")
    else:
        messagebox.showerror(message="There is no user with these characteristice exists")
 
for i in range(1,100):
    def page_search():
        b_register2.place_forget()
        b_search.place_forget()
        l_title_register.place_forget()
        l_id.place_forget()
        l_name.place_forget()
        l_family.place_forget()
        e1.place_forget()
        e2.place_forget()
        e3.place_forget()
        l_title_search.place(x=440,y=70)
        b_register1.place(x=400,y=200)
        l_id_s.place(x=400,y=230) 
        l_name_s.place(x=400,y=300)
        l_family_s.place(x=400,y=370)
        b_search1.place(x=550,y=200)
        b_search2.place(x=400,y=470)
        e4.place(x=400,y=260) 
        e5.place(x=400,y=330)
        e6.place(x=400,y=400)

for i in range(1,100):
    def page_login():
        l_title_search.place_forget()
        l_id_s.place_forget()
        l_name_s.place_forget()
        l_family_s.place_forget()
        b_search2.place_forget()
        b_register1.place_forget()
        e4.place_forget() 
        e5.place_forget()
        e6.place_forget()
        b_search.place(x=550,y=200)
        b_register.place(x=400,y=200)
        b_register2.place(x=400,y=470)
        l_search.place(x=539,y=149)
        l_title_register.place(x=440,y=70)
        l_id.place(x=400,y=230) 
        l_name.place(x=400,y=300)
        l_family.place(x=400,y=370)
        e1.place(x=400,y=260) 
        e2.place(x=400,y=330)
        e3.place(x=400,y=400)
    
    

#image
image1 = Image.open("tamrin.py/blue-white-leafy-background-vector_53876-136080.jpg").resize((250,600))
image2 = ImageTk.PhotoImage(image1)

#register
#Button
b_register = ttk.Button(root, style="Custom.TButton", padding=(44,-5), command=page_login)
b_register.place(x=400,y=200)
b_register1 = ttk.Button(root, style="Custom2.TButton", padding=(44,-5), command=page_login)
b_register1.place_forget()
b_search = ttk.Button(root, style="Custom2.TButton", padding=(44,-5), command=page_search)
b_search.place(x=550,y=200)
b_search1 = ttk.Button(root, style="Custom.TButton", padding=(44,-5), command=page_search)
b_search1.pack_forget()
b_search2 = ttk.Button(root, style="Custom.TButton", padding=(44,-5))
b_search2.place_forget()
b_register2 = ttk.Button(root,text="Register",style="Custom.TButton",width=34, command=checkfill_register) 
b_register2.place(x=400,y=470)



#Label
l_image = ttk.Label(root, image=image2)
l_image.place(x=-5,y=0)
l_register = ttk.Label(root, text="Register", foreground="cadetblue", font=("Calibry",13,"bold") ,padding=(13,10))
l_register.place(x=385,y=149)
l_search = ttk.Label(root, text="Search", foreground="cadetblue", font=("Calibry",14,"bold") ,padding=(13,10))
l_search.place(x=539,y=149)
l_title_register = ttk.Label(root, text="Register", style="Custom.Label", foreground="cadetblue")
l_title_register.place(x=440,y=70)
l_id = ttk.Label(root,text='Id',font=('tohama',11),foreground="cadetblue") 
l_id.place(x=400,y=230) 
l_name = ttk.Label(root,text='Name',font=('tohama',11),foreground="cadetblue") 
l_name.place(x=400,y=300)
l_family = ttk.Label(root,text='Family',font=('tohama',11),foreground="cadetblue") 
l_family.place(x=400,y=370)

#Entery
check_number1 = root.register(check_number)
e1 = ttk.Entry(root, background="cadetblue", foreground='black', width=35, style="Custom.TEntry", validate='key',validatecommand=(check_number1,'%P')) 
e1.place(x=400,y=260) 
e2 = ttk.Entry(root,foreground="black",width=35,style="Custom.TEntry") 
e2.place(x=400,y=330)
e3 = ttk.Entry(root,foreground="black",width=35,style="Custom.TEntry") 
e3.place(x=400,y=400)

#Search
#Button
b_search = ttk.Button(root, style="Custom2.TButton", padding=(44,-5), command=page_search)
b_search.place_forget()
b_search2 = ttk.Button(root,text="Search",style="Custom.TButton",width=34, command=checkfill_search) 
b_search2.pack_forget()

#Label
l_title_search = ttk.Label(root, text="Search", style="Custom.Label", foreground="cadetblue")
l_title_search.place_forget()
l_id_s = ttk.Label(root,text='Id',font=('tohama',11),foreground="cadetblue") 
l_id_s.place_forget()
l_name_s = ttk.Label(root,text='Name',font=('tohama',11),foreground="cadetblue") 
l_name_s.place_forget()
l_family_s = ttk.Label(root,text='Family',font=('tohama',11),foreground="cadetblue") 
l_family_s.place_forget()

#Entery
check_number1 = root.register(check_number)
e4 = ttk.Entry(root, background="cadetblue", foreground='black', width=35, style="Custom.TEntry", validate='key',validatecommand=(check_number1,'%P')) 
e4.place_forget()
e5 = ttk.Entry(root,foreground="black",width=35,style="Custom.TEntry") 
e5.place_forget()
e6 = ttk.Entry(root,foreground="black",width=35,style="Custom.TEntry") 
e6.place_forget()

root.mainloop()