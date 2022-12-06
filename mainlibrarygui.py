import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.ttk import *
from book import *
from book import Book
from tkinter import *
from io import BytesIO
from PIL import ImageTk, Image
from tkinter import ttk
import requests
import os
import urllib
import io
import time
#coverList = ['9783426452936','9780553593716','0735219095','1791392792']
                
from isbngui import *

import bookdb

class LibraryModel(object):
	def __init__(self):
		self.session = bookdb.create_session()
	
	def get_books(self):
		return bookdb.get_books(self.session)
	
	def add_book(self, book):
		return bookdb.add_book(self.session, book)
	
	def remove_book(self, book):
		return bookdb.remove_book(self.session, book.isbn)

libModel = LibraryModel()

#coverList = []
#favList = []



class mainLibGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("800x800")
        self.title("Encyclomedia")
        
        
        #adds a background
        bg2 = PhotoImage(file="images/libraryBR.png")
        #set and add backround
        gui_bk = Label(self, image = bg2, bg="black")
        gui_bk.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        isbnButton = tk.Button(self, text="Add a book", font=('Arial', 18), command=self.addIsbn)
        isbnButton.pack(padx=10, pady=10)
        
        achButton = tk.Button(self, text= "View Statisics", font=('Arial', 18), command=self.viewStats)
        achButton.pack()
        
        label = Label(self, text="Your Bookshelf", font=('Arial', 18))
        label.pack(padx=20, pady=20)
        
        bookFrame = Frame(self, bg="brown")
        bookFrame.pack()
        
        
        bookFrame.columnconfigure(0)
        bookFrame.columnconfigure(1)
        bookFrame.columnconfigure(2)
        bookFrame.columnconfigure(3)
        bookFrame.columnconfigure(4)

        self.book0 = tk.Button(bookFrame, bg="brown", command=self.goalBox)
        self.book0.grid(row=0, column=0, )

        self.book1 = tk.Button(bookFrame, bg="brown", command=self.goalBox)
        self.book1.grid(row=0, column=1)

        self.book2 = tk.Button(bookFrame, bg="brown", command=self.goalBox)
        self.book2.grid(row=0, column=2)

        self.book3 = tk.Button(bookFrame, bg="brown", command=self.goalBox)
        self.book3.grid(row=0, column=3)
        
        self.book4 = tk.Button(bookFrame, bg="brown", command=self.goalBox)
        self.book4.grid(row=0, column=4)
        
        self.book5 = tk.Button(bookFrame, bg="brown", command=self.goalBox)
        self.book5.grid(row=1, column=0)
        
        self.book6 = tk.Button(bookFrame, bg="brown", command=self.goalBox)
        self.book6.grid(row=1, column=1)
        
        self.book7 = tk.Button(bookFrame, bg="brown", command=self.goalBox)
        self.book7.grid(row=1, column=2)
        
        self.book8 = tk.Button(bookFrame, bg="brown", command=self.goalBox)
        self.book8.grid(row=1, column=3)
        
        self.book9 = tk.Button(bookFrame, bg="brown", command=self.goalBox)
        self.book9.grid(row=1, column=4)
        
        #self.book10 = tk.Button(bookFrame)
        
        self.daily = tk.IntVar()
        self.completed = tk.IntVar()
        
        self.bookCount = tk.IntVar(self, value=0, name = "bookCount")
        #counter for daily and complete to be used in statistics
        self.DCount = tk.IntVar(self, value=0, name = "Dcount")
        self.CCount = tk.IntVar(self, value=0, name = "Ccount")

        bookFrame.pack(fill='x')
        
        for book in libModel.get_books():
            self.addCover(book)
        
        self.mainloop()

    

    def addCover(self, newBook):
        bookCounter = self.bookCount.get()
         
        #cv = coverList[bookCounter]
        print(newBook.getISBN())
        
        newCover = newBook.getCover()
        
        print(newCover)        
        #print("from the book object" + newCover)
        #print(cv)
        
        # u = urlopen(newCover)
        # raw_data = u.read()
        # u.close()
        # image = ImageTk.PhotoImage(data=raw_data)
        
        # reponse = requests.get(newCover)
        # img_data = reponse.content        
        # image = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        
        raw_data = urllib.request.urlopen(newCover).read()
        im = Image.open(io.BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        
        if bookCounter == 0:
            self.book0.configure(image=image)
            self.book0.image = image
        elif bookCounter == 1:
            self.book1.configure(image=image)
            self.book1.image = image
        elif bookCounter == 2:
            self.book2.configure(image=image)
            self.book2.image = image
        elif bookCounter == 3:
            self.book3.configure(image=image)
            self.book3.image = image
        elif bookCounter == 4:
            self.book4.configure(image=image)
            self.book4.image = image
        elif bookCounter == 5:
            self.book5.configure(image=image)
            self.book5.image = image
        elif bookCounter == 6:
            self.book6.configure(image=image)
            self.book6.image = image
        elif bookCounter == 7:
            self.book7.configure(image=image)
            self.book7.image = image
        elif bookCounter == 8:
            self.book8.configure(image=image)
            self.book8.image = image
        elif bookCounter == 9:
            self.book9.configure(image=image)
            self.book9.image = image                
        else:
            pass
            
        bookCounter = bookCounter + 1
            
        self.bookCount.set(bookCounter)
            
        #    self.bookCount = self.bookCount.get() + 1 
    
    def addIsbn(self):
        isbn = simpledialog.askstring("Input", "Add a ISBN",
                                 parent=self)
       #print(isbn)
        
        if isbn == None:
                return
        
        try:
            newBook = lookup_isbn(isbn)
            libModel.add_book(newBook)
            self.addCover(newBook)
        except Exception:
            messagebox.showwarning(title="Error", message="Couldn't find the ISBN!")

        
    def viewStats(self):
        
        print("The value of bookCount is: ", self.getvar(name="bookCount"))
        
        #how the statistics box works
        Stats = Tk()
        Stats.title("Library Statistics")
        count = self.bookCount.get()
        total_books = tk.Label(Stats, text="Books Added: " + str(count))
        total_books.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        read_label = tk.Label(Stats, text="Books Completed: " + str(self.CCount.get()))
        read_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        read_label = tk.Label(Stats, text="Total Daily revisits: " + str(self.DCount.get()))
        read_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        percDOne = 0
        #corrects a divide by zero error when there are no books added
        if count == 0:
            percDOne = 1
        else: 
            percDOne = (self.completed.get()/count)
        
        
        read_label = tk.Label(Stats, text="Percentage Completed: " + str(percDOne*100) + "%")
        read_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        close_button = ttk.Button(Stats, text="return", command=Stats.destroy)
        close_button.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        

    def closebutton(Stats):
        return # destroy current window
    
    def updateDaily(self):
        #increments daily
        if self.daily.get() == 1:
            self.DCount.set(self.DCount.get()+1)
    def updateCompleted(self):
        #increments completed
        if self.completed.get() == 1:
            self.CCount.set(self.CCount.get()+1)
        

        
        
    
    def goalBox(self):
        goalBox = Toplevel()
        goalBox.title('Book Options')
        tk.Checkbutton(goalBox, text = 'Did you read today?', variable=self.daily, onvalue= 1, offvalue=0, command=self.updateDaily).pack()
        tk.Checkbutton(goalBox, text = 'Completed a Book', variable=self.completed, onvalue= 1, offvalue=0, command=self.updateCompleted).pack()
        tk.Button(goalBox, text='OK', command=goalBox.destroy).pack()

        
mainLibGUI()

