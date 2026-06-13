class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        
        if self.rank[root_x] > self.rank[root_y]:
            self.par[root_y] = root_x
            self.rank[root_x] = self.rank[root_y]
        else:
            self.par[root_x] = root_y
            self.rank[root_y] += self.rank[x]
        



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        uf = UnionFind(len(accounts))

        emailToAcc = {} # email to index of acc

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        
        print(emailToAcc)

        emailGroup = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)

        res =  []
        for i, emails in emailGroup.items():
            res.append(["".join(accounts[i][0])] + emails)

        return res