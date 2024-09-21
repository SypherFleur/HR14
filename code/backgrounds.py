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

# Main loop
running = True
show_welcome_screen = False
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

# Initialize pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600

# Use windowed mode for testing (remove FULLSCREEN for now)
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the background image
background_image = pygame.image.load('introimg.png')

# Optionally scale the image to fit the screen if it's not the same size
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Set up a clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the window's close button is clicked
            running = False

        # You can also add a keyboard event to close the window (press 'ESC' to quit)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Update the display
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit pygame
pygame.quit()
