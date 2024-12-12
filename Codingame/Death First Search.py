import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# Breadth First not DepthFirst (name of the game can be misleading)
# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
network = {}
n, l, e = [int(i) for i in input().split()]
print(f"n: {n}, l: {l},e: {e}", file=sys.stderr, flush=True)
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    #print(f"n1: {n1}, n2: {n2}", file=sys.stderr, flush=True)
    if n1 not in network:
        network[n1] = set()
    if n2 not in network:
        network[n2] = set()
    network[n1].add(n2)
    network[n2].add(n1)
    
gateways = set()
for i in range(e):
    ei = int(input())  # the index of a gateway node
    print(f"gatewayindex: {ei}", file=sys.stderr, flush=True)
    gateways.add(ei)


print("Network adjacency list:", file=sys.stderr, flush=True)
for key, value in network.items():
    print(f"  {key}: {sorted(value)}", file=sys.stderr, flush=True)
# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    l1 = None
    l2 = None
    print(f"bobnetindex: {si}", file=sys.stderr, flush=True)
    for gateway in gateways:
        if gateway in network[si]:
            l1 = si
            l2 = gateway
            #print(si,gateway)
            link_choice = True
            
    if l1 is None:
        for gateway in gateways:
            for node in network[gateway]:
                print("here", file=sys.stderr, flush=True)

                if node in network[si]:
                    l1 = gateway
                    l2 = node
                   # print(gateway, node)
                else:
                    continue
    print(l1,l2)


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    #print(si, ei)
