import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Level Display")

#setting display
white = (255, 255, 255)
font = pygame.font.Font(None, 36)

# setting 'change level' functon
def display_text(text):
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    WIN.fill((0, 0, 0))
    WIN.blit(text_surface, text_rect)
    pygame.display.flip()

# defining main
def main():
    
    run = True
    level = 0

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    level += 1
                    if level == 1:
                        display_text("Level One")
                    elif level == 2:
                        display_text("Level Two")
                    elif level == 3:
                        display_text("Level Three")
                    elif level == 4:
                        display_text("Level Four")
                    elif level == 5:
                        display_text("Level Five")
                    elif level == 6:
                        display_text("Level Six")
                    elif level == 7:
                        display_text("Level Seven")
                    else:
                        display_text("You won! Game ended for now.")

        pygame.time.Clock().tick(60)

    pygame.quit()

if __name__ == "__main__":
    display_text("Let's begin.")
    main()