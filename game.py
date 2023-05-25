import pygame 

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("fireboy and watergirl")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

RedLine = pygame.Surface((100,10))


RedLine.fill((255,60,0))

BlueLine = pygame.Surface((100,10))
BlueLine.fill((35,137,218))

GreenLine = pygame.Surface((80,10))
GreenLine.fill((170, 255, 0))

bg = pygame.image.load('images/bg2.png')

bg_sound = pygame.mixer.Sound('sounds/sth.mp3')
bg_sound.play()


door = pygame.image.load('door/door0.jpg')
door = pygame.transform.scale(door, (70,90))

doorx = 850
doory = 530

doors = [
	pygame.transform.scale(pygame.image.load('door/door0.jpg'),(70, 90)),
	pygame.transform.scale(pygame.image.load('door/door1.jpg'),(70, 90)),
	pygame.transform.scale(pygame.image.load('door/door2.jpg'),(70, 90)),
	pygame.transform.scale(pygame.image.load('door/door3.jpg'),(70, 90)),
	pygame.transform.scale(pygame.image.load('door/door4.jpg'),(70, 90)),
	pygame.transform.scale(pygame.image.load('door/door5.jpg'),(70, 90))
]

pause = pygame.image.load('images/pause.png')
pause = pygame.transform.scale(pause, (70,70))
pause_rect = pause.get_rect(topleft=(930,0))
pause_bool = False


fireboy_speed = 10
fireboy_x = 50
fireboy_y = 550
f_jump = False
f_jump_cnt = 8

fr_right = [
	pygame.transform.scale(pygame.image.load('fireboy-right/fr-1.png'),(50, 70)),
	pygame.transform.scale(pygame.image.load('fireboy-right/fr-2.png'),(50, 70)),
	pygame.transform.scale(pygame.image.load('fireboy-right/fr-3.png'),(50, 70)),
	pygame.transform.scale(pygame.image.load('fireboy-right/fr-4.png'),(50, 70))
]


watergirl_speed = 10
watergirl_x = 10
watergirl_y = 550 
w_jump = False
w_jump_cnt = 8

wr = [
	pygame.transform.scale(pygame.image.load('watergirl-right/wr-1.png'),(50,70)),
	pygame.transform.scale(pygame.image.load('watergirl-right/wr-2.png'),(50,70)),
	pygame.transform.scale(pygame.image.load('watergirl-right/wr-3.png'),(50,70)),
	pygame.transform.scale(pygame.image.load('watergirl-right/wr-4.png'),(50,70)),
]



myfont = pygame.font.Font('fonts/starborn/Starborn.otf', 70);
win_label = myfont.render("YOU WIN!", True, 'Red')
restart_label = myfont.render("RESTART", True, 'Blue')

restart_rect = restart_label.get_rect(topleft=(100,150))

next_label = myfont.render("NEXT", True, 'Green')
next_rect = next_label.get_rect(topleft=(600,350))

continue_label = myfont.render("CONTINUE", False, 'Green')

continue_rect = continue_label.get_rect(topleft=(550,150))

lose_label = myfont.render("YOU LOSE!", True, 'Red')
lose_bool = False


fr_cnt = 0
wr_cnt = 0
door_cnt = 0
opendoor = False
opendoor_cnt = 0

gameplay = True

running = True


karta1 = True
karta2 = False


stena = pygame.Surface((10,300))
stena.fill('Black')
stena_x = 490
stena_y = 320

levers = [
	pygame.transform.scale(pygame.image.load('lever/lever1.png'),(60,50)),
	pygame.transform.scale(pygame.image.load('lever/lever2.png'),(60,50)),
	pygame.transform.scale(pygame.image.load('lever/lever3.png'),(60,50)),
]

lever1_cnt = 0
lever2_cnt = 0

openstena = False
lever_bool1 = False
lever_bool2 = False

fireboyPassStena = False
watergirlPassStena = False


while running:


	screen.blit(bg, (0, 0))
	screen.blit(pause, pause_rect)

	mouse = pygame.mouse.get_pos();
	fireboy_rect = fr_right[fr_cnt%4].get_rect(topleft=(fireboy_x,fireboy_y))

	


	if gameplay and pause_bool == False and lose_bool == False:

		if karta2:
			screen.blit(GreenLine, (300,615))
			screen.blit(GreenLine, (580,615))
			screen.blit(doors[door_cnt], (920,530))
			

			screen.blit(stena, (stena_x,stena_y))
			doorx = 920
			doory = 530

			screen.blit(levers[lever1_cnt], (150,570))
			screen.blit(levers[lever2_cnt], (750,570))

			if (fireboy_x >= 150 and fireboy_x <= 170 and fireboy_y == 550) or (watergirl_x >= 150 and watergirl_x <= 170 and watergirl_y == 550):
				lever_bool1 = True
			else:
				lever_bool1 = False

			if (fireboy_x >= 750 and fireboy_x <= 770 and fireboy_y == 550) or (watergirl_x >= 750 and watergirl_x <= 770 and watergirl_y == 550):
				lever_bool2 = True
			else:
				lever_bool2 = False

			
			if lever_bool1 and lever1_cnt < 2:
				openstena = True
				lever1_cnt += 1

			if lever_bool1 == False and lever1_cnt > 0:
				openstena = False
				lever1_cnt -= 1

			if lever_bool2 and lever2_cnt < 2:
				openstena = True
				lever2_cnt += 1

			if lever_bool2 == False and lever2_cnt > 0:
				openstena = False
				lever2_cnt -= 1



			if openstena and stena_y > 220:
				stena_y -= 2
			if openstena == False and stena_y < 320:
				stena_y += 2

			if fireboy_x > 270 and fireboy_x < 360 and fireboy_y == 550:
				lose_bool = True

			if watergirl_x > 270 and watergirl_x < 360 and watergirl_y == 550:
				lose_bool = True

			if fireboy_x > 550 and fireboy_x < 640 and fireboy_y == 550:
				lose_bool = True

			if watergirl_x > 550 and watergirl_x < 640 and watergirl_y == 550:
				lose_bool = True

			if openstena == False and (fireboy_x > stena_x - 42) and fireboyPassStena == False:
				fireboy_x -= fireboy_speed

			if openstena == False and (fireboy_x < stena_x - 22) and fireboyPassStena == True:
				fireboy_x += fireboy_speed

			if openstena == False and (watergirl_x > stena_x - 42) and watergirlPassStena==False:
					watergirl_x -= watergirl_speed

			if openstena == False and (watergirl_x < stena_x - 22) and watergirlPassStena == True:
				watergirl_x += watergirl_speed


			if fireboy_x > stena_x - 42:
				fireboyPassStena = True
			else:
				fireboyPassStena = False

			if watergirl_x > stena_x - 42:
				watergirlPassStena = True
			else:
				watergirlPassStena = False








		elif karta1:
			screen.blit(RedLine, (300,615))
			screen.blit(BlueLine, (500,615))
			screen.blit(doors[door_cnt], (doorx,doory))


			if fireboy_x > 470 and fireboy_x < 590 and fireboy_y == 550:
				lose_bool = True

			if watergirl_x > 270 and watergirl_x < 390 and watergirl_y == 550:
				lose_bool = True




		if pause_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
				pause_bool = True

		screen.blit(fr_right[fr_cnt%4],(fireboy_x,fireboy_y))
		fr_cnt += 1
		screen.blit(wr[wr_cnt%4], (watergirl_x,watergirl_y))
		wr_cnt += 1


		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and fireboy_x > 0:
			fireboy_x -= fireboy_speed
		elif keys[pygame.K_RIGHT] and fireboy_x < 950:
			fireboy_x += fireboy_speed

		if keys[pygame.K_a] and watergirl_x > 0:
			watergirl_x -= watergirl_speed
		elif keys[pygame.K_d] and watergirl_x < 950:
			watergirl_x += watergirl_speed

		if not f_jump:
			if(keys[pygame.K_UP]): 
				f_jump = True
		else:
			if f_jump_cnt >= -8:
				if f_jump_cnt > 0:
					fireboy_y -= (f_jump_cnt ** 2)/2
				else:
					fireboy_y += (f_jump_cnt ** 2)/2	
				f_jump_cnt -= 1
			else:
				f_jump = False
				f_jump_cnt = 8



		if not w_jump:
			if(keys[pygame.K_w]):
				w_jump = True
		else:
			if w_jump_cnt >= -8:
				if w_jump_cnt > 0:
					watergirl_y -= (w_jump_cnt ** 2)/2
				else:
					watergirl_y += (w_jump_cnt ** 2)/2
				w_jump_cnt -= 1
			else:
				w_jump = False
				w_jump_cnt = 8


		if fireboy_x >= doorx+10 and watergirl_x >= doorx+10:
			opendoor = True
			opendoor_cnt += 1

		if opendoor == True and door_cnt < 5:
			door_cnt += 1

		if opendoor_cnt >= 20:
			gameplay = False
			
	 



	elif gameplay and lose_bool:
		screen.blit(lose_label, (300,200))
		screen.blit(restart_label, restart_rect)
		restart_rect = restart_label.get_rect(topleft=(100,350))
		if(restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]):
			bg_sound.stop()
			bg_sound.play()
			fireboy_x = 50
			watergirl_x = 10
			lose_bool = False




	elif gameplay and pause_bool == True:
		# bg_sound.stop()
		screen.blit(restart_label, restart_rect)

		if (continue_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]):
			pause_bool = False
			# bg_sound.play()
		if(restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]):
			bg_sound.stop()
			bg_sound.play()
			fireboy_x = 50
			watergirl_x = 10
			pause_bool = False

		

		screen.blit(continue_label, continue_rect)
		screen.blit(pause, pause_rect)

		if karta1:
			screen.blit(doors[door_cnt], (doorx,doory))
			screen.blit(fr_right[fr_cnt%4],(fireboy_x,fireboy_y))
			screen.blit(wr[wr_cnt%4], (watergirl_x,watergirl_y))


	else:
		# screen.fill((87,88,89))
		bg_sound.stop()
		screen.blit(win_label, (300,200))
		screen.blit(restart_label, (100, 350))
		restart_rect = restart_label.get_rect(topleft=(100,350))
		screen.blit(next_label, (600,350))
		# next_rect = next_label.get_rect(topleft=(600,350))


		if(restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]):
			bg_sound.play()
			fireboy_x = 50
			watergirl_x = 10
			opendoor = False
			opendoor_cnt = 0
			door_cnt = 0
			gameplay = True

		if(next_rect.collidepoint(mouse)) and pygame.mouse.get_pressed()[0]:
			bg_sound.play()
			karta1 = False
			karta2 = True
			fireboy_x = 50
			watergirl_x = 10
			opendoor = False
			opendoor_cnt = 0
			door_cnt = 0
			gameplay = True





	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()



	clock.tick(20)

# def next():




