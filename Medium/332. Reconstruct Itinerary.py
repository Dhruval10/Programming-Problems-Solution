from collections import defaultdict, deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary = []
        def dfs(starting):
            path = places[starting]
            while len(path) != 0:
                dfs(path.popleft())
            itinerary.append(starting)
        places = defaultdict(list)
        for ticket in tickets:
            places[ticket[0]].append(ticket[1])
        for key in places.keys():
            places[key]=deque(sorted(places[key]))
        dfs("JFK")
        return itinerary[::-1]
