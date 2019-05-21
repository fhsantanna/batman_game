#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:25:45 2019

@author: fernando
"""

import sys
import pygame

def check_events(batman):
    """Responde a eventos de pressionamento de teclas e mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #Move o batman para direita
                batman.moving_right = True
            elif event.key == pygame.K_LEFT:
                #Move o batman para esquerda
                batman.moving_left = True
            #elif event.key == pygame.K_UP:
            #    batman.isjump = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                batman.moving_right = False             
            elif event.key == pygame.K_LEFT:
                batman.moving_left = False
        
        #https://pythonspot.com/jump-and-run-in-pygame/ --- verificar para botar pulo
            
 
def update_screen(ai_settings, screen, batman, coringa):          
        """Atualiza a imagens na tela e alterna para a nova tela."""
        #Redesenha a tela a cada passagem pelo laço
        screen.fill(ai_settings.bg_color)
        batman.blitme()
        coringa.blitme()

        #Deixa a tela mais recente visível
        pygame.display.flip()