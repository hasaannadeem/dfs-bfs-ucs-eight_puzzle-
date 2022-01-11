from copy import deepcopy
goal = [[1,2,3],[4,5,6],[7,8,0]]
arr = [[1,2,3],[4,5,6],[7,0,8]]

class bfs:
    list = []
    explore = []
    def nqueue(self,input):
        self.list.append(input);

    def dqueue(self):
        try:
            temp = self.list.pop(0)
            return temp
        except:
            return None

    def explored(self,input):
        self.explore.append(input)

    def check_explored(self,input):
        for col in range(len(self.explore)):
            if(self.goal_check(input,self.explore[col])):
                return True
        return False

    def display(self):
        for col in range(len(self.list)):
            for row in range(len(self.list[col])):
                print(self.list[col][row])
            print()
            
    def goal_check(self,a,b):
        for col in range(len(a)):
            for row in range(len(a[col])):
                if(a[col][row] != b[col][row]):
                    return False
        return True

    def move_up(self,input1,col,row):
        input = deepcopy(input1)
        if(col != 0):
            temp = input[col -1][row]
            input[col - 1][row] = 0
            input[col][row] = temp
            self.nqueue(deepcopy(input))
        
    def move_down(self,input1,col,row):
        input = deepcopy(input1)
        if(col != 2):
            temp = input[col + 1][row]
            input[col + 1][row] = 0
            input[col][row] = temp
            self.nqueue(deepcopy(input))

    def move_left(self,input1,col,row):
        input = deepcopy(input1)
        if(row != 0):
            temp = input[col][row-1]
            input[col][row - 1] = 0
            input[col][row] = temp
            self.nqueue(deepcopy(input))

    def move_right(self,input1,col,row):
        input = deepcopy(input1)
        if(row != 2):
            temp = input[col][row+1]
            input[col][row+1] = 0
            input[col][row] = temp
            self.nqueue(deepcopy(input))


    def move(self,input):
        temp_col = 0
        temp_row = 0
        for col in range(len(input)):
            for row in range(len(input[col])):
                if(input[col][row] == 0 ):
                    temp_col = col
                    temp_row = row 
        self.move_down(input,temp_col,temp_row)
        self.move_up(input,temp_col,temp_row)
        self.move_left(input,temp_col,temp_row)
        self.move_right(input,temp_col,temp_row)



    def start(self,start_point):
        while (True):
            print("Exploring = ",start_point)
            if(self.goal_check(goal,start_point)):
                print("goal found.")
                break
            if(not self.check_explored(start_point)):
                self.move(start_point)
            
            self.explored(start_point)
            start_point = self.dqueue()
            if(start_point == None):
                print("dqueue error")
                break


a = bfs()
a.start(arr)
