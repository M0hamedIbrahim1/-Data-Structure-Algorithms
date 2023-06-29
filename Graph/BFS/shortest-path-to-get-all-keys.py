# link   : https://leetcode.com/problems/shortest-path-to-get-all-keys
# author : Mohamed Ibrahim

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int: 
        m, n = len(grid), len(grid[0])
        total_keys = 0
        for i in range(m):
            for j in range(n):
                if 'a' <= grid[i][j] <= 'z':
                    total_keys+=1
                if grid[i][j] == '@':
                    start = (i, j)
        
        moves = 0
        que = deque([(start, '')])
        visited = set()
        def get_neis(i, j):
            return [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]

        def is_valid(i,j):
            return 0 <= i < m and 0 <= j < n 

        while len(que):
            for _ in range(len(que)):
                idx, key = que.popleft()
                if (idx, key) in visited:
                    continue
                if len(key) == total_keys:
                    return moves
                visited.add((idx, key))
                for x, y in get_neis(idx[0], idx[1]):
                    if is_valid(x, y) and grid[x][y] != '#':
                        val = grid[x][y]

                        if 'A' <= val <= 'Z' and val.lower() in key:
                            que.append(((x,y), key))

                        elif val in '.@':
                            que.append(((x, y), key))

                        elif 'a' <= val <= 'z':
                            if val not in key:
                                que.append(((x,y), key+val))
                            else:
                                que.append(((x,y), key))
            moves+=1
        return -1
          
