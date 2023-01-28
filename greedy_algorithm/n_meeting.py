class Meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos

class Solution:
    def maximumMeetings(self,n,start,end):
            # code here
            l = []
            for i in range(n):  
                l.append(Meeting(start[i], end[i], i))
            
            l.sort(key = lambda x:x.end)
            limit = l[0].end
            c = 1
            for j in range(1,n):
                if l[j].start >limit:
                    c += 1
                    limit = l[j].end
            
            return c