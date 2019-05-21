#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:23:06 2019

@author: fernando
"""

import pygame
from pygame.sprite import Sprite

class Batarangue(Sprite):
    """Classe ue administra projeteis."""
    def __init__(self, ai_settings, screen, batman):
        """Cria um objeto para o projétil na posição atual do batman."""
        super(Batarangue, self).__init__()