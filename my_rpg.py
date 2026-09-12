import random
import time

print("выбирете сложность:\n  лёгкая-1  \n  сложная-2  \n  да-3")
i=0
while i == 0:
	try:
	    i=int(input("выбрал: "))
	except ValueError:
		print("ты чё думал сломать игру? ВЫБИРАЙ ЗАНОВО")

if i == 1:
	print("у тебя 40 хп из 75 возможных и 50 золота")
	hp=40
	mhp=75
	monet=50
	pari=0

elif i == 2:
	print("у тебя 20 хп из 25 возможных, возможность делать дабл хит и 10 золота")
	hp=20
	mhp=25
	monet=10
	pari=1

else:
	if i != 3:
		print(f"а чё с лицом? хули выбрал число {i}? ладно будешь играть на сложности \"да\"")
	print("у тебя 1 hp, возможность парировать и 0 золота")
	hp=1
	mhp=1
	monet=0
	pari=2

input("нажми enter для продолжения...")

if True:
	print("перед тобой обучающий враг, твои действия:\n  атаковать-1\n  защитится-2\n  проверить-3")
	if pari == 0:
		print(" ???-4")
	elif pari == 2:
		print("  парировать-4")
	else:
		print("  дабл хит-4")
	i1=0
	while i1 == 0:
		try:
		    i1=int(input("действие: "))
		except ValueError:
			print("ты чё думал сломать игру? ВЫБИРАЙ ЗАНОВО")
	if i1==1:
		u=random.randint(1,10)
		print(f"ты атакуешь врага и наносишь: {u} урона")
	elif i1==2:
		print("следуйщий урон понижен в 2 раза")
		n=1
	elif i1==3:
		print("маникен: 15 хп и урон 0")
	elif i1==4:
		print("ты ничего не сделал...")
	print("маникен является... не одушлевлённым предметом.\nты обходищь маникен")


print("гоблин преграждает путь,")
hp_enemy=40
u_enemy=6
unit="гоблин"
def game(hp,mhp,pari,u_enemy,hp_enemy,unit):
	n=0
	while hp > 0 and hp_enemy > 0:
		print(f"у тебя {hp}/{mhp} хп")
		pari_time=0
		if n != 0:
			n-=1
		print("твои действия:\n  атаковать-1\n  защитится-2\n  проверить-3")
		if pari == 0:
			print(" ???-4")
		elif pari == 2:
			print("  парировать-4")
		else:
			print("  дабл хит-4")
		print("  сильное лечение-5")
		i=0
		while i == 0:
			try:
			    i=int(input("действие: "))
			except ValueError:
				print("ты чё думал сломать игру? ВЫБИРАЙ ЗАНОВО")
		if i==1:
			u=random.randint(10,15)
			print(f"ты атакуешь врага и наносишь: {u} урона")
			hp_enemy-=u
		elif i==2:
			print("на следуйщие 2 хода урон понижен в 2 раза")
			n=2
		elif i==3:
			print(f"{unit}: {hp_enemy} хп и урон {u_enemy} ")
		elif i==4:
			if pari==2:
				print("ты парируещь атаку противника после мини игры")
				pari_time=1
			elif pari==1:
				print("ты атакуешь 2 раза после мини игры")
				pari_time=2
			else:
				print("ты ничего не сделал...")
		elif i==5:
			q=random.randint(15,32)
			if hp+q > mhp:
				q=mhp-hp
			print(f"ты начинаешь лечение и излечиваешь {q} хп")
			hp+=q
			
		if pari_time==1:
			input("когда ты парируещь нужно быстро написать букву которая написанно. когда готов нажми enter:")
			pari_dop=random.randint(1,4)
			print("приготовся парировать...")
			print("3")
			time.sleep(1)
			print("2")
			time.sleep(1)
			print("1")
			time.sleep(1)
			print("ПАРИРУЙ")
			if pari_dop==1:
			    t="w"
			elif pari_dop==2:
				t="a"
			elif pari_dop==3:
				t="s"
			else:
				t="d"
			pari_enemy=time.time()
			if input("	"+t) == t and pari_enemy-time.time()>-1:
				print("парирование удалось и ты нанёс 15 урона противнику")
				hp_enemy-=15
			else:
				print(f"ты не вовремя парировал и получил: {u_enemy} урона")
				hp-=u_enemy
		elif pari_time==2:
			input("когда ты делаешь дабл хит нужно за короткое время нажать a d enter или d a enter как написать будет понятно в процессе. когда готов нажми enter:")
			pari_dop=random.randint(1,2)
			print("приготовся...")
			print("3")
			time.sleep(1)
			print("2")
			time.sleep(1)
			print("1")
			time.sleep(1)
			print("ДАБЛ ХИТ")
			pari_enemy=time.time()
			if pari_dop==1:
				t="ad"
			else:
				t="da"
			if input("	"+t) == t and pari_enemy-time.time()>-3:
				print("ты нанёс 30 урона")
				hp_enemy-=30
			if n >= 1:
				if random.randint(1,5)<=3:
					print(f"ты впитал {u_enemy-(u_enemy/2)} урона")
					hp-=u_enemy-(u_enemy/2)
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
					print(f"ты впитал {u_enemy-(u_enemy/2)} урона")
					hp-=u_enemy-(u_enemy/2)
				else:
					print("щит можно было и не ставить. враг промахнулся")
			else:
				if random.randint(1,5)<=3:
					print(f"ты впитал {u_enemy} урона")
					hp-=u_enemy
				else:
					print("удача! враг промахнулся")
	return hp
if int(game(hp,mhp,pari,u_enemy,hp_enemy,unit)) > 0:
	print("ты победил гоблина и стал сильнее, продолжая путь")
	if i >= 3:
		mhp+=14
		hp+=4
		print("ты стали более сильным и у тебя теперь не 1 hp\nсменить парирование на дабл хит?\n  да-1\n  нет-2")
		i1=0
		while i1 == 0 or i1 > 2:
			try:
			    i1=int(input("выбор: "))
			    if i1 == 0 or i1 > 2:
			    	print("принимаются ТОЛЬКО 1 или 2")
			except ValueError:
				print("ты чё думал сломать игру? ВЫБИРАЙ ЗАНОВО")
		if i1 == 1:
			print("это твоё решение сменить пери на дабл хит я тебя не могу судить")
			pari=1
		else:
			print("это твоё решение оставить пери я тебя не могу судить")
	mhp+=10
	hp+=5
	print("через некоторое время...")
	print("маг телепортировался и преграждает путь")
	hp_enemy=150
	u_enemy=17
	unit="маг"
	if int(game(hp,mhp,pari,u_enemy,hp_enemy,unit)) > 0:
		mhp+=15
		hp+=5
		print("ты выйграл")
	else:
		print("ты проиграл")
else:
	print("ты проиграл")
input("нажмите enter для завершения...")
	
		
		
	