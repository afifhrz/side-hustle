def addroute(source, destination):
    # Write your code here
    return source, destination

#
# Complete the 'checkroute' function below.
#
# The function is expected to return a STRING.
#

def checkroute():
    # Write your code here
    graph = {}
    
    # to list all the vertex and list its neighbor
    for item in res:
        u, v = item
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
    
    # make a empty set to save the visited and recursion stack
    visited = set()
    recursion_stack = set()
    def searching(vertex):
        visited.add(vertex)
        recursion_stack.add(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                if searching(neighbor):
                    return True
            elif neighbor in recursion_stack:
                return True
        recursion_stack.remove(vertex)
        return False
    
    for vertex in graph:
        if vertex not in visited:
            if searching(vertex):
                return "Yes"
    return "No"

res = [(1,2), (2,4)]
print(checkroute())
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])
#     res = []
#     for m_itr in range(m):
#         second_multiple_input = input().rstrip().split()

#         x = int(second_multiple_input[0])

#         y = int(second_multiple_input[1])

#         res.append(addroute(x, y))

#     result = checkroute()

#     fptr.write(result + '\n')

#     fptr.close()