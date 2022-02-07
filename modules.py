from tkinter import *
from tkinter import ttk
import mysql.connector as connector
import mysql.connector.errors
from tkinter import messagebox
from time import strftime, sleep
from datetime import datetime

root = Tk()
mydb = connector.connect(host="localhost", user='your_username',
                         password='your_password', database='customers')
cursor = mydb.cursor()
