import pygame

from settings import Settings
from batman import Batman
from coringa import Coringa
import game_functions as gf

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Duelo")

    batman = Batman(screen)
    coringa = Coringa(screen)
    
    #Inicia o laço principal do jogo
    while True:
        gf.check_events(batman)
        batman.update()
        gf.update_screen(ai_settings, screen, batman, coringa)
        
run_game()