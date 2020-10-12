class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        mapping_distance = []
        
        for value in costs:
            difference = value[0] - value[1]
            mapping_distance.append([value,difference])
        
        mapping_distance = sorted(mapping_distance, key = lambda x: x[1])
        total_distance = 0
        
        length = int(len(mapping_distance)/2)
        
        for i in range(length):
            ele1 = mapping_distance[i][0][0]
            ele2 = mapping_distance[i+length][0][1]
            
            total_distance = total_distance + ele1 + ele2
        
        return total_distance
