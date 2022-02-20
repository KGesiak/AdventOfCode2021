
# part 1

# These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.
#
# If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).
#
# Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:
#
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.
#
# Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)
#
# In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.
#
# The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.
#
# Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

#CODE

# f = open("input.txt")
# input = f.readlines()
#
# for i,t in enumerate(input):
#     input[i] = t.strip()
#
# for i,t in enumerate(input):
#     input[i] = [int(c) for c in t]
# #print(tekst)
# col_len = len(input[0])
# row_len = len(input)
#
# lows = []
# for i in range(row_len):
#     for j in range(col_len):
#         num = input[i][j]
#         lowest = 1
#         if(j != 0):
#             if( num >= input[i][j - 1]):
#                 lowest = 0
#         if (i != 0):
#             if (num >= input[i - 1][j]):
#                 lowest = 0
#         if (j != col_len - 1):
#             if (num >= input[i][j + 1]):
#                 lowest = 0
#         if (i != row_len - 1):
#             if (num >= input[i + 1][j]):
#                 lowest = 0
#
#         if(lowest):
#             lows.append(num + 1)
#
# print(sum(lows))

#part2

# Next, you need to find the largest basins so you know what areas are most important to avoid.
#
# A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.
#
# The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.
#
# The top-left basin, size 3:
#
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The top-right basin, size 9:
#
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The middle basin, size 14:
#
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# The bottom-right basin, size 9:
#
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678
# Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.
#
# What do you get if you multiply together the sizes of the three largest basins?

#CODE

f = open("input.txt")
input = f.readlines()

for i,t in enumerate(input):
    input[i] = t[:-1]

for i,t in enumerate(input):
    input[i] = [int(c) for c in t]

col_len = len(input[0])
row_len = len(input)

seen = []
def back(i,j,temp):
    seen.append((i,j))
    if (i != 0):
        if (input[i - 1][j] != 9 and (i - 1, j) not in seen):
            back(i - 1, j, temp)
    if (j != col_len - 1):
        if (input[i][j + 1] != 9 and (i, j + 1) not in seen):
            back(i, j + 1, temp)
    if (i != row_len - 1):
        if (input[i + 1][j] != 9 and (i + 1, j) not in seen):
            back(i + 1, j, temp)
    if (j != 0):
        if (input[i][j - 1] != 9 and (i, j - 1) not in seen):
            back(i,j-1,temp)
    temp.append(1)


basins = []
for i in range(row_len):
    for j in range(col_len):
        if(input[i][j] == 9):
            continue
        temp = []
        back(i,j,temp)
        basins.append(temp)

sizes = [len(b) for b in basins]
sizes.sort(reverse=True)
result = 1
for i in range(3):
    result*=sizes[i]
print(result)