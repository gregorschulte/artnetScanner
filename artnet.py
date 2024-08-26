import pygame
import sys
import python_artnet as Artnet

# setup
artnet_server = "127.0.0.1"
device_address = 1

# Initialize Pygame
pygame.init()

# By default it will listen on 0.0.0.0 (all interfaces)
artNet = Artnet.Artnet(artnet_server)

# Set up the display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Fullscreen mode

# Define colors
background_color = (0, 0, 0)

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
        r = dmxPacket[device_address -1]
        g = dmxPacket[device_address]
        b = dmxPacket[device_address + 1]     
        background_color = (r,g,b)

    # Fill the screen with red color
    screen.fill(background_color)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()