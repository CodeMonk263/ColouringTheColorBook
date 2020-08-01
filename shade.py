import pygame
from algo import Scan
import time

##Shade class for filling inside given figure
class Shade():
    ##Initialize all variables
    def __init__(self,origin,grid,color_sel,origin_color,rows,cols):
        self.origin = origin
        self.grid = grid
        self.color_sel = color_sel
        self.origin_color = origin_color
        self.agendas = {"1":[],"-1":[]}
        self.ver_dir = 1
        self.ch_ver_dir = False
        self.lines = None

    ##Pause function for step by step debugging
    def pause(self):
        programPause = input("Press the <ENTER> key to continue...")

    ##Returns the beginning, end and change value required for a range for given list
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

    ## main shade function
    def shade(self):
        self.initialize_agendas()
        while(len(self.agendas[str(self.ver_dir)]) or len(self.agendas[str(-self.ver_dir)])):
            if (not len(self.agendas[str(self.ver_dir)])):
                self.ver_dir = -self.ver_dir
                self.ch_ver_dir = True
            begin, end, ch = self.getParams(len(self.agendas[str(self.ver_dir)]), self.ver_dir)
            if (len(self.agendas[str(self.ver_dir)])):
                i = begin
                if (not self.ch_ver_dir):
                    while (begin <= i < end):
                        self.shade_vert(self.agendas[str(self.ver_dir)].pop(i))
                        begin, end, ch = self.getParams(len(self.agendas[str(self.ver_dir)]),self.ver_dir)
                        i += ch
                else:
                    while (begin >= i > end):
                        self.shade_vert(self.agendas[str(self.ver_dir)].pop(i))
                        begin,end,ch = self.getParams(len(self.agendas[str(self.ver_dir)]),self.ver_dir)
                        i += ch
    
    ## initializes agendas for first scans
    def initialize_agendas(self):
        scan = Scan(self.origin, self.grid)    #Create scan object for getting lines to be shaded using dfs
        self.lines = scan.main()
        for i in range(len(self.lines)):
            if (self.lines[i][0] == self.origin.row):
                self.agendas[str(self.ver_dir)].append(self.lines[i:])   #all lines after the origin are in the UPward section of agenda
                self.agendas[str(-self.ver_dir)].append(self.lines[:i])  #all lines before the origin are in the DOWNward section of agenda
            i = len(self.lines)
        del scan   
    
    ## vertical shade scan function
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

    ## horizontal shade function for coloring given line
    def shade_hor(self,shade_line):
        time.sleep(0.05)  #added time delay so that we can see shading of each line
        for i in range(shade_line[1],shade_line[2]+1):
            point = self.grid.getGrid()[i][shade_line[0]]
            point.click(self.grid.screen, self.color_sel)
            pygame.display.update()
        

