import math

# Öklid mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaların listesi
points = [(1, 2), (4, 6), (7, 8), (2, 3)]

# Mesafeleri hesapla
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# Minimum mesafeyi bul
print("Minimum Mesafe:", min(distances))
