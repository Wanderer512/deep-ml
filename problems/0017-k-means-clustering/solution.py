import math
def distance(x: tuple[float, ...], y: tuple[float, ...]) -> float:
    return math.sqrt(sum((x[i] - y[i]) ** 2 for i in range(len(x))))

def find_centroid(points: list[tuple[float, ...]]) -> tuple[float, ...]:
    n = len(points)
    dims = len(points[0])
    return tuple(sum(p[d] for p in points) / n for d in range(dims))

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# Your code here
	

	centroids = initial_centroids
	for _ in range(max_iterations):
		groups = [[] for _ in range(len(initial_centroids))]
		for  i in range(len(points)):
			mn = 100000000
			for j in range(len(centroids)):
				if distance(points[i], centroids[j])<mn:
					nearest_centroid = centroids[j] 
					nearest_centroid_idx = j
					mn = distance(points[i], centroids[j])

			groups[nearest_centroid_idx].append(points[i])
		
		centroids = [find_centroid(groups[i]) for i in range(len(groups))]


		
	return centroids