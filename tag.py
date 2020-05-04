import pygame
import glob
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
import sys
pygame.init()
# print(os.listdir('../images/'))


pygame.display.set_caption("Layout Tagger")
clock = pygame.time.Clock()

loop = True
press = False
color = "white"
cnt = 0
WINDOW_WIDTH  = 193
WINDOW_HEIGHT = 262
surface_type = pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE
# [os.remove(png) for png in glob.glob("*png")]
# global filename
window = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ), surface_type )

def assign_back():
    tk.Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    print(filename)
    if filename:
        background = pygame.image.load(filename)
        screen.blit(background, (0, 0))
    else:
        pass
    return(filename)

filename=assign_back()

while loop:
    try:
        #
        # pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_b:
                    print('b')
                    filename=assign_back()

                if event.key == pygame.K_c:
                    print('c')
                    screen.fill(pygame.Color(1, 1, 1))
                if event.key == pygame.K_s:
                    pygame.image.save(screen,f"tagged{os.path.basename(filename)}.png")
                    break
                if event.key == pygame.K_g:
                    frames = []
                    imgs = glob.glob("*.png")
                    for i in imgs:
                        new_frame = Image.open(i)
                        frames.append(new_frame)

                    # Save into a GIF file that loops forever
                    frames[0].save('animated.gif', format='GIF',
                                   append_images=frames[1:],
                                   save_all=True,
                                   duration=300, loop=0)
                    os.startfile("animated.gif")

        px, py = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.draw.rect(screen, (255, 0, 0), (px, py, 10, 10))
        if pygame.mouse.get_pressed() == (0, 0, 1):
            pygame.draw.rect(screen, (0, 0, 0), (px, py, 10, 10))

        if event.type == pygame.MOUSEBUTTONUP:
            press == False
        pygame.display.update()
        clock.tick(1000)
    except Exception as e:
        print(e)
        pygame.quit()

pygame.quit()