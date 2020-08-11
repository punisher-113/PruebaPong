import pygame, sys, random

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
game_over =False

##generamos posiciones aleatorias en la pantalla y las guardamos


##Definir Colores formato RGB

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE= (255,0,255)
##colores agregados

player_width =15
player_height =130


##Coordenadas y velocidad player1
Player1_x_coord = 50
Player1_y_coord = 300-45 ## 300-45
Player1_y_speed= 2

##Coordenadas y velocidad player2
Player2_x_coord = 750
Player2_y_coord = 300-45
Player2_y_speed= 0

##Coordenadas de la pelota

pelota_x= 400
pelota_y= 300
pelota_speed_x=2
pelota_speed_y=2


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True
        ##Eventos teclado

    #Jugador1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                Player1_y_speed=3
            if event.key == pygame.K_w:
                Player1_y_speed=-3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                Player1_y_speed = 3
            if event.key == pygame.K_w:
                Player1_y_speed = 3
    ##Mueve Al P1
    Player1_y_coord += Player1_y_speed
    ##Rutina de rebote P1
    if Player1_y_coord >540 or Player1_y_coord <10:
        Player1_y_speed *=-1
    ##Rutina de rebote P1

    # Jugador2
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            Player2_y_speed = 3
        if event.key == pygame.K_UP:
            Player2_y_speed = -3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            Player2_y_speed = 0
        if event.key == pygame.K_UP:
            Player2_y_speed = 0
    ##Mueve Al P2
    Player2_y_coord += Player2_y_speed

    #Movimiento P2
    Player2_y_coord += Player2_y_speed

    ##Rutina de rebote P2
    if Player2_y_coord > 510 or Player2_y_coord < 60:
        Player2_y_speed *= -1

    ##500 y 60

    ##Rebote de Pelota
    if pelota_y >590 or pelota_y <10:
        pelota_speed_y *=-1
    ##if pelota_x >790 or pelota_x <10:
    ##  pelota_speed_x *=-1
    ##Movimiento pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    ##Revisa si la pelota sale lado derecho
    if pelota_x >800:
        pelota_x= 400
        pelota_y= 300
    ##Si Sale de la pantalla, la pelota vuelve al centro
        pelota_speed_x *= -1
        pelota_speed_y *= -1


    ##Revisa si la pelota sale lado derecho
    if pelota_x < 000:
        pelota_x= 400
        pelota_y= 300
    ##Si Sale de la pantalla, la pelota vuelve al centr
        pelota_speed_x *= -1
        pelota_speed_y *= -1





    screen.fill(BLACK)
    ##Logica de programa

    ##Zona de dibujo

    ##Creacion de jugadores
    jugador1 = pygame.draw.rect(screen, PURPLE, (Player1_x_coord, Player1_y_coord, player_width, player_height)) ## Rectangulo 1
    jugador2 =pygame.draw.rect(screen, BLUE, (Player2_x_coord,Player2_y_coord, player_width, player_height))  ## Rectangulo 2
    ##Creacion pelota
    pelota = pygame.draw.circle(screen,WHITE,(pelota_x,pelota_y),25)
    ##Zona de dibujo


    ##Colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect (jugador2):
        pelota_speed_x *=-1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()



