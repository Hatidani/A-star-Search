from A_star_search import astar, graph, weights, heuristic, start, goal
import time

def simulate_path(path, visit_order, total_cost):
    
    print("Truck traveling")
    
    for node in path:
        print(f"Car is now at: {node}")
        time.sleep(1)
    print("\nDestination reached")
    
    print("\nSUMMARY")
    
    print(f"Visited Order: {' > '.join(visit_order)}")
    print(f"Optimal Path: {' > '.join(path)}")
    print(f"Total Cost: {total_cost} km")
path, visited_order, total_cost = astar(graph, weights, heuristic, start, goal)
simulate_path(path, visited_order, total_cost)