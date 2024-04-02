from queue import PriorityQueue

def uniform_cost_search(graph,start,goal):

    frontier=PriorityQueue()
    frontier.put((0,start))

    explored={start:0}
    print(explored)

    while not frontier.empty():
        
        cost,current_node=frontier.get()
        print(f"Cost is {cost}, Current node is {current_node}")

        if current_node==goal:
            return cost
        
        for neighbor,edge_cost in graph[current_node].items():
            new_cost=cost+edge_cost

            print(new_cost)

            if neighbor not in explored or new_cost<explored[neighbor]:
                explored[neighbor]=new_cost
                frontier.put((new_cost,neighbor))


        print(explored)        


    return float('inf')        






if __name__ == '__main__':
    
    graph = {
        'A': {'B': 2, 'C': 5},
        'B': {'A': 2, 'D': 3, 'E': 1},
        'C': {'A': 5, 'F': 6},
        'D': {'B': 3},
        'E': {'B': 1, 'F': 3},
        'F': {'C': 6, 'E': 3}
    }
    
    start_node = 'A'
    goal_node = 'F'
    
    min_cost = uniform_cost_search(graph, start_node, goal_node)
    if min_cost != float('inf'):
        print(f"The minimum cost from {start_node} to {goal_node} is {min_cost}.")
    else:
        print(f"There is no path from {start_node} to {goal_node}.")

    