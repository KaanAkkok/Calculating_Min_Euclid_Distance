points = [(1, 1), (4, 5), (0, 0), (5, 12)]

def euclideanDistance(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]

    return ((x2-x1)**2 + (y2-y1)**2) ** 0.5

print("Euclid: ", euclideanDistance(points[2], points[3]))

distance = []
n = len(points)

for i in range(n):
    for j in range(i+1, n):
        dist = euclideanDistance(points[i], points[j])
        distance.append(dist)
    
min_dist = min(distance)

print("The min euclid distance is: ", min_dist)
