from tkinter.ttk import setup_master
from modules import *




def view_customers():
    global viewScr, s_entry, treev
    viewScr = Toplevel(root)
    viewScr.title("Customers List")
    viewScr.minsize(width=600, height=300)
    treev = ttk.Treeview(viewScr, selectmode=BROWSE)
    treev.pack(fill=BOTH, expand=TRUE)

    # constructing the vertical scrollbar

    verscrlbar = ttk.Scrollbar(viewScr, orient=VERTICAL, command=treev.yview)
    verscrlbar.pack(side=RIGHT, fill='both')

    treev.configure(xscrollcommand=verscrlbar.set)

    treev['columns'] = ('1', '2', '3', '4', '5', '6','7')

    treev['show'] = 'headings'

    treev.column('1', width=3, anchor='c')
    treev.column('2',  anchor='c')
    treev.column('3',  anchor='c')
    treev.column('4', anchor='c')
    treev.column('5', anchor='c')
    treev.column('6', anchor='c')
    treev.column('7', anchor='c')

    treev.heading('1', text='id')
    treev.heading('2', text='Name')
    treev.heading('3', text='Address')
    treev.heading('4', text='Paid')
    treev.heading('5', text='Balance')
    treev.heading('6', text='Time')
    treev.heading('7', text='Date')

    cursor.execute("select * from database_name order by name asc")
    details = cursor.fetchall()
    for data in details:
        treev.insert("", 'end', iid=data[0], text=data[0], values=(
            data[0], data[1], data[2], data[3],data[4],data[5],data[6]))
