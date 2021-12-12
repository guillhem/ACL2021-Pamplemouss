# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 14:40:44 2021

@author: sabri
"""
import pygame as py
import param as p



size_p = 400,400
size_b = width, height = 150,80
#%% fenetre
fen_p = py.Rect((330,330),size_p)
fen_p.center = p.rectScreen.center

#%% boutons

bout_res = py.Rect((260,260),size_b)
bout_quit = py.Rect((260,380),size_b)
# bout_save = py.Rect(430,630,size_b)

#%%

title = p.police_deb.render("PAUSE", True, p.pamplemou)
title_rect = title.get_rect()
title_rect.topleft = fen_p.topleft

txt_bou_res = p.police_ui.render("RESUME", True, p.black, p.pamplemou)
txt_bou_quit = p.police_ui.render("MAIN MENU", True, p.black, p.pamplemou)

txt_bou_res_rect = txt_bou_res.get_rect(center=bout_res.center)
txt_bou_quit_rect = txt_bou_quit.get_rect(center=bout_quit.center)





def pause() :
    continuer_pause = 1

    while continuer_pause :
        
        for event in py.event.get() :
            
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1 :
                
                pos = mx,my = py.mouse.get_pos()
                
                if bout_res.collidepoint(pos) :  #resume
                    continuer_pause = 0
                    return 1
                
                if bout_quit.collidepoint(pos) : #quit
                    continuer_pause = 0
                    return 0
        
        
        
        
        
        py.draw.rect(p.screen,p.black,fen_p)
        py.draw.rect(p.screen,p.pamplemou,bout_res)
        py.draw.rect(p.screen,p.pamplemou,bout_quit)
        
        p.screen.blit(txt_bou_res,txt_bou_res_rect)
        p.screen.blit(txt_bou_quit,txt_bou_quit_rect)
        
        p.screen.blit(title,title_rect)
        py.display.update()
        
        