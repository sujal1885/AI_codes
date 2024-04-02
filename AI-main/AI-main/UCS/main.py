from queue import PriorityQueue

def uniform_cost_search(graph, start, goal):
    # Priority queue to store nodes to be explored
    frontier = PriorityQueue()
    frontier.put((0, start))  # (cost, node)
    
    # Dictionary to keep track of explored nodes and their costs
    explored = {start: 0}
    
    while not frontier.empty():
        # Get node with the lowest cost from the priority queue
        cost, current_node = frontier.get()
        print(f"cost = {cost}, current_node = {current_node}")
        
        # If goal node is reached, return the cost
        if current_node == goal:
            print("Goal Node is reached")
            return cost
        
        # Explore neighbors of the current node
        for neighbor, edge_cost in graph[current_node].items():
            new_cost = cost + edge_cost
            
            # If neighbor has not been explored or new cost is lower
            if neighbor not in explored or new_cost < explored[neighbor]:
                explored[neighbor] = new_cost
                frontier.put((new_cost, neighbor))
    
    # If goal node is not reachable from start node
    return float('inf')

# Example usage
if __name__ == '__main__':
    # Define the graph (adjacency list representation)
    graph = {
        'A': {'B': 2, 'C': 5},
        'B': {'A': 2, 'D': 3, 'E': 1},
        'C': {'A': 5, 'F': 6},
        'D': {'B': 3},
        'E': {'B': 1, 'F': 3},
        'F': {'C': 6, 'E': 3}
    }
    
    # Define start and goal nodes
    start_node = 'A'
    goal_node = 'F'
    
    # Find the minimum cost path from start to goal node
    min_cost = uniform_cost_search(graph, start_node, goal_node)
    if min_cost != float('inf'):
        print(f"The minimum cost from {start_node} to {goal_node} is {min_cost}.")
    else:
        print(f"There is no path from {start_node} to {goal_node}.")
