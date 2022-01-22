"""
It’s another day in the office, and you’re a mastermind of not doing 
any work yourself. Instead, you’ll go to your coworkers for “help,” 
but secretly have them do all the work.

You’ve determined that the more one of your coworkers helps you, the 
more annoyed they become. You’ve also been able to determine how much 
more annoyed a coworker gets everytime you ask them for help. At the 
beginning of the day, a coworker is initially a annoyed at you. That’s 
their annoyance level. Everytime you ask them for help though, they 
become d more annoyed at you – their annoyance level a increases 
by a constant amount d so that a += d.

You want to complete a project of h tasks solely with “help” from your 
coworkers, but you need to be careful not to annoy any of them too much.

What’s the best you can do?

The first line contains 2 integers h and c, where h is the number of 
times you have to ask for help to complete the project, and c denotes 
the number of coworkers you have. Each of the following c lines contains 
two positive integers a and d, representing a coworker whose initial 
annoyance level is a and who is getting more annoyed at you by an 
increase of d every time you ask them for help.

Output a single number, which is the maximum annoyance level any coworker 
has at you provided you use an optimal strategy to minimize this level.

Run: 

echo "4 4
1 2
2 3
3 4
4 5" | python AnnoyedCoworkers.py

echo "3 2
1 1000
1000 1" | python AnnoyedCoworkers.py

"""

#! /usr/bin/python3

import sys

def annoyance_level(coworkers, num_of_tasks, num_of_coworkers):
    """Method to find out maximum annoyance level"""
    annoyance = []
    annoyance_levels = []
    for worker in coworkers:
        annoyance.append(worker[0]+worker[1])
        annoyance_levels.append(worker[0])
    for i in range(num_of_tasks):
        min_index = annoyance.index(min(annoyance))
        increase_annoy = coworkers[min_index][1]
        annoyance_levels[min_index] += increase_annoy  
        annoyance[min_index] += increase_annoy    
    return max(annoyance_levels)
        
if __name__ == '__main__':
    lines_raw = sys.stdin.readlines()
    lines = [list(map(int, line.strip().split(" "))) for line in lines_raw]
    num_of_tasks = lines[0][0]
    num_of_coworkers = lines[0][1]
    lines.pop(0)
    coworkers = lines
    result = annoyance_level(coworkers, num_of_tasks, num_of_coworkers)
    print(result)
