from tkinter import *
from pyttsx3 import init
from functools import partial
from tkinter import scrolledtext 
from PyDictionary import PyDictionary as Dictionary

class MyWindow:      
    def __init__(self,win):
        self.win=win
        self.text=Text(win)
        self.meaning = Dictionary.meaning
        self.lbl1=Label(win, text='Insert Word Here')
        self.lbl3=Label(win, text='Result:')
        self.t1=Entry(bd=3)
        self.t3=scrolledtext.ScrolledText(win,  
                                      wrap = WORD,    
                                      font = ("Times New Roman", 
                                              15)) 
        self.t3['state']=DISABLED

        self.lbl1.place(x=80, y=50)
        self.t1.place(x=200, y=50)
        #self.t2.place(x=200, y=100)
        self.b1=Button(win, text='Adjective', command=partial(self.__get_meaning,'Adjective'))
        self.b2=Button(win, text='Adverb',command=partial(self.__get_meaning,'Adverb'))
        self.b3=Button(win, text='Noun', command=partial(self.__get_meaning,'Noun'))
        self.b4=Button(win, text='Verb',command=partial(self.__get_meaning,'Verb'))
        #self.b5=Button(win, text="Speech",command = self.speech)

        #self.b2.bind('<Button-1>', self.verb)
        self.b1.place(x=100, y=100)
        self.b2.place(x=200, y=100)
        self.b3.place(x=300, y=100)
        self.b4.place(x=400, y=100)
       # self.b5.place(x=300,y=50)
        self.lbl3.place(x=80, y=140)
        self.t3.place(x=40, y=180,width=500,height=100)
        #print(dir(self.t3))

    # create and destry the scrolled text
    '''def speech(self):
        word =str(self.t1.get())
        engine=init()
        engine.say(word)
        engine.runAndWait()'''
    def destroy_create_scrtext(self):
        self.t3.destroy()
        self.t3=scrolledtext.ScrolledText(self.win,  
                                      wrap = WORD,    
                                      font = ("Times New Roman", 
                                              15)) 
        self.t3.place(x=40, y=180,width=500,height=100)

    def __get_meaning(self,form):
        word=str(self.t1.get())
        text =''
        try:
            meaning = self.meaning(word)
        except TypeError:
            text = 'Error: Please check the spelling again'
        try:
            meaning = meaning[form]
        except KeyError:
            text = 'Error: %s form does not exist.'%form
        except TypeError:
            text = 'Error: %s form does not exist.'%form
        if text =='':
            for i in meaning:
                text += i + '\n'
        
        self.destroy_create_scrtext()
        self.t3.insert(INSERT, text)
        #self.t3.insert(END, '\n'*10)
        self.t3['state']=DISABLED
    
window=Tk()
window.iconphoto(False, PhotoImage(file='dict.png'))
mywin=MyWindow(window)
window.title('My Dictionary')
window.geometry("600x300+10+10")
window.mainloop()
