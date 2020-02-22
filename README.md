# ENPM661_Project1

## Dependencies
Python2.7
Python3.5

## Libraries needed
numpy
copy

## How to run
Open ternimal and run the below commands
```
$ git clone https://github.com/varunasthana92/ENPM661_Project1.git
$ cd cd ENPM661_Project1
$ python proj1_Varun_Asthana.py
```

Program will prompt the user to Enter the initial state of the puzzle ROW-WISE. Data to be provided from 1st row tll last row separated by commas.
(Blank tile is denoted by number 0)

Example of input: 1,2,3,4,5,0,7,8,6


This will be considered as

1 2 3

4 5 0

7 8 6


If any wrong input is provided, the program will display an error message and terminate.

## How to visulaize
Once a solution is reched, the program will prompt the message "Solved"


Run the below commands to visualize the steps to be taken to solve the puzzle
```
$ python3 plot_path.py
```

## Output text files
Program will generate 3 text files- Nodes.txt, NodesInfo.txt and nodesPath.txt


nodePath.txt contains the node states of the shortest path.


Nodes.txt contains the node states of all the explored nodes.


NodesInfo.txt contains the data of node's own ids in first column and parent ids in the second column
