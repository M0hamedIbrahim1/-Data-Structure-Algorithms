# link   : https://leetcode.com/problems/accounts-merge/description/
# author : Mohamed Ibrahim

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def findParent(u):
            if u==parent[u]:
                return u
            else:
                parent[u]=findParent(parent[u])
                return parent[u]
                
        def unionBySize(u,v):
            pu,pv=findParent(u),findParent(v)
            if pu==pv:
                return 
            parent[pu]=pv
            size[pv]+=size[pu]
            
        n=len(accounts)
        parent=[i for i in range(n)]
        size=[1]*n
        d={}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                s=accounts[i][j]
                if s not in d:
                    d[s]=i
                else:
                    unionBySize(i,d[s])
        temp=defaultdict(list)
        for k,v in d.items():
            pv=findParent(v)
            temp[pv].append(k)
        res=[]
        for i in temp:
            temp2=sorted(temp[i])
            ans=[accounts[i][0]]
            ans.extend(temp2)
            res.append(ans)
        return res
        
