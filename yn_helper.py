import time
import json
import curses
import sys
import os
import pathlib
class Game_helper():
	@staticmethod
	def music(pyt):
	    if 'ANDROID_ARGUMENT' in os.environ or hasattr(sys, 'getandroidapilevel'):
	        import androidhelper
	        droid = androidhelper.Android()
	        abs_path = os.path.abspath(pyt)
	        droid.mediaPlay(abs_path)
	    else:
	        from playsound3 import playsound
	        playsound(pyt, block=False) 
	@staticmethod
	def input_int(*args):
		i="i"
		l=len(args)
		if l >= 1:
			out="\x1b[A\r"+str(args[0])
		else:
			raise TypeError(f"input_int() takes 1 positional arguments but {len(args)} was given")
		if l >= 2:
			error="\x1b[A\r"+str(args[1])
		else:
			error="\x1b[A\r"
		print("")
		while i == "i":
			try:
				print("\x1b[A\r"+(" "*100),end="")
				i=int(input("\r"+out))
			except ValueError:
				print(error)
				time.sleep(2)
				i="i"
		return i
	@staticmethod
	def input_float(*args):
		i="i"
		l=len(args)
		if l >= 1:
			out=str(args[0])
		else:
			raise TypeError(f"input_float() takes 1 positional arguments but {len(args)} was given")
		if l >= 2:
			error=str(args[1])
		else:
			error=""
		while i == "i":
			try:
				i=float(input(out).replace(",","."))
			except ValueError:
				print(error)
				i="i"
		return i
	@staticmethod
	def input_chois(*args):
		i=""
		l=len(args)
		if l < 3:
			raise TypeError(f"input_chois() takes 3 positional arguments but {len(args)} was given")
		out="\x1b[A\r"+str(args[0])+"("
		yes=str(args[1])
		no=str(args[2])
		if l >= 4:
			error="\x1b[A\r"+str(args[3])
		else:
			error="\x1b[A\r"
		print("")
		while i == "":
			i=input(out+yes+","+no+"): ")
			if i.upper() in [yes.upper(),no.upper()]:
				if i.upper() == yes.upper():
					return True
				else:
					return False
			else:
				print("\x1b[A\r"+(" "*100),end="")
				i=""
	@staticmethod
	def random(a,b,seed_genireate=True,seed_start=None):
		if not(seed_genireate):
			if seed_start != None:
				seed=seed_start
			else:
				raise NameError("name \"seed_start\" not defined")
		if seed_genireate:
			#первая формула
			seed=(a*b)+float(str(time.perf_counter())[::-1])
		#вторая формула
		ord_list=str(int(seed))
		for i in range(len(ord_list)):
			seed+=int(ord(ord_list[i]))
		if seed_genireate:
			#третья формула
			seed-=(b/a+1)+time.perf_counter()
		#четвёртая формула
		seed_see=seed/a+1%b
		seed-=(float(str(seed_see)[::-1])*(10**len(str(b))))
		if seed_genireate:
			#пятая формула
			seed+=a+float(str(time.perf_counter())[::-1])
		#подвод результатов к более точному числу
		seed%=(b+1)-a
		seed+=a
		return int(seed)
	@staticmethod
	def timer(*args):
		print("")
		if len(args) == 2:
			#таймер с выводом в конце
			for i in range(args[0],0,-1):
				print("\x1b[A\r"+str(i)+" ")
				time.sleep(1)
			print("\x1b[A\r"+str(args[1])+" ")
		elif len(args) == 1:
			#таймер без вывода в конце
			for i in range(args[0],0,-1):
				print("\x1b[A\r"+str(i)+" ")
				time.sleep(1)
			print("\x1b[A\r ",end="")
		else:
			raise TypeError(f"timer() takes 1 positional arguments but {len(args)} was given")

class App_helper():
	@staticmethod
	def saveApp(*args):
		#запись пути
		if len(args) == 2:
			a=f"{args[0]}.json"
			data=args[1]
		elif len(args) == 3:
			a=f"{args[0]}.{args[1]}"
			data=args[2]
		else:
			raise TypeError
		#запись данных
		with open(a,"w") as a:
			json.dump(data,a,ensure_ascii=False,indent=4)
	@staticmethod
	def loadApp(*args):
		#запись пути
		if len(args) == 1:
			a=f"{args[0]}.json"
		elif len(args) == 2:
			a=f"{args[0]}.{args[1]}"
		else:
			raise TypeError
		#попытка выгрузить данные
		try:
			with open(a,"r") as a:
				b=json.load(a)
		except FileNotFoundError:
			return ""
		return b
	@staticmethod
	def createFile(*args):
		#запись пути
		if len(args) == 1:
			a=f"{args[0]}.json"
		elif len(args) == 2:
			a=f"{args[0]}.{args[1]}"
		else:
			raise TypeError
		#создание файла
		try:
			#проверка на файл
			with open(a,"a") as b:
				pass
		except FileNotFoundError:
			#создание пути файла с файлом
			b=pathlib.Path(f"{a}")
			b.parent.mkdir(True, True)
			b=open(a,"w")
			b.close()
		except FileExistsError:
			#создание файла
			b=open(a,"w")
			b.close()
class Menu_helper():
	@staticmethod
	def menu(up,down,enter,start,s_start,*args):
		#создание окна
		curses.initscr()
		curses.noecho()
		curses.cbreak()
		#очистка места под выводы
		for i in range(len(args)+10):
			curses.initscr().addstr(i,0," "*len(start))
		curses.initscr().addstr(0,0,f"{start}({up},{down} перемещение; {enter} выбрать)")
		c=s_start
		#вывод вариантов
		for i in range(len(args)):
			curses.initscr().addstr(i+s_start,0,str(args[i])+f" [{i+1}]")
			c+=1
		global a
		a = 1
		def up_yn():
			#если пользователь ввёл клавишу up
			global a
			if a > 1:
				a-=1
		def down_yn():
			#если пользователь ввёл клавишу down
			global a
			if a < len(args):
				a+=1
		curses.initscr().addstr(c,0,f"{a}")
		b=curses.initscr().getch()
		while chr(b).upper() != enter.upper():
			#цикл бесконечен до клавиши enter
			if chr(b).upper() == up.upper():
				up_yn()
			elif chr(b).upper() == down.upper():
				down_yn()
			curses.initscr().addstr(c,0,f"{a}")
			curses.initscr().refresh()
			b=curses.initscr().getch()
		curses.endwin()
		#возрашение ответа
		return a-1