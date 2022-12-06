coords = [[1, 2], [3, 4], [3, 0], [2, 4], [4, 3], [1, 1], [3, 2], [2, 2], [0, 4], [3, 0], [2, 3], [4, 0], [1, 3], [4, 1], [0, 2], [3, 1], [2, 1], [1, 0], [4, 2], [0, 1]]
# points should be a list of W S R O G U V R P C L Y E D I A O A C O M N T O D

points = ['M', 'N', 'T', 'O', 'D', 'A', 'O', 'A', 'C', 'O', 'L', 'Y', 'E', 'D', 'I', 'U', 'V', 'R', 'P', 'C', 'W', 'S', 'R', 'O', 'G']
ref = []
for pair in coords:
    ref.append(pair[0] + 5 * pair[1])

for i in range(len(ref)):
    print(points[ref[i]], end='')