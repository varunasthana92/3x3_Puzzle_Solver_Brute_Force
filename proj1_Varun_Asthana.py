import numpy as np

# defining all possible action set for each position of blank tile
def action(zeroPos):
    actions= {0: np.array([1,3]), 1: np.array([0,2,4]), 2: np.array([1,5]),
          3: np.array([0,4,6]), 4: np.array([1,3,5,7]), 5: np.array([2,4,8]),
          6: np.array([3,7]), 7: np.array([4,6,8]), 8: np.array([5,7]),
         }
    return actions[zeroPos]

# Node class to store data of Node's state, ownID and parentID
class Node():
    # Initialize class object
    def __init__(self, stateData, oID):
        self.state= stateData
        self.pID= 0
        self.ownID= oID

# allNodes class to store data of each object of class Node
class allNodes():
    # Initialize class object
    def __init__(self):
        self.allNodesData=[]
    
    # Function to check if new obtained state is unique or not
    def unique(self, state):
        for node in self.allNodesData:
            comp = state == node.state
            if(comp.all()):
                return -1
        return len(self.allNodesData)
    
    # Function to add new unique node in the Nodes data set
    def push(self,nodeData):
        tempData= cp.deepcopy(nodeData)                      
        self.allNodesData.append(tempData)
    
    # Function to get a Node data from the Nodes data set   
    def getNode(self,oid):
        return self.allNodesData[oid]


def main():
    # graph object created for allNodes class
    graph= allNodes()
    print('Enter the initial state ROW-WISE top to bottom (separated by commas): ')
    init= np.array(input())

    # Check if input data is correct
    if(len(init)!=9):
        print 'Wrong input'
        print 'Terminating'
        return
    for i in init:
        if(i>8 and i<0):
            print 'Wrong input'
            print 'Terminating'
            return

    # goal state defiend as finalState
    finalState= np.array([1,2,3,4,5,6,7,8,0])
    parentState= init.reshape(-1)

    # code block to check if the given input state is solvable or not
    inv_count = 0
    for i in range(8):
        j= i+1
        while(j<9):
            if(parentState[j] and parentState[i] and parentState[i]>parentState[j]):
                inv_count+=1
            j+=1
    if(inv_count%2):
        print('UNSOLVABLE')
        return

    # initializing first node data as initital state with own id and parent id both as 0
    parentNode= Node(parentState,0)

    # appending the first node into allNodes data set
    graph.push(parentNode)
    found= False

    # check if initial state is same as final state
    compare= parentState == finalState
    if(compare.all()):
        found =True
        print('Input state is same as goal state')
        return

    # writing initial data of state, ownID and parentID to the respective txt files
    nodes= open("Nodes.txt", 'w')
    NodesInfo= open("NodesInfo.txt", 'w')
    data= cp.deepcopy((parentState).reshape(3,3))
    data= data.transpose()
    data= data.reshape(-1)
    content= str(data[0]) + " " + str(data[1]) + " " + str(data[2]) + " "
    content+= str(data[3]) + " " + str(data[4]) + " " + str(data[5]) + " "
    content+= str(data[6]) + " " + str(data[7]) + " " + str(data[8]) + "\n"
    nodes.write(content)
    content2= str(parentNode.ownID) + " " + str(parentNode.pID) + "\n"
    NodesInfo.write(content2)

    print('Processing...')
    idx= 0

    # iterations to reach to the final state
    while(found != True):
        # current node is termed as parent node
        parentNode= graph.getNode(idx)

        # finding the position of blank tile (represented by 0)
        zeroPos= np.where(parentNode.state == 0)

        # to reduce computations of going back to same node from where the current node
        # is obtained, and compare if it was unique or not (which in all case will not be unique)
        # checking position of zero of parent of current node
        pastZero= np.where((graph.getNode(parentNode.pID)).state==0)

        # checking all possible set of actions
        all_actions= action(zeroPos[0][0])
        for step in all_actions:
            # ignoring the state which will lead to parent state of current node
            if(step != pastZero):
                tempNode= cp.deepcopy(parentNode)
                tempNode.state[zeroPos[0][0]]= tempNode.state[step]
                tempNode.state[step]= 0
                tempNode.pID= parentNode.ownID
                uniqueID= graph.unique(tempNode.state)
                if(uniqueID != -1):
                    tempNode.ownID= uniqueID
                    graph.push(tempNode)
                    data= cp.deepcopy((tempNode.state).reshape(3,3))
                    data= data.transpose()
                    data= data.reshape(-1)
                    content= str(data[0]) + " " + str(data[1]) + " " + str(data[2]) + " "
                    content+= str(data[3]) + " " + str(data[4]) + " " + str(data[5]) + " "
                    content+= str(data[6]) + " " + str(data[7]) + " " + str(data[8]) + "\n"
                    nodes.write(content)

                    content2= str(tempNode.ownID) + " " + str(tempNode.pID) + "\n"
                    NodesInfo.write(content2)

                    # check if the final state is achieved
                    compare= tempNode.state == finalState
                    if(compare.all()):
                        found =True
                        print('Solved')
                        break
        idx+=1
    nodes.close()

if __name__ == '__main__':
    # calling main function
    main()