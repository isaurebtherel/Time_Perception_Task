import pygame
import simpleaudio as sa
import time
import random
from sys import exit
width=1425
height=775
BLACK=(100,100,100)
WHITE = (255, 255, 255)
#light_blue= (155,218,210)
#light_pink=(85,33,71)
bubbles= (57,39,75)
#light_pink=(60,67,85)
beige= (250, 244, 227)
beige=(255,255,255)
light_blue=(216, 233, 248)
light_pink=((246, 230, 230))
bubbles=(155,218,210)
##### settings #####
screen=pygame.display.set_mode((width,height))
screen.fill(beige)
pygame.display.set_caption('experiment_time_perception')

#### sounds ####
from pygame import mixer
mixer.init()
win=pygame.mixer.Sound("mixkit-bonus-earned-in-video-game-2058.wav")
loss=pygame.mixer.Sound("system-notification-199277.mp3")
equal=pygame.mixer.Sound("click.wav")
page=pygame.mixer.Sound("handle-paper-foley-2-172689.mp3")
#### sounds ####

#### illustrations settings ####
#jellyfish pnj
pnj_surface=pygame.image.load('jellyfish2.jpeg').convert_alpha()
scaling_factor = 0.3
original_width, original_height = pnj_surface.get_size()
new_width = int(original_width * scaling_factor)
new_height = int(original_height * scaling_factor)
pnj_surface = pygame.transform.scale(pnj_surface, (new_width, new_height))

# text1
text1=pygame.image.load('text.png')
scaling_factor = 0.8
original_width, original_height = text1.get_size()
new_width = int(original_width * scaling_factor)
new_height = int(original_height * scaling_factor)
text1 = pygame.transform.scale(text1, (new_width, new_height))

# text2
text2=pygame.image.load('text2.png')
scaling_factor = 0.8
original_width, original_height = text2.get_size()
new_width = int(original_width * scaling_factor)
new_height = int(original_height * scaling_factor)
text2 = pygame.transform.scale(text2, (new_width, new_height))
#rsp à compléter
pierre = pygame.image.load('pierre.jpg')
scaling_factor = 1.3
#original_width, original_height = pnj_surface.get_size()
new_width = int(original_width * scaling_factor)
new_height = int(original_height * scaling_factor)
# Resize the image


pnj_pos=1300

#### illustrations settings ####

### functions ####
def rsp(choice):
    screen.blit(rsp_choice, ((width - r_instruction.get_width()) / 1.75, height / 5))
    screen.blit(rsp_choice2, ((width - r_instruction.get_width()) / 1.75, height / 5))
    pygame.display.update()
    computer_answer_display = pygame.image.load(computer_answer)
    screen.blit((pygame.image.load(choice)), ((width) / 3, height / 3))
    screen.blit(computer_answer_display, ((width) / 2, height / 3))
### functions ####

### instructions ###

instructions = pygame.font.Font('Brightly_Crush.ttf', 70)
instructionss = pygame.font.SysFont('Brightly_Crush.ttf', 50)
score_font =  pygame.font.Font('Brightly_Crush.ttf', 70)
choice = pygame.font.SysFont('Brightly_Crush.ttf', 70)
instructions = instructions.render('Experiment instructions: ', True, (light_pink))
rsp_choice=choice.render('You               ', True, (light_blue))
rsp_choice2=choice.render('                   AI', True, (light_pink))
r_instruction = choice.render('Rock has been chosen', True, (light_pink))
s_instruction = choice.render('Scissors have been chosen', True, (light_pink))
p_instruction = choice.render('Paper has been chosen', True, (light_pink))
instructions1 = instructionss.render('This is a rock paper scissors game', True, (light_blue))
instructions2 = instructionss.render('Press R to choose rock', True, (light_blue))
instructions3 = instructionss.render('Press S to choose scissors', True, (light_blue))
instructions4 = instructionss.render('Press P to choose paper', True, (light_blue))
instructions5 = instructionss.render('Please wear headphones for the experiment.', True, (light_blue))
instructions6 = instructionss.render('Press space when ready', True, (light_blue))
instructions7 = instructionss.render('Press T when 30 seconds have passed', True, (light_blue))


instructions_reading = pygame.font.Font('Brightly_Crush.ttf', 70)
instructionss_reading = pygame.font.SysFont('Brightly_Crush.ttf', 50)
score_font =  pygame.font.Font('Brightly_Crush.ttf', 70)
choice_reading = pygame.font.SysFont('Brightly_Crush.ttf', 70)
reading_instructions = instructions_reading.render('Experiment instructions: ', True, (light_pink))
reading_instructions1 = instructionss.render('This is a reading task', True, (light_blue))
reading_instructions2 = instructionss.render('There are two texts to read', True, (light_blue))
reading_instructions3 = instructionss.render('These will be followed by simple questions', True, (light_blue))
reading_instructions4 = instructionss.render('Please wear headphones for the experiment', True, (light_blue))
reading_instructions6 = instructionss.render('Press N to access questions', True, (light_blue))
reading_instructions5 = instructionss.render('Press P to acess the first text', True, (light_blue))
reading_instructions7 = instructionss.render('Press D to acess the second text', True, (light_blue))
reading_instructions8 = instructionss.render('Press T when 30 seconds have passed', True, (light_blue))
### instructions ###

def rsp_after_choice(score):
    score_surface = score_font.render(('Score:' + str(score)), True, (bubbles))
    screen.blit(score_surface, (width / 10, (height / 20)))
    instructions = pygame.font.Font('Brightly_Crush.ttf', 20)
    answer3 = instructions.render('Press L for the reading task once score:10', True, (bubbles))
    screen.blit(answer3, (width / 4 + 600, (height / 4) + 530))
    pygame.display.update()
    pygame.time.delay(2000)
    screen.fill(beige)
    instructions = pygame.font.Font('Brightly_Crush.ttf', 20)
    answer3 = instructions.render('Press L for the reading task once score:10', True, (bubbles))
    screen.blit(answer3, (width / 4 + 600, (height / 4) + 530))
    pygame.display.update()

def reading_after_choice():
    pygame.display.update()
    pygame.time.delay(2000)
    screen.fill(beige)
    answer3 = instructionss.render('Press N for the next question', True, (light_blue))
    screen.blit(answer3, (width / 4 + 550, (height / 4) + 530))
    pygame.display.update()

questions=[
    "Was Jenny Fields arrested in Boston in 1942?",
    "Did the incident at the movie theater happen shortly after the bombing of Pearl Harbor?",
    "Did people generally become more tolerant of soldiers after Pearl Harbor?",
    "Did Jenny Fields exhibit tolerance towards soldiers in the movie theater?",
    "Did Jenny move three times in the movie theater to avoid the soldier?",
    "Did the soldier move closer to Jenny each time she moved?",
    "Did Jenny resolve not to move again when the soldier sat beside her?",
    "Was Jenny twenty-two years old at the time of the incident?",
    "Did Jenny drop out of college soon after starting?",
    "Did Jenny finish her nursing-school program at the top of her class?",
    "Did Jenny enjoy being a nurse?",
    "Did Jenny have dark, glossy hair?",
    "Did Jenny feel that she was doing the right choice ?",
    "Did Jenny suspect that her parents sent her to college to find a husband?",
    "Did Jenny major in English literature?"
]
