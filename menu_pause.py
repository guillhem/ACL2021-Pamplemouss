# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 14:40:44 2021

@author: sabri
"""
import pygame as py
import param as p
import sys



size_p = 400,400
size_b = width, height = 150,80
#%% fenetre
fen_p = py.Rect((480,330),size_p)
fen_p.center = p.rectScreen.center

#%% boutons

bout_res = py.Rect((260,200),size_b)
bout_main = py.Rect((260,320),size_b)
bout_quit = py.Rect((260,440),size_b)
# bout_save = py.Rect(430,630,size_b)

#%%

title = p.police_deb.render("PAUSE", True, p.pamplemou)
title_rect = title.get_rect()
title_rect.topleft = fen_p.topleft

txt_bou_res = p.police_ui.render("RESUME", True, p.black, p.pamplemou)
txt_bou_main = p.police_ui.render("MAIN MENU", True, p.black, p.pamplemou)
txt_bou_quit = p.police_ui.render("QUIT", True, p.black, p.pamplemou)

txt_bou_res_rect = txt_bou_res.get_rect(center=bout_res.center)
txt_bou_main_rect = txt_bou_main.get_rect(center=bout_main.center)
txt_bou_quit_rect = txt_bou_quit.get_rect(center=bout_quit.center)





def pause() :
    continuer_pause = 1

    while continuer_pause :
        
        for event in py.event.get() :
            
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1 :
                
                pos = mx,my = py.mouse.get_pos()
                
                if bout_res.collidepoint(pos) :  #resume
                    continuer_pause = 0
                    return 1,1
                
                if bout_main.collidepoint(pos) : #acceuil
                    continuer_pause = 0
                    return 0,1
                
                if bout_quit.collidepoint(pos) : #quit
                    continuer_pause = 0
                    py.display.quit()
                    py.quit()
                    sys.exit()
                    return 0,0
                    
                
        
        
        
        py.draw.rect(p.screen,p.black,fen_p)
        py.draw.rect(p.screen,p.pamplemou,bout_res)
        py.draw.rect(p.screen,p.pamplemou,bout_quit)
        py.draw.rect(p.screen,p.pamplemou,bout_main)
        
        p.screen.blit(txt_bou_res,txt_bou_res_rect)
        p.screen.blit(txt_bou_quit,txt_bou_quit_rect)
        p.screen.blit(txt_bou_main,txt_bou_main_rect)
        
        p.screen.blit(title,title_rect)
        py.display.update()
        
        