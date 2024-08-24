import pygame
import sys
import python_artnet as Artnet
import time

# Initialize Pygame
pygame.init()

# By default it will listen on 0.0.0.0 (all interfaces)
artNet = Artnet.Artnet()

# Set up the display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Fullscreen mode

# Define colors
background_color = (255, 0, 0)
gobo = pygame.image.load("gobo_spiral.png")
gobo_rotation = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False    
    
    # Fetch the latest packet we received from universe 0.
    artNetPacket = artNet.readBuffer()[0]
    # And extract the DMX data from that packet.
    dmxPacket = artNetPacket.data
    
    
    if type(dmxPacket) == list:        
        print("list")
        r = dmxPacket[0]
        g = dmxPacket[1]
        b = dmxPacket[2]
        
        gobo_on_off = dmxPacket[3]
        #gobo_rotation = dmxPacket[4]
        gobo_size = dmxPacket[5]
        
        background_color = (r,g,b)

    # Fill the screen with red color
    screen.fill(background_color)
    
    gobo = pygame.transform.scale(gobo,(1920,1920))
    
    gobo_rotation = gobo_rotation + 1
    if (gobo_rotation > 359):
        gobo_rotation = 0
    gobo = pygame.transform.rotate(gobo,gobo_rotation)
    
    
    screen.blit(gobo,(-259,-530))


    # Update the display
    pygame.display.flip()
    time.sleep(0.01)

# Quit Pygame
pygame.quit()
sys.exit()