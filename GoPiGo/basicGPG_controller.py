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
