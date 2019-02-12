import pygame
pygame.mixer.init()

i = 1
if i == 1:
	pygame.mixer.music.load("mortuza.mp3")
elif i==2:
	pygame.mixer.music.load("sajjad.mp3")

#pygame.mixer.music.load("test.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
