import heapq
import math

class DroneDeliveryOptimizer:
    def __init__(self, delivery_points):
        self.points = delivery_points
        self.graph = self._create_distance_graph()

    def _create_distance_graph(self):
        n = len(self.points)
        graph = [[math.inf] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    graph[i][j] = self._calculate_distance(self.points[i], self.points[j])
        
        return graph

    def _calculate_distance(self, point1, point2):
        return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

    def optimize_route(self):
        n = len(self.points)
        unvisited = set(range(1, n))
        route = [0]
        current = 0

        while unvisited:
            next_point = min(unvisited, key=lambda x: self.graph[current][x])
            route.append(next_point)
            unvisited.remove(next_point)
            current = next_point

        route.append(0)
        return route

def main():
    delivery_points = [
        (0, 0),   # Starting point
        (10, 20), # First delivery
        (30, 15), # Second delivery
        (25, 35), # Third delivery
        (40, 5)   # Fourth delivery
    ]

    optimizer = DroneDeliveryOptimizer(delivery_points)
    optimal_route = optimizer.optimize_route()

    total_distance = sum(
        optimizer._calculate_distance(
            delivery_points[optimal_route[i]], 
            delivery_points[optimal_route[i+1]]
        ) for i in range(len(optimal_route)-1)
    )

    print("Optimal Delivery Route:", optimal_route)
    print(f"Total Travel Distance: {total_distance:.2f} units")

if __name__ == "__main__":
    main()