"""
Triángulos, Pirámides, Rombo, Otras formas...
"""


def trianguloTA():
	tamaina = 5
	for i in range(tamaina, 0, -1):
		for j in range(0, i):
			print("*", end=" ")
		print()

def trianguloTB():
	tamaina = 5
	for i in range(tamaina, 0, -1):
		for j in range(tamaina - i):
			print(" ", end=" ")
		for k in range(0, i):
			print("x", end=" ")
		print()

def trianguloTC():
	tamaina = 5
	for i in range(tamaina):
		for j in range(tamaina - i - 1):
			print(" ", end=" ")
		for k in range(0, i + 1):
			print("*", end=" ")
		print()

def trianguloTD():
	tamaina = 5
	for i in range(tamaina):
		for j in range(0, i + 1):
			print("*", end=" ")
		print()

def piramidePA():
	tamaina = 5
	for i in range(tamaina, 0, -1):
		for j in range(tamaina - i):
			print(" ", end=" ")
		for k in range(0, i):
			print("*", end=" ")
		for l in range(1, i):
			print("*", end=" ")
		print()



if __name__=="__main__":
	#.......triángulos.......
	#trianguloTA()
	#trianguloTB()
	#trianguloTC()
	#trianguloTD()
	#.......pirámides.......
	piramidePA()