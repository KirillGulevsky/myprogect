import pygame
from copy import deepcopy
from random import choice, randrange
from time import time
import pickle
from os import path

RES = 1032, 760
FPS = 120
#РАЗЛИЧНЫЕ ПЕРЕМЕННЫЕ
poz = ['     +', ' вверх', '  вниз', 'вправо', ' влево', '    w ']
mod = 20
s = 0
count_1 = 0
count_2 = 2
b = 0
proval = 0
a  = time()
game_mod = 'standart'
mod1 = 1
mod2 = 30
prosto = 0
pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
#ЗВУКИ
snd = path.join(path.dirname(__file__), 'snd')
wow = pygame.mixer.Sound(path.join(snd, 'wow.mp3'))
nice = pygame.mixer.Sound(path.join(snd, 'nice.mp3'))
beepstandart = pygame.mixer.Sound(path.join(snd, 'beepstandart.mp3'))
beepreverse = pygame.mixer.Sound(path.join(snd, 'beepreverse.mp3'))
beepsad = pygame.mixer.Sound(path.join(snd, 'beepsad.mp3'))
sad = pygame.mixer.Sound(path.join(snd, 'sad.mp3'))

#ВИД ТЕКСТА
main_font = pygame.font.Font('font/font.ttf', 55)
font = pygame.font.Font('font/font.ttf', 35)

#ОСНОВНЫЕ НАДПИСИ
title_game = main_font.render('БЫСТРЕЕ!', True, pygame.Color('white'))
title_score = font.render('score:', True, pygame.Color('white'))
title_record = font.render('record:', True, pygame.Color('white'))

#РЕКОРД
q = 0
score = q

try:
    with open('newrecord', 'rb') as f:
        record = pickle.load(f)
except:
    record = 0

title_dein = main_font.render('пробел', True, (255, 255, 255))
sc.blit(title_dein, (400, 300))

next_dei = deepcopy(choice(poz))

while True:
    taimer = int(time() - a)
    #ИЗМЕНЕНИЕ РЕЖИМОВ ИГРЫ
    if q == mod2:
        game_mod = 'standart'
        s = 0
        mod1 = 1
        mod2 += 20
        prosto = 0
        wow.play(0)
    if q == mod:
        game_mod = 'reverse'
        s = 0
        mod1 = 1
        mod += 20
        nice.play(0)
    #ИЗМЕНЕНИЯ В ЗАВИСИМОСТИ ОТ РЕЖИМА ИГРЫ
    if game_mod == 'standart' and mod >= 30 and prosto != 1:
        sc.fill('black')
        next_dei = deepcopy(choice(poz))
        title_dein = main_font.render(next_dei, True, (255, 255, 255))
        sc.blit(title_dein, (400, 300))
        prosto = 1
    if game_mod == 'standart':
        title_score = font.render('score:', True, pygame.Color('white'))
        title_record = font.render('record:', True, pygame.Color('white'))
        sc.blit(title_score, (10, 680))
        sc.blit(font.render(str(score), True, pygame.Color('white'), (0, 0, 0)), (200, 680))
        sc.blit(title_game, (380, -10))
        sc.blit(title_record, (300, 680))
        sc.blit(font.render(str(record), True, pygame.Color('white')), (520, 680))
    if game_mod == 'reverse' and mod1 == 0:
        title_score = font.render('score:', True, pygame.Color('black'))
        title_record = font.render('record:', True, pygame.Color('black'))
        sc.blit(title_score, (10, 680))
        sc.blit(font.render(str(score), True, pygame.Color('black')), (200, 680))
        sc.blit(title_record, (300, 680))
        sc.blit(font.render(str(record), True, pygame.Color('black')), (520, 680))
    if game_mod == 'reverse' and mod1 == 1:
        b = 0
        if s == 1:
            b = 1
        # ВСЁ БЕЛОЕ
        sc.fill('white')
        pygame.draw.rect(sc, (255, 255, 255), (80, -10, 900, 75))
        pygame.draw.rect(sc, (255, 255, 255), (200, 280, 700, 200))
        pygame.draw.rect(sc, (255, 255, 255), (500, 150, 100, 100))
        pygame.draw.rect(sc, (255, 255, 255), (175, 670, 100, 75))
        # РЕКОРД И СКОР СТАНОВЯТСЯ ЧЁРНЫМИ
        title_score = font.render('score:', True, pygame.Color('black'))
        title_record = font.render('record:', True, pygame.Color('black'))
        sc.blit(title_score, (10, 680))
        sc.blit(font.render(str(score), True, pygame.Color('black')), (200, 680))
        sc.blit(title_record, (300, 680))
        sc.blit(font.render(str(record), True, pygame.Color('black')), (520, 680))
        # ТЕКСТ ОБРАТНОГО РЕЖИМА
        title_game_mod = main_font.render('ОБРАТНЫЙ РЕЖИМ', True, pygame.Color('black'))
        sc.blit(title_game_mod, (230, 580))
        game_over_1 = main_font.render('нажмите пробел', True, (0, 0, 0))
        sc.blit(game_over_1, (255, 350))
        count_1 = int(time() - a)
    #ТАЙМЕРЫ
    if taimer - count_1 == 1 and count_2 > -1 and b == 1 and game_mod == 'standart':
        pygame.draw.rect(sc, (0, 0, 0), (500, 150, 100, 100))
        sc.blit(main_font.render(str(count_2), True, (225, 225, 225)), (500, 150))
        count_1 += 1
        count_2 -= 1
    if taimer - count_1 == 1 and count_2 > -1 and b == 1 and game_mod == 'reverse':
        pygame.draw.rect(sc, (255, 255, 255), (500, 150, 100, 100))
        sc.blit(main_font.render(str(count_2), True, (0, 0, 0)), (500, 150))
        count_1 += 1
        count_2 -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            #ВЗАИМОДЕЙСТВИЕ С КЛАВИШАМИ
            if next_dei == ' влево' and event.key == pygame.K_LEFT and count_2 != -1 and game_mod == 'standart':
                next_dei = deepcopy(choice(poz))
                pygame.draw.rect(sc, (0, 0, 0), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (255, 255, 255))
                sc.blit(title_dein, (400, 300))
                proval = 0
                pygame.draw.rect(sc, (0, 0, 0), (175, 670, 100, 75))
                q += 1
                score = q
                count_2 = 2
                beepstandart.play(0)
            elif next_dei == 'вправо' and event.key == pygame.K_RIGHT and count_2 != -1 and game_mod == 'standart':
                next_dei = deepcopy(choice(poz))
                pygame.draw.rect(sc, (0, 0, 0), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (255, 255, 255))
                sc.blit(title_dein, (400, 300))
                proval = 0
                pygame.draw.rect(sc, (0, 0, 0), (175, 670, 100, 75))
                q += 1
                score = q
                count_2 = 2
                beepstandart.play(0)
            elif next_dei == '  вниз' and event.key == pygame.K_DOWN and count_2 != -1 and game_mod == 'standart':
                next_dei = deepcopy(choice(poz))
                pygame.draw.rect(sc, (0, 0, 0), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (255, 255, 255))
                sc.blit(title_dein, (400, 300))
                proval = 0
                pygame.draw.rect(sc, (0, 0, 0), (175, 670, 100, 75))
                q += 1
                score = q
                count_2 = 2
                beepstandart.play(0)
            elif next_dei == ' вверх' and event.key == pygame.K_UP and count_2 != -1 and game_mod == 'standart':
                next_dei = deepcopy(choice(poz))
                pygame.draw.rect(sc, (0, 0, 0), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (255, 255, 255))
                sc.blit(title_dein, (400, 300))
                proval = 0
                pygame.draw.rect(sc, (0, 0, 0), (175, 670, 100, 75))
                q += 1
                score = q
                count_2 = 2
                beepstandart.play(0)
            elif next_dei == '    w ' and event.key == pygame.K_w and count_2 != -1 and game_mod == 'standart':
                next_dei = deepcopy(choice(poz))
                pygame.draw.rect(sc, (0, 0, 0), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (255, 255, 255))
                sc.blit(title_dein, (400, 300))
                proval = 0
                pygame.draw.rect(sc, (0, 0, 0), (175, 670, 100, 75))
                q += 1
                score = q
                count_2 = 2
                beepstandart.play(0)
            elif next_dei == '     +' and event.key == pygame.K_EQUALS and count_2 != -1 and game_mod == 'standart':
                next_dei = deepcopy(choice(poz))
                pygame.draw.rect(sc, (0, 0, 0), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (255, 255, 255))
                sc.blit(title_dein, (400, 300))
                proval = 0
                pygame.draw.rect(sc, (0, 0, 0), (175, 670, 100, 75))
                q += 1
                score = q
                count_2 = 2
                beepstandart.play(0)
            elif proval == 1 and event.key == pygame.K_SPACE:
                # ПРОБЕЛ ПОСЛЕ ПРОИГРЫША
                next_dei = deepcopy(choice(poz))
                pygame.draw.rect(sc, (0, 0, 0), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (255, 255, 255))
                sc.blit(title_dein, (400, 300))
                count_2 = 2
                b = 1
                a = time()
                count_1 = 0
            elif event.key == pygame.K_SPACE and q == 0 and s == 0 and game_mod == 'standart':
                # ПРОБЕЛ НАЧАЛЬНЫЙ
                pygame.draw.rect(sc, (0, 0, 0), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (255, 255, 255))
                sc.blit(title_dein, (400, 300))
                b = 1
                s = 1
                a = time()
            elif next_dei == ' влево' and event.key == pygame.K_RIGHT and count_2 != -1 and game_mod == 'reverse':
                next_dei = deepcopy(choice(poz))
                pygame.draw.rect(sc, (255, 255, 255), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (0, 0, 0))
                sc.blit(title_dein, (400, 300))
                proval = 0
                pygame.draw.rect(sc, (255, 255, 255), (175, 670, 100, 75))
                q += 1
                score = q
                count_2 = 2
                beepreverse.play(0)
            elif next_dei == 'вправо' and event.key == pygame.K_LEFT and count_2 != -1 and game_mod == 'reverse':
                next_dei = deepcopy(choice(poz))
                pygame.draw.rect(sc, (255, 255, 255), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (0, 0, 0))
                sc.blit(title_dein, (400, 300))
                proval = 0
                pygame.draw.rect(sc, (255, 255, 255), (175, 670, 100, 75))
                q += 1
                score = q
                count_2 = 2
                beepreverse.play(0)
            elif next_dei == '  вниз' and event.key == pygame.K_UP and count_2 != -1 and game_mod == 'reverse':
                next_dei = deepcopy(choice(poz))
                pygame.draw.rect(sc, (255, 255, 255), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (0, 0, 0))
                sc.blit(title_dein, (400, 300))
                proval = 0
                pygame.draw.rect(sc, (255, 255, 255), (175, 670, 100, 75))
                q += 1
                score = q
                count_2 = 2
                beepreverse.play(0)
            elif next_dei == ' вверх' and event.key == pygame.K_DOWN and count_2 != -1 and game_mod == 'reverse':
                next_dei = deepcopy(choice(poz))
                pygame.draw.rect(sc, (255, 255, 255), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (0, 0, 0))
                sc.blit(title_dein, (400, 300))
                proval = 0
                pygame.draw.rect(sc, (255, 255, 255), (175, 670, 100, 75))
                q += 1
                score = q
                count_2 = 2
                beepreverse.play(0)
            elif next_dei == '    w ' and event.key == pygame.K_s and count_2 != -1 and game_mod == 'reverse':
                next_dei = deepcopy(choice(poz))
                pygame.draw.rect(sc, (255, 255, 255), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (0, 0, 0))
                sc.blit(title_dein, (400, 300))
                proval = 0
                pygame.draw.rect(sc, (255, 255, 255), (175, 670, 100, 75))
                q += 1
                score = q
                count_2 = 2
                beepreverse.play(0)
            elif next_dei == '     +' and event.key == pygame.K_MINUS and count_2 != -1 and game_mod == 'reverse':
                next_dei = deepcopy(choice(poz))
                pygame.draw.rect(sc, (255, 255, 255), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (0, 0, 0))
                sc.blit(title_dein, (400, 300))
                proval = 0
                pygame.draw.rect(sc, (255, 255, 255), (175, 670, 100, 75))
                q += 1
                score = q
                count_2 = 2
                beepreverse.play(0)
            elif event.key == pygame.K_SPACE and q == (mod - 20) and game_mod == 'reverse':
                # ПРОБЕЛ НАЧАЛЬНЫЙ ОБРАТНЫЙ РЕЖИМ
                pygame.draw.rect(sc, (255, 255, 255), (200, 280, 700, 300))
                title_dein = main_font.render(next_dei, True, (0, 0, 0))
                sc.blit(title_dein, (400, 300))
                b = 1
                s = 1
                a = time()
                mod1 = 0
                count_1 = int(time() - a)
            else:
                #ПРОИГРЫШЬ
                if q >= 30:
                    sad.play(0)
                else:
                    beepsad.play(0)
                sc.fill('black')
                b = 0
                pygame.draw.rect(sc, (0, 0, 0), (200, 280, 700, 200))
                pygame.draw.rect(sc, (0, 0, 0), (500, 150, 100, 100))
                game_over = main_font.render('провал', True, (255, 255, 255))
                game_over_1 = main_font.render('нажмите пробел', True, (255, 255, 255))
                sc.blit(game_over, (400, 300))
                sc.blit(game_over_1, (255, 350))
                proval = 1
                pygame.draw.rect(sc, (0, 0, 0), (175, 670, 100, 75))
                game_mod = 'standart'
                if mod > 20:
                    mod -= 20
                if mod2 > 30:
                    mod2 -= 20
                if q > record:
                    pygame.draw.rect(sc, (0, 0, 0), (500, 670, 100, 75))
                    record = q
                    with open('newrecord', 'wb') as f:
                        pickle.dump(record, f)
                q = 0
                score = q

    pygame.display.flip()
    clock.tick(FPS)