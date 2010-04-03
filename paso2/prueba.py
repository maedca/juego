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

screen=pygame.display.set_mode((640, 480))#define ventana
pygame.display.set_caption("Mono Vs Cazador")#define titulo de ventana
# crea dos objetos "Surface".
#
# nota: las funciones "convert" y "convert_alpha" convierten la superficie
#       creada por "load" a un formato de color que permite imprimirlas mucho
#       mas rápido sobre la pantalla.
fondo=pygame.image.load("fondo.jpg").convert()
logotipo=pygame.image.load("logo.png").convert_alpha()
# imprime ambas "Surface" sobre la ventana, e invoca a "flip" para
# actualizar la pantalla principal. Mostrando los cambios.
screen.blit(fondo, (0, 0))
screen.blit(logotipo, (570, 390))
pygame.display.flip()#muestra cambios
# Detiene el programa hasta que surja el evento QUIT. Esto es: que el
# usuario pulse el botón "cerrar" de la ventana.
pygame.event.set_allowed(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.wait()
