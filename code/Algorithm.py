import data_utils
import numpy as np
import time

# 一致代价搜索的实现，在这种情况下相当于BFS
class UCS(object):
    # 初始化步骤
    def __init__(self, maze, start, end):
        '''
        参数说明：
        maze：用于存储迷宫图
        is_visited：用于记录迷宫的位置是否被访问过
        reached：标记是否到达终点
        start：迷宫的起点
        end：迷宫的终点
        path：用于存储路径的列表
        '''
        self.maze = maze
        self.start = start
        self.end = end
        self.is_visited = np.array([[False for i in range(len(maze[0]))] for j in range(len(maze))])
        self.reached = False
        self.path = list([[(0,0) for i in range(len(maze[0]))] for j in range(len(maze))])
    # 一致代价搜索的距离
    def distance(self, pre_point, point):
        return np.sqrt(np.square(point[0]-pre_point[0]) + np.square(point[1]-pre_point[1]))
    
    # 判断当前位置是否可行
    def cond(self, x, y):
        # 如果当前位置是墙壁，则不可行
        if self.maze[x][y] == '1':
            return False
        # 如果当前位置被访问过，则不可行：
        if self.is_visited[x][y] == True:
            return False
        # 如果当前位置超出迷宫范围，则不可行
        if x < 0 or y < 0:
            return False
        if x > len(self.maze) or y > len(self.maze[0]):
            return False
        return True

    # 一致代价搜索过程   
    def search(self):
        '''
            对当前的位置进行搜索
        '''
        start_time = time.time()
        x = self.start[0]
        y = self.start[1]
        
        # 一个队列，作用是实现BFS的功能
        queue = []
        queue.append((x,y))
        while(len(queue) > 0):
            m = queue.pop(0)
            # self.path.append(m)
            # 将当前位置标记为已被访问
            self.is_visited[m[0]][m[1]] = 1
            # 如果当前位置是终点，那么就可以结束搜索过程
            if m[0] == self.end[0] and m[1] == self.end[1]:
                self.reached = True
                break
            node = []
            if self.reached == False:
                if self.cond(m[0]-1,m[1]):
                    node.append((m[0]-1,m[1]))
                    self.path[m[0]-1][m[1]] = m
                if self.cond(m[0],m[1]-1):
                    node.append((m[0],m[1]-1))
                    self.path[m[0]][m[1]-1] = m
                if self.cond(m[0]+1,m[1]):
                    node.append((m[0]+1,m[1]))
                    self.path[m[0]+1][m[1]] = m
                if self.cond(m[0],m[1]+1):
                    node.append((m[0],m[1]+1))
                    self.path[m[0]][m[1]+1] = m
            sorted(node, key=lambda p:(self.distance((m[0],m[1]),p), 1))
            for item in node:
                queue.append(item)
        end_time = time.time()
        return end_time - start_time
            #print(queue)
            #print(m)


# 双向搜索的实现
class TWS(object):
    # 初始化步骤
    def __init__(self, maze, start, end):
        '''
        参数说明：
        maze：用于存储迷宫图
        is_visited：用于记录迷宫的位置是否被访问过
        reached：标记是否到达终点
        start：迷宫的起点
        end：迷宫的终点
        path：用于存储路径的列表
        '''
        self.maze = maze
        self.start = start
        self.end = end
        self.is_visited = np.array([[False for i in range(len(maze[0]))] for j in range(len(maze))])
        self.reached = False
        self.path1 = list([[(0,0) for i in range(len(maze[0]))] for j in range(len(maze))])
        self.path2 = list([[(0,0) for i in range(len(maze[0]))] for j in range(len(maze))])
    
    # 判断当前位置是否可行
    def cond(self, x, y):
        # 如果当前位置是墙壁，则不可行
        if self.maze[x][y] == '1':
            return False
        # 如果当前位置被访问过，则不可行：
        if self.is_visited[x][y] == True:
            return False
        # 如果当前位置超出迷宫范围，则不可行
        if x < 0 or y < 0:
            return False
        if x > len(self.maze) or y > len(self.maze[0]):
            return False
        return True

    def search(self):
        '''
            对当前的位置进行搜索
        '''
        start_time = time.time()
        x1 = self.start[0]
        y1 = self.start[1]
        x2 = self.end[0]
        y2 = self.end[1]
        
        # 一个队列，作用是实现BFS的功能
        queue1 = []
        queue2 = []
        queue1.append((x1,y1))
        queue2.append((x2,y2))
        while(len(queue1) > 0 and len(queue2) > 0):
            m1 = queue1.pop(0)
            m2 = queue2.pop(0)
            #print(m1, m2)
            if(m1 == m2):
                self.reached = True
                break
            if(len(queue2) and m1 == queue2[0]):
                self.reached = True
                break
            if(len(queue1) and m2 == queue1[0]):
                self.reached = True
                break
            # if(len(queue1) and len(queue2)):
            #     print(m1 ,m2 ,queue1[0], queue2[0])

            # 将当前位置标记为已被访问
            self.is_visited[m1[0]][m1[1]] = 1
            self.is_visited[m2[0]][m2[1]] = 1

            node = []
            if self.reached == False:
                if self.cond(m1[0]-1,m1[1]):
                    node.append((m1[0]-1,m1[1]))
                    self.path1[m1[0]-1][m1[1]] = m1
                if self.cond(m1[0],m1[1]-1):
                    node.append((m1[0],m1[1]-1))
                    self.path1[m1[0]][m1[1]-1] = m1
                if self.cond(m1[0]+1,m1[1]):
                    node.append((m1[0]+1,m1[1]))
                    self.path1[m1[0]+1][m1[1]] = m1
                if self.cond(m1[0],m1[1]+1):
                    node.append((m1[0],m1[1]+1))
                    self.path1[m1[0]][m1[1]+1] = m1
            for item in node:
                queue1.append(item)
            
            node = []
            if self.reached == False:
                if self.cond(m2[0]-1,m2[1]):
                    node.append((m2[0]-1,m2[1]))
                    self.path2[m2[0]-1][m2[1]] = m2
                if self.cond(m2[0],m2[1]-1):
                    node.append((m2[0],m2[1]-1))
                    self.path2[m2[0]][m2[1]-1] = m2
                if self.cond(m2[0]+1,m2[1]):
                    node.append((m2[0]+1,m2[1]))
                    self.path2[m2[0]+1][m2[1]] = m2
                if self.cond(m2[0],m2[1]+1):
                    node.append((m2[0],m2[1]+1))
                    self.path2[m2[0]][m2[1]+1] = m2
            for item in node:
                queue2.append(item)
            # print('queue1:', queue1)
            # print('queue2:', queue2)
        end_time = time.time()
        return end_time - start_time, m1

# 迭代加深搜索的实现
class IDS(object):
    # 初始化部分
    '''
        参数说明：
        path为路径存储
        depth为迭代加深搜索的深度
    '''
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.reached = False
        self.path = list([[(0,0) for i in range(len(maze[0]))] for j in range(len(maze))])
        self.depth = 1
    
    # 判断当前位置是否可行
    def cond(self, x, y, m):
        # 如果当前位置是墙壁，则不可行
        if self.maze[x][y] == '1':
            return False
        # 如果当前位置超出迷宫范围，则不可行
        if x < 0 or y < 0:
            return False
        if x > len(self.maze) or y > len(self.maze[0]):
            return False
        
        t = m
        while(t != self.start):
            #print(t, end="")
            t = self.path[t[0]][t[1]]
            if t[0] == x and t[1] == y:
                return False

        return True


    # 单个搜索部分
    def search(self, x, y, depth):
        #print(self.path)
        if(x == self.end[0] and y == self.end[1]):
            self.reached = True
            return

        if(depth <= self.depth):
            if(self.cond(x+1, y, (x,y)) and self.reached == False):
                self.path[x+1][y] = (x,y)
                self.search(x+1, y, depth+1)
            if(self.cond(x-1,y, (x,y)) and self.reached == False):
                self.path[x-1][y] = (x,y)
                self.search(x-1, y, depth+1)
            if(self.cond(x,y-1, (x,y)) and self.reached == False):
                self.path[x][y-1] = (x,y)
                self.search(x, y-1, depth+1)
            if(self.cond(x,y+1, (x,y)) and self.reached == False):
                self.path[x][y+1] = (x,y)
                self.search(x,y+1, depth+1)
                

        return
    
    # 综合迭代加深搜索部分
    def Itersearch(self):
        start_time = time.time()
        x = self.start[0]
        y = self.start[1]
        
        depth = 1
        while(self.reached == False and self.depth <= 100):
            self.path = list([[(0,0) for i in range(len(self.maze[0]))] for j in range(len(self.maze))])
            # print(self.depth)
            self.search(x, y, depth)
            # print(self.path)
            self.depth += 1

        # self.depth = 2
        # self.search(x,y,depth)
        
        # print(self.depth, self.reached)
        # print(self.path)
        
        end_time = time.time()
        return end_time - start_time
    

# A星搜索的实现
class Astar(object):
    # 初始化实现
    def __init__(self, maze, start, end):
        '''
            参数说明
            gx为初始节点到当前节点的实际代价
            hx为当前节点到最终节点的估计代价
        '''
        self.maze = maze
        self.start = start
        self.end = end
        self.is_visited = np.array([[False for i in range(len(maze[0]))] for j in range(len(maze))])
        self.reached = False
        self.path = list([[(0,0) for i in range(len(maze[0]))] for j in range(len(maze))])
        self.gx = list([[0 for i in range(len(maze[0]))] for j in range(len(maze))])
        self.hx = list([[0 for i in range(len(maze[0]))] for j in range(len(maze))])
    
    # 判断当前位置是否可行
    def cond(self, x, y):
        # 如果当前位置是墙壁，则不可行
        if self.maze[x][y] == '1':
            return False
        # 如果当前位置被访问过，则不可行：
        if self.is_visited[x][y] == True:
            return False
        # 如果当前位置超出迷宫范围，则不可行
        if x < 0 or y < 0:
            return False
        if x > len(self.maze) or y > len(self.maze[0]):
            return False
        return True

    # 填充hx表，使用曼哈顿距离
    def fillHx_manhadun(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                self.hx[i][j] = np.abs(i-self.end[0])+np.abs(j-self.end[1])
    
    # 填充hx表，使用对角线距离
    def fillHx_duijiaoxian(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                self.hx[i][j] = np.sqrt(np.square(i-self.end[0]) + np.square(j-self.end[1]))

    # 找到当前队列中启发式函数最小的元素的下标      
    def findMinIdx(self, queue):
        MIN = 1000
        idx = -1
        for ide in range(len(queue)):
            c = queue[ide]
            if (self.gx[c[0]][c[1]] + self.hx[c[0]][c[1]]) <= MIN:
                MIN = self.gx[c[0]][c[1]] + self.hx[c[0]][c[1]]
                idx = ide
        
        return idx
    
    # A星搜索的主要部分
    def search(self):
        start_time = time.time()
        x = self.start[0]
        y = self.start[1]
        self.gx[x][y] = 0
        
        # 一个队列，作用是实现BFS的功能
        queue = []
        queue.append((x,y))
        while(len(queue) > 0):
            c = self.findMinIdx(queue)
            m = queue.pop(c)
            # self.path.append(m)
            # 将当前位置标记为已被访问
            self.is_visited[m[0]][m[1]] = 1
            # 如果当前位置是终点，那么就可以结束搜索过程
            if m[0] == self.end[0] and m[1] == self.end[1]:
                self.reached = True
                break
            node = []
            if self.reached == False:
                if self.cond(m[0]-1,m[1]):
                    node.append((m[0]-1,m[1]))
                    self.path[m[0]-1][m[1]] = m
                    self.gx[m[0]-1][m[1]] = self.gx[m[0]][m[1]] + 1
                if self.cond(m[0],m[1]-1):
                    node.append((m[0],m[1]-1))
                    self.path[m[0]][m[1]-1] = m
                    self.gx[m[0]][m[1]-1] = self.gx[m[0]][m[1]] + 1
                if self.cond(m[0]+1,m[1]):
                    node.append((m[0]+1,m[1]))
                    self.path[m[0]+1][m[1]] = m
                    self.gx[m[0]+1][m[1]] = self.gx[m[0]][m[1]] + 1
                if self.cond(m[0],m[1]+1):
                    node.append((m[0],m[1]+1))
                    self.path[m[0]][m[1]+1] = m
                    self.gx[m[0]][m[1]+1] = self.gx[m[0]][m[1]] + 1

            for item in node:
                queue.append(item)
        end_time = time.time()
        return end_time - start_time


class IDAstar(object):
    # 初始化
    def __init__(self, maze, start, end):
        '''
            参数说明
            path存储路径信息
        '''
        self.maze = maze
        self.start = start
        self.end = end
        self.reached = False
        self.path = list([[(0,0) for i in range(len(maze[0]))] for j in range(len(maze))])
        self.depth = 1  
        self.bound = (np.abs(start[0]-end[0]) + np.abs(start[1]-end[1])) * 2

    # 判断当前位置是否可行
    def cond(self, x, y, m):
        # 如果当前位置是墙壁，则不可行
        if self.maze[x][y] == '1':
            return False
        # 如果当前位置超出迷宫范围，则不可行
        if x < 0 or y < 0:
            return False
        if x > len(self.maze) or y > len(self.maze[0]):
            return False
        
        # 如果当前位置已经在以前的路径中被访问，则不可行
        t = m
        while(t != self.start):
            #print(t, end="")
            t = self.path[t[0]][t[1]]
            if t[0] == x and t[1] == y:
                return False

        return True


    # 计算当前位置的启发式函数的值,使用曼哈顿距离
    def fx1(self, x, y, depth):
        return np.abs(x-self.end[0]) + np.abs(y-self.end[1]) + depth-1
    
    # 计算当前位置的启发是函数的值，使用对角线距离
    def fx2(self, x, y, depth):
        return np.sqrt(np.square(x-self.end[0]) + np.square(y-self.end[1])) + depth-1

    def cmp1(self, a):
        return self.fx1(a[0], a[1], 0)
    def cmp2(self, a):
        return self.fx2(a[0], a[1], 0)

    # 根据启发式函数的值对四个方向的优先级进行排序，并去掉大于阈值的方向
    def fx2idx(self, x, y, depth, fx_type):
        arr = []
        if(fx_type == 'manhadun'):
            if(self.fx1(x+1, y, depth) <= self.bound):
                arr.append((x+1, y))
            if(self.fx1(x-1, y, depth) <= self.bound):
                arr.append((x-1,y))
            if(self.fx1(x, y+1, depth) <= self.bound):
                arr.append((x,y+1))
            if(self.fx1(x, y-1, depth) <= self.bound):
                arr.append((x,y-1))
            arr.sort(key=lambda x:self.cmp1(x))
        elif(fx_type == 'duijiaoxian'):
            if(self.fx2(x+1, y, depth) <= self.bound):
                arr.append((x+1, y))
            if(self.fx2(x-1, y, depth) <= self.bound):
                arr.append((x-1,y))
            if(self.fx2(x, y+1, depth) <= self.bound):
                arr.append((x,y+1))
            if(self.fx2(x, y-1, depth) <= self.bound):
                arr.append((x,y-1))
            arr.sort(key=lambda x:self.cmp2(x))
        
        return arr
        
        

    # 单个搜索部分
    def search(self, x, y, depth, fx_type):
        #print(self.bound)
        #print(self.path)
        if(x == self.end[0] and y == self.end[1]):
            self.reached = True
            return

        if(depth <= self.depth):
            arr = self.fx2idx(x, y, depth, fx_type)
            for item in arr:
                if(self.cond(item[0], item[1], (x,y)) and self.reached == False):
                    self.path[item[0]][item[1]] = (x,y)
                    self.search(item[0], item[1], depth+1, fx_type)

            # if(self.cond(x+1, y, (x,y)) and self.reached == False):
            #     self.path[x+1][y] = (x,y)
            #     self.search(x+1, y, depth+1)
            # if(self.cond(x-1,y, (x,y)) and self.reached == False):
            #     self.path[x-1][y] = (x,y)
            #     self.search(x-1, y, depth+1)
            # if(self.cond(x,y-1, (x,y)) and self.reached == False):
            #     self.path[x][y-1] = (x,y)
            #     self.search(x, y-1, depth+1)
            # if(self.cond(x,y+1, (x,y)) and self.reached == False):
            #     self.path[x][y+1] = (x,y)
            #     self.search(x,y+1, depth+1)
                

        return
    
    # 综合迭代加深搜索部分
    def Itersearch(self, fx_type):
        start_time = time.time()
        x = self.start[0]
        y = self.start[1]
        
        depth = 1
        # while(self.reached == False and self.depth <= 100):
        #     self.path = list([[(0,0) for i in range(len(self.maze[0]))] for j in range(len(self.maze))])
        #     # print(self.depth)
        #     self.search(x, y, depth, fx_type)
        #     # print(self.path)
        #     self.depth += 1
        #     print(self.depth, self.reached)
        self.depth = 69
        self.search(x, y, depth, fx_type)
        # print(self.path)
        # self.depth = 2
        # self.search(x,y,depth)
        
        # print(self.depth, self.reached)
        # print(self.path)
        
        end_time = time.time()
        return end_time - start_time
