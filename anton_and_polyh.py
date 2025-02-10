# https://codeforces.com/problemset/problem/785/A

num_faces_per_polyh = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20,
}

n = int(input())
s = 0
for _ in range(n):
    s += num_faces_per_polyh[input()]

print(s)
