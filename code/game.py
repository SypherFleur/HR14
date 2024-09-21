import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Game with Play Button')

# Load the background image
background_image = pygame.image.load('background.jpg')

# Define the Play button
button_font = pygame.font.Font(None, 74)
button_text = button_font.render('Play', True, (255, 255, 255))
button_rect = button_text.get_rect(center=(400, 300))

# Define the Welcome screen text
welcome_font = pygame.font.Font(None, 74)
welcome_text = welcome_font.render('WELCOME TO FINANCE101', True, (255, 255, 255))
welcome_rect = welcome_text.get_rect(center=(400, 300))

# Get user input for the name
user_name = input("Enter your name: ")
thought_text = pygame.font.Font(None, 50).render(f'Hey {user_name}', True, (0, 0, 0))
thought_rect = thought_text.get_rect(center=(600, 200))

# Define the thought bubble text
thought_font = pygame.font.Font(None, 50)
thought_text = thought_font.render(f'Hey {user_name}', True, (0, 0, 0))
thought_rect = thought_text.get_rect(center=(600, 200))

# Define sprite classes
class Sprite(pygame.sprite.Sprite):
	def __init__(self, image_path, x, y):
		super().__init__()
		self.image = pygame.image.load(image_path)
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

	def update(self):
		pass

class WalkingSprite(Sprite):
	def __init__(self, image_path, x, y):
		super().__init__(image_path, x, y)
		self.speed = 5

	def update(self):
		if self.rect.x < 400:
			self.rect.x += self.speed

# Create sprite instances
sprite1 = WalkingSprite('sprite1.png', 0, 400)
sprite2 = Sprite('sprite2.png', 600, 400)

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Main loop
running = True
show_welcome_screen = False
show_thought_bubble = False
clock = pygame.time.Clock()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if button_rect.collidepoint(event.pos) and not show_welcome_screen:
				show_welcome_screen = True

	# Draw the background image
	screen.blit(background_image, (0, 0))

	if show_welcome_screen:
		# Draw the Welcome screen text
		screen.blit(welcome_text, welcome_rect)
		# Update and draw sprites
		all_sprites.update()
		all_sprites.draw(screen)
		# Check if sprite1 has reached the target position
		if sprite1.rect.x >= 400:
			show_thought_bubble = True
		# Draw the thought bubble
		if show_thought_bubble:
			pygame.draw.ellipse(screen, (255, 255, 255), (500, 150, 200, 100))
			screen.blit(thought_text, thought_rect)
	else:
		# Draw the Play button
		screen.blit(button_text, button_rect)

	# Update the display
	pygame.display.update()

	# Limit the frame rate to 60 FPS
	clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
import pygame
import sys

# Define constants for image paths
BACKGROUND_IMAGE_PATH = 'path/to/your/background.jpg'
SPRITE1_IMAGE_PATH = 'path/to/your/sprite1.png'
SPRITE2_IMAGE_PATH = 'path/to/your/sprite2.png'

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Game with Play Button')

# Load the background image
background_image = pygame.image.load(BACKGROUND_IMAGE_PATH)

# Define the Play button
button_font = pygame.font.Font(None, 74)
button_text = button_font.render('Play', True, (255, 255, 255))
button_rect = button_text.get_rect(center=(400, 300))

# Define the Welcome screen text
welcome_font = pygame.font.Font(None, 74)
welcome_text = welcome_font.render('WELCOME TO FINANCE101', True, (255, 255, 255))
welcome_rect = welcome_text.get_rect(center=(400, 300))

# Get user input for the name
user_name = input("Enter your name: ")

# Define the thought bubble text
thought_font = pygame.font.Font(None, 50)
thought_text = thought_font.render(f'Hey {user_name}', True, (0, 0, 0))
thought_rect = thought_text.get_rect(center=(600, 200))

# Define sprite classes
class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pass

class WalkingSprite(Sprite):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
        self.speed = 5

    def update(self):
        if self.rect.x < 400:
            self.rect.x += self.speed

# Create sprite instances
sprite1 = WalkingSprite(SPRITE1_IMAGE_PATH, 0, 400)
sprite2 = Sprite(SPRITE2_IMAGE_PATH, 600, 400)

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Main loop
running = True
show_welcome_screen = False
show_thought_bubble = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos) and not show_welcome_screen:
                show_welcome_screen = True

    # Draw the background image
    screen.blit(background_image, (0, 0))

    if show_welcome_screen:
        # Draw the Welcome screen text
        screen.blit(welcome_text, welcome_rect)
        # Update and draw sprites
        all_sprites.update()
        all_sprites.draw(screen)
        # Check if sprite1 has reached the target position
        if sprite1.rect.x >= 400:
            show_thought_bubble = True
        # Draw the thought bubble
        if show_thought_bubble:
            pygame.draw.ellipse(screen, (255, 255, 255), (500, 150, 200, 100))
            screen.blit(thought_text, thought_rect)
    else:
        # Draw the Play button
        screen.blit(button_text, button_rect)

    # Update the display
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()