#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 21:51:51 2019

@author: fernando
"""

import pygame

class Coringa():
    
    def __init__(self, screen):
        """Inicializa o Coringa e define sua posição inicial."""
        self.screen = screen
        
        #Carrega a imagem do batman e obtém seu rect
        self.image = pygame.image.load("../imagem/coringa_200.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Inicia cada novo batman na parte inferior central da tela
        self.rect.right = self.screen_rect.right
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        """Desenha o Coringa em sua posição atual."""
        self.screen.blit(self.image, self.rect)