import random
import time
import yn_helper as helper
print("                     ДИСКЛЕЙМЕК")
print("перед началом игры нужно поставить англискую раскладку и выключить капслок")
time.sleep(5)
print("\x1b[A\r                                                                       \x1b[A\r\x1b[A\r                                                                       \x1b[A\r\x1b[A\r                                                                          ",end="\x1b[A\r")
if helper.App_helper.loadApp("save/istoria") != "нет сохранения":
	print("найдено сохранение,загрузить его?\n  да-1\n  нет-2")
if helper.App_helper.loadApp("save/istoria") == "нет сохранения" or helper.Game_helper.input_int("выбор: ","можно выбрать нормально да или нет?") == 2:
	if helper.App_helper.loadApp("save/istoria") != "нет сохранения":
		print("\x1b[A\r                                                    ")
		time.sleep(1)
		print("\x1b[A\r\x1b[A\r                                                    ")
		time.sleep(1)
		print("\x1b[A\r\x1b[A\r                                                    ")
		time.sleep(1)
		print("\x1b[A\r\x1b[A\r                                                    ",end="\r")
		time.sleep(1)
	start=1
	cheker=0
	print("выбирете сложность:\n  лёгкая-1\n  нормальная-2\n  сложная-3\n  да-4\n")
	i=0
	while i == 0:
		try:
		    i=int(input("\x1b[A\rвыбрал: "))
		except ValueError:
			print("\x1b[A\rты чё думал сломать игру? ВЫБИРАЙ ЗАНОВО")
			time.sleep(2)
			print("\x1b[A\r                                                   ")
	print("\x1b[A\r                                                    ")
	time.sleep(1)
	print("\x1b[A\r\x1b[A\r                                                    ")
	time.sleep(1)
	print("\x1b[A\r\x1b[A\r                                                    ")
	time.sleep(1)
	print("\x1b[A\r\x1b[A\r                                                    ")
	time.sleep(1)
	print("\x1b[A\r\x1b[A\r                                                    ")
	time.sleep(1)
	print("\x1b[A\r\x1b[A\r                                                    ",end="\r")
	time.sleep(1)
	if i == 1:
		print("у тебя 40 хп из 75 возможных и 50 золота")
		hp=40
		mhp=75
		monet=50
		pari=0
	elif i == 2:
		print("у тебя 30 хп из 50 возможных, возможность парирования и 30 золота")
		hp=30
		mhp=50
		monet=30
		pari=2
	elif i == 3:
		print("у тебя 20 хп из 25 возможных, возможность делать дабл хит и 10 золота")
		hp=20
		mhp=25
		monet=10
		pari=1
	else:
		if i != 4:
			print(f"а чё с лицом? хули выбрал число {i}? ладно будешь играть на сложности \"да\"")
		print("у тебя 1 hp, возможность парировать и 0 золота")
		hp=1
		mhp=1
		monet=0
		pari=2
	input("нажми enter для продолжения...")
	print("\x1b[A\r                                                    ")
	time.sleep(1)
	print("\x1b[A\r\x1b[A\r                                                    \x1b[A\r                                                                   \x1b[A",end="\r")
	time.sleep(1)
else:
	start=0
	hp,mhp,cheker,pari,pari_all,max_shote,monet,map_num,act=helper.App_helper.loadApp("save/istoria")
	max_shote=helper.App_helper.loadApp("save/.realrecord/record")
	print("\x1b[A\r                                                    ")
	time.sleep(1)
	print("\x1b[A\r\x1b[A\r                                                    ")
	time.sleep(1)
	print("\x1b[A\r\x1b[A\r                                                    ")
	time.sleep(1)
	print("\x1b[A\r\x1b[A\r                                                    ",end="\r")
	time.sleep(1)
def game(hp,mhp,pari,u_enemy,hp_enemy,unit,cheker,magic):
	n=0
	ws=0
	check=""
	if cheker != 0:
		check=f"артефакт показывает что противник наносит {u_enemy} урона\n"
		ws=1
		if magic == 1:
			check+="и он ещё показывает большое присутствие магии\n"
			ws=2
	while hp > 0 and hp_enemy > 0:
		if cheker != 0:
			check+=f"артефакт показывает что у противника {hp_enemy} здоровья\n"
		pari_time=0
		if n != 0:
			n-=1
		if pari == 0:
			a=" ???"
		elif pari == 2:
			a="  парировать"
		elif pari == 1:
			a="  дабл хит"
		elif pari == 3:
			a="  контр-атака"
		else :
			a="  атака-щитом"
		i=helper.Menu_helper.menu("w","s","e",f"{check}у тебя {hp}/{mhp} хп\nтвои действия:",2 + (1 if cheker != 0 else 0) + ws,"  атаковать","  защитится","  проверить",a,"  сильное лечение")
		ws=0
		if i==0:
			u=random.randint(10,15)
			print(f"ты атакуешь врага и наносишь: {u} урона")
			hp_enemy-=u
		elif i==1:
			print("на следуйщие 2 хода урон понижен в 2 раза")
			if magic ==1:
				print("изза магии защита стала менее эфективной")
			n=2
		elif i==2:
			print(f"{unit}: {hp_enemy} хп и урон {u_enemy} ")
		elif i==3:
			if pari==2:
				print("ты парируещь атаку противника после мини игры")
				pari_time=1
			elif pari==1:
				print("ты атакуешь 2 раза после мини игры")
				pari_time=2
			elif pari==3:
				print("ты контр атакуешь после мини игры")
				pari_time=3
			elif pari==4:
				print("ты атакуешь щитом после мини игры")
				pari_time=4
			else:
				print("ты ничего не сделал...")
		elif i==4:
			q=random.randint(15,32)
			if hp+q > mhp:
				q=mhp-hp
			print(f"ты начинаешь лечение и излечиваешь {q} хп")
			hp+=q
		if pari_time==1:
			input("когда ты парируещь, нужно быстро написать букву которая написанно. когда готов нажми enter:")
			pari_dop=random.randint(1,4)
			print("приготовся парировать...")
			helper.Game_helper.timer(3,"ПАРИРУЙ")
			if pari_dop==1:
			    t="w"
			elif pari_dop==2:
				t="a"
			elif pari_dop==3:
				t="s"
			else:
				t="d"
			pari_enemy=time.time()
			if input("	"+t) == t and pari_enemy-time.time()>-2:
				print("парирование удалось и ты нанёс 15 урона противнику")
				hp_enemy-=15
			else:
				print(f"ты не вовремя парировал и получил: {u_enemy} урона")
				hp-=u_enemy
		elif pari_time==2:
			input("когда ты делаешь дабл хит, нужно за короткое время нажать a d enter или d a enter как написать будет понятно в процессе. когда готов нажми enter:")
			pari_dop=random.randint(1,2)
			print("приготовся делать дабл хит...")
			helper.Game_helper.timer(3,"ДАБЛ ХИТ")
			if pari_dop==1:
				t="ad"
			else:
				t="da"
			pari_enemy=time.time()
			if input("	"+t) == t and pari_enemy-time.time()>-3:
				print("ты нанёс 30 урона")
				hp_enemy-=30
			if n >= 1:
				if random.randint(1,5)<=3:
					if magic == 1:
						print(f"ты впитал {(u_enemy/2)*1.5} урона")
						hp-=(u_enemy/2)*1.5
					else:
						print(f"ты впитал {u_enemy/2} урона")
						hp-=u_enemy/2
				else:
					print("щит можно было и не ставить. враг промахнулся")
			else:
				if random.randint(1,5)<=3:
					print(f"ты впитал {u_enemy} урона")
					hp-=u_enemy
				else:
					print("удача! враг промахнулся")
		elif pari_time == 3:
			input("когда ты делаешь контр-атаку,тебе нужно написать нужные буквы на клавиатуре за нужное время. когда готов нажми enter:")
			print("приготовся делать контр-атаку...")
			helper.Game_helper.timer(3,"БЛОК")
			pari_enemy=time.time()
			if input("	w") == "w" and pari_enemy-time.time()>-2:
				pari_dop=random.randint(1,2)
				print("блок удался но раслаблятся нельзя")
				helper.Game_helper.timer(3,"АТАКА")
				if pari_dop==1:
					t="ad"
				else:
					t="da"
				pari_enemy=time.time()
				if input("	"+t) == t and pari_enemy-time.time()>-2:
					u=random.randint(30,45)
					print(f"ты нанёс {u} урона")
					hp_enemy-=u
				if n >= 1:
					if random.randint(1,5)<=3:
						if magic == 1:
							print(f"ты впитал {(u_enemy/6)*1.5} урона")
							hp-=(u_enemy/6)*1.5
						else:
							print(f"ты впитал {(u_enemy/6)} урона")
							hp-=(u_enemy/6)
					else:
						print("щит можно было и не ставить. враг промахнулся")
				else:
					if random.randint(1,5)<=3:
						if magic == 1:
							print(f"ты впитал {u_enemy/3*1.5} урона")
							hp-=(u_enemy/3)*1.5
						else:
							print(f"ты впитал {u_enemy/3} урона")
							hp-=(u_enemy/3)
					else:
						print("удача! враг промахнулся")
			else:
				pari_dop=random.randint(1,2)
				print("блокнуть атаку не удалось но сохраняй концентрацию")
				helper.Game_helper.timer(3,"АТАКА")
				if pari_dop==1:
					t="ad"
				else:
					t="da"
				pari_enemy=time.time()
				if input("	"+t) == t and pari_enemy-time.time()>-2:
					u=random.randint(20,35)
					print(f"ты нанёс {u} урона")
					hp_enemy-=u
				if n >= 1:
					if random.randint(1,5)<=3:
						if magic == 1:
							print(f"ты впитал {(u_enemy/2)*1.5} урона")
							hp-=(u_enemy/2)*1.5
						else:
							print(f"ты впитал {(u_enemy/2)} урона")
							hp-=u_enemy/2
					else:
						print("щит можно было и не ставить. враг промахнулся")
				else:
					if random.randint(1,5)<=3:
						print(f"ты впитал {u_enemy} урона")
						hp-=u_enemy
					else:
						print("удача! враг промахнулся")
		elif pari_time == 4:
			input("когда ты атакуешь щитом нужно прожать нужную комбинацию клавишь, нажми enter когда готов:")
			print("приготорвся атаковать щитом...\n3")
			pari_dop=random.randint(1,2)
			helper.Game_helper.timer(3,"ЗАМАХ")
			if pari_dop==1:
				t="sd"
			else:
				t="sa"
			pari_enemy=time.time()
			if input("	"+t) == t and pari_enemy - time.time()>-2:
				pari_enemy=time.time()
				print("УДАР")
				if input("	w") == "w" and pari_enemy -time.time()>-2:
					n=3
					print("следующие 2 хода урон понижен в 2 раза (не включая этот ход)")
				print("ты нанёс 20 урона")
				hp_enemy-=20
				if random.randint(1,5)<=3:
					if magic == 1:
						print(f"ты впитал {(u_enemy/3)*1.5} урона")
						hp-=(u_enemy/3)*1.5
					else:
						print(f"ты впитал {(u_enemy/3)} урона")
						hp-=(u_enemy/3)
				else:
					print("щит можно было и не ставить. враг промахнулся")
			else:
				if n >= 1:
					if random.randint(1,5)<=3:
						if magic == 1:
							print(f"ты впитал {(u_enemy/2)*1.5} урона")
							hp-=(u_enemy/2)*1.5
						else:
							print(f"ты впитал {(u_enemy/2)} урона")
							hp-=(u_enemy/2)
					else:
						print("щит можно было и не ставить. враг промахнулся")
				else:
					if random.randint(1,5)<=3:
						print(f"ты впитал {u_enemy} урона")
						hp-=u_enemy
					else:
						print("удача! враг промахнулся")
		elif hp_enemy >0:
			if n >= 1:
				if random.randint(1,5)<=3:
					if magic == 1:
						print(f"ты впитал {(u_enemy/2)*1.5} урона")
						hp-=(u_enemy/2)*1.5
					else:
						print(f"ты впитал {(u_enemy/2)} урона")
						hp-=(u_enemy/2)
				else:
					print("щит можно было и не ставить. враг промахнулся")
			else:
				if random.randint(1,5)<=3:
					print(f"ты впитал {u_enemy} урона")
					hp-=u_enemy
				else:
					print("удача! враг промахнулся")
		check=""
		h=0
		time.sleep(3)
	return hp
def shop(monet,pari,pari_all,hp,mhp,n):
	i=0
	if n == 1:
		h="  купить контр атаку-1\n  поменять способность-2\n  зелье жизни-3\n  выйти-4"
		g=4
	elif n == 2:
		h="  купить атаку щитом-1\n  поменять способность-2\n  зелье жизни-3\n  выйти-4"
		g=4
	while i != g:
		i=0
		print(f"у тебя {monet} монет")
		print("что ты хочешь сделать?\n"+h)
		while i == 0 :
			try:
			    i=int(input("выбор: "))
			    if i == 0 or i > g:
			    	print("принимается ТОЛЬКО 1, 2 или 3")
			    	i=0
			except ValueError:
				print("ты чё думал сломать игру? ВЫБИРАЙ ЗАНОВО")
		if i == 1:
			if n == 1:
				a1={"name":"контр-атака","damage":"45-20","opi":"наносит урон как 3 атаки и понижает урон противника в 3 раза за комбинацию [w],[a],[d] или [w],[d],[a]","num":"3"}
				print("контр-атака: урон 45-20, наносит урон как 3 атаки и понижает урон противника в 3 раза за комбинацию [w],[a],[d] или [w],[d],[a]\nстоит 45 монет покупаешь?\n  да-1\n  нет-2")
				i=0
				while i == 0 :
					try:
					    i=int(input("выбор: "))
					    if i == 0 or i > 2:
					    	print("принимается ТОЛЬКО 1 или 2")
					    	i=0
					except ValueError:
						print("ты чё думал сломать игру? ВЫБИРАЙ ЗАНОВО")
				if i == 1 and monet >= 45:
					print("ты купил контр-атаку")
					monet-=45
					if pari_all == []:
						pari=3
					pari_all.append(a1)
				elif monet < 45 and i==1:
					print("у тебя не хватает монет")
				else:
					pass
			elif n==2:
				a1={"name":"атака-щитом","damage":"20","opi":"защитись щитом и одновременно атакуй противника","num":"4"}
				print(f"{a1["name"]}, урон {a1["damage"]}, {a1["opi"]}\nстоит 85 монет покупаешь?\n  да-1\n  нет-2")
				i=0
				while i == 0 :
					try:
					    i=int(input("выбор: "))
					    if i == 0 or i > 2:
					    	print("принимается ТОЛЬКО 1 или 2")
					    	i=0
					except ValueError:
						print("ты чё думал сломать игру? ВЫБИРАЙ ЗАНОВО")
				if i == 1 and monet >= 85:
					print("ты купил атаку-щитом")
					monet-=85
					if pari_all == []:
						pari=4
					pari_all.append(a1)
				elif monet < 85 and i==1:
					print("у тебя не хватает монет")
				else:
					pass
		elif i == 2:
			if pari_all != [] and len(pari_all) != 1:
				print("на какую способность ты хочешь поменять")
				for i in range(len(pari_all)):
					print(pari_all[i]["name"]+": урон",pari_all[i]["damage"],",описание:",pari_all[i]["opi"]+"-"+str(i+1))
				i1=0
				while i1 == 0 :
					try:
					    i1=int(input("выбор: "))
					    if i1 == 0 and i > len(pari_all):
					    	print(f"принимается ТОЛЬКО цифры с 1 до {len(pari_all)}")
					    	i1=0
					except ValueError:
						print("ты чё думал сломать игру? ВЫБИРАЙ ЗАНОВО")
				i1-=1
				print(pari_all[i1]["name"])
				pari=int(pari_all[i1]["num"] )
			elif len(pari_all) == 1:
				print("у тебя всего одна техника ты её не можешь сменить")
			else:
				print("у тебя нет техник")
		elif i == 3 :
			print("зелье жизни +10 хп и +15 мхп за 50 монет покупаешь?\n  да-1\n  нет-2")
			i1=0
			while i1 == 0 :
				try:
				    i1=int(input("выбор: "))
				    if i1 == 0 and i > len(pari_all):
				    	print(f"принимается ТОЛЬКО цифры 1 и 2")
				    	i1=0
				except ValueError:
					print("ты чё думал сломать игру? ВЫБИРАЙ ЗАНОВО")
			if i1 == 1 and monet>=50:
				print("ты покупаешь и пьёшь зелье")
				hp+=10
				mhp+=15
				monet-=50
			elif i1 == 1 and monet < 50:
				print("не хватает деняг")
	print("ты выходишь из магазина")
	return monet,pari,pari_all,hp,mhp
if start == 1:
	act=0
	max_shote = 0
	if i == 1:
		pari_all=[]
	elif i == 2:
		pari_all=[{"name": "парирование","damage": "15","opi": "блокирует удар противника, используя клавиши [w] или [a] или [s] или [d]","num": 2}]
	elif i == 3:
		pari_all=[{"name": "дабл хит","damage": "30","opi": "наносит урон как 2 атаки при максимальной удаче, используя клавиши [a],[d] или [d],[a]","num": 1}]
	else:
		pari_all=[
	    {
	        "name": "парирование",
	        "damage": "15",
	        "opi": "блокирует удар противника, используя клавиши [w] или [a] или [s] или [d]",
	        "num": 2
	    },
	    {
	        "name": "дабл хит",
	        "damage": "30",
	        "opi": "наносит урон как 2 атаки при максимальной удаче, используя клавиши [a],[d] или [d],[a]",
	        "num": 1
	    }
	]
	map_num=[0,0,-1]
t=hp
this=1
map_l=[
				"""
----------
|     .2 /
\\    /  /
 \\  .1  |
  \\_____/
  1-поселение людей
  2-тренеровочная арена
""",
"""
------------
|     .2   /
|    /    /
|   .1   /
\\   |   /
 \\  .3 /
  ~~~~~
  1-поселение людей
  2-тренеровочная арена
  3-проход к полю боя
"""
]
map_pb=[
					"""
/~~~~~~~\\
\\  .3  ~ \\
 \\  \\     \\__
  |  |-\\_.5 /
  \\  .4____/
   \\--/
  3-проход к поселению людей
  4-магазин техника
  5-аванпост людей
""",
					"""
|~~~~~~~~~~~|       /---\\
|  .3  ~  ~ \\_/~\\__/ .7  \\
|   \\ ~      ~       |    \\____
|    |-\\_.5/-\\___/\\--•6---\\__.8\\
| ~  .4      /~\\__/-/ / /-/____/
|-----------/\\     /_.9/
  3-проход к поселению людей
  4-магазин техника
  5-аванпост людей
  6-поле боя
  7-аванпост гоблинов
  8-аванпост магов
"""

]
while t > 0:
	print(f"у тебя есть кусок карты:{map_l[map_num[1]] if map_num[0] == 0 else map_pb[map_num[2]]}  ты в точке: {this}")
	go=helper.Game_helper.input_int("выбор: ","ты чё думал игру сломать? ВЫБИРАЙ ЗАНОГО")
	if this != go:
		if go >= 9:
			print("такой локации несуществует в данной версии игры")
		elif go == 8 and this == 6:
			print("на данный момент пройти в деревню магов нельзя")
			go=6
		elif go == 7 and this == 6:
			if cheker != 2:
				print("магическое поле не дал тебе пройти")
			else:
				print("а не пойти ли тебе нахуй мамский хакер?")
			go = 6
		elif go == 7 or go == 8:
			print("для аванпостов магов и гоблиннов нужно прийти в поле боя")
		elif go == 6:
			print("на пути к полю боя на тебя нападает группа гоблинов и маг")
			u_enemy=20
			unit="гоблин"
			hp_enemy=65
			for r in range(3):
				u_enemy-=5
				t=game(hp,mhp,pari,u_enemy,hp_enemy,unit,cheker,0)
				print("1 гоблин повержен осталось:",2-r)
				if t <= 0:
					print("у тебя здоровье стало меньше 0 и ты умер")
					helper.App_helper.saveApp("save/istoria","нет сохранения")
					input("enter чтобы завершить игру")
					exit()
			print("убив гоблинов на тебя... не нападает нападает маг, хотя они истребляют твой народ, но тебя он не трогает и телепортируется")
			if t <= 0:
				print("у тебя здоровье стало меньше 0 и ты умер")
				helper.App_helper.saveApp("save/istoria","нет сохранения")
				input("enter чтобы завершить игру")
				exit()
			print("ты добираещься до поля боя")
		elif go == 5 and map_num[2] >= 0:
			print("на пути к аванпосту на тебя нападает группа гоблинов и маг")
			u_enemy=20
			unit="гоблин"
			hp_enemy=65
			for r in range(3):
				u_enemy-=5
				t=game(hp,mhp,pari,u_enemy,hp_enemy,unit,cheker,0)
				print("1 гоблин повержен осталось:",2-r)
				if t <= 0:
					print("у тебя здоровье стало меньше 0 и ты умер")
					helper.App_helper.saveApp("save/istoria","нет сохранения")
					input("enter чтобы завершить игру")
					exit()
			print("убив гоблинов на тебя... не нападает нападает маг, хотя они истребляют твой народ, но тебя он не трогает и телепортируется")
			if t <= 0:
				print("у тебя здоровье стало меньше 0 и ты умер")
				helper.App_helper.saveApp("save/istoria","нет сохранения")
				input("enter чтобы завершить игру")
				exit()
			print("ты добираещься до аванпоста")
		elif ((go == 4 and this == 3) or (this == 4 and go == 3)) and map_num[2] >= 0:
			pass
		elif go == 3 and map_num[1] < 1:
			print("ты никуда не пошёл")
			go=this
		elif go == 4 and map_num[2] >= 0:
			print("на тебя нападает гоблин разведчик")
			u_enemy=6
			hp_enemy=40
			unit="гоблин разведчик"
			t=game(hp,mhp,pari,u_enemy,hp_enemy,unit,cheker,0)
			if t <= 0:
				print("у тебя здоровье стало меньше 0 и ты умер")
				helper.App_helper.saveApp("save/istoria","нет сохранения")
				input("enter чтобы завершить игру")
				exit()
		elif go >= 4 and map_num[2] < 0:
			print("ты никуда не пошёл")
			go=this
		elif go == 3 or this == 3:
			print("на тебя нападает гоблин разведчик")
			u_enemy=6
			hp_enemy=40
			unit="гоблин разведчик"
			t=game(hp,mhp,pari,u_enemy,hp_enemy,unit,cheker,0)
		if t <= 0:
			print("у тебя здоровье стало меньше 0 и ты умер")
			helper.App_helper.saveApp("save/istoria","нет сохранения")
			input("enter чтобы завершить игру")
			exit()
		this=go
	if this == 1:
		print("что тебе нужно сделать?\n  ничего-1\n  выйти из игры-2")
		map_num[0]=0
		if helper.Game_helper.input_int("выбор: ","ты чё думал игру сломать? ВЫБИРАЙ ЗАНОГО") == 2:
			helper.App_helper.saveApp("save/istoria",[hp,mhp,cheker,pari,pari_all,max_shote,monet,map_num,act])
			exit()
	elif this == 2:
		map_num[0]=0
		if map_num[1] == 0:
			print("тебя обучили здешнему искуству и дали 2 кусок карты поселения людей")
			map_num[1]+=1
		elif act == 1:
			print("тебе предлагают поучаствовать в тренеровке (здесь бесконечный режим и если хп опустится до 0 то ты выживешь) по участвовать?\n  да-1\n  нет-2")
			if helper.Game_helper.input_int("выбор: ","ты чё думал игру сломать? ВЫБИРАЙ ЗАНОГО") == 1:
				print("ты решаешь поучаствовать в тренеровке")
				unit="человек"
				hp_enemy=90
				u_enemy=10
				shote = 0
				while game(hp,mhp,pari,u_enemy,hp_enemy,unit,cheker,0) > 0:
					print("человек ушёл с арены и на замену ему пришёл более сильный человек")
					shote+=1
					hp_enemy+=10
					u_enemy+=2
				print("тебя по итогу одалел человек под номером:",shote+1)
				if shote > max_shote:
					print("ты определённо стал совершеннее. в прошлый раз ты победил",max_shote,"людей а в этот:",shote)
					max_shote = shote
			else:
				print("ты решил не учавствовать")
		else:
			print("тебе покачто здесь делать нечего")
			map_num[0]=0
	elif this == 3:
		if map_num[2] == -1:
			print("ты находишь кусок карты который относится к полю боя и 30 монет")
			monet+=30
			map_num[2]=0
		if map_num[0]==0:
			print("открыть карту поля боя?")
			print("  да-1\n  нет-2")
			map_num[0]=1 if helper.Game_helper.input_int("выбор: ","ты чё думал игру сломать? ВЫБИРАЙ ЗАНОГО") == 1 else 0
		else:
			print("закрыть карту поля боя?")
			print("  да-1\n  нет-2")
			map_num[0]=helper.Game_helper.input_int("выбор: ","ты чё думал игру сломать? ВЫБИРАЙ ЗАНОГО") -1
	elif this == 4:
		print("ты входишь в магазин")
		monet,pari,pari_all,hp,mhp=shop(monet,pari,pari_all,hp,mhp,1)
		map_num[0]=1
	elif this == 5:
		map_num[0]=1
		if map_num[2] == 0:
			print("тебе в аванпосте дают артефакт, 20 монет, зелье жизни, кусок карты поля боя и переходишь из вступления в 1 акт")
			hp+=10
			mhp+=15
			monet+=20
			cheker=1
			map_num[2]+=1
			act=1
			print("===== акт 1 =====")
			time.sleep(3)
			print("БОЙ НА ПОЛЕ БОЯ")