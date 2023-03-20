# link   : https://leetcode.com/problems/get-watched-videos-by-your-friends/description/
# author : Mohamed Ibrahim


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        graph = defaultdict(list)
        for i in range(len(friends)):
            graph[i] = friends[i]

        s = set()
        dic = defaultdict(int)
        visited = [False]*len(friends)
        visited[id] = True
        q = deque()
        q.append([id,0])
        while q:
            node , d = q.popleft()
            if d == level:
                for i in watchedVideos[node]:
                    dic[i]+=1
            for neigh in graph[node]:
                if not visited[neigh]:
                    q.append([neigh,d+1])
                    visited[neigh] = True
        return sorted(list(dic.keys()), key = lambda k: (dic[k], k))
        
        
