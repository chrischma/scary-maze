import pygame
import sys

# General pygame settings
pygame.init()
pygame.FULLSCREEN
window = pygame.display.set_mode((700,700))
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

# Sounds
zisch = pygame.mixer.Sound('zisch.wav')
music = pygame.mixer.music.load('music.mp3')
monster = pygame.mixer.Sound('monster.wav')
pygame.mixer.music.play(-1,0.0) 

path_color = (230, 134, 35, 255)


def main_loop():
	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	        pygame.quit()
	        sys.exit()

	    if event.type == pygame.KEYDOWN:
	        pygame.quit()
	        sys.exit()


def next_level():
	if level_count == 1:
		level_2()
	else:
		final_level()

def check_mouse_position():

	global color, mouse_position, mouse_x, mouse_y, path
	color = window.get_at(pygame.mouse.get_pos())
	mouse_position = pygame.mouse.get_pos()
	mouse_x,mouse_y = mouse_position[0],mouse_position[1]


	if color != path_color:
		pygame.mouse.set_pos(position_start)
		pygame.mixer.Sound.play(zisch)

	if mouse_x in range (goal_hitbox_x1, goal_hitbox_x2) and mouse_y in range (goal_hitbox_y1, goal_hitbox_y2):
		next_level()

def update_screen():
	level_Image = pygame.image.load(level_image_source).convert()
	window.blit(level_Image,(0,0)) 
	pygame.display.update()

def main_menu():

	while True:
		level_Image = pygame.image.load("menu.png").convert()
		window.blit(level_Image,(0,0))
		pygame.display.update()


		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				position = pygame.mouse.get_pos()
				if position[1] in range (275,330):
						while True:
							show_image("objective.png")		

							for event in pygame.event.get():
								if event.type == pygame.MOUSEBUTTONDOWN:
									level_1()

				elif position[1] in range(330,415):
						while True:
							show_image("about.png")		

							for event in pygame.event.get():
								if event.type == pygame.MOUSEBUTTONDOWN:
									main_menu()

				elif position[1] in range(415,522):
					pygame.quit()
					sys.exit()



def show_image(image):
	level_Image = pygame.image.load(image).convert()
	window = pygame.display.set_mode((700,700))
	window.blit(level_Image,(0,0))
	pygame.display.update()
	



def jumpscare():
	pygame.mixer.Sound.play(monster)
	pygame.mixer.music.stop()

	while True:

		zombieImage = pygame.image.load("zombie.png").convert()
		overlay = pygame.display.set_mode((700,700))
		overlay.blit(zombieImage,(0,0))
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.quit()
				sys.exit()

def level_1():

	global level_count, level_image_source, position_start, goal_hitbox_x1, goal_hitbox_x2, goal_hitbox_y1, goal_hitbox_y2

	level_count = 1
	position_start = (130,470)
	goal_hitbox_x1, goal_hitbox_x2, goal_hitbox_y1, goal_hitbox_y2 = 460,650,440,490
	level_image_source = "level_1.png"

	pygame.mouse.set_pos(position_start)

	

	while True:

	    main_loop()

	    update_screen()
	    check_mouse_position()

def level_2():
	global level_count, level_image_source, position_start, goal_hitbox_x1, goal_hitbox_x2, goal_hitbox_y1, goal_hitbox_y2

	level_count = 2
	position_start = (90,650)
	goal_hitbox_x1, goal_hitbox_x2, goal_hitbox_y1, goal_hitbox_y2 = 300,500,550,700
	level_image_source = "level_2.png"
	pygame.mouse.set_pos(position_start)

	while True:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            pygame.quit()
	            sys.exit()

	        if event.type == pygame.KEYDOWN:
	            pygame.quit()
	            sys.exit()

	    main_loop()
	    update_screen()
	    check_mouse_position()

def final_level():
	global level_count, level_image_source, position_start, goal_hitbox_x1, goal_hitbox_x2, goal_hitbox_y1, goal_hitbox_y2

	level_count = 3

	position_start = (90,650)

	goal_hitbox_x1, goal_hitbox_x2, goal_hitbox_y1, goal_hitbox_y2 = 0,0,0,0
	level_image_source = "level_3.png"
	pygame.mouse.set_pos(position_start)

	while True:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            pygame.quit()
	            sys.exit()

	        if event.type == pygame.KEYDOWN:
	            pygame.quit()
	            sys.exit()

	    main_loop()
	    update_screen()
	    check_mouse_position()
 
    
	    if (mouse_x in range(540,595)) and (mouse_y in range (650,670)):
	    	jumpscare()


main_menu()