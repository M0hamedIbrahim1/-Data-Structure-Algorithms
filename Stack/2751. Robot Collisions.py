# link   : https://leetcode.com/problems/robot-collisions/description/
# authur : Mohamed Ibrahim

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        ind = [i for i in range(n)]
        ind.sort(key=lambda x: positions[x])
        s = []
        for x in ind:
            if directions[x] == 'L':
                while s:
                    y = s[-1]
                    if healths[x] == healths[y]:
                        healths[x] = healths[y] = 0
                        s.pop()
                        break
                    if healths[x] > healths[y]:
                        healths[x] -= 1
                        healths[y] = 0
                        s.pop()
                    else:
                        healths[x] = 0
                        healths[y] -= 1
                        break
            else:
                s.append(x)
        r = [x for x in healths if x]
        return r
