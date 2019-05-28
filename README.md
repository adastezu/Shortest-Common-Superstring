# Shortest-Common-Superstring

The Shortest Common Superstring problem is defined as follows: 

Given a finite set of strings S, output the shortest string w such that for all strings w' in S, w' is a substring of w.

The problem is NP-Hard. In this project we have implemented Ukkonnen's greedy algorithm, designed and implemented an exact (exponential time) algorithm and used that to give a parameterized boosting procedure which can be run as subroutine of the greedy procedure to improve the quality of the solution outputted. The parameters of the boosting procedure determine the time and space taken by the greedy algorithm and in the limiting case, the boost becomes the exponential algorithm.

## Running the code
Run the main.py file to run the greedy procedure and the boosting procedure in the greedy algorithm. 
## Notes
The programs only run in python 2.X and might throw errors in other versions. The program requires a data file "MH0004.seq.fa" which can be found [Here](google.com). Place the data file in the same directory as the program files while running the code.
