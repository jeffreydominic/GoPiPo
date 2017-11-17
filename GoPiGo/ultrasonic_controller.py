#---------------------------------------------------------------
# basicGPG_controller.py
# Matt Dorow for Shurjo Banjree
# Created 27 January 2017
# Updated 27 January 2017
#
# GoPiGo Robot Controller: Basic keyboard input controller
#   for GoPiGo robot
#---------------------------------------------------------------

from gopigo import * # Robot controls/information
import pygame # GUI and keypress event handler
import print_trial_information # Script to print the trial information
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 20
GPIO_ECHO = 21
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

# GUI window setup
pygame.init()
window = pygame.display.set_mode((310, 270))
pygame.display.set_caption('GoPiGo Keyboard Controller')

# Fill background
background = pygame.Surface(window.get_size())
background = background.convert()
background.fill((250, 250, 250))

# Display some text
instructions = '''         CONTROLS


             Forward
                 (w)
          
Left     Backward     Right
 (a)            (s)             (d)

                Exit
                 (x)
''';
size_inc=22
index=0
for i in instructions.split('\n'):
	font = pygame.font.Font(None, 36)
	text = font.render(i, 1, (10, 10, 10))
	background.blit(text, (10,10+size_inc*index))
	index+=1

# Blit everything to the screen
window.blit(background, (0, 0))
pygame.display.flip()

# Record the initial total distance that has been logged on the encoder
initialDistance = enc_read(0)

# Loop until broken by instruction from user
while True:
    dist = distance()
    print ("Measured Distance = %.1f cm" % dist)
    time.sleep(.2)
    
    # Wait for an event/instruction
    event = pygame.event.wait();

    # Continue to execute the control until the key is released
    if (event.type == pygame.KEYUP):
	stop();
	continue;
    if (event.type != pygame.KEYDOWN):
	continue;

    # Convert input to unicode letter
    instruction = event.unicode;

    # Follow instruction
    if (instruction == 'w'):
	fwd(); # Forward - w
    elif (instruction == 'a'):
	left(); # Left - a
    elif (instruction == 'd'):
	right(); # Right - d
    elif (instruction == 's'):
	bwd(); # Backward - s
    elif (instruction == 'x'):
	break # Exit - x

# Print trial information
print_trial_information.print_output(initialDistance, enc_read(0))
GPIO.cleanup()
