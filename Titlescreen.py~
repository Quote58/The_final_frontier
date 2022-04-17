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
		self.non_static = False
		self.game = 0

	def draw(self):
		if self.bold == False:
			self.img = pygame.image.load("Images/Title/%d.png" % self.index)
		else:
			self.img = pygame.image.load("Images/Title/%db.png" % self.index)
		self.rect = self.img.get_rect()
		self.rect.center = self.pos
		screen.blit(self.img, self.rect)		
		if self.non_static == True:
			if self.index == 2:
				exit()
			elif self.index == 1:
				self.game = 1
	def game_check(self):
		return self.game


#:::Definitions:::

width = 800 ; height = 600 ; size = (width, height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

mouse_click = False
Game = 0

background = (255,255,255)
Title = Choice(0,(width//2,100),False)
GameStart = Choice(1,(width//2,250),False)
Quit = Choice(2,(width//2-38,300),False)
Options = [Title,GameStart,Quit]

Title = pygame.mixer.Sound("Sounds/Title.wav")
Title.set_volume(0.1)


mouse_pos = (0,0)


while True:

	for i in pygame.event.get():	
		if i.type == pygame.QUIT:
			exit()
		elif i.type == pygame.MOUSEMOTION:
			mouse_pos = i.pos
		elif i.type == pygame.MOUSEBUTTONDOWN:
			mouse_click = True
		elif i.type == pygame.MOUSEBUTTONUP:
			mouse_click = False

	#title screen part
	Title.play(-1)
	screen.fill(background)
	for i in Options:
		i.draw()
		if i.rect.collidepoint(mouse_pos):
			i.bold = True
		else:
			i.bold = False
		i.draw()
		if i.bold == True and mouse_click == True:
			i.non_static = True
		else:
			i.non_static = False
	Game = Options[1].game_check()



	pygame.display.flip()



















