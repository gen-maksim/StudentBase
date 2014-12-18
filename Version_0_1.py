# Created by FMaT-Team

# Чтение из файла_______________________________________________________
numbers = []
perehod = []
with open('base.txt') as f:
    length = len(f.readlines())
    f.seek(0)
    for k in range(length):
        a = f.readline()
        a = a[0:-1]
        perehod.append(a.split(sep=":"))
for i in perehod:
    numbers.append({'number' : i[0], 'surname' : i[1], 'adress' : i[2]})
#_______________________________________________________________________

# Импортирование библиотек______________________________________________
from tkinter import *
from tkinter.messagebox import *
#_______________________________________________________________________

# Объявление переменных_________________________________________________
x = 0
line1 = ''
line2 = ''
line3 = ''
surname = ''
number = ''
adress = ''
#_______________________________________________________________________

# Главное окно__________________________________________________________
class main:
    
    # Заполнение главного окна_________________
    def __init__(self, master):

        def center(win):
            win.update_idletasks()
            width = win.winfo_width()
            frm_width = win.winfo_rootx() - win.winfo_x()
            win_width =  width + 2 * frm_width
            height = win.winfo_height()
            titlebar_height = win.winfo_rooty() - win.winfo_y()
            win_height = height + titlebar_height + frm_width
            x = win.winfo_screenwidth() // 2 - win_width // 2
            y = win.winfo_screenheight() // 2 - win_height // 2
            win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
            if win.attributes('-alpha') == 0:
                win.attributes('-alpha', 1.0)
            win.deiconify()
        
        self.master = master
        self.master.title('Телефонный справочник')
        self.master.geometry('300x170')
        self.master.protocol('WM_DELETE_WINDOW', 
                            self.exitMethod)
        self.master.resizable(False, False)
        self.button = Button(self.master,
                             width = 40,
                             height = 3,
                             text = 'Показать весь список',
                             command = self.openDialog)
        self.button.pack()
        self.button1 = Button(self.master,
                              width = 40,
                              height = 3,
                              text = 'Добавить запись',
                              command = self.openDialog1)      
        self.button1.pack()
        self.buttonSr = Button(self.master,
                               width = 40,
                               height = 3,
                               text = 'Поиск',
                               command = self.openSearch)
        self.buttonSr.pack()
        center(self.master)
        self.master.mainloop()
    #______________________________________________

    # Объявление окна вывода списка________________    
    def openDialog(self):
        global x, line1, line2, line3
        x = 0
        line1 = ''
        line2 = ''
        line3 = ''
        try:
            for i in numbers:
                x += 1
        except:
                x += 0
        y = 0
        while y < (x):
                line1 += str(numbers[y]['number'])
                line2 += str(numbers[y]['surname'])
                line3 += str(numbers[y]['adress'])
                line1 += '\r\n'
                line2 += '\r\n'
                line3 += '\r\n'
                y += 1

        self.dialog = child(self.master)
    #_______________________________________________

    # Объявление окон поиска и добавления___________
    def openDialog1(self):
        self.dialog = child1(self.master)
        
    def openSearch(self):
        self.dialog = child2(self.master)
    #_______________________________________________

    # Вопрос о сохранении___________________________
    def exitMethod(self):
        self.dialog = yesno(self.master)
        self.returnValue = self.dialog.go('Выход',
                                          'Сохранить изменения?')
        if self.returnValue:
            with open('base.txt','w') as v:
                perehod=''
                for j in numbers:
                    perehod+=str(j['number'])+':'+str(j['surname'])+':'+str(j['adress'])+'\n'
                v.write(perehod) 
            self.master.destroy()
        elif self.returnValue == False:
            self.master.destroy()
    #________________________________________________

#________________________________________________________________________

# Окно со списком________________________________________________________
class child:
    def __init__(self, master):
        def myfunction(event):
            canvas.configure(scrollregion = canvas.bbox('all'), width=325,height=200)

        self.slave = Toplevel(master)
        self.slave.title('Весь список')
        self.slave.geometry('325x200')
        self.frame = Frame(self.slave)
        self.slave.resizable(False, False)
        self.frame.pack()

        # ScrollBar________________
        sizex = 365
        sizey = 225
        posx  = 100
        posy  = 100
        self.slave.wm_geometry('%dx%d+%d+%d' % (sizex, sizey, posx, posy))
        myframe = Frame(self.slave, relief = GROOVE, width = 50, height = 100, bd = 1)
        myframe.place(x = 10,y = 10)
        canvas = Canvas(myframe)
        frame = Frame(canvas)
        myscrollbar = Scrollbar(myframe, orient = 'vertical',command = canvas.yview)
        canvas.configure(yscrollcommand = myscrollbar.set)

        myscrollbar.pack(side = 'right', fill = 'y')
        canvas.pack(side = 'left')
        canvas.create_window((0,0), window = frame, anchor = 'nw')
        frame.bind('<Configure>', myfunction)
        for i in range(1): 
            self.text1 = Label(frame, text = line1).grid(row = i, column = 0)
            self.text2 = Label(frame, text = line2).grid(row = i, column = 1)
            self.text3 = Label(frame, text = line3).grid(row = i, column = 2)
        #__________________________
            
#__________________________________________________________________________

# Окно добавления записи __________________________________________________
class child1:
    #Создение окна_________________________
    def __init__(self, master):         
        self.slave1 = Toplevel(master)
        self.slave1.title('Добавление номера')
        self.frame1 = Frame(self.slave1)
        self.slave1.resizable(False, False)
        self.frame1.pack()
        self.textsurname = Label(self.slave1,
                                 width = 40,
                                 height = 3,
                                 text = 'Введите фамилию')
        self.textsurname.pack()
        self.vvodsurname = Entry(self.slave1)
        self.vvodsurname.pack()
        self.textnum = Label(self.slave1,
                             width = 40,
                             height = 3,
                             text = 'Введите номер')
        self.textnum.pack()
        self.vvodnum = Entry(self.slave1)
        self.vvodnum.pack()
        self.textadress = Label(self.slave1,
                                width = 40,
                                height = 3,
                                text = 'Введите адрес')
        self.textadress.pack()
        self.vvodadress = Entry(self.slave1)
        self.vvodadress.pack()
        self.but = Button(self.slave1,
                          width = 10,
                          height = 1,
                          text = 'ОK',
                          command = self.zap)
        self.but.pack()
    # Метод добавления___________________________
    def zap(self):
        for i in str(self.vvodsurname.get()):
            if i.isnumeric():
                showwarning('Ошибка ввода фамилии','Формат данных неверный!')
                self.slave1.focus_set()
                return()
            else:
                surname = self.vvodsurname.get()
        try:
            number = int(self.vvodnum.get())
        except:
            self.vvodnum.configure(text = '123')
            showwarning('Ошибка ввода номера', 'Формат данных неверный!')
            slave1.focus_set()
            return()
        
        adress = self.vvodadress.get()
        numbers.append({'number' : number, 'surname' : surname, 'adress' : adress})
        self.slave1.destroy()
        showwarning('Оповещение','Номер успешно добавлен!')
        
# Поиск___________________________________________________________________
class child2:
    #Создание окна____________________________________
    def __init__(self, master):
        self.slave2 = Toplevel(master)
        self.slave2.title('Поиск')
        self.slave2.geometry('480x200')
        self.frame2 = Frame(self.slave2)
        self.slave2.resizable(False, False)
        self.frame2.pack()
        self.textName = Label(self.slave2,
                         text = 'Введите Фамилию')
        self.textName.pack()
        self.textName.place(relx = 0.02, rely = 0.1)
        self.vvodName = Entry(self.slave2)
        self.vvodName.pack()
        self.vvodName.place(relx = 0.02, rely = 0.2)
        self.textadress1 = Label(self.slave2,
                         text = 'Введите Адрес')
        self.textadress1.pack()
        self.textadress1.place(relx = 0.29, rely = 0.1)
        self.vvodadress1 = Entry(self.slave2)
        self.vvodadress1.pack()
        self.vvodadress1.place(relx = 0.29, rely = 0.2)
        self.textNumber = Label(self.slave2,
                         text = 'Введите Номер')
        self.textNumber.pack()
        self.textNumber.place(relx = 0.57, rely = 0.1)
        self.vvodNumber = Entry(self.slave2)
        self.vvodNumber.pack()
        self.vvodNumber.place(relx = 0.57, rely = 0.2)
        self.but1 = Button(self.slave2,
                  text = 'Поиск',
                  command = self.Srch)
        self.but1.pack()
        self.but1.place(relx = 0.85, rely = 0.18)
        self.vvodDel = Entry(self.slave2)
        self.vvodDel.pack()
        self.vvodDel.place(relx = 0.02, rely = 0.36)

        self.butDel = Button (self.slave2,text = 'Удаление', command = self.Del)
        self.butDel.pack()
        self.butDel.place(relx=0.3, rely = 0.35)
        self.textresN = Label(self.slave2,text = '')
        self.textresN.pack()
        self.textresN.place(relx = 0.7, rely = 0.5)

        self.textresI = Label(self.slave2,text = '')
        self.textresI.pack()
        self.textresI.place(relx=  0.02, rely = 0.5)
        
        self.textresA = Label(self.slave2,text = '')
        self.textresA.pack()
        self.textresA.place(relx = 0.4, rely = 0.5)
        
        self.textresS = Label(self.slave2,text = '')
        self.textresS.pack()
        self.textresS.place(relx = 0.1, rely = 0.5)
    #Метод поиска________________________________________    
    def Srch(self):
        y = 0
        a = 0
        n = 0
        schet=0
        resN = ''
        test=''
        resA = ''
        resI = ''
        resS = ''
        if str(self.vvodNumber.get()).strip() != '':
            Zapros = self.vvodNumber.get()
            schet=1
            for y in numbers:
                if Zapros.upper() in str(y['number']).upper():
                    if self.vvodName.get().strip() != '' or self.vvodadress1.get().strip() != '':
                        if self.vvodName.get().upper()==str(y['surname']).upper():
                            resN += str(y['number']) + '\n'
                            resA += str(y['adress']) + '\n'
                            resS += str(y['surname']) + '\n'
                            resI += str(schet)+'\n'
                            
                        if self.vvodadress1.get().upper()==str(y['adress']).upper():
                            resN += str(y['number']) + '\n'
                            resA += str(y['adress']) + '\n'
                            resS += str(y['surname']) + '\n'
                            resI += str(schet)+'\n'
                    else:
                        resN += str(y['number']) + '\n'
                        resA += str(y['adress']) + '\n'
                        resS += str(y['surname']) + '\n'
                        resI += str(schet)+'\n'
                schet+=1
            
                    
        elif str(self.vvodName.get()).strip() != '':
            Zapros = self.vvodName.get()
            schet=1
            for n in numbers:
                if Zapros.upper() in n['surname'].upper():
                    if self.vvodNumber.get().strip() != '' or self.vvodadress1.get().strip() != '':
                        if self.vvodNumber.get().upper()==str(n['number']).upper():
                            resN += str(n['number']) + '\n'
                            resA += str(n['adress']) + '\n'
                            resS += str(n['surname']) + '\n'
                            resI += str(schet)+'\n'
                            
                        if self.vvodadress1.get().upper()==str(n['adress']).upper():
                            resN += str(n['number']) + '\n'
                            resA += str(n['adress']) + '\n'
                            resS += str(n['surname']) + '\n'
                            resI += str(schet)+'\n'
                    else:
                        resN += str(n['number']) + '\n'
                        resA += str(n['adress']) + '\n'
                        resS += str(n['surname']) + '\n'
                        resI += str(schet)+'\n'
                schet+=1
                    
        elif str(self.vvodadress1.get()).strip() != '':
            Zapros = self.vvodadress1.get()
            schet=1
            for a in numbers:
                if Zapros.upper() in a['adress'].upper():
                    if self.vvodNumber.get().strip() != '' or self.vvodadress1.get().strip() != '':
                        if self.vvodNumber.get().upper()==str(a['number']).upper():
                            resN += str(a['number']) + '\n'
                            resA += str(a['adress']) + '\n'
                            resS += str(a['surname']) + '\n'
                            resI += str(schet)+'\n'
                            
                        if self.vvodName.get().upper()==str(a['surname']).upper():
                            resN += str(a['number']) + '\n'
                            resA += str(a['adress']) + '\n'
                            resS += str(a['surname']) + '\n'
                            resI += str(schet)+'\n'
                    else:
                        resN += str(a['number']) + '\n'
                        resA += str(a['adress']) + '\n'
                        resS += str(a['surname']) + '\n'
                        resI += str(schet)+'\n'
                schet+=1
                    
        self.textresN.configure(text = resN)
        self.textresA.configure(text = resA)
        self.textresS.configure(text = resS)
        self.textresI.configure(text = resI)
        self.vvodName.insert(0,'')
    #Метод удаления__________________________________________
    def Del(self):
        if (str(self.vvodDel.get()).strip() != '') and (self.vvodDel.get().isnumeric()):
            numbers.pop(int(self.vvodDel.get())-1)
#Сохранение изменений_______________________________________________________________
class yesno:
    def __init__(self, master):

        def center(win):
            win.update_idletasks()
            width = win.winfo_width()
            frm_width = win.winfo_rootx() - win.winfo_x()
            win_width =  width + 2 * frm_width
            height = win.winfo_height()
            titlebar_height = win.winfo_rooty() - win.winfo_y()
            win_height = height + titlebar_height + frm_width
            x = win.winfo_screenwidth() // 2 - win_width // 2
            y = win.winfo_screenheight() // 2 - win_height // 2
            win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
            if win.attributes('-alpha') == 0:
                win.attributes('-alpha', 1.0)
            win.deiconify()
  
        self.slave = Toplevel(master)
        self.slave.title('Выход')
        self.slave.geometry('200x100')
        self.slave.resizable(False, False)
        center(self.slave)
        self.frame = Frame(self.slave)
        self.frame.pack(side = BOTTOM)
        self.yes_button = Button(self.frame,
                                 text = 'Да',
                                 command = self.yes)
        self.yes_button.pack(side = LEFT)
        self.no_button = Button(self.frame,
                                text = 'Нет',
                                command = self.no)
        self.no_button.pack(side = RIGHT)
        self.label = Label(self.slave)
        self.label.pack(side = TOP, fill = BOTH, expand = YES)
        self.slave.protocol('WM_DELETE_WINDOW', self.no)

    def go(self, title = '', message = ''):
        self.slave.title(title)
        self.label.configure(text = message)
        self.booleanValue = TRUE
        self.slave.grab_set()
        self.slave.focus_set()
        self.slave.wait_window()
        return self.booleanValue

    def yes(self):
        self.booleanValue = TRUE
        # сохранить.
        self.slave.destroy()

    def no(self):
        self.booleanValue = FALSE
        self.slave.destroy()

root = Tk()

# запуск окна
main(root)
