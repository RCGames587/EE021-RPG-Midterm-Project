import random
import pygame

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("My RPG Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 200)
PINK = ()

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.font = pygame.font.Font(None, 36)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.color
        if self.rect.collidepoint(mouse_pos):
            current_color = self.hover_color

        pygame.draw.rect(surface, current_color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()

class Textbox:
    def __init__(self, x, y, width, height, font_name='freesansbold.ttf', font_size=32, color=(0, 0, 0), bg_color=None, border_color=(0,0,0), border_thickness=2):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(font_name, font_size)
        self.color = color
        self.bg_color = bg_color
        self.border_color = border_color
        self.border_thickness = border_thickness

    def render(self, text):
        return self.font.render(text, True, self.color, self.bg_color)

    def draw(self, surface, text):
        # Draw background box
        if self.bg_color:
            pygame.draw.rect(surface, self.bg_color, self.rect)
        # Draw border
        if self.border_thickness > 0:
            pygame.draw.rect(surface, self.border_color, self.rect, self.border_thickness)
        # Draw text (centered)
        text_surface = self.render(text)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

## Image Load
knight_preview_img = pygame.image.load("Images/Stark.jpg")
knight_preview_img = pygame.transform.scale(knight_preview_img, (150, 150))

wizard_preview_img = pygame.image.load("Images/Frieren.jpg")
wizard_preview_img = pygame.transform.scale(wizard_preview_img, (150, 150))

paladin_preview_img = pygame.image.load("Images/Paladin.jpg")
paladin_preview_img = pygame.transform.scale(paladin_preview_img, (150, 150))


### Difficulty Stuff


def select_easy():
    global current_screen, current_difficulty, difficulty_mult, enemy_defense, enemy_strength, enemy_luck
    current_screen = "class"

    current_difficulty = "easy"
    difficulty_mult = 0.8
    enemy_strength = .8
    enemy_luck = .75
    enemy_defense = .6
    show_role()

def select_normal():
    global current_screen, current_difficulty, difficulty_mult, enemy_defense, enemy_strength, enemy_luck
    current_screen = "class"

    current_difficulty = "medium"
    difficulty_mult = 0.8
    enemy_strength = 1
    enemy_luck = 1
    enemy_defense = 1
    show_role()

def select_hard():
    global current_screen, current_difficulty, difficulty_mult, enemy_defense, enemy_strength, enemy_luck
    current_screen = "class"
   
    current_difficulty = "hard"
    enemy_strength = 1.2
    enemy_luck = 1.1
    enemy_defense = 1.2
    difficulty_mult = 1.2
    show_role()
## Class details

def select_knight():
    global current_screen, role, player_strength, player_luck, player_defense, player_magic, mana
    current_screen = "battle"

    role = "knight"
    player_strength = 1.1
    player_luck = 1
    player_defense = 1.2
    player_magic = 0
    mana = 0

def select_wizard():
    global current_screen, role, player_strength, player_luck, player_defense, player_magic, mana
    current_screen = "battle"

    role = "wizard"
    player_strength = .8
    player_luck = .9
    player_defense = .9
    player_magic = 1.3
    mana = 100

def select_paladin():
    global current_screen, role, player_strength, player_luck, player_defense, player_magic, mana
    current_screen = "battle"

    role = "paladin"
    player_strength = 1
    player_luck = 1.05
    player_defense = 1.1
    player_magic = 1.1
    mana = 50

###Title Screen Stuff
current_screen = "title"
title = Textbox(250,50, 300, 100,"freesansbold.ttf",32, BLACK, WHITE,RED,3)
tit_img = pygame.image.load('Images/titimage.jpg')
tit_img = pygame.transform.scale(tit_img, (800, 600))

## Screen Management
def show_title():
    global current_screen,turn,action_message, score_recorded,enemy_defend,player_health,enemy_health, enemy_strength, enemy_luck, enemy_defense, difficulty_mult, role, current_difficulty, max_enemy_health, battle_text, selected_range, charge, battle_flavor_text
    current_screen = "title"
    #initialized values
    turn = "player"
    score_recorded = False
    player_health = 500
    enemy_health = 1000
    max_enemy_health = 1000
    enemy_defend = False
    current_difficulty = "none"
    enemy_strength = 0
    enemy_luck = 0
    enemy_defense = 0
    difficulty_mult = 0
    role = "none"
    battle_flavor_text = ""
    charge = False
    action_message = ""

def draw_title():
    screen.blit(tit_img, (0, 0)) 
    start_button.draw(screen)
    title.draw(screen,"Trevor's RPG")

def show_difficulty():
    global current_screen
    current_screen = "difficulty"
    
def draw_difficulty():
    screen.fill(RED)
    easy_button.draw(screen)
    normal_button.draw(screen)
    hard_button.draw(screen)

def show_role():
    global current_screen
    current_screen = "class"

def draw_role():
    screen.fill(WHITE)
    knight_button.draw(screen)
    wizard_button.draw(screen)
    paladin_button.draw(screen)

    mouse_pos = pygame.mouse.get_pos()
    
    if knight_button.rect.collidepoint(mouse_pos):
        screen.blit(knight_preview_img, (550, 200))
    elif wizard_button.rect.collidepoint(mouse_pos):
        screen.blit(wizard_preview_img, (550, 200))
    elif paladin_button.rect.collidepoint(mouse_pos):
        screen.blit(paladin_preview_img, (550, 200))

#Battle Stuff
def show_battle():
    global current_screen
    current_screen = "battle"
def draw_battle():   
    global player_health, enemy_health, max_enemy_health, role, selected_range, battle_text, battle_flavor_text, player_defend, action_message
    bg_img = pygame.image.load('Images/battle_background.jpg')
    bg_img = pygame.transform.scale(bg_img, (800, 600))

    screen.blit(bg_img, (0, 0)) 
    
    enemy_name.draw(screen,"Trevor the Terrible")
    enemy_hp.draw(screen,f"{enemy_health}")
    #battle message
    if turn == "player" and battle_flavor_text == "": 
        flavor_text = open("TextFiles/FlavorText.txt")
        list = [line.strip() for line in flavor_text]
    
        if enemy_health <= (max_enemy_health/2):
            selected_range = list[10:15]
        elif enemy_health <= (max_enemy_health/4):
            selected_range = list[15:20]
        else:
            selected_range = list[0:10]
        battle_flavor_text = f"{random.choice(selected_range)}"
    if action_message != "":
        battle_text.draw(screen,action_message)
    else:
        battle_text.draw(screen,f"{battle_flavor_text}")

    ## Player battle logic
    if turn == "player":
        player_defend = False
        hp.draw(screen, f"{player_health}")
        attack_button.draw(screen)
        if role == "knight":
            skill_button.draw(screen)
        else:
            spell_button.draw(screen)
        defend_button.draw(screen)
        stats_button.draw(screen)
    
    ## enemy turn stuff
    if turn == "enemy":
        enemy_turn()


#def battle_background_functions():

    #loop music

    
def select_attack ():
    #random roll for miss, hit, and crit
    global player_damage,roll,variance, enemy_health, enemy_defend, turn, battle_flavor_text,action_message
    roll = random.uniform(0,10)
    variance = float(random.uniform(0.85,1.2))
    if enemy_defend == True and roll != 10:
        ##Display defend animation
        ##Play Defend sound
        ## show smug enemy
        ##Text box describing defending
        turn = "enemy"
    elif roll != 1 and roll != 10 and enemy_defend == False:
        player_damage = int((variance)*(35 * player_strength)/(enemy_defense))
        enemy_health = enemy_health - player_damage
        ## display attack animation
        ## play attack sound
        ##show hurt enemy
        ## text box describing defending
        turn = "enemy"
    elif roll == 1 and enemy_defend == False:
        action_message = ("Your attack missed!")
        ## sad sound insert
        turn = "enemy"
    elif roll == 10:
        #critical!
        player_damage = 2 * int((variance)*(35 * player_strength)/(enemy_defense))
        enemy_health = enemy_health - player_damage
        ## display crit animation
        ## play crit sound
        ## Show hurt enemy
        action_message = (f"CRITICAL HIT: You hit for {player_damage} damage")
    turn = "enemy"

def select_skill ():
    global player_damage,roll,variance, enemy_health, enemy_defend, battle_flavor_text, turn, action_message
    roll = int(random.uniform(0,10))
    variance = float(random.uniform(0.75,1.1))
    if enemy_defend == True and roll != 10:
            enemy_health = enemy_health - player_damage
            ##Display defend animation
            ##Play Defend sound
            ## show smug enemy
            action_message=("The Enemy Blocked your attack!")
    
    elif roll != 1 and roll != 10 and enemy_defend == False:
            player_damage = int((variance)*(50 * player_strength)/(enemy_defense))
            enemy_health = enemy_health - player_damage
            ## display attack animation
            ## play attack sound
            ##show hurt enemy
            action_message = (f"You performed a sword skill for {player_damage} damage")
            
    elif roll == 1 and enemy_defend == False:
            ##Text saying you missed
            ## sad sound insert
            action_message =("Your attack missed!")

    elif roll == 10:
            #critical!
            player_damage = 2 * int((variance)*(35 * player_magic)/(enemy_defense))
            enemy_health -= player_damage
            ## display crit animation
            ## play crit sound
            ## Show hurt enemy
            action_message = (f"CRITICAL HIT: You hit for {player_damage} damage")
    turn = "enemy"

def select_spell():
    global player_damage,roll,variance, enemy_health, enemy_defend, mana, turn, action_message
    roll = random.uniform(0,10)
    variance = float(random.uniform(0.85,1.2))
    if mana >= 10:
        mana = mana-10
        if enemy_defend == True and roll != 10:
            ##Display defend animation
            ##Play Defend sound
            ## show smug enemy
            ##Text box describing defending
            turn = "enemy"
        elif roll != 1 and roll != 10 and enemy_defend == False:
            player_damage = int((variance)*(35 * player_strength)/(enemy_defense))
            enemy_health = enemy_health - player_damage
            ## display attack animation
            ## play attack sound
            ##show hurt enemy
            ## text box describing defending
            turn = "enemy"
        elif roll == 1 and enemy_defend == False:
            ##Text saying you missed
            ## sad sound insert
            turn = "enemy"
        elif roll == 10:
            #critical!
            player_damage = 2 * int((variance)*(35 * player_magic)/(enemy_defense))
            enemy_health = enemy_health - player_damage
            ## display crit animation
            ## play crit sound
            ## Show hurt enemy
            ## text box describing critical hit!
            turn = "enemy"
    else:
        print("out of mana!")


def select_defend():
    global player_defend, turn
    player_defend = True
    battle_text.draw(screen,"You Braced and defended!")
    turn = "enemy"

def select_stats():
    global action_message, player_health, player_defense, player_magic, player_strength, enemy_health, battle_flavor_text
    action_message = ( f"HP: {player_health}  Defense: {int(player_defense*100)}  Magic: {int(player_magic*100)}  Strength: {int(player_strength*100)}")


def enemy_turn():
    global enemy_defend, player_health,action_message, enemy_health,decide_roll, turn, player_defend, charge, enemy_damage, variance, battle_flavor_text
    enemy_defend == False
    decide_roll = int(random.uniform(0,12))
    variance = float(random.uniform(0.85,1.2))
    if charge == False and player_defend == False:    
        if decide_roll == 12:
            charge == True
            action_message = ("The Enemy starts charging for a strong attack!")
        elif decide_roll == 1:
            enemy_defend = True
            action_message = ("The Enemy braces for impact and defends!")

        else:
            enemy_damage = int((variance)*(35 * enemy_strength)/(player_defense))
            player_health -= enemy_damage
            action_message = ("The Enemy starts charging for a strong attack!")


    elif charge == True and player_defend == False:
        enemy_damage = int((variance)*(35 * enemy_strength)/(enemy_defense))
        player_health -= enemy_damage
        action_message = ("The Enemy performs a monumental attack!")

    elif player_defend == True:
        action_message = ("The enemy tried to attack, but you blocked it!")
        


    player_defend = False
    turn = "player"
    action_message = ""
    battle_flavor_text = ""

        

                
def show_victory():
    global current_screen
    current_screen = "victory"

def draw_victory():
    global score, score_recorded
    screen.fill(GREEN)
    battle_text.draw(screen, "YOU WIN")
    score = player_health + (difficulty_mult)*100
    if score_recorded == False:
        with open('scores.txt', 'a') as scoreboard:
            scoreboard.write(f"{role},{current_difficulty},{score}\n")
        score_recorded = True
        print(score)

def show_defeat():
    global current_screen
    current_screen = "defeat"

def draw_defeat():
    global score_recorded, score
    screen.fill(BLACK)
    battle_text.draw(screen, "YOU LOSE")
    score = enemy_health/10 +(difficulty_mult)*10 #10 is the defeat bonus i guess
    if score_recorded == False:
        with open('scores.txt', 'a') as scoreboard:
            scoreboard.write(f"{role},{current_difficulty},{score}\n")
        score_recorded = True
        print(score)

## Buttons
start_button = Button(300, 500, 200, 50, "Start Game", GREEN, BRIGHT_GREEN, show_difficulty)

easy_button = Button(300, 200, 150, 50, "EASY", WHITE, BRIGHT_GREEN,select_easy )
normal_button = Button(300, 300, 150, 50, "NORMAL", WHITE, BRIGHT_GREEN, select_normal)
hard_button = Button(300, 400, 150, 50, "HARD", WHITE, BRIGHT_GREEN, select_hard)

knight_button = Button(75, 300, 300, 100, "KNIGHT", RED, WHITE, select_knight )
wizard_button = Button(75, 200, 300, 100, "WIZARD", RED, WHITE, select_wizard)
paladin_button = Button(75, 100, 300, 100, "PALADIN", RED, WHITE, select_paladin)

attack_button = Button(50, 500, 150, 100, "Attack", WHITE, BLACK, select_attack)
spell_button = Button(200, 500, 150, 100, "Spell", WHITE, BLACK, select_spell)
skill_button = Button (200,500, 150, 100, "Skill",WHITE, BLACK, select_skill  )
defend_button = Button(400,500, 150, 100, "Defend", WHITE, BLACK, select_defend)
stats_button = Button(600,500, 150, 100, "Stats", WHITE, BLACK, select_stats)

##Text and Stat Values
hp = Textbox(300,400,100,50,"freesansbold.ttf",32, BLACK, WHITE,RED,3)
enemy_name = Textbox(150,0,500,75,'freesansbold.ttf',36,WHITE,BLACK,None,0)
battle_text = Textbox(150,300,300,100,'freesansbold.ttf',32,WHITE, BLACK, GREEN,2)
enemy_hp = Textbox(300,50,100,50,"freesansbold.ttf",32, BLACK, WHITE,RED,3)

## Title Screen



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if current_screen == "title":
            start_button.handle_event(event)
        
        if current_screen == "difficulty":
            easy_button.handle_event(event)
            normal_button.handle_event(event)
            hard_button.handle_event(event)

        if current_screen == "class":
            knight_button.handle_event(event)
            wizard_button.handle_event(event)
            paladin_button.handle_event(event)

        if current_screen == "battle" and turn == "player":
            attack_button.handle_event(event)
            defend_button.handle_event(event)
            if role == "knight":
                skill_button.handle_event(event)
            else:
                spell_button.handle_event(event)
            stats_button.handle_event(event)


    if current_screen == "title":
        show_title()
        draw_title()
    if current_screen == "difficulty":
        draw_difficulty()
        show_difficulty()
    if current_screen == "class":
        draw_role()
        show_role()
    if current_screen == "battle":
        show_battle()
        draw_battle()
        if enemy_health <= 0:
            current_screen = "victory"
        elif player_health <= 0:
            current_screen = "defeat"
        
        if turn == "enemy":
            enemy_turn()    
    if current_screen == "victory":
        draw_victory()
    if current_screen == "defeat":
        draw_defeat()
    
 
    pygame.display.flip()  # Update the display

