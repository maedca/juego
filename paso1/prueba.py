#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       sin título.py
#       
#       Copyright 2010 Manuel Camacho <manuel@manuel-laptop>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.



import pygame
#creamos la ventana
pygame.display.set_mode((640, 480))
pygame.display.set_caption("Mono Vs Cazador")
#regla para esperar el cierre de la ventana
pygame.event.set_allowed(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.wait()


