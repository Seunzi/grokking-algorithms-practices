# -*- codig: utf-8 -*-

# create graph (dict) with weight
graph = {
    "start":{"a":6,"b":2},
    "a":{"fin":1},
    "b":{"a":3,"fin":5},
    "fin":{}
    }
# from start to node total cost dict
costs = {
    "a":6,
    "b":2,
    "fin":float("inf")
}
# node child-parent dict
parents = {
    "a":"start",
    "b":"start",
    "fin":None
}
# list to remember processed node
processed = []
# function of finding the lowest cost node
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# main algorithem
# get the cheapest node
node = find_lowest_cost_node(costs)
# caculate the neighbors' cost and update the dicts
# stop after run out of node
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    # mark as processed
    processed.append(node)
    # generate next node
    node = find_lowest_cost_node(costs)

# geneate loeset cost path string for output
lowest_path_list = ["fin"]
child = lowest_path_list[0]
while len(lowest_path_list) <= len(parents):
    lowest_path_list.append(parents[child])
    child = parents[child]
# make the path start with starting node
lowest_path_list.reverse()

lowest_path = "--".join(str(n) for n in lowest_path_list)
print("The lowest costs path is {}, total cost {}.".format(lowest_path,costs["fin"]))
