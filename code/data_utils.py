'''
    头文件部分，
    numpy对数组进行操作
    time对算法的时间性能进行评估
    turtle对得到的路径进行可视化操作
'''
import numpy as np
import time
import turtle
from random import randint


rows_count = 18
cols_count = 36
cell_size = 20



# 数据的读取部分，从txt文件中读取迷宫数据到np数组中
def loadData(File_name):
    with open(File_name, 'r') as file:
        data = []
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            data.append(list(line))
    data = np.array(data)
    return data

# 得到迷宫的出入口的位置，用一个元组保存，位置信息也是一个元组
def getStartAndEnd(data):
    start = None
    end = None
    for i in range(len(data)):
        for j in range(len(data[i])):
            if(data[i][j] == 'S'):
                start = (i,j)
            if(data[i][j] == 'E'):
                end = (i,j)
    
    return (start, end)

# 显示地图（图形化显示）
def draw_maze(list_maze, path):
    t_cell = turtle.Turtle()
    t_cell.hideturtle()
    for ri in range(len(list_maze)):
        for ci in range(len(list_maze[0])):
            # 如果为墙则画灰色正方形
            if list_maze[ri][ci] in ['1', '2']:
                draw_cell(ci, ri, t_cell)
            # 如果为起点,则返回全局变量,同时标记为青色点
            elif list_maze[ri][ci] == 'S':
                draw_dot(ci, ri, 'cyan', t_cell)
            # 如果为终点,则标记红点
            elif list_maze[ri][ci] == 'E':
                draw_dot(ci, ri, 'red', t_cell)
    for ri in range(len(path)):
        draw_dot(path[ri][1], path[ri][0], 'blue', t_cell)

# 显示地图（图形化显示,这个部分用于双向搜索）
def draw_maze_double(list_maze, path1, path2):
    t_cell = turtle.Turtle()
    t_cell.hideturtle()
    for ri in range(len(list_maze)):
        for ci in range(len(list_maze[0])):
            # 如果为墙则画灰色正方形
            if list_maze[ri][ci] in ['1', '2']:
                draw_cell(ci, ri, t_cell)
            # 如果为起点,则返回全局变量,同时标记为青色点
            elif list_maze[ri][ci] == 'S':
                draw_dot(ci, ri, 'cyan', t_cell)
            # 如果为终点,则标记红点
            elif list_maze[ri][ci] == 'E':
                draw_dot(ci, ri, 'red', t_cell)
    for ri in range(len(path1)):
        draw_dot(path1[ri][1], path1[ri][0], 'blue', t_cell)
    for ri in range(len(path2)):
        draw_dot(path2[ri][1], path2[ri][0], 'yellow', t_cell)

# 用于将turtle画笔跳转到特定位置
def skip_to(x, y, pen):
    """turtle跳跃至指定坐标点"""
    pen.up()
    pen.goto(x, y)
    pen.down()


# 用于绘制迷宫的墙壁
def draw_cell(ci, ri, t_cell):
    # cell_size为主程序变量,代表迷宫图形中一个单元格的像素尺寸,(x,y)分别为单元格的左上角坐标
    x, y = (ci - cols_count * 0.5) * cell_size, (rows_count * 0.5 - ri) * cell_size
    skip_to(x, y, t_cell)
    # 随机颜色,RGB需要一致,否则可能不是灰色
    n = randint(110, 150)
    t_cell.color((n, n, n), (n, n, n))
    t_cell.begin_fill()
    for _ in range(4):
        t_cell.forward(cell_size)
        t_cell.right(90)
    t_cell.end_fill()


# 用于绘制迷宫的路径
def draw_dot(ci, ri, color, t_cell):
    # cell_size为主程序变量,代表迷宫图形中一个单元格的像素尺寸,(x,y)分别为单元格的左上角坐标向右下方偏移cell_size*0.5,即x+0.5,y-0.5
    x, y = (ci - cols_count * 0.5) * cell_size + cell_size * 0.5, (rows_count * 0.5 - ri) * cell_size - cell_size * 0.5
    skip_to(x, y, t_cell)
    t_cell.dot(int(cell_size * 0.5), color)
