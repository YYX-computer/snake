from tkinter.messagebox import showinfo as msg
from random import randint as rand
from pygame.locals import *
import tkinter as tk
import pygame
import time
win = tk.Tk()
win.withdraw()
pygame.init()
def render(surf,blocks):
	for x,y in blocks.keys():
		renderingf = (x * 40,y * 40)
		color = blocks[(x,y)]
		pygame.draw.rect(surf,color,Rect(renderingf,(40,40)))
def render_snake(surf,pos):
	def unique(pos):
		for i in pos:
			if(pos.count(i) > 1):
				return False
		return True
	if(not unique(pos)):
		return False
	d = {}
	for i in pos:
		d[tuple(i)] = (255,255,255)
	d[pos[-1]] = (0,0,255)
	render(surf,d)
	return True
def main(size):
	scr = pygame.display.set_mode((40 * size[0],40 * size[1]))
	stop = False
	l = 3
	pos = [(0,0),(1,0),(2,0)]
	last = 'd'
	dir = {'w':(0,-1),'s':(0,1),'a':(-1,0),'d':(1,0)}
	oppsite = {'w':'s','s':'w','a':'d','d':'a'}
	food = (rand(0,size[0] - 1),rand(0,size[1] - 1))
	n = 1
	speed = 30
	while(1):
		if((food in pos) and (not stop)):
			l += 1
			food = (rand(0,size[0] - 1),rand(0,size[1] - 1))
		if(l == size[0] * size[1]):
			return l
		if(pos[-1][0] < 0 or pos[-1][1] < 0 or pos[-1][0] >= size[0] or pos[-1][1] >= size[1]):
			return l
		pygame.display.update()
		speed = 30 - int(l / (1 - 3 / (size[0] * size[1])))
		n += 1
		n %= speed
		pos = pos[-l:]
		if((not n) and (not stop)):
			t = (pos[-1][0] + dir[last][0],pos[-1][1] + dir[last][1])
			pos.append(t)
		scr.fill((0,0,0))
		for ev in pygame.event.get():
			if(ev.type == QUIT):
				exit()
			elif(ev.type == KEYDOWN and ev.unicode in 'aAwWsSdD' and ev.unicode):
				if(ev.unicode == oppsite[last]):
					return l
				t = (pos[-1][0] + dir[ev.unicode.lower()][0],
				     pos[-1][1] + dir[ev.unicode.lower()][1])
				pos.append(t)
				last = str(ev.unicode.lower())
			elif(ev.type == MOUSEBUTTONDOWN):
				stop = not stop
			elif(ev.type == KEYDOWN and ev.key == K_ESCAPE and stop):
				return l
		if(stop):
			img = pygame.image.load('pause.jpg')
			img = pygame.transform.scale(img,(40 * size[0],40 * size[1]))
			scr.blit(img,(0,0))
		else:
			render(scr,{food:(0,255,0)})
			if(not render_snake(scr,pos)):
				return l
if(__name__ == '__main__'):
	size = [15,15]
	while(1):
		l = main(size)
		msg("GAMEOVER!","GAMEOVER! score:%s"%l)
