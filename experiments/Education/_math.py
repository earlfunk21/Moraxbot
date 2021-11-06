from typing import List


class Statistics:
    def __init__(self, scores) -> list:
        self.scores = scores
        self.scores.sort()
        
    def mean(self):
        return sum(self.scores)/len(self.scores)
    
    def median(self):
        N = len(self.scores)
        if N % 2 == 0:
            median = (self.scores[int(N/2 - 1)] + self.scores[int(N/2)])
            return median/2
        else:
            th = (N+1)/2
            return self.scores[int(th)-1]
    
    def mode(self):
        shows = []
        modeList = []
        for num in self.scores:
            shows.append(self.scores.count(num))
        max_count = max(shows)
        for item, count in zip(self.scores, shows):
            if count == max_count and item not in modeList:
                modeList.append(item)
        if modeList == self.scores:
            return None
        return modeList

# # Mean
# Smean = Statistics([84, 92, 78, 82, 90])
# print(Smean.mean())

# # Median
# # IF ODD 
# Smedianodd = Statistics([6, 11, 15, 14, 9])
# print(Smedianodd.median())
# # IF Even
# Smedianeven = Statistics([2, 4, 6, 8, 10, 12])
# print(Smedianeven.median())

# #Mode
# Smode = Statistics([1, 2, 3, 3 , 2, 1, 4])
# print(Smode.mode())
