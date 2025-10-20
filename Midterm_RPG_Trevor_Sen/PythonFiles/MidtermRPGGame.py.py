import random
import pygame


pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Trevor's RPG of Doom and Suffering and Weird Expression")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
PINK = (255, 192, 203)
DARKPINK = (255, 20,147)
BRIGHTRED = (255,0,0)
BRIGHTBLUE = (0,0,255)
YELLOW = (200,200,0)
BRIGHTYELLOW = (255,255,0)

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.font = pygame.font.Font("Fonts/MedievalSharp-Regular.ttf", 36)

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
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()

class Textbox:
    def __init__(self, x, y, width, height, font_name='freesansbold.ttf', font_size=32, color=(WHITE), bg_color=None, border_color=(WHITE), border_thickness=2):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(font_name, font_size)
        self.color = color
        self.bg_color = bg_color
        self.border_color = border_color
        self.border_thickness = border_thickness

    def render(self, text):
        return self.font.render(text, True, self.color, self.bg_color)

    def draw(self, surface, text):
        if self.bg_color:
            pygame.draw.rect(surface, self.bg_color, self.rect)
        if self.border_thickness > 0:
            pygame.draw.rect(surface, self.border_color, self.rect, self.border_thickness)
        text_surface = self.render(text)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        

## Image Load
knight_preview_img = pygame.image.load("Images/Stark.jpg")
knight_preview_img = pygame.transform.scale(knight_preview_img, (300, 300))

wizard_preview_img = pygame.image.load("Images/Frieren.jpg")
wizard_preview_img = pygame.transform.scale(wizard_preview_img, (300, 300))

paladin_preview_img = pygame.image.load("Images/Paladin.jpg")
paladin_preview_img = pygame.transform.scale(paladin_preview_img, (300, 300))

easy_img = pygame.image.load("Images/easyimage.jpg")
easy_img = pygame.transform.scale(easy_img, (300, 300))

normal_img = pygame.image.load("Images/normalimage.png")
normal_img = pygame.transform.scale(normal_img, (300, 300))

hard_img = pygame.image.load("Images/hardimage.jpg")
hard_img = pygame.transform.scale(hard_img, (300, 300))

bg_img = pygame.image.load('Images/battle_background.jpg')
bg_img = pygame.transform.scale(bg_img, (800, 600))

#enemy images
enemy_idle_img = pygame.image.load("Images/Enemy/enemyidle.jpg")
enemy_idle_img = pygame.transform.scale(enemy_idle_img, (250, 250))

enemy_hurt_img = pygame.image.load("Images/Enemy/enemyhurt.jpg")
enemy_hurt_img = pygame.transform.scale(enemy_hurt_img, (250, 250))

enemy_defend_img = pygame.image.load("Images/Enemy/enemymog.jpg")
enemy_defend_img = pygame.transform.scale(enemy_defend_img, (250, 250))

enemy_charge_img = pygame.image.load("Images/Enemy/enemycharge.jpg")
enemy_charge_img = pygame.transform.scale(enemy_charge_img, (250, 250))

enemy_superattack_img = pygame.image.load("Images/Enemy/enemyohshit.jpg")
enemy_superattack_img = pygame.transform.scale(enemy_superattack_img, (250, 250))

enemy_dead_img = pygame.image.load("Images/Enemy/enemydead.jpg")
enemy_dead_img = pygame.transform.scale(enemy_dead_img, (250, 250))

enemy_bite_img = pygame.image.load("Images/Enemy/enemybitelip.jpg")
enemy_bite_img = pygame.transform.scale(enemy_bite_img, (250, 250))

enemy_attack_img = pygame.image.load("Images/Enemy/enemysurprised.jpg")
enemy_attack_img = pygame.transform.scale(enemy_attack_img, (250, 250))

enemy_surprised_img = pygame.image.load("Images/Enemy/enemysurprised.jpg")
enemy_surprised_img = pygame.transform.scale(enemy_attack_img, (250, 250))

enemy_confused_img = pygame.image.load("Images/Enemy/enemyconfused.jpg")
enemy_confused_img = pygame.transform.scale(enemy_confused_img, (250, 250))

## Sound Loads

pygame.mixer.init()
hit_sound = pygame.mixer.Sound("SoundEffects/hit.wav")
slash_sound = pygame.mixer.Sound("SoundEffects/slash.wav")
crit_sound = pygame.mixer.Sound("SoundEffects/lightning.wav")
defend_sound = pygame.mixer.Sound("SoundEffects/defendblock.wav")
enemy_damage_sound = pygame.mixer.Sound("SoundEffects/enemydam.flac")
fireball = pygame.mixer.Sound("SoundEffects/fireball.mp3")
victorymusic = pygame.mixer.Sound("Music/win.mp3")
defeatmusic = pygame.mixer.Sound("Music/lose.mp3")



slash_sound.set_volume(0.8)
hit_sound.set_volume(.8)
defend_sound.set_volume(1)

# Difficulty Stuff

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

    current_difficulty = "normal"
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
    mana = 300

def select_paladin():
    global current_screen, role, player_strength, player_luck, player_defense, player_magic, mana
    current_screen = "battle"

    role = "paladin"
    player_strength = 1
    player_luck = 1.05
    player_defense = 1.1
    player_magic = 1.1
    mana = 150

titlemusic = False
defeatmusic = False
victorymusic = False

def find_overall_high_score(file_path="Scores.txt"):
    
    best = None  #(role, difficulty, score)
    try:
        with open(file_path, "r") as scorelist:
            for line in scorelist:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    role, difficulty, score_s = parts
                    try:
                        score = int(float(score_s))
                    except ValueError:
                        continue
                    if (best is None) or (score > best[2]):
                        best = (role, difficulty, score)
                    
    except FileNotFoundError:
        pass
    return best 

high_score_box = Textbox(100, 25, 600, 50, "Fonts/MedievalSharp-Regular.ttf", 32, BLACK, WHITE, RED, 3)


###Title Screen Stuff
current_screen = "title"
title = Textbox(250,50, 300, 100,"Fonts/MedievalSharp-Regular.ttf",42, BLACK, WHITE,RED,3)
tit_img = pygame.image.load('Images/titimage.jpg')
tit_img = pygame.transform.scale(tit_img, (800, 600))

## Screen Management
def show_title():
    global current_screen,turn,action_message, score_recorded,enemy_defend,player_health,enemy_health, enemy_strength, enemy_luck, enemy_defense, difficulty_mult, role, current_difficulty, max_enemy_health, battle_text, selected_range, charge, battle_flavor_text, enemy_pose, enemy_pose_timer
    global battle_state, pause_duration, pause_start, music1play, titlemusic, player_defend, messagepicked
    current_screen = "title"
    #initialized values
    turn = "player"
    score_recorded = False
    player_health = 500
    enemy_health = 1000
    max_enemy_health = 1000
    enemy_defend = 1
    current_difficulty = "none"
    enemy_strength = 0
    enemy_luck = 0
    enemy_defense = 0
    difficulty_mult = 0
    role = "none"
    battle_flavor_text = ""
    charge = False
    action_message = ""
    enemy_pose_timer = 0
    enemy_pose = "idle"
    battle_state = "player_turn"   
    pause_start = 0
    pause_duration = 2000
    music1play = False
    player_defend = 1
    messagepicked = "false"
    if titlemusic == False:
        pygame.mixer.music.load("Music/titlemusic.mp3")
        pygame.mixer.music.play() 
        pygame.mixer.music.set_volume(0.6)
        titlemusic = True
    


def draw_title():
    screen.blit(tit_img, (0, 0)) 
    start_button.draw(screen)
    title.draw(screen,"Trevor's RPG")


def show_difficulty():
    global current_screen
    current_screen = "difficulty"
    
def draw_difficulty():
    global hsmessage, top_score
    screen.fill(RED)
    easy_button.draw(screen)
    normal_button.draw(screen)
    hard_button.draw(screen)
    
    top_score = find_overall_high_score("scores.txt")
    if top_score:
        role, difficulty, score = top_score
        hsmessage = f"High Score: {score} - {role} ({difficulty})"
    else:
        hsmessage = "No high scores yet!"

    high_score_box.draw(screen, hsmessage)


    mouse_pos = pygame.mouse.get_pos()


    if easy_button.rect.collidepoint(mouse_pos):
        screen.blit(easy_img, (75, 175))
    elif normal_button.rect.collidepoint(mouse_pos):
        screen.blit(normal_img, (75, 175))
    elif hard_button.rect.collidepoint(mouse_pos):
        screen.blit(hard_img, (75, 175))

def show_role():
    global current_screen
    current_screen = "class"

def draw_role():
    screen.fill(PINK)
    knight_button.draw(screen)
    wizard_button.draw(screen)
    paladin_button.draw(screen)
    high_score_box.draw(screen,"Choose your Class")
    mouse_pos = pygame.mouse.get_pos()
    
    if knight_button.rect.collidepoint(mouse_pos):
        screen.blit(knight_preview_img, (450, 150))
    elif wizard_button.rect.collidepoint(mouse_pos):
        screen.blit(wizard_preview_img, (450, 150))
    elif paladin_button.rect.collidepoint(mouse_pos):
        screen.blit(paladin_preview_img, (450, 150))

#Battle Stuff
def show_battle():
    global current_screen, enemy_pose,music1play
    current_screen = "battle"
    if music1play != True:
        pygame.mixer.music.load("Music/Stronger_Monsters.mp3")
        pygame.mixer.music.play() 
        pygame.mixer.music.set_volume(0.6)
        music1play = True

def draw_battle():   
    global player_health, enemy_health, max_enemy_health, role, selected_range, battle_text, battle_flavor_text, player_defend, action_message, enemy_pose_timer, enemy_pose, messagepicked

    screen.blit(bg_img, (0, 0)) 
    
    enemy_name.draw(screen,"Trevor the Terrible")
    enemy_hp.draw(screen,f"HP: {enemy_health}")

    if enemy_pose == "idle":
        screen.blit(enemy_idle_img, (275, 150)) 
    elif enemy_pose == "hurt":
        screen.blit(enemy_hurt_img, (275, 150))
    elif enemy_pose == "defend":
        screen.blit(enemy_defend_img, (275, 150))
    elif enemy_pose == "charge":
        screen.blit(enemy_charge_img, (275,150))
    elif enemy_pose == "superattack":
        screen.blit(enemy_superattack_img, (275,150))
    elif enemy_pose == "attack":
        screen.blit(enemy_attack_img, (275,150))
    elif enemy_pose == "surprised":
        screen.blit(enemy_surprised_img, (275,150))
    elif enemy_pose == "confused":
        screen.blit(enemy_confused_img, (275,150))


    #battle message
    if turn == "player" and action_message == "" and messagepicked == "false": 
        flavor_text = open("TextFiles/FlavorText.txt")
        list = [line.strip() for line in flavor_text]
    
        if enemy_health <= (max_enemy_health/2):
            selected_range = list[10:15]
        elif enemy_health <= (max_enemy_health/4):
            selected_range = list[15:20]
        else:
            selected_range = list[0:10]
        battle_flavor_text = f"{random.choice(selected_range)}"
        messagepicked = "true"
    if action_message != "":
        battle_text.draw(screen,action_message)
    else:
        battle_text.draw(screen,f"{battle_flavor_text}")

    ## Player battle logic
    if turn == "player":
        player_defend = 1
        hp.draw(screen, f"HP {player_health}|{mana} MANA")
        attack_button.draw(screen)
        if role == "knight":
            skill_button.draw(screen)
        else:
            spell_button.draw(screen)
        defend_button.draw(screen)
        stats_button.draw(screen)


    
def select_attack ():
    #random roll for miss, hit, and crit
    global player_damage,roll,variance, enemy_health, enemy_defend, turn, battle_flavor_text,action_message, enemy_pose, enemy_pose_timer
    global battle_state, pause_duration, pause_start, player_defend
    player_defend = 1
    roll = random.uniform(0,11)
    variance = float(random.uniform(0.85,1.2))
    if roll != 1 and roll != 10:
        player_damage = int((variance)*(40 * player_strength)/(enemy_defense*enemy_defend))
        hit_sound.play()
        enemy_pose = "hurt"
        enemy_pose_timer = pygame.time.get_ticks()
        action_message = (f"You attacked for {player_damage} damage!")
        battle_text.draw(screen,action_message)
        battle_state = "pause"
        pause_start = pygame.time.get_ticks()
        enemy_health = enemy_health - player_damage       

    elif roll == 1 and enemy_defend == False:
        hit_sound.play()
        action_message = ("Your attack missed!")

        battle_text.draw(screen,action_message)
        battle_state = "pause"
        pause_start = pygame.time.get_ticks()  

    
    elif roll == 10:
        hit_sound.play()
        crit_sound.play()
        player_damage = 2 * int((variance)*(70 * player_strength)/(enemy_defense))
        enemy_pose = "hurt"
        action_message = (f"CRITICAL HIT: You hit for {player_damage} damage")
        battle_text.draw(screen,action_message)
        enemy_pose_timer = pygame.time.get_ticks()
        battle_state = "pause"
        pause_start = pygame.time.get_ticks()

        enemy_health = enemy_health - player_damage

    battle_state = "player_pause"
    pause_start = pygame.time.get_ticks()
    pause_duration = 1100

def select_skill ():
    global player_damage,roll,variance, enemy_health, enemy_defend, battle_flavor_text, turn, action_message, enemy_pose_timer, enemy_pose
    global pause_start, pause_duration,battle_state, player_defend
    player_defend = 1
    roll = int(random.uniform(0,11))
    variance = float(random.uniform(0.75,1.1))
    print(roll,variance)
    if roll != 1 and roll != 10 :
            player_damage = int((variance)*(50 * player_strength)/(enemy_defense*enemy_defend))
            enemy_health = enemy_health - player_damage
            ## display attack animation
            slash_sound.play()
            enemy_pose = "hurt"
            enemy_pose_timer = pygame.time.get_ticks()
            action_message = (f"You performed a sword skill for {player_damage} damage")
            battle_state = "pause"
            pause_start = pygame.time.get_ticks()

    elif roll == 1:
            ## sad sound insert
            action_message =("Your attack missed!")

    elif roll == 10:
        #critical!
        player_damage = int((variance)*(90 * player_magic)/(enemy_defense))
        enemy_health -= player_damage
        slash_sound.play()
        crit_sound.play()
        enemy_pose = "hurt"
        enemy_pose_timer = pygame.time.get_ticks()
        action_message = (f"CRITICAL HIT: You hit for {player_damage} damage")
        battle_state = "pause"
        pause_start = pygame.time.get_ticks()

    battle_state = "player_pause"
    pause_start = pygame.time.get_ticks()
    pause_duration = 1100

def select_spell():
    global player_damage,roll,variance, enemy_health, enemy_defend, mana, turn, action_message, enemy_pose, enemy_pose_timer,battle_state, pause_start, pause_duration
    roll = random.uniform(0,11)
    variance = float(random.uniform(0.85,1.2))
    if mana >= 10:
        mana = mana-10
        if roll != 1 and roll != 10:
            player_damage = int((variance)*(50 * player_strength)/(enemy_defense*enemy_defend))
            ## display attack animation
            fireball.play()
            enemy_pose = "hurt"
            enemy_pose_timer = pygame.time.get_ticks()
            action_message = f"You fireball the Enemy for {player_damage} damage!"
            battle_state = "player_pause"
            pause_start = pygame.time.get_ticks()
            pause_duration = 1100
            enemy_health = enemy_health - player_damage
        elif roll == 1 and enemy_defend == False:
            fireball.play()
            action_message =("Your attack missed!")
            battle_state = "player_pause"
            pause_start = pygame.time.get_ticks()
            pause_duration = 1100            
        elif roll == 10:
            player_damage = int((variance)*(100 * player_magic)/(enemy_defense))
            fireball.play()
            crit_sound.play()
            enemy_pose = "hurt"
            enemy_pose_timer = pygame.time.get_ticks()
            action_message = f"Critical Hit! Your fireball hit's for {player_damage} damage!"
            battle_state = "player_pause"
            pause_start = pygame.time.get_ticks()
            pause_duration = 1100
            enemy_health = enemy_health - player_damage
    else:
        print("out of mana!")


def select_defend():
    global player_defend, turn, enemy_defend, battle_state, pause_start, pause_duration,action_message
    player_defend = 2
    action_message = ("You Braced and defended!")
    
    battle_state = "player_pause"
    pause_start = pygame.time.get_ticks()
    pause_duration = 1100

def select_stats():
    global action_message, player_health, player_defense, player_magic, player_strength, enemy_health, battle_flavor_text
    action_message = ( f"HP: {player_health}  Defense: {int(player_defense*100)}  Magic: {int(player_magic*100)}  Strength: {int(player_strength*100)}")


 
def start_enemy_action():
    global action_message, enemy_pose, enemy_pose_timer
    global enemy_action, enemy_damage, enemy_defend

    enemy_defend = 1
    decide_roll = int(random.uniform(0,12))
    variance = float(random.uniform(0.85,1.2))
    if charge == True:
        enemy_damage = int((variance)*(40 * enemy_strength)/(enemy_defense*player_defend))
        enemy_pose = "superattack"
        enemy_pose_timer = pygame.time.get_ticks()
        action_message = (f"The Enemy performs a monumental attack for {enemy_damage} damage!")
        enemy_action = "superattack"
    else:
        if decide_roll == 12:
            enemy_pose = "charge"
            enemy_pose_timer = pygame.time.get_ticks()
            action_message = "The Enemy starts charging for a strong attack!"
            enemy_action = "charge"
        elif decide_roll == 1:
            enemy_pose = "defend"
            enemy_pose_timer = pygame.time.get_ticks()
            action_message = "The Enemy braces for impact and defends!"
            enemy_action = "defend"
        elif decide_roll == 2:
            enemy_damage_sound.play()
            enemy_pose = "attack"
            enemy_pose_timer = pygame.time.get_ticks()
            enemy_pose = "confused"
            enemy_pose_timer = pygame.time.get_ticks()
            action_message = (f"The Enemy misses his attack!")
            enemy_action = "miss"
        else:
            enemy_damage = int((variance)*(30 * enemy_strength)/(player_defense*player_defend))
            enemy_damage_sound.play()
            enemy_pose = "attack"
            enemy_pose_timer = pygame.time.get_ticks()
            action_message = f"The Enemy attacks for {enemy_damage}!"
            enemy_action = "attack"


def resolve_enemy_action():
    global player_health, action_message, charge, enemy_defend, player_defend, messagepicked
    if enemy_action == "attack":
        player_health -= enemy_damage
    elif enemy_action == "charge":
        charge = True
    elif enemy_action == "defend":
        enemy_defend = 2
    elif enemy_action == "superattack":
        player_health -= enemy_damage
        charge = False
    elif enemy_action == "miss":
        player_defend = 1
    player_defend = 1
    action_message = ""
    messagepicked = "false"

                
def show_victory():
    global current_screen, music1play, titlemusic
    current_screen = "victory"
    music1play = False
    titlemusic = False
    screen.blit(enemy_dead_img, (275, 150)) 


def draw_victory():
    global score, score_recorded, top_score
    screen.fill(GREEN)
    title_button.draw(screen)
    screen.blit(enemy_dead_img, (275, 150)) 
    score = int(player_health + (difficulty_mult)*100)
    if score_recorded == False:
        with open('scores.txt', 'a') as scoreboard:
            scoreboard.write(f"{role},{current_difficulty},{score}\n")
        score_recorded = True
        print(score)
    battle_text.draw(screen, f"YOU WIN, Score:{score}")

def show_defeat():
    global current_screen, defeatmusic, music1play, titlemusic
    current_screen = "defeat"
    music1play = False
    titlemusic = False


def draw_defeat():
    global score_recorded, score
    screen.fill(BLACK)
    title_button.draw(screen)
    screen.blit(enemy_bite_img, (275, 150)) 
    score = int(enemy_health/10 +(difficulty_mult)*10) #10 is gonna be the defeat bonus
    if score_recorded == False:
        with open('scores.txt', 'a') as scoreboard:
            scoreboard.write(f"{role},{current_difficulty},{score}\n")
        score_recorded = True
        print(score)
    battle_text.draw(screen, f"YOU LOSE, Score: {score}")
    
    

## Buttons
start_button = Button(300, 500, 200, 50, "Start Game", GREEN, BRIGHT_GREEN, show_difficulty)

easy_button = Button(500, 150, 200, 100, "EASY", WHITE, BRIGHT_GREEN,select_easy )
normal_button = Button(500, 300, 200, 100, "NORMAL", WHITE, BRIGHT_GREEN, select_normal)
hard_button = Button(500, 450, 200, 100, "HARD", WHITE, BRIGHT_GREEN, select_hard)

knight_button = Button(75, 400, 300, 100, "KNIGHT", RED, WHITE, select_knight )
wizard_button = Button(75, 250, 300, 100, "WIZARD", RED, WHITE, select_wizard)
paladin_button = Button(75, 100, 300, 100, "PALADIN", RED, WHITE, select_paladin)

attack_button = Button(0, 500, 150, 100, "Attack", BRIGHTRED, RED, select_attack)
spell_button = Button(150, 500, 150, 100, "Spell", BRIGHTYELLOW, YELLOW, select_spell)
skill_button = Button (150,500, 150, 100, "Skill",BRIGHTYELLOW, YELLOW, select_skill  )
defend_button = Button(500,500, 150, 100, "Defend", BRIGHTBLUE, BLUE, select_defend)
stats_button = Button(650,500, 150, 100, "Stats", PINK, DARKPINK, select_stats)

title_button = Button(300, 500, 200, 50, "Play Again?", RED, PINK, show_title)

##Text and Stat Values
hp = Textbox(300,500,200,100,"freesansbold.ttf",20, BLACK, WHITE,RED,3)
enemy_name = Textbox(150,0,500,75,'Fonts/MedievalSharp-Regular.ttf',36,WHITE,BLACK,None,0)
battle_text = Textbox(50,400,700,100,'freesansbold.ttf',24,WHITE, BLACK, GREEN,2)
enemy_hp = Textbox(325,75,150,50,"freesansbold.ttf",32, BLACK, WHITE,RED,3)


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
        
        if current_screen == "victory":
            title_button.handle_event(event)
        
        if current_screen == "defeat":
            title_button.handle_event(event)


    if current_screen == "title":
        show_title()
        draw_title()
    if current_screen == "difficulty":
        draw_difficulty()
        show_difficulty()
    if current_screen == "class":
        draw_role()
        show_role()
    
    #This contains the battle loop and the timing function (I hate this timing function)
    if current_screen == "battle":
        show_battle()
        draw_battle()

        if enemy_pose != "idle" and pygame.time.get_ticks() - enemy_pose_timer > 1500:
            enemy_pose = "idle"
        
        now = pygame.time.get_ticks()

        if battle_state == "player_turn":
            pass

        elif battle_state == "player_pause":
            if now - pause_start > pause_duration:
                battle_state = "enemy_action"


        elif battle_state == "enemy_action":

            start_enemy_action()
            battle_state = "enemy_pause"
            pause_start = pygame.time.get_ticks()
            pause_duration = 1500 

        elif battle_state == "enemy_pause":
            if now - pause_start > pause_duration:
                resolve_enemy_action()
                battle_state = "player_turn"
            
            #if health equals zero, do victory/defeat stuff
            if enemy_health <= 0:
                current_screen = "victory"
            elif player_health <= 0:
                current_screen = "defeat"
  
    #Victory and defeat stuff
    if current_screen == "victory":
        draw_victory()
    if current_screen == "defeat":
        draw_defeat()
    
 
    pygame.display.flip()  # Update the display

