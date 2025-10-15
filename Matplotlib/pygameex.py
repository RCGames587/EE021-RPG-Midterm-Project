import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))



pygame.display.set_caption("My RPG Game")



enemy_image = pygame.image.load("enemy_image.jpg")
enemy_rect = enemy_image.get_rect()
enemy_rect.center = (width // 2 + 50, height // 2)

player_speed = 5

quest_complete = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_rect.move_ip(-player_speed, 0)
    if keys[pygame.K_RIGHT]:
        player_rect.move_ip(player_speed, 0)
    if keys[pygame.K_UP]:
        player_rect.move_ip(0, -player_speed)
    if keys[pygame.K_DOWN]:
        player_rect.move_ip(0, player_speed)

if player_rect.colliderect(enemy_rect):
    if not quest_complete:
        print("You must complete the quest before fighting the enemy!")
    else:
        print("You defeated the enemy!")
        running = False

if not quest_complete:
    quest_rect = pygame.Rect(width // 2 - 25, height // 2 - 25, 50, 50)
    pygame.draw.rect(screen, (255, 0, 0), quest_rect)

    if player_rect.colliderect(quest_rect):
        print("You completed the quest!")
        quest_complete = True

screen.fill((255, 255, 255))

screen.blit(player_image, player_rect)
screen.blit(enemy_image, enemy_rect)

pygame.display.flip()
pygame.quit()