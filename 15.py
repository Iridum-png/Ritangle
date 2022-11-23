from math import cos, pi

point = [x/10 for x in range(9, 2, -1)]
angles = []
length = 1
prev = 0

for value in point:
    angles.append(round((180 * (1 - value))))
    
for angle in angles:
    x = angle - (prev/2)
    length += 1/cos(x * (pi/180))
    prev = angle

# 1 + 1/cos(27) + 1/cos(36) + 1/cos()

print(length, length * 0.74)
