import pygame

pygame.init()
pygame.mixer.init()
timer = pygame.time.Clock()

screen = pygame.display.set_mode([600,600])
playlist = ["lagu/1.mp3"]
current_track = 0
pygame.mixer.music.load(playlist[current_track])
pygame.mixer.music.play(-1)


### home gambar #####
home_gam = pygame.image.load("gambar/home/1.jpg")
home_gam1 = pygame.transform.scale(home_gam,(screen.get_rect().width,screen.get_rect().height))


clock = pygame.time.Clock()
running = True

while running:
	pygame.time.Clock().tick(60)
	screen.fill(("#FFFFFF"))
	#background
	screen.blit(home_gam,(0,0))
	
pygame.quit()
