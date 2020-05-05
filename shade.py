import pygame
from algo import Scan
import time

class Shade():
    def __init__(self,origin,grid,color_sel,origin_color,rows,cols):
        self.origin = origin
        self.grid = grid
        self.color_sel = color_sel
        self.origin_color = origin_color
        self.agendas = {"1":[],"-1":[]}
        self.ver_dir = 1
        self.ch_ver_dir = False
        self.lines = None

    def pause(self):
        programPause = input("Press the <ENTER> key to continue...")

    def getParams(self,len_list,ver_dir):
        if (ver_dir == 1):
            begin = 0
            end = len_list
            ch = 1
        else:
            begin = len_list-1
            end = -1
            ch = -1
        return begin,end,ch

    def shade(self):
        self.initialize_agendas()
        while(len(self.agendas[str(self.ver_dir)]) or len(self.agendas[str(-self.ver_dir)])):
            if (not len(self.agendas[str(self.ver_dir)])):
                self.ver_dir = -self.ver_dir
                self.ch_ver_dir = True
            begin,end,ch = self.getParams(len(self.agendas[str(self.ver_dir)]),self.ver_dir)
            if (len(self.agendas[str(self.ver_dir)])):
                for i in range(begin,end,ch):
                    self.shade_vert(self.agendas[str(self.ver_dir)][i]) #.pop(i))
                    x = self.agendas[str(self.ver_dir)].pop(i)
                    print (x)   
    def initialize_agendas(self):
        scan = Scan(self.origin, self.grid)
        self.lines = scan.main()
        for i in range(len(self.lines)):
            if (self.lines[i][0] == self.origin.row):
                self.agendas[str(self.ver_dir)].append(self.lines[i:])
                self.agendas[str(-self.ver_dir)].append(self.lines[:i])
            i = len(self.lines)
        del scan
    
    def shade_vert(self,ver_scan):
        shade_lines = ver_scan
        agenda_temp = []
        begin,end,ch = self.getParams(len(shade_lines),self.ver_dir)
        for i in range(begin,end,ch):
            if (i > 0 and shade_lines[i][0] == shade_lines[i-1][0]):
                agenda_temp.append(shade_lines[i])
            else:
                self.shade_hor(shade_lines[i])
        if (len(agenda_temp)):
            if (ch == 1):
                agenda_temp.reverse()
            self.agendas[str(self.ver_dir)].append(agenda_temp)

    def shade_hor(self,shade_line):
        time.sleep(0.2)
        for i in range(shade_line[1],shade_line[2]+1):
            point = self.grid.getGrid()[i][shade_line[0]]
            point.click(self.grid.screen, self.color_sel)
            pygame.display.update()
        

