
#Tower Of Hanoi Game
class TowerOfHanoi:
    def __init__(self,start,Aux,end):
        self.Start = start
        self.Auxillary = Aux
        self.End = end
    def PushFromStartPopInAuxillary(self):
        if self.Start != []:
            value=self.Start.pop()
            if self.Auxillary == []:
                self.Auxillary.append(value)
            elif self.Auxillary != [] and value < self.Auxillary[-1]:
                self.Auxillary.append(value)
            else:
                self.Start.append(value)
                return -1
        else:
            return -1
    def PushFromStartPopInEnd(self):
        if self.Start != []:
            value=self.Start.pop()
            if self.End == []:
                self.End.append(value)
            elif self.End != [] and value < self.End[-1]:
                self.End.append(value)
            else:
                self.Start.append(value)
                return -1
        else:
            return -1
    def PushFromAuxillaryPopInStart(self):
        if self.Auxillary != []:
            value=self.Auxillary.pop()
            if self.Start == []:
                self.Start.append(value)
            elif self.Start != [] and value < self.Start[-1]:
                self.Start.append(value)
            else:
                self.Auxillary.append(value)
                return -1
        else:
            return -1
    def PushFromAuxillaryPopInEnd(self):
        if self.Auxillary != []:
            value=self.Auxillary.pop()
            if self.End == []:
                self.End.append(value)
            elif self.End != [] and value < self.End[-1]:
                self.End.append(value)
            else:
                self.Auxillary.append(value)
                return -1
        else:
            return -1
    def PushFromEndPopInStart(self):
        if self.End != []:
            value=self.End.pop()
            if self.Start == []:
                self.Start.append(value)
            elif self.Start != [] and value < self.Start[-1]:
                self.Start.append(value)
            else:
                self.End.append(value)
                return -1
        else:
            return -1
    def PushFromEndPopInAuxillary(self):
        if self.End != []:
            value=self.End.pop()
            if self.Auxillary == []:
                self.Auxillary.append(value)
            elif self.Auxillary != [] and value < self.Auxillary[-1]:
                self.Auxillary.append(value)
            else:
                self.End.append(value)
                return -1
        else:
            return -1
    def Status(self):
        print("Start:",self.Start)
        print("Auxillary",self.Auxillary)
        print("End",self.End)
    


#Greedy best first search on Tower Of Hanoi
class GreedyBFS_Node(TowerOfHanoi):
    def __init__(self,start,Aux,end):
        TowerOfHanoi.__init__(self,start,Aux,end)
    def Heuristic(self,node):
        heur_value = 10
        if len(node[-1])==3:
            if node[-1][0]==3 and node[-1][1]==2 and node [-1][2]==1:
                heur_value = 0
        elif len(node[-1])==2:
            if node[-1][0]==3 and node[-1][1]==2:
                heur_value = 1
        elif len(node[-1])==1:
            if node[-1][0]==3:
                heur_value = 2
        return heur_value
    def Child(self):
        path = []
        queue=[]
        TempPath=[]
        n=GreedyBFS_Node(self.Start,self.Auxillary,self.End)
        
        path.append([n.Start,n.Auxillary,n.End])
        TempPath.append([n.Start,n.Auxillary,n.End])

        queue.append([path,self.Heuristic(path[-1])])

        
        while True:
            path = []
            node=queue.pop(0)
            s=node[0][-1]
            print(s)
            
            lst=[]
            for i in range(6):
                lst.append([s[0].copy(),s[1].copy(),s[2].copy()])
                
            if self.CheckGoalState(s):
                break
            
            
            n1=GreedyBFS_Node(lst[0][0],lst[0][1],lst[0][2])
            
            if n1.PushFromStartPopInAuxillary() != -1:
                if [n1.Start,n1.Auxillary,n1.End] not in TempPath:
                    path.append([n1.Start,n1.Auxillary,n1.End])
                    TempPath.append([n1.Start,n1.Auxillary,n1.End])
       

            n2=GreedyBFS_Node(lst[1][0],lst[1][1],lst[1][2])
            if n2.PushFromStartPopInEnd() != -1:
                if [n2.Start,n2.Auxillary,n2.End] not in TempPath:
                    path.append([n2.Start,n2.Auxillary,n2.End])
                    TempPath.append([n2.Start,n2.Auxillary,n2.End])

            
            n3=GreedyBFS_Node(lst[2][0],lst[2][1],lst[2][2])
            if n3.PushFromAuxillaryPopInStart() != -1:
                if [n3.Start,n3.Auxillary,n3.End] not in TempPath:
                    path.append([n3.Start,n3.Auxillary,n3.End])
                    TempPath.append([n3.Start,n3.Auxillary,n3.End])

            
            n4=GreedyBFS_Node(lst[3][0],lst[3][1],lst[3][2])
            if n4.PushFromAuxillaryPopInEnd() != -1:
                if [n4.Start,n4.Auxillary,n4.End] not in TempPath:
                    path.append([n4.Start,n4.Auxillary,n4.End])
                    TempPath.append([n4.Start,n4.Auxillary,n4.End])
                                

            n5=GreedyBFS_Node(lst[4][0],lst[4][1],lst[4][2])
            if n5.PushFromEndPopInStart() != -1:
                if [n5.Start,n5.Auxillary,n5.End] not in TempPath:
                    path.append([n5.Start,n5.Auxillary,n5.End])
                    TempPath.append([n5.Start,n5.Auxillary,n5.End])
                
                
            n6=GreedyBFS_Node(lst[5][0],lst[5][1],lst[5][2])
            if n6.PushFromEndPopInAuxillary() != -1:
                if [n6.Start,n6.Auxillary,n6.End] not in TempPath:
                    path.append([n6.Start,n6.Auxillary,n6.End])
                    TempPath.append([n6.Start,n6.Auxillary,n6.End])
            queue.append([path,self.Heuristic(path[-1])])
            queue.sort(key=lambda x:x[0][-1])
            
            
    def CheckGoalState(self,mylist):
        if mylist[0]==[] and mylist[1] ==[] and mylist[2]==[3,2,1]:
            return True
        return False
        



if __name__ == "__main__":
    print("\n......Greedy best first search......")
    g=GreedyBFS_Node([3,2,1],[],[])
    g.Child()
    print("\n\n")
    
