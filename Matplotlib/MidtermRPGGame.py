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

class Text:
    def __init__(self, font_name='freesansbold.ttf', font_size=32, color=(0, 0, 0), bg_color=None):
        self.font = pygame.font.Font(font_name, font_size)
        self.color = color
        self.bg_color = bg_color

    def render(self, text):
        return self.font.render(text, True, self.color, self.bg_color)

    def draw(self, surface, text, pos):
        text_surface = self.render(text)
        surface.blit(text_surface, pos)

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


## Screen Management
def show_title():
    global current_screen,enemy_defend,player_health,enemy_health, enemy_strength, enemy_luck, enemy_defense, difficulty_mult, role, current_difficulty
    current_screen = "title"
    #initialized values
    player_health = 500
    enemy_health = 1000
    enemy_defend = False
    current_difficulty = "none"
    enemy_strength = 0
    enemy_luck = 0
    enemy_defense = 0
    difficulty_mult = 0
    role = "none"

def draw_title():
    screen.fill(BLUE)
    screen.fill(WHITE)
    start_button.draw(screen)

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

#Battle Stuff
def show_battle():
    global current_screen
    current_screen = "battle"
    bg_img = pygame.image.load('battle_background.jpg')
    bg_img = pygame.transform.scale(bg_img, (800, 600))

def battle_background_functions():
    screen.fill(WHITE)
    #loop music


def playerturn():
    #Need to define the global variables that need to be accessed and changed throughout the fight
    global role, player_defend
    player_defend = False
    ##Idle images
    ##Place flavor text and display stats

    ##Create Buttons
    attack_button.draw(screen)
    if role == "knight":
        print("skill instead of spell")
    elif role == "wizard" or role == "paladin":
        print("spell instead of skill")
    defend_button.draw(screen)
    
def select_attack ():
    #random roll for miss, hit, and crit
    global player_damage,roll,variance, enemy_health, enemy_defend
    roll = random.uniform(0,10)
    variance = float(random.uniform(0.85,1.2))
    if enemy_defend == True and roll != 10:
        ##Display defend animation
        ##Play Defend sound
        ## show smug enemy
        ##Text box describing defending
        enemy_turn()
    elif roll != 1 and roll != 10 and enemy_defend == False:
        player_damage = int((variance)*(35 * player_strength)/(enemy_defense))
        ## display attack animation
        ## play attack sound
        ##show hurt enemy
        ## text box describing defending
    elif roll == 1 and enemy_defend == False:
        ##Text saying you missed
        ## sad sound insert
        enemy_turn()
    elif roll == 10:
        #critical!
        player_damage = 2 * int((variance)*(35 * player_strength)/(enemy_defense))
        ## display crit animation
        ## play crit sound
        ## Show hurt enemy
        ## text box describing critical hit!

def select_skill ():
    global player_damage,roll,variance, enemy_health, enemy_defend
    roll = int(random.uniform(0,10))
    variance = float(random.uniform(0.85,1.2))
    if roll != 1 and roll != 10 and enemy_defend == False:
        player_damage = int((variance)*(50 * player_strength)/(enemy_defense))

def select_defend():
    global player_defend
    player_defend = True

def select_stats():
    global player_health, player_defense, player_magic, player_strength, enemy_health
    ##Textbox that contains the player's stats

def enemy_turn():
    global enemy_defend, player_health, enemy_health
    enemy_defend == False
    if 


    
#def battle_loop():
    while player_health > 0 or enemy_health > 0:
        playerturn()
        enemy_turn()
                
#def show_victory_screen():

#def show_defeat_screen():
    #screen.fill(BLACK)


## Buttons
start_button = Button(300, 500, 200, 50, "Start Game", GREEN, BRIGHT_GREEN, show_difficulty)

easy_button = Button(300, 200, 150, 50, "EASY", WHITE, BRIGHT_GREEN,select_easy )
normal_button = Button(300, 300, 150, 50, "NORMAL", WHITE, BRIGHT_GREEN, select_normal)
hard_button = Button(300, 400, 150, 50, "HARD", WHITE, BRIGHT_GREEN, select_hard)

knight_button = Button(75, 300, 100, 100, "KNIGHT", BLACK, WHITE, select_knight )
wizard_button = Button(200, 300, 100, 100, "WIZARD", BLACK, WHITE, select_wizard)
paladin_button = Button(325, 300, 100, 100, "PALADIN", BLACK, WHITE, select_paladin)

attack_button = Button(350, 200, 100, 50, "Attack", WHITE, BLACK, select_attack)
spell_button = Button()
skill_button = Button ()
defend_button = Button()

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


    
 
    pygame.display.flip()  # Update the display

## Main Menu (Difficulty and Class Selection)



## Battle Initiation


## Battle Loop


## Post Battle
#score 
score_details = [role, current_difficulty, score]