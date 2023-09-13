# Importer les bibliothèques
import pygame
import time
from pygame.locals import *
from utils import *

# Initialiser les sous-modules
pygame.init()

# Initialiser les variables
screen_width = 640
screen_height = 480
screen_flags = pygame.RESIZABLE
background_image = "golf.png"
polygon_color = pygame.Color(4, 250, 250)
polygon_position = {"x": 20, "y": 50}
polygon_move = {"x": 0, "y": 0}
color_up = pygame.Color(186, 27, 172)
color_down = pygame.Color(27, 131, 186)
color_left = pygame.Color(186, 126, 27)
color_right = pygame.Color(250, 250, 4)
color_red = pygame.Color(250, 0, 0)
color_black = pygame.Color(0, 0, 0)
color_ball = pygame.Color(199, 0, 57)
color_list = [color_up, color_down, color_left, color_right]
score = 0
track_time = pygame.time.Clock()
name_player = input("Quel est ton nom de joueur ? ")

# Créer la fenêtre de jeu
screen = pygame.display.set_mode((screen_width, screen_height), screen_flags)

# Initialiser les éléments à la fenêtre de jeu
pygame.display.set_caption("Bienvenue dans mon premier jeu Python !")
background = pygame.image.load(background_image).convert()


# Fonction pour afficher le polygone
def show_polygon(background_target, color, position):
    polygon_coord1 = (5 + position['x'], 0 + position['y'])
    polygon_coord2 = (10 + position['x'], 5 + position['y'])
    polygon_coord3 = (5 + position['x'], 10 + position['y'])
    polygon_coord4 = (0 + position['x'], 5 + position['y'])
    pygame.draw.polygon(background_target, color, [polygon_coord1, polygon_coord2, polygon_coord3, polygon_coord4], 0)
    screen.blit(background_target, (0, 0))


# Fonction pour afficher le score
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)

# Fonction pour afficher la balle
def show_ball(target, color, position):
    pygame.draw.rect(target, color, pygame.Rect(position["x"], position["y"], 10, 10))


# Fonction GameOver
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Perdu ' + name_player + '!  Score : ' + str(score), True, color_red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width / 2, screen_height / 4)
    screen.fill(color_black)
    # Afficher le message de game over
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    time.sleep(2)

    # Quitter pygame et python
    pygame.quit()
    quit()


# Position de la balle
ball_position = {"x": random.randrange(1, screen_width-10), "y": random.randrange(1, screen_height-10)}
ball_spawn = True

# Initialiser une variable pour gérer le clic sur le bouton pour fermer la fenêtre
isRunning = True


# Création du jeu
while isRunning:
    for event in pygame.event.get():
        # Contrôler la fin du jeu
        if event.type == pygame.QUIT:
            isRunning = False
        # Changer la couleur du polygon en déplacant la souris
        if event.type == pygame.MOUSEMOTION:
            polygon_color = random_color(color_list)
        # Déplacer le polygone avec les touches du clavier
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                polygon_move["x"] = -1
                polygon_color = color_left
            elif event.key == K_RIGHT:
                polygon_move["x"] = +1
                polygon_color = color_right
            elif event.key == K_UP:
                polygon_move["y"] = -1
                polygon_color = color_up
            elif event.key == K_DOWN:
                polygon_move["y"] = +1
                polygon_color = color_down
        # elif event.type == KEYUP:
        #     if event.key == K_LEFT:
        #         polygon_move["x"] = 0
        #     elif event.key == K_RIGHT:
        #         polygon_move["x"] = 0
        #     elif event.key == K_UP:
        #         polygon_move["y"] = 0
        #     elif event.key == K_DOWN:
        #         polygon_move["y"] = 0

    # Mettre à jour les positions du polygone
    polygon_position["x"] += polygon_move["x"]
    polygon_position["y"] += polygon_move["y"]

    # Afficher le polygon
    show_polygon(background, polygon_color, polygon_position)

    # print(polygon_position["x"], polygon_position["y"])

    # Gérer la colision avec la balle et mettre à jour le score
    if (abs(polygon_position["x"] - ball_position["x"])) >= 0 and abs((polygon_position["x"] - ball_position["x"])) <= 5 \
            and 5 >= abs((polygon_position["y"] - ball_position["y"])) >= 0:
        score += 1
        ball_spawn = False

    # Gérer si la balle est trouvé
    if not ball_spawn:
        ball_position = {"x": random.randrange(1, screen_width - 10), "y": random.randrange(1, screen_height - 10)}

    ball_spawn = True

    # Afficher la balle
    show_ball(screen, color_ball, ball_position)

    # Gérer le game over
    if polygon_position["x"] < 0 or polygon_position["x"] > screen_width - 10:
        game_over()
    if polygon_position["y"] < 0 or polygon_position["y"] > screen_height - 10:
        game_over()

    # Afficher le score
    show_score(color_black, 'times new roman', 20)

    # Rendre visible les mises à jour du jeu à l'écran
    pygame.display.update()

    # Configurer la vitesse du polygone
    track_time.tick(100)

# Quitter pygame
pygame.quit()

# Quitter python
quit()
