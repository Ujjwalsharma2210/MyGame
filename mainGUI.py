import pygame

pygame.init()

# ____GLOBAL VARIABLES____
positionOfKeys = []

currentPositionOfPlayer = ()

# Size of grid
max = 3
min = -max

# Initial position of player
x, y = 0, 0

# State of the game : Running or not
gameRunning = True

# Tells if the current position is a corner or not
isCorner = False
# Tells if the current position is an edge or not
isEdge = False

# number of keys
numberOfKeys = 3

# tracks the number of keys found
keyCount = 0

# regularly used Colors
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
white = (255, 255, 255)

width, height = 900, 500

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("The Legend of Zaaru")

pygame.draw.line(screen, white, (500, 0), (500, 500))
pygame.draw.line(screen, white, (500, 250), (900, 250))

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


class InputBox:

	def __init__(self, x, y, w, h, text=''):
		self.rect = pygame.Rect(x, y, w, h)
		self.color = COLOR_INACTIVE
		self.text = text
		self.txt_surface = FONT.render(text, True, self.color)
		self.active = False

	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			# If the user clicked on the input_box rect.
			if self.rect.collidepoint(event.pos):
				# Toggle the active variable.
				self.active = not self.active
			else:
				self.active = False
			# Change the current color of the input box.
			self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
		if event.type == pygame.KEYDOWN:
			if self.active:
				if event.key == pygame.K_RETURN:
					print(self.text)
					self.text = ''
				elif event.key == pygame.K_BACKSPACE:
					self.text = self.text[:-1]
				else:
					self.text += event.unicode
				# Re-render the text.
				self.txt_surface = FONT.render(self.text, True, self.color)

	def update(self):
		# Resize the box if the text is too long.
		width = max(200, self.txt_surface.get_width()+10)
		self.rect.w = width

	def draw(self, screen):
		# Blit the text.
		screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
		# Blit the rect.
		pygame.draw.rect(screen, self.color, self.rect, 2)


def printText(strOut):
	font = pygame.font.Font('freesansbold.ttf', 14)
	text = font.render(strOut, True, red, black)
	screen.blit(text, (505, 5))


def initialization():
	printText("Hello wanderer! What's your name?")


def createGame():
	gameRunning = True

	# pygame.draw.circle(screen, red, (250, 250), 5)
	input_box1 = InputBox(505, 255, 390, 192)
	input_box1.draw(screen)

	# Asks for users name
	initialization()

	while gameRunning:

		for event in pygame.event.get():
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.QUIT()

				input_box1.handle_event(event)
				input_box1.update()

				screen.fill((30, 30, 30))
				input_box1.draw(screen)

		pygame.display.update()


createGame()
