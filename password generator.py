#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox as mbox
import random
import string


root = Tk()
root.title("Генератор паролей") 
root.geometry("620x400")
root.resizable(width=False, height=False)

#Логика
stup = StringVar()
stup.set('easy')


small_letters = string.ascii_lowercase
big_letters = string.ascii_uppercase
digits = string.digits
znaki = '!@#$%^&*()+-'


easy_pas = small_letters + digits
normal_pas = small_letters + big_letters + digits
hard_pas = small_letters + big_letters + digits + znaki

def passwd(event=None):
	try:
		for n in range(int(number_len.get())):
			password =''
			for i in range(int(pas_len.get())):
				if stup.get() == 'easy':
					password += random.choice(easy_pas)
				if stup.get() == 'normal':
					password += random.choice(normal_pas)
				if stup.get() == 'hard':
					password += random.choice(hard_pas)
			output_pas.insert(END, password + "\n")
	except (TypeError, ValueError):
		mbox.showerror("Ошибка", "Должно быть введено число")


def info():
	mbox.showinfo("Справка", "Программа:Генератор паролей\n\n\
Разработчик:Лихтнер Виктор Алексеевич\n\n\
Email:Likhtnerviktor@mail.ru\n\n\
Версия: alhpa 0.1\n\n\
Лицензия:GPLv3 GNU General Public License Version 3)")


def clear(event=None):
	output_pas.delete('1.0', END)
#Конец Логике

class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()


#Интерфейс
pas_lab = Label(root, text="Выберите длину пароля")
pas_lab.grid(row = 0, column=0)

pas_len = Spinbox(root, from_=1, to = 100, width = 5)
pas_len.grid(row = 0, column=1)
pas_len.focus()

number_lab = Label(root, text="Выберите количество\nпаролей")
number_lab.grid(row = 1, column=0)

number_len = Spinbox(root, from_=1, to=100, width=5)
number_len.grid(row = 1, column=1)

complexity_lab = Label(root, text="Выберите сложность\nгенерации пароля")
complexity_lab.grid(row = 2, column=1)

easy_rad = Radiobutton(root, text = 'Лёгкий', value = 'easy', variable = stup)
easy_rad.grid(row = 3, column=0)
normal_rad = Radiobutton(root, text = 'Средний', value = 'normal', variable = stup)
normal_rad.grid(row = 3, column=1)
hard_rad = Radiobutton(root, text = 'Сложный', value = 'hard', variable = stup)
hard_rad.grid(row = 3, column=2)

gen_button = Button(root, text = 'Сгенерировать\nпароль', command=passwd)
gen_button.grid(row = 4, column=0)

clear_button = Button(root, text = 'Очистить', command=clear)
clear_button.grid(row = 4, column=2)

#Справка
ref_Button = Button(root,	 text='?', command=info)
ref_Button["border"] = "0" 
ref_Button.grid(row = 0, column=2, sticky = E)


output_pas = Text(root, width=40, height=10)
output_pas.grid(row = 5, column=1)

sy = Scrollbar(root, command=output_pas.yview)
sy.grid(row=5, column=1, sticky='nse')
output_pas.configure(yscrollcommand=sy.set)


#Всплывающие подсказки
tooltips_gen = CreateToolTip(gen_button, 'Горячая клавиша "Enter"')
tooltips_clear = CreateToolTip(clear_button, 'Горячая клавиша "Delete"')
tool_easy = CreateToolTip(easy_rad, 'Используются буквы в нижнем регистре и цифры')
tool_normal = CreateToolTip(normal_rad, 'Используются буквы в нижнем, верхнем регистре и цифры')
tool_hard = CreateToolTip(hard_rad, 'Используются буквы в нижнем, верхнем регистре, цифры и знаки')
tool_ref = CreateToolTip(ref_Button, 'Справка')

#Горячие клавиши
root.bind('<Return>', passwd)
root.bind('<Delete>', clear)


root.mainloop()
#Конец интерфейса
