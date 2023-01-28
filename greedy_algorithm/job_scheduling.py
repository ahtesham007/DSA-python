class Jobs:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def JobScheduling(Jobs,n):
        
        # code here
        Jobs.sort(key=lambda x:x.profit, reverse=True)
        
        m_d = 0
        for i in range(n):
            m_d = max(m_d,Jobs[i].deadline)
        
        vis = [-1]*m_d
        vis[Jobs[0].deadline - 1] = Jobs[0].id
        c = 1
        profit = Jobs[0].profit
        for i in range(1,n):
            for j in range(Jobs[i].deadline - 1, -1, -1):
                if vis[j] == -1:
                    vis[j] = Jobs[i].id
                    profit += Jobs[i].profit
                    c += 1
                    break
        
        return [c, profit]