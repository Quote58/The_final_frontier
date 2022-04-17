#:::My game:::

from __future__ import division
import pygame ; import math ; import random
pygame.init()

#:::classes:::
class Ship(object):
	def __init__(self, position):
		self.frames = []	#ship animation
		self.frame = 0		
		for i in range (3):
			self.frames.append(pygame.image.load
				("Images/Game/ship%d.png" % i))

		self.pos = position	
		self.rect = self.frames[self.frame].get_rect()
		self.rect.center = self.pos
		self.m_p = 0
		self.cool_down = 0
		self.pickup = False
		self.exploding = False

	def draw(self, screen):
		img = self.frames[self.frame//10]
		self.frame = (self.frame + 1) % (10*len(self.frames))
		screen.blit(img, self.rect)
	#would put this somewhere else but it needs to happen every frame
	#so might as well not waste another method on it
		if self.cool_down > 0:
			self.cool_down = (self.cool_down + 1) % self.firerate

		if self.pickup == True:
			self.firerate = 10
		else:
			self.firerate = 20

	def fire(self):
		if self.cool_down == 0:
			self.cool_down += 1
			return True

	def get_pos(self, mouse_pos):
		self.m_p = mouse_pos
		self.rect.center = self.m_p

class Beam(object):
	def __init__(self, position):
		self.pos = position
		self.img = pygame.image.load("Images/Game/beams/10.png")
		self.rect = self.img.get_rect()

	def draw(self, screen):
		self.rect.center = self.pos
		screen.blit(self.img, self.rect)

	def move(self):
		dx = self.speed * math.cos(math.radians(0))
		dy = self.speed * math.sin(math.radians(0))
		self.pos = (self.pos[0] + dx, self.pos[1] - dy)

	def check_item(self, player):
		if player.pickup == True:
			self.speed = 20
			self.img = pygame.image.load("Images/Game/beams/11.png")
		else:
			self.speed = 10
			self.img = pygame.image.load("Images/Game/beams/10.png")

class Pickup(object):
	def __init__(self):
		self.pos = (random.randint(200,800),random.randint(100,600))
		self.img = pygame.image.load("Images/Game/powerups/pickup.png")
		self.rect = self.img.get_rect()
		self.rect.center = self.pos

	def draw(self, screen):
		screen.blit(self.img, self.rect)

class Life(object):
	def __init__(self, index):
		self.pos = (400+index*20,20)
		self.img = pygame.image.load("Images/Game/powerups/lives.png")
		self.rect = self.img.get_rect()
		self.rect.center = self.pos

	def draw(self, screen):
		screen.blit(self.img, self.rect)

class Difficulty(object):
	def __init__(self, index):
		self.pos = (200, 20)
		self.img = pygame.image.load("Images/Game/hud/D%d.png" % index)
		self.rect = self.img.get_rect()
		self.rect.center = self.pos

	def draw(self, screen):
		screen.blit(self.img, self.rect)


#:::Other functions:::

def Collide(rect1, img1, rect2, img2):
	mask1 = pygame.mask.from_surface(img1)
	mask2 = pygame.mask.from_surface(img2)
	dx = rect1.left - rect2.left
	dy = rect1.top - rect2.top
	return mask2.overlap(mask1, (dx,dy)) != None

def check_bounds(objrect, screen):
	return screen.get_rect().colliderect(objrect)


#:::Definitions:::

width = 800 ; height = 600 ; size = (width, height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

Shots = []
Pickups = []
gametime = 0
mouse_click = False
lives = [Life(0),Life(1),Life(2)]



Player = Ship((width/2,height/2))

hudline = pygame.transform.scale(pygame.image.load("Images/Game/hud/hud line.png"), (width, 5))
hudlinerect = hudline.get_rect()
hudlinerect.center = (width/2,33)
livestext = pygame.image.load("Images/Game/hud/livestext.png")
livestextrect = livestext.get_rect()
livestextrect.center = (325,20)

difficultytext = pygame.image.load("Images/Game/hud/difficultytext.png")
difftxtrect = difficultytext.get_rect()
difftxtrect.center = (75,20)

bgmusic = pygame.mixer.Sound("Sounds/bgmusic.wav")
bgmusic.set_volume(0.1)
shoot = pygame.mixer.Sound("Sounds/laser.wav")
shoot.set_volume(1)
gamelevel = 0
gameleveltime = 0

how_many = 5

difflist = [Difficulty(gamelevel)]


while True:
	bgmusic.play(-1)
	clock.tick(fps)
	gametime += 1 ; gameleveltime += 1

	for i in pygame.event.get():	
		if i.type == pygame.QUIT:
			exit()
		elif i.type == pygame.MOUSEMOTION:
			if i.pos[1] > 45:
				Player.get_pos(i.pos)
		elif i.type == pygame.MOUSEBUTTONDOWN:
			mouse_click = True
			if Player.fire():
				shoot.play()
				Shots.append(Beam((Player.rect.centerx,Player.rect.centery+8)))
		elif i.type == pygame.MOUSEBUTTONUP:
			mouse_click = False

	screen.fill((0,0,0))
	
	screen.blit(hudline,hudlinerect)
	screen.blit(livestext,livestextrect)
	screen.blit(difficultytext, difftxtrect)

	for i in Shots:
		i.draw(screen)
		i.check_item(Player)
		i.move()

	Shots = [ i for i in Shots if check_bounds(i.rect,screen) ]


	Player.draw(screen)

	if gametime == fps*20:
		gametime = 0
		Pickups.append(Pickup())
	elif gametime == fps*10:
		Pickups = []
	elif gametime == fps*5:
		Player.pickup = False

	if gameleveltime == fps*60:
		gameleveltime = 0
		if gamelevel < 2:
			gamelevel += 1
			for i in difflist:
				difflist.remove(i)
				difflist.append(Difficulty(gamelevel))
				asterlist = []
				how_many += 2
				pygame.time.wait(500)


	for i in Pickups:
		i.draw(screen)
		if Collide(i.rect, i.img, Player.rect, Player.frames[Player.frame//10]):
			Pickups.remove(i)
			Player.pickup = True
					

	for i in lives:
		i.draw(screen)
	difflist[0].draw(screen)
	

	pygame.display.flip()



















