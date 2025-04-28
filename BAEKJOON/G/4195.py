from sys import stdin
input = stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        root[b] = a
        network_size[a] += network_size[b]
    print(network_size[a])


for _ in range(int(input())):
    F = int(input())
        
    root = {}
    network_size = {}
    
    for _ in range(F):
        A, B = input().split()
        if A not in root:
            root[A] = A
            network_size[A] = 1
        if B not in root:
            root[B] = B
            network_size[B] = 1
        union(A, B)