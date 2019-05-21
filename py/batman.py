#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 21:51:51 2019

@author: fernando
"""

import pygame

class Batman():
    
    def __init__(self, screen):
        """Inicializa o Batman e define sua posição inicial."""
        self.screen = screen
        
        #Carrega a imagem do batman e obtém seu rect
        self.image = pygame.image.load("../imagem/batman_200.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Inicia cada novo batman na parte inferior central da tela
        self.rect.left = self.screen_rect.left
        self.rect.bottom = self.screen_rect.bottom
        
        #Flag de movimento
        self.moving_right = False
        self.moving_left = False
        self.isjump = False

        
    def update(self):
        """Atualiza a posição do batmna de acordo com a flag de movimento."""
        if self.moving_right:
            self.rect.right += 1
        if self.moving_left:
            self.rect.left -= 1
            
        
    def blitme(self):
        """Desenha o batman em sua posição atual."""
        self.screen.blit(self.image, self.rect)