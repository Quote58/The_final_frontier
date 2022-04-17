#:::My game:::

from __future__ import division
import pygame ; import math ; import random
pygame.init()

#:::classes:::
class Choice(object):
	def __init__(self, index, position, bold):
		self.index = index
		self.bold = bold
		self.pos = position		

	def draw(self):
		if self.bold == False:
			self.img = pygame.image.load("Images/Title/%d.png" % self.index)
		else:
			self.img = pygame.image.load("Images/Title/%db.png" % self.index)
		self.rect = self.img.get_rect()
		self.rect.center = self.pos
		screen.blit(self.img, self.rect)	
	



class Text(object):
	def __init__(self, index, position):
		pass
class Points(object):
	def __init__(self, points, position):
		pass
class Ship(object):
	def __init__(self, position):
		pass
class Pickup(object):
	def __init__(self, position):
		pass
class Asteroid(object):
	def __init__(self):
		pass
#:::other functions:::



#:::defines:::
height = 800 ; width = 600 ; size = (height, width)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

Game = 0   # 0 = title, 1 = game, 2 = endgame

	#::Objects::
		#:Title Screen:
Title = Choice(0,(width//2,100),False)
GameStart = Choice(1,(width//2,250),False)
Quit = Choice(2,(width//2-38,300),False)
Options = [Title,GameStart,Quit]
background = (255,255,255)

	#::Other variables::
#counter = 0 ; points = 0



#:::main loop:::

while True:
	clock.tick(fps)
	for i in pygame.event.get():	
		if i.type == pygame.QUIT:
			exit()
		elif i.type == pygame.MOUSEMOTION:
			mouse_pos = i.pos


	#::Title screen::
	if Game == 0:
		screen.fill(background)
		for i in Options:
			i.draw()
			if i.rect.collidepoint(mouse_pos):
				i.bold = True
			else:
				i.bold = False


	#::Main game::
	elif Game == 1:
	#	Title.stop()
	#	MainGame.play(-1)
		pass




	#::Game Over::
	elif Game == 2:
#		MainGame.stop()
#		GameOver.play(-1)
#		GameOverText.draw()
#		Points.draw(points, [position])
#		if counter < 1500:
#			counter += 1
		pass

	pygame.display.flip()


'''
		#:Game Screen:
Difficulty = Text(0, [position])
Lives = Text(0, [position])
Difficulty = Text(0, [position])
Points = Points(points,[position]) 

Ship = Ship(...)
Pickups = []
asteroids = []
		#:Game Over:
GameOverText = Choice(4, [position])

	#::Music::
Title = pygame.mixer.Sound("sounds/Title.mp3")
Title.set_volume(0.8)
MainGame = pygame.mixer.Sound("sounds/Main.x")
MainGame.set_volume(0.8)
GameOver = pygame.mixer.Sound("sounds/End.x")
GameOver.set_volume(0.8)
	#::Sound effects::
ShipExplode = pygame.mixer.Sound("sounds/Shipexplode.x")
ShipExplode.set_volume(1)
ShotFired = pygame.mixer.Sound("sounds/Shipfire.x")
ShotFired.set_volume(1)
ItemGet = pygame.mixer.Sound("sounds/Itemget.x")
ItemGet.set_volume(1)
EnemyBoom = pygame.mixer.Sound("sounds/Enemyboom.x")
EnemyBoom.set_volume(1)
'''
'''
	#::Backgrounds::
GameBack = \
pygame.transform.scale(pygame.image.load("images/Game.x"), size)
GOBack = \
pygame.transform.scale(pygame.image.load("images/End.x"), size)
'''














