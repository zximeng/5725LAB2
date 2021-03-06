''' 
XIMENG ZHANG (XZ737)
YIFEI XU (YX459)
LAB2
2/17/2020
'''

import pygame     # Import pygame graphics library
import os    # for OS calls
import time
import RPi.GPIO as GPIO
# os.putenv('SDL_VIDEODRIVER', 'fbcon')   
# Display on piTFT#   os.putenv('SDL_FBDEV', '/dev/fb1') 
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN,pull_up_down = GPIO.PUD_UP)    
pygame.init()
size = width, height = 320, 240 
speed = [2,2]
speed1 = [-1,-1] 
black = 0, 0, 0
screen = pygame.display.set_mode(size)
ball = pygame.image.load("magic_ball.png")
ballrect = ball.get_rect()
ballrect.left = ballrect.bottom = 20

ball1 = pygame.image.load("soccer_ball.png")
ballrect1 = ball1.get_rect()
ballrect1.left = ballrect1.bottom = 200

start = time.time()
flag = True  # global flag
def GPIO19_callback(channel):
    flag = False
GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO19_callback, bouncetime=200)

while (flag):    
    ballrect = ballrect.move(speed)    
    if ballrect.left < 0 or ballrect.right > width:       
		speed[0] = -speed[0]    
    if ballrect.top < 0 or ballrect.bottom > height:     
		speed[1] = -speed[1]
    ballrect1 = ballrect1.move(speed1)    
    if ballrect1.left < 0 or ballrect1.right > width:       
		speed1[0] = -speed1[0]    
    if ballrect1.top < 0 or ballrect1.bottom > height:     
		speed1[1] = -speed1[1]
    if ballrect.colliderect(ballrect1):
        speed1[1] = -speed1[1]
        speed1[0] = -speed1[0]
        speed[0] = -speed[0]
        speed[1] = -speed[1]
	screen.fill(black)               # Erase the Work space   
	screen.blit(ball, ballrect)   # Combine Ball surface with workspace 
	screen.blit(ball1, ballrect1)
	if(not time.time() - start < 20):
		flag = False
	pygame.display.flip()        # display workspace on screen
