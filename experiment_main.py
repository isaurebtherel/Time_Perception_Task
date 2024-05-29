##### requirements #####
import itertools
import pygame
import simpleaudio as sa
import time
import random
from sys import exit
pygame.init() # starts pygame
from settings import *
from plotting import *
##### requirements #####
##### settings #####

user_time_rsp=[]
# Main loop
clock = pygame.time.Clock()
instruction_timer = 10000  # 10 seconds in milliseconds
white_screen_timer = 20000  # 20 seconds in milliseconds
time_since_last_instruction = 0
running = True
keyboard = {}
def get_key(key):
    try:
        return keyboard[key]
    except KeyError:
        return False



screen.fill(beige)
screen.blit(instructions, (((width - instructions.get_width()) // 2), height / 4))
screen.blit(instructions1, (width / 4, (height / 4) + 120))
screen.blit(instructions2, (width / 4, (height / 4) + 160))
screen.blit(instructions3, (width / 4, (height / 4) + 200))
screen.blit(instructions4, (width / 4, (height / 4) + 240))
screen.blit(instructions5, (width / 4, (height / 4) + 280))
screen.blit(instructions6, (width / 4, (height / 4) + 320))
screen.blit(instructions7, (width / 4, (height / 4) + 360))
screen.blit(pnj_surface, (pnj_pos, 630))
pygame.display.update()
pygame.display.flip()

key_press=False
while not key_press:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
            exit()
       if event.type == pygame.KEYDOWN:
            key_press=True

screen.fill(beige)
pygame.display.update()
pygame.display.flip()


######### rock paper scissors game instructions #######
computer_choices=['papier.jpg','pierre.jpg','ciseaux.jpg']
def rsp(choice):
    screen.blit(rsp_choice, ((width - r_instruction.get_width()) / 1.75, height / 5))
    screen.blit(rsp_choice2, ((width - r_instruction.get_width()) / 1.75, height / 5))
    pygame.display.update()
    computer_answer_display = pygame.image.load(computer_answer)
    screen.blit((pygame.image.load(choice)), ((width) / 3, height / 3))
    screen.blit(computer_answer_display, ((width) / 2, height / 3))

timing=[]

######### rock paper scissors game instructions #######

######### whole task #######
i=0
key_press=False
score=0
while not key_press:
    ######### rsp task #######
       for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            computer_answer = random.choice(computer_choices)
            if event.key==pygame.K_t:
                print(pygame.time.get_ticks())
                print("time")
                user_time_rsp.append(pygame.time.get_ticks())
            elif event.key == pygame.K_r:
                rsp("pierre.jpg")
                answer="pierre.jpg"
                if computer_answer == answer:
                    score = score
                    equal.play()
                if computer_answer == "papier.jpg":
                    score = score -1
                    loss.play()
                if computer_answer == "ciseaux.jpg":
                    score = score +1
                    win.play()
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
            elif event.key == pygame.K_s:
                rsp('ciseaux.jpg')
                answer = "ciseaux.jpg"
                if computer_answer == answer:
                    score = score
                    equal.play()
                if computer_answer == "papier.jpg":
                    score = score +1
                    win.play()
                if computer_answer == "pierre.jpg":
                    score = score -1
                    loss.play()
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
            elif event.key == pygame.K_p:
                rsp("papier.jpg")
                answer ="papier.jpg"
                if computer_answer == answer:
                    score = score
                    equal.play()
                if computer_answer == "ciseaux.jpg":
                    score = score -1
                    loss.play()
                if computer_answer == "pierre.jpg":
                    score = score +1
                    win.play()
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
            elif event.key == pygame.K_t:
               print(pygame.time.get_ticks())
               print("time")
               user_time_rsp.append(pygame.time.get_ticks())
               ######### rsp task #######
               ######### reading task #######
            elif event.key == pygame.K_l:
                user_time_reading=[]
                pnj_pos = 1300
                screen.fill(beige)
                instructions = pygame.font.Font('Brightly_Crush.ttf', 70)
                screen.blit(reading_instructions, (((width - reading_instructions.get_width()) // 2), height / 4))
                screen.blit(reading_instructions1, (width / 4, (height / 4) + 120))
                screen.blit(reading_instructions2, (width / 4, (height / 4) + 160))
                screen.blit(reading_instructions3, (width / 4, (height / 4) + 200))
                screen.blit(reading_instructions4, (width / 4, (height / 4) + 240))
                screen.blit(reading_instructions5, (width / 4, (height / 4) + 280))
                screen.blit(reading_instructions8, (width / 4, (height / 4) + 320))
                screen.blit(pnj_surface, (pnj_pos, 630))
                pygame.display.update()
                pygame.display.flip()
                key_press = False
                while not key_press:
                    # list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
                    # for i in list:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                print("premier")
                                screen.fill(beige)
                                screen.blit(text1, (0, 0))
                                instructions = pygame.font.Font('Brightly_Crush.ttf', 10)
                                answer3 = instructionss.render('Press S for the second text', True, (BLACK))
                                screen.blit(answer3, (width / 4 + 550, (height / 4) + 530))
                                pygame.display.update()
                                pygame.display.flip()
                            elif event.key == pygame.K_s:
                                print("deuxième")
                                screen.fill(beige)
                                screen.blit(text2, (0, 0))
                                instructions = pygame.font.Font('Brightly_Crush.ttf', 20)
                                answer3 = instructionss.render('Press N for the first question', True, (BLACK))
                                screen.blit(answer3, (width / 4 + 550, (height / 4) + 530))
                                pygame.display.update()
                                pygame.display.flip()
                            elif event.key == pygame.K_a:
                                pygame.display.update()
                                pygame.time.delay(2000)
                                screen.fill(beige)
                                answer3= instructionss.render('Press N for the next question', True, (light_blue))
                                screen.blit(answer3,(width / 4+550, (height / 4) + 530))
                                pygame.display.update()
                            elif event.key == pygame.K_b:
                                pygame.display.update()
                                pygame.time.delay(2000)
                                screen.fill(beige)
                                answer3= instructionss.render('Press N for the next question', True, (light_blue))
                                screen.blit(answer3,(width / 4+550, (height / 4) + 530))
                                pygame.display.update()
                            elif event.key == pygame.K_t:
                                print(pygame.time.get_ticks())
                                print("time")
                                user_time_reading.append(pygame.time.get_ticks())
                            elif event.key == pygame.K_n:
                                screen.fill(beige)
                                question = questions[i]
                                print(i)
                                instructions = pygame.font.Font('Brightly_Crush.ttf', 30)
                                question = instructions.render(question, True, (light_pink))
                                answer1 = instructionss.render('a: Yes ', True, (light_blue))
                                answer2 = instructionss.render('b: No', True, (light_blue))
                                screen.blit(question, (((width - question.get_width()) // 2), height / 4))
                                screen.blit(answer1, (width / 4, (height / 4) + 120))
                                screen.blit(answer2, (width / 4, (height / 4) + 160))
                                pygame.display.update()
                                pygame.display.flip()
                                i += 1
                                if i>14:
                                    i=0
                                print("rrr")
                                print("user_time_rsp:", user_time_rsp)
                                print("user_time_reading:", user_time_reading)
                                ######### reading task #######
                                ######### results #######
                            elif event.key == pygame.K_r:
                                results_rsp1=average_difference(user_time_rsp)
                                results_reading2 = average_difference(user_time_reading)
                                plotting([results_rsp1],[results_reading2])
                                screen.fill(beige)
                                trial= pygame.image.load('trial.png')
                                scaling_factor = 1.5
                                original_width, original_height = trial.get_size()
                                new_width = int(original_width * scaling_factor)
                                new_height = int(original_height * scaling_factor)
                                trial = pygame.transform.scale(trial, (new_width, new_height))
                                screen.blit(trial, (0, 0))
                                results_rsp1 = instructionss.render(f'Results rsp task:{(results_rsp1/1000):.1f} s', True,
                                                                                   (light_pink))
                                screen.blit(results_rsp1, (width / 1.5, (height / 4) + 120))
                                results_reading2 = instructionss.render(f'Results reading task:{(results_reading2/1000):.1f} s', True,
                                                                                   (light_pink))
                                screen.blit(results_reading2, (width / 1.5, (height / 4) + 160))
                                print(user_time_rsp)
                                print(user_time_reading)
                                print(results_rsp1)
                                print(results_reading2)
                                pygame.display.update()
                                pygame.display.flip()
                                ######### results #######
######### whole task #######

key_press=False
while not key_press:
       for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


