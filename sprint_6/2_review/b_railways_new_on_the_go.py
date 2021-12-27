import sys


def is_optimal_map(count):
    graph = []
    for vertex in range(count-1):
        graph.append([])
        current = sys.stdin.readline().rstrip()
        for index_route in range(len(current)):
            end_vertex = vertex + index_route + 1
            if current[index_route] == 'R':
                graph[vertex].append(end_vertex)
                continue
            for _ in range(len(graph), end_vertex+1):
                graph.append([])
            graph[vertex+index_route+1].append(vertex)
    colors = [0] * count
    for current in range(count):
        if colors[current] == 2:
            continue
        stack = [current]
        while len(stack) != 0:
            current = stack.pop()
            if colors[current] == 1:
                colors[current] = 2
                continue
            colors[current] = 1
            stack.append(current)
            for vertex in graph[current]:
                if colors[vertex] == 1:
                    return 'NO'
                if colors[vertex] == 0:
                    stack.append(vertex)
    return 'YES'


# def test_is_optimal_map():
#     result = is_optimal_map(3, [
#         'RR',
#         'R',
#     ])
#     assert result == 'YES', f'Wrong answer: {result}'
#     result = is_optimal_map(3, [
#         'RR',
#         'B',
#     ])
#     assert result == 'YES', f'Wrong answer: {result}'
#     result = is_optimal_map(3, [
#         'RB',
#         'R',
#     ])
#     assert result == 'NO', f'Wrong answer: {result}'
#     result = is_optimal_map(3, [
#         'BR',
#         'R',
#     ])
#     assert result == 'YES', f'Wrong answer: {result}'
#     result = is_optimal_map(4, [
#         'RBR',
#         'RR',
#         'R',
#     ])
#     assert result == 'NO', f'Wrong answer: {result}'
#     result = is_optimal_map(4, [
#         'RRR',
#         'BR',
#         'R',
#     ])
#     assert result == 'YES', f'Wrong answer: {result}'
#     result = is_optimal_map(4, [
#         'RRR',
#         'RB',
#         'R',
#     ])
#     assert result == 'NO', f'Wrong answer: {result}'
#     result = is_optimal_map(4, [
#         'BBB',
#         'RB',
#         'B',
#     ])
#     assert result == 'YES', f'Wrong answer: {result}'
#     result = is_optimal_map(5, [
#         'RRRB',
#         'BRR',
#         'BR',
#         'R',
#     ])
#     assert result == 'NO', f'Wrong answer: {result}'
#     result = is_optimal_map(5, [
#         'RBRR',
#         'RBR',
#         'RB',
#         'R',
#     ])
#     assert result == 'NO', f'Wrong answer: {result}'
#     result = is_optimal_map(5, [
#         'BRBR',
#         'BBR',
#         'BB',
#         'R',
#     ])
#     assert result == 'NO', f'Wrong answer: {result}'
#     result = is_optimal_map(10, [
#         'RRBRRBRRR',
#         'BBBBBBRB',
#         'BBRBRRR',
#         'RRBRRR',
#         'RBRRR',
#         'BBRR',
#         'RRR',
#         'RR',
#         'B',
#     ])
#     assert result == 'YES', f'Wrong answer: {result}'
#     print('All tests passed!')


if __name__ == '__main__':
    # test_is_optimal_map()
    count = int(input())
    print(is_optimal_map(count))
