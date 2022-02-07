from modules import *
from add_cust import *
from view_cust import *

root.geometry("600x500")
root.title('Shop Management')
root.minsize(width=400, height=400)

# Main ui goes from here

# heading frame

headingFrame1 = Frame(root, bg="red", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n Shop Name",
                     bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
# Add customers button
btn1 = Button(root, text="Add customer", fg='white',
              bg='black', command=add_customer)
btn1.place(relheight=0.1, relwidth=0.45, relx=0.28, rely=0.4)

# View customers button
btn2 = Button(root, text="View customers", fg='white',
              bg='black', command=view_customers)
btn2.place(relheight=0.1, relwidth=0.45, relx=0.28, rely=0.5)

# Delete Records Button
btn3 = Button(root, text='Delete Records', fg='white',
              bg='black', command=delete_screen)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

# Exit Button
btn4 = Button(root, text='Exit', fg='white', bg='black', command=confirm_exit)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)
root.mainloop()
