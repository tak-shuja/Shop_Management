from modules import *


def add_customer():
    global addScr, en1, en2, lb3,en4,en5
    addScr = Toplevel(root)
    addScr.geometry("600x500")
    addScr.minsize(height=400, width=600)
    addScr.maxsize(height=500, width=600)

    # Name of customer

    lb1 = Label(addScr, text='Name- ', font=(23))
    lb1.place(relx=0.2, rely=0.35)

    en1 = Entry(addScr, width=30,)
    en1.config(highlightbackground='black')
    en1.place(relheight=0.05, relx=0.32, rely=0.35)

    # Address of customer
    lb2 = Label(addScr, text="Address- ", font=(23))
    lb2.place(relx=0.18, rely=0.45)

    en2 = Entry(addScr, width=30,)
    en2.config(highlightbackground='black')
    en2.place(relheight=0.05, relx=0.32, rely=0.45)

    # Paid Amount
    lb4 = Label(addScr,text="Paid amount- ",font=(23))
    lb4.place(relx=0.12,rely=0.55)

    en4 = Entry(addScr, width=30,)
    en4.config(highlightbackground='black')
    en4.place(relheight=0.05, relx=0.32, rely=0.55)

    # Unpaid Amount
    lb5 = Label(addScr,text="Unpaid amount- ",font=(23))
    lb5.place(relx=0.09,rely=0.65)

    en5 = Entry(addScr, width=30,)
    en5.config(highlightbackground='black')
    en5.place(relheight=0.05, relx=0.32, rely=0.65)
    # Submit button

    b1 = Button(addScr, text='Submit', background='black',
                foreground='white', command=submit)
    b1.place(relx=0.32, rely=0.85, relheight=0.07)

    # Exit button

    b2 = Button(addScr, text='Exit', fg='white',
                bg='black', width=6, command=addScr.destroy)
    b2.place(relx=0.58, rely=0.85, relheight=0.07)

    # Confirmation message

    lb3 = Label(addScr, text='')
    lb3.place(relx=0.32, rely=0.75)

    addScr.mainloop()


def clr_txt():
    lb3.config(text='')

# Submit


def submit():
    name = en1.get()
    address = en2.get()
    paid = "Rs "+en4.get()
    unpaid = "Rs "+en5.get()
    time = strftime("%I:%M:%S %p")
    date = strftime(f"%d-%m-{datetime.now().year}")
    name, address = name.title(), address.title()
    if len(name) == 0:
        lb3.config(text="Name can not be empty!",
                   foreground='red')
        lb3.after(1300, clr_txt)
    elif len(address) == 0:
        lb3.config(text="Address can not be empty!",
                   foreground='red')
        lb3.after(1300, clr_txt)

    else:
        sql = 'insert ignore into customers (name,address,paid,unpaid,time,date) values(%s,%s,%s,%s,%s,%s)'
        val = (name, address, paid, unpaid, time, date)
        cursor.execute(sql, val)
        try:    
            mydb.commit()
            lb3.config(text="Records successfully inserted", foreground='green')
            lb3.after(1000, clr_txt)
            en1.delete(0, END)
            en2.delete(0, END)
        except:
            messagebox.showerror("Error",'Name already registered')
        # print(len(name), len(address))


def delete():

    ask = messagebox.askyesno(
        "Clear Records!", "Are you sure you want to clear all records?")
    if ask == True:

        user_name = user_e.get()
        user_password = pass_e.get()

        # print(user_name, user_password)

        cursor.execute(
            "select * from authentication where name=%s and password = %s", (user_name, user_password))

        result = cursor.fetchone()

        if result:
            for i in result:
                cursor.execute("truncate table customers;")
                authenticate.destroy()
                mydb.commit()
                messagebox.showinfo("Info", "All records cleared")
                break
        else:
            messagebox.showerror("error", "Incorrect username or password!")
            authenticate.destroy()
     
    authenticate.destroy()



def delete_screen():
    global user_name, user_password, user_e, pass_e, authenticate

    authenticate = Toplevel(root)
    authenticate.geometry("300x150")
    Label(authenticate,text="Login",font=(20)).place(relx=0.45,rely=0)
    user_l = Label(authenticate, text='username- ')
    user_l.place(relx=0.1, rely=0.20)
    user_e = Entry(authenticate, width=15, show='*')
    user_e.config(highlightbackground='black')
    user_e.place(relx=0.35, rely=0.20)
    pass_l = Label(authenticate, text='password- ')
    pass_l.place(relx=0.1, rely=0.40)
    pass_e = Entry(authenticate, width=15, show='*')
    pass_e.config(highlightbackground='black')
    pass_e.place(relx=0.35, rely=0.40)
    del_btn = Button(authenticate, text="Delete",
                     command=delete, fg='white', bg='black')
    del_btn.place(relx=0.40, rely=0.65)

def confirm_exit():
    ask = messagebox.askyesno(
        "Exit", "Are you sure you want to exit?")
    if ask == True:
        root.destroy()
    else:
        pass