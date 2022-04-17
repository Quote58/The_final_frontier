#:::Credits:::
#titlescreen background music........Author, 'cynicmusic'. License, 'CC-BY 3.0', 'CC-BY-SA 3.0', 'GPL 3.0'
#gamescreen background music.........Author, 'Zander Noriega'. Licence, 'CC-BY 3.0'
#gameoverscreen background music.....Author, 'avgvsta'. License, 'CC-BY-SA 3.0'
#shot sound..........................Author,'dklon'. License, 'CC-BY 3.0'
#explosion sound.....................Author, 'Luke.RUSTLTD'. License, 'CC0'
#powerup sound.......................Author, 'Blender Foundation'. License, 'CC-BY 3.0'
#death sound.........................Author,'sauer2'. License, 'CC0'

#All artwork in this game was drawn by me using the program mtPaint editor, as
#well as Gimp photo editor (mainly used for transparencies and cropping).


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
		if index == 3:		
			self.game = 2
		else:
			self.game = 0
	def draw(self):
		if self.bold == False:
			self.img = pygame.image.load("images/title/%d.png" % self.index)
		else:
			self.img = pygame.image.load("images/title/%db.png" % self.index)
		self.rect = self.img.get_rect()
		self.rect.center = self.pos
		screen.blit(self.img, self.rect)		
		if self.non_static == True:
			if self.index == 2:
				exit()
			elif self.index == 1:
				self.game = 1
			elif self.index == 3 or self.index == 4:
				self.game = 0
			elif self.index == 5:
				self.game = 3
	def game_check(self):
		return self.game

#----------------------------------------


class Ship(object):
	def __init__(self, position):
		self.pos = position ; self.beamlvl = 0
		self.exploding = False
		self.fast = False
		self.cool_down = 0 ; self.fastime = 0
		self.supermetre = 0 ; self.supermetremax = 150
		self.barwait = 0 ; self.hudcount = 0
		self.lives = [0,1,2,3]
		self.points = 0

		#ship animation
		self.frames = [] ; self.frame = 0
		for i in range (3):
			self.frames.append(pygame.image.load
				("images/game/ship%d.png" % i))
		self.rect = self.frames[self.frame].get_rect()
		self.rect.center = self.pos

	def draw(self, screen):
		img = self.frames[self.frame//10]
		self.frame = (self.frame + 1) % (10*len(self.frames))
		screen.blit(img, self.rect)

		if self.fast == True:
			self.firerate = 10
		else:
			self.firerate = 20
		
		if self.cool_down > 0:
			self.cool_down = (self.cool_down + 1) % self.firerate

	def checkmode(self, fps):
		if self.fast and self.fastime == fps*6:
			self.fast = False
			self.fastime = 0 ; self.supermetre = 0 ; self.barwait = 0
		elif self.fast:
			self.fastime += 1
		else:
			self.barwait += 1

	def can_fire(self):
		if self.cool_down == 0:
			self.cool_down += 1
			return True

	def get_pos(self, mouse_pos):
		self.rect.center = mouse_pos

#----------------------------------------

class Beam(object):
	def __init__(self,position,player):
		self.pos = position
		self.angle = 0
		self.hit = False
		if player.fast:
			self.a = 1 ; self.speed = 20
		else:
			self.a = 0 ; self.speed = 10
	def draw(self,screen):
		self.rect.center = self.pos
		screen.blit(self.img,self.rect)

	def move(self):
		dx = self.speed * math.cos(math.radians(self.angle))
		dy = self.speed * math.sin(math.radians(self.angle))
		self.pos = (self.pos[0] + dx, self.pos[1] - dy)

class Default(Beam):
	def __init__(self,position,player):
		super(Default, self).__init__(position,player)
		self.img = pygame.image.load("images/game/beams/0%d.png" % self.a)
		self.rect = self.img.get_rect()
		self.damage = 1

class Wide(Beam):
	def __init__(self,position,player):
		super(Wide, self).__init__(position,player)
		self.img = pygame.image.load("images/game/beams/1%d.png" % self.a)
		self.rect = self.img.get_rect()
		self.damage = 3

class Spread(Beam):
	def __init__(self,position,player,index):
		super(Spread, self).__init__(position,player)
		self.img = pygame.image.load("images/game/beams/2%d%d.png" % (index,self.a))
		self.rect = self.img.get_rect()
		anglelist = [40, 0, 330]
		self.angle = anglelist[index]
		self.damage = 3

#----------------------------------------

class Powerup(object):
	def __init__(self,type,position):
		self.pos = position
		self.frames = []
		self.frame = 0
		self.time = 0
		for i in range(3):
			self.frames.append(pygame.image.load
				("images/game/powerups/%d%d.png" % (type,i)))
		self.rect = self.frames[self.frame].get_rect()
		self.rect.center = self.pos

	def draw(self, screen):
		self.time += 1
		img = self.frames[self.frame//5]
		self.frame = (self.frame + 1) % (5*len(self.frames))
		screen.blit(img, self.rect)

class Life(Powerup):
	def __init__(self,position):
		self.type = 2
		self.maxtime = 4
		super(Life, self).__init__(self.type,position)

	def collision(self, player):
		if len(player.lives) == 1:
			player.lives.append(1)
		elif len(player.lives) == 2:
			player.lives.append(2)
		elif len(player.lives) == 3:
			player.lives.append(3)
		else:
			player.points += 100

class Accellmetre(Powerup):
	def __init__(self,position):
		self.maxtime = 8
		self.type = 3
		super(Accellmetre, self).__init__(self.type,position)

	def collision(self, player):
		if player.supermetremax > 50:
			player.supermetremax -= 50
			if player.supermetre > 50:
				player.supermetre = 50
		else:
			player.points += 200
class Beams(Powerup):
	def __init__(self, type,position):
		self.maxtime = 10
		super(Beams, self).__init__(type-1,position)

	def collision(self, player):
		player.beamlvl = self.type

class Widebeam(Beams):
	def __init__(self,position):
		self.type = 1
		super(Widebeam, self).__init__(self.type,position)

class Spreadbeam(Beams):
	def __init__(self,position):
		self.type = 2
		super(Spreadbeam, self).__init__(self.type,position)

#----------------------------------------

class Enemy(object):
	def __init__(self,type,angle):
		self.pos = (740,random.randint(70,530))
		self.speed = (random.randint(0,6))
		self.frames = []
		self.frame = 0
		self.hit = False
		self.dead = False
		t = random.randint(8,18)
		if t > 14:
			self.health += 1
		for i in range(6):
			self.frames.append(pygame.transform.scale(pygame.image.load
				("images/game/enemies/%d%d.png" % (type,i)),(t*6,t*2)))
		self.rect = self.frames[self.frame].get_rect()
		self.comframes = []
		self.comframe = 0
		for i in range(4):
			self.comframes.append(pygame.image.load
				("images/game/enemies/ex%d%d.png" % (type,i)))
		self.angle = angle
		self.speed = random.randint(6,12)

	def move(self):
		dx = self.speed * math.cos(math.radians(self.angle))
		dy = self.speed * math.sin(math.radians(self.angle))
		self.pos = (self.pos[0] + dx, self.pos[1] - dy)


class CommetS(Enemy):
	def __init__(self):
		self.type = 0
		self.health = 1
		super(CommetS,self).__init__(self.type,180)

	def draw(self,screen):
		self.rect.center = self.pos
		if self.dead == True:
			img = self.comframes[self.comframe//5]
			if self.comframe != 5*len(self.comframes):
				self.comframe += 1
		else:
			img = self.frames[self.frame//5]
			self.frame = (self.frame + 1) % (5*len(self.frames))
		screen.blit(img, self.rect)

class CommetC(Enemy):
	def __init__(self):

		self.type = 0
		self.health = 1
		angle = 0
		if random.randint(0,1) == 1:
			angle = 180-random.randint(5,50)
			self.minus = True
		else:
			angle = 180+random.randint(5,50)
			self.minus = False
		super(CommetC,self).__init__(self.type,angle)

	def rotate(self):
		self.rotangle = -self.angle
		tempimg = self.frames[self.frame//5]
		self.rotimg = pygame.transform.flip(pygame.transform.rotate(tempimg, self.rotangle), True, False)
		self.rect = self.rotimg.get_rect()

	def draw(self,screen):
		if self.minus == True:
			self.angle -= 1
		else:
			self.angle += 1
		if self.dead == True:
			self.rotimg = self.comframes[self.comframe//5]
			if self.comframe != 5*len(self.comframes):
				self.comframe += 1
		else:
			self.frame = (self.frame + 1) % (5*len(self.frames))
		self.rect.center = self.pos
		screen.blit(self.rotimg, self.rect)

#:::Other functions:::

def Collide(rect1, img1, rect2, img2):
	mask1 = pygame.mask.from_surface(img1)
	mask2 = pygame.mask.from_surface(img2)
	dx = rect1.left - rect2.left
	dy = rect1.top - rect2.top
	return mask2.overlap(mask1, (dx,dy)) != None

def check_bounds(objrect, screen):
	return screen.get_rect().colliderect(objrect)

def Super_metre(v, screen, xpos, tilemaps, maxv):
	xpos_blank = tuple(xpos)
	xpos_blank = list(xpos_blank)
	for i in range(maxv):
		screen.blit(tilemaps[0],tuple(xpos_blank))
		xpos_blank[0] += 1
	if v < maxv:
		tile = tilemaps[1]
	else:
		tile = tilemaps[2]
	for i in range(v):
		screen.blit(tile,tuple(xpos))
		xpos[0] += 1

def drawpoints(points, newsize, pos, pixels,angle):
	if points > 9999:
		points = 9999
	digit1 = points // 1000	# 1
	digit2 = (points - digit1*1000) // 100	# 2
	digit3 = (points - (digit1*1000+digit2*100)) // 10
	digit4 = points - (digit1*1000+digit2*100+digit3*10)
	digits = [digit1,digit2,digit3,digit4]
	for i in range(4):
		screen.blit(pygame.transform.rotate(
			   pygame.transform.scale
			   (pygame.image.load("images/game/hud/numbers/%d.png" 
			   % digits[i]), tuple(newsize)), angle),(pos[0]+pixels*i,pos[1]))

def asterstuff(i,player,plist,death):
	if i.health < 1:
		i.dead = True ; player.points += 10 ; lilexplode.play()
		if random.randint(0,5) == 1:	#tem drop chances
			plist.append(Life(i.pos))
		if random.randint(0,65) == 1:
			plist.append(Accellmetre(i.pos))
		if random.randint(0,35) == 1:
			plist.append(Widebeam(i.pos))
		if random.randint(0,55) == 1:
			plist.append(Spreadbeam(i.pos))
	if Collide(i.rect,i.frames[i.frame//5],player.rect,player.frames
		   [player.frame//10]) and i.hit == False:
		i.dead = True
		player.lives.remove(player.lives[len(player.lives)-1])
		death.play() ; player.get_pos((100,height//2))
		pygame.time.wait(800) ; return True



#:::General definitions:::
width = 800 ; height = 600 ; size = (width, height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
Game = 0
	#:::Sound:::
Titlemusic = pygame.mixer.Sound("sounds/Title.wav")
Titlemusic.set_volume(0.3)
shoot = pygame.mixer.Sound("sounds/shoot.wav")
shoot.set_volume(0.5)
bgmusic = pygame.mixer.Sound("sounds/bgmusic.wav")
bgmusic.set_volume(0.4)
powerup = pygame.mixer.Sound("sounds/powerup.flac")
powerup.set_volume(1)
lilexplode = pygame.mixer.Sound("sounds/explode.wav")
lilexplode.set_volume(0.4)
bigexplode = pygame.mixer.Sound("sounds/explode.wav")
bigexplode.set_volume(0.8)
death = pygame.mixer.Sound("sounds/death.wav")
death.set_volume(0.5)
gameover = pygame.mixer.Sound("sounds/game over.ogg")
gameover.set_volume(0.5)
	#hud setup
TL = pygame.transform.scale(pygame.image.load("images/game/hud/divider.png"),(width,3))
BL = pygame.transform.scale(pygame.image.load("images/game/hud/divider.png"),(width,3))
SBL = pygame.image.load("images/game/hud/SBL.png")
SBR = pygame.image.load("images/game/hud/SBR.png")
DT = pygame.image.load("images/game/hud/DT.png")
LT = pygame.image.load("images/game/hud/LT.png")
PT = pygame.image.load("images/game/hud/PT.png")
ST = pygame.image.load("images/game/hud/ST.png")
TP = pygame.image.load("images/title/TP.png")
imgs = [TL,DT,LT,PT,ST,BL,SBL,SBR]
	#super metre
tilemaps = [pygame.image.load("images/game/hud/0.png"),
	    pygame.image.load("images/game/hud/1.png"),
	    pygame.image.load("images/game/hud/2.png")]
bgframes = []

for i in range(7):
	bgframes.append(pygame.image.load("images/game/background/%d.png" % i))

while True:

	while Game == 3:
		#definitions specific to the title screen
		optionsbg = pygame.image.load("images/title/options.png")
		Title = Choice(0,(width//2,100),False)
		Back = Choice(4,(width//2,400),False)
		mouse_pos = (0,0)
		mouse_click = False
		while Game == 3:
			for i in pygame.event.get():	
				if i.type == pygame.QUIT:
					exit()
				elif i.type == pygame.MOUSEMOTION:
					mouse_pos = i.pos
				elif i.type == pygame.MOUSEBUTTONDOWN:
					mouse_click = True
				elif i.type == pygame.MOUSEBUTTONUP:
					mouse_click = False

			screen.blit(optionsbg,(0,0))
			Title.draw()
			Back.draw()
			if Back.rect.collidepoint(mouse_pos):
				Back.bold = True
			else:
				Back.bold = False
			Back.draw()
			if Back.bold == True and mouse_click == True:
				Game = 0
			pygame.display.flip()


	while Game == 2:
		Titlescreen = Choice(3,(width//2-20,400),False)
		bgmusic.stop()
		gameover.play(-1)
		background = (0,0,0)
		mouse_pos = (0,0)
		mouse_click = False
		angle = 250 ; anglechange = 1
		while Game == 2:
			for i in pygame.event.get():	
				if i.type == pygame.QUIT:
					exit()
				elif i.type == pygame.MOUSEMOTION:
					mouse_pos = i.pos
				elif i.type == pygame.MOUSEBUTTONDOWN:
					mouse_click = True
				elif i.type == pygame.MOUSEBUTTONUP:
					mouse_click = False

			screen.fill(background)
			screen.blit(TP,(250,200))

			if angle == 80:
				anglechange = -1
			elif angle == 280:
				anglechange = 1
			angle = (angle + anglechange) % 360

			drawpoints(player.points,[20,40],[width//2-100,height//2-20],40,angle)
			Titlescreen.draw()
			if Titlescreen.rect.collidepoint(mouse_pos):
				Titlescreen.bold = True
			else:			
				Titlescreen.bold = False
			Titlescreen.draw()
			if Titlescreen.bold == True and mouse_click == True:
				Titlescreen.non_static = True
			else:
				Titlescreen.non_static = False
			Game = Titlescreen.game_check()
	
			pygame.display.flip()

	while Game == 0:
		bgmusic.stop()
		gameover.stop()
		#definitions specific to the title screen
		background = (255,255,255)
		Title = Choice(0,(width//2,100),False)
		GameStart = Choice(1,(width//2,250),False)
		Quit = Choice(2,(width//2-35,350),False)
		Controls = Choice(5,(width//2-15,300),False)
		Options = [Title,GameStart,Quit,Controls]
		mouse_pos = (0,0)
		mouse_click = False
		Titlemusic.play(-1)
		while Game == 0:
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

			if Options[3].game_check() == 3:
				Game = 3
			else:
				Game = Options[1].game_check()
			pygame.display.flip()

	while Game == 1:
		Titlemusic.stop()
		#definitions specific to the game screen
		gametype = 0	#0 = easy, 1 = medium, 2 = hard
		gametime = 0
			#objects/variables
		player = Ship((100,height//2))
		shots = []
		plist = []
		stroids = []
		ctroids = []
		going_down = False
		initsize = [10,20]
		pos = [(0,35),(25,15),(300,15),(550,15),(25,565),(0,555),
		       (178,570),(178+player.supermetremax+1,570)]
		bgmusic.play(-1)
		bgframe = 0
		while Game == 1:
			clock.tick(fps)

			if gametime == fps*60:
				gametype = 1
				powerup.play()
			elif gametime == fps*60*3:
				gametype = 2
				powerup.play()
	
			gametime += 1

			if len(player.lives) == 0:
				Game = 2

			screen.fill((0,0,0))
			screen.blit(bgframes[bgframe//7],bgframes[bgframe//7].get_rect())
			bgframe = (bgframe + 1) % (7*len(bgframes))

			shotype = [ Default((player.rect.centerx+10,player.rect.centery+8), player),
			  	    Wide((player.rect.centerx+50,player.rect.centery+8), player), ]

			for i in range(len(pos)):
				screen.blit(imgs[i],pos[i])

			for i in player.lives:
				screen.blit(pygame.image.load("images/game/powerups/20.png"), (400+i*20,15))
			screen.blit(pygame.image.load("images/game/hud/D%d.png" % gametype), (200,15))

			#player input handling - god that if tree is ugly :(
			for i in pygame.event.get():
				if i.type == pygame.QUIT:
					exit()

				if i.type == pygame.MOUSEMOTION:
					if 545 > i.pos[1] > 45:
						player.get_pos(i.pos)

				elif i.type == pygame.MOUSEBUTTONDOWN:
					if player.can_fire():
						if player.beamlvl > 1:
							index = 0 ; ypos = 3
							xpos = player.rect.centerx+50
							for i in range(3):
								shots.append(
							Spread((xpos,player.rect.centery+ypos), 
								player, index))
								index += 1 ; ypos += 5
							if player.points >= 5000:
								shots.append(shotype[1])
						else:
							shots.append(shotype[player.beamlvl])
						shoot.play()

				elif i.type == pygame.KEYDOWN:
					if i.key == pygame.K_SPACE and player.supermetre == player.supermetremax:
						player.fast = True


			#everything else (mostly enemies/beams/player stuff)
			for i in shots:
				i.draw(screen) ; i.move()
				for u in stroids:
					if Collide(i.rect,i.img,u.rect,u.frames[u.frame//5]):
						u.health -= i.damage
						i.hit = True ; u.hit = True
				for u in ctroids:
					if Collide(i.rect,i.img,u.rect,u.frames[u.frame//5]):
						u.health -= i.damage
						i.hit = True ; u.hit = True

			shots = [i for i in shots if check_bounds(i.rect,screen) and 45 < i.pos[1] < 555 
				 and i.hit == False]

			player.draw(screen) ; player.checkmode(fps)
	
			for i in plist:
				i.draw(screen)
				if Collide(i.rect,i.frames[i.frame//5],
					   player.rect,player.frames[player.frame//10]):
					i.collision(player) ; powerup.play() ; plist.remove(i)
				if i.time == fps*i.maxtime:
					plist.remove(i)		

			for i in stroids:
				i.draw(screen)
				if i.dead == True:
					if i.comframe == 5*len(i.comframes)-1:
						stroids.remove(i)
				else:
					i.move()
					if asterstuff(i,player,plist,death):
						stroids = [] ; ctroids = []

			for i in ctroids:
				i.rotate()
				i.draw(screen)
				if i.dead == True:
					if i.comframe == 5*len(i.comframes)-1:
						ctroids.remove(i)
				else:
					i.move()
					if asterstuff(i,player,plist,death):
						stroids = [] ; ctroids = []

			stroids = [i for i in stroids if check_bounds(i.rect,screen) and 45 < i.pos[1] < 555]
			ctroids = [i for i in ctroids if check_bounds(i.rect,screen) and 60 < i.pos[1] < 520]

			if len(stroids) < 3+gametype:
				stroids.append(CommetS())
			if len(ctroids) < 2+gametype:
				ctroids.append(CommetC())


			if player.supermetre < player.supermetremax and player.barwait == 10:
				player.supermetre += 1 ; player.barwait = 0
			Super_metre(player.supermetre,screen,[180,570],tilemaps,player.supermetremax)	
			if initsize == [14,24]:
				going_down = True
			elif initsize == [10,20]:
				going_down = False

			if going_down == True and player.hudcount == 2:
				initsize[0] -= 1 ; initsize[1] -= 1 ; player.hudcount = 0
			elif going_down == False and player.hudcount == 2:
				initsize[0] += 1 ; initsize[1] += 1 ; player.hudcount = 0
	
			player.hudcount += 1

			drawpoints(player.points, initsize, [660,10], 20,0)
			pygame.display.flip()






































