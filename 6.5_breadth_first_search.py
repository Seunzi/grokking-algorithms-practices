# -*- coding:utf-8 -*-

from collections import deque

# create graph
graph = {}
graph['you'] = ['alice','bob','claire']
graph['bob'] = ['anuj','peggy']
graph['alice'] = ['peggy']
graph['claire'] = ["thom","jonny"]
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

# check if the person is mango seller
# by her/his name ends with letter m
def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    # create a queue
    search_queue = deque()
    # adding name to queue
    search_queue += graph[name]
    # create a list to remember checked people
    searched = []
    # when the queue is not empty run the code
    while search_queue:
        # take out first person from queue left
        person = search_queue.popleft()
        # check if the peron already searched
        if person not in searched:
            # check if the person is the one
            if person_is_seller(person):
                print('{} is a mango seller!'.format(person))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

if __name__ == '__main__':
    search("you")

# run time
# O(V + E) V:vertice E:edge

