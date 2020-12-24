import Algorithm as AL 
import time
import numpy as np
import data_utils as du
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import turtle
from random import randint


# 对一致代价搜索进行评估
def evaluateUCS(maze, start, end):
    # # 设置绘图信息
    # scr = turtle.Screen()
    # scr.tracer(0)
    # scr.colormode(255)
    # # 设置窗口大小
    # scr.setup(du.cols_count * du.cell_size, du.rows_count * du.cell_size)

    test = AL.UCS(maze, start, end)
    time = test.search()
    print('UCS time: ', time)
    # 得到输出的路径信息
    x = end
    path = []
    while(x != start):
        #print(x, " " ,end="")
        path.append(x)
        x = test.path[x[0]][x[1]]
    # du.draw_maze(maze, path)
    # scr.tracer(1)
    # input()

def evaluateTWS(maze, start, end):
    # # 设置绘图信息
    # scr = turtle.Screen()
    # scr.tracer(0)
    # scr.colormode(255)
    # # 设置窗口大小
    # scr.setup(du.cols_count * du.cell_size, du.rows_count * du.cell_size)

    test = AL.TWS(maze, start, end)
    time, m = test.search()
    print('TWS time: ', time)
    # 得到输出的路径信息
    x1 = m
    x2 = m
    path1 = []
    path2 = []
    while(x1 != start):
        #print(x1, end="")
        path1.append(x1)
        x1 = test.path1[x1[0]][x1[1]]
    #print('\n')
    while(x2 != end):
        #print(x2, end="")
        path2.append(x2)
        x2 = test.path2[x2[0]][x2[1]]
    # du.draw_maze_double(maze, path1, path2)
    # scr.tracer(1)
    # input()


# 迭代加深搜索进行评估
def evaluateIDS(maze, start, end):
    # # 设置绘图信息
    # scr = turtle.Screen()
    # scr.tracer(0)
    # scr.colormode(255)
    # # 设置窗口大小
    # scr.setup(du.cols_count * du.cell_size, du.rows_count * du.cell_size)

    test = AL.IDS(maze, start, end)
    time = test.Itersearch()
    print('IDS time: ', time)
    # 得到输出的路径信息
    x = end
    path = []
    while(x != start):
        #print(x, " " ,end="")
        path.append(x)
        x = test.path[x[0]][x[1]]
    # du.draw_maze(maze, path)
    # scr.tracer(1)
    # input()

# A星搜索进行评估
def evaluateAstar(maze, start, end):
    # # 设置绘图信息
    # scr = turtle.Screen()
    # scr.tracer(0)
    # scr.colormode(255)
    # # 设置窗口大小
    # scr.setup(du.cols_count * du.cell_size, du.rows_count * du.cell_size)

    test = AL.Astar(maze, start, end)
    test.fillHx_manhadun()
    time = test.search()
    print('Astar time: ', time)
    # 得到输出的路径信息
    x = end
    path = []
    while(x != start):
        #print(x, " " ,end="")
        path.append(x)
        x = test.path[x[0]][x[1]]
    # du.draw_maze(maze, path)
    # scr.tracer(1)
    # input()

def evaluateIDAstar(maze, start, end, fx_type):
    # # 设置绘图信息
    # scr = turtle.Screen()
    # scr.tracer(0)
    # scr.colormode(255)
    # # 设置窗口大小
    # scr.setup(du.cols_count * du.cell_size, du.rows_count * du.cell_size)

    test = AL.IDAstar(maze, start, end)
    time = test.Itersearch(fx_type)
    print('IDAstar time: ', time)
    # 得到输出的路径信息
    x = end
    path = []
    while(x != start):
        # print(x, " " ,end="")
        path.append(x)
        x = test.path[x[0]][x[1]]
    # du.draw_maze(maze, path)
    # scr.tracer(1)
    # input()

if __name__ == "__main__":
    maze = du.loadData('MazeData.txt')
    start, end = du.getStartAndEnd(maze)
    # 对每一个算法进行评估
    evaluateUCS(maze, start, end)
    evaluateIDS(maze, start, end)
    evaluateTWS(maze, start, end)
    evaluateAstar(maze, start ,end)
    evaluateIDAstar(maze, start, end, 'manhadun')
    # evaluateIDAstar(maze ,start, end, 'duijiaoxian')

