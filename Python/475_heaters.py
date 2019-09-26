class Solution:
    def findRadius(self, houses, heaters):
        new = []
        pointer1 = 0
        pointer2 = 0
        houses = sorted(houses)
        heaters = sorted(heaters)
        
        while pointer1 < len(houses) or pointer2 < len(heaters):
            if pointer1 < len(houses) and pointer2 < len(heaters):
                if houses[pointer1] < heaters[pointer2]:
                    new.append((houses[pointer1], 'house'))
                    pointer1 += 1
                else:
                    new.append((heaters[pointer2], 'heater'))
                    pointer2 += 1
            elif pointer1 < len(houses):
                new.append((houses[pointer1], 'house'))
                pointer1 += 1
            else:
                new.append((heaters[pointer2], 'heater'))
                pointer2 += 1
                    
        house_dist = {i: None for i in houses}
        prev = None
        pointer = 0
        
        while pointer < len(new):
            pos, htype = new[pointer]
            if htype == 'heater':
                prev = pos
            else:
                if prev:
                    dist = pos - prev
                    if house_dist[pos] is None:
                        house_dist[pos] = dist
                    else:
                        house_dist[pos] = min(house_dist[pos], dist)
            
            pointer += 1
        
        prev = None
        pointer = len(new) - 1
        
        while pointer >= 0:
            pos, htype = new[pointer]
            if htype == 'heater':
                prev = pos
            else:
                if prev:
                    dist = prev - pos
                    if house_dist[pos] is None:
                        house_dist[pos] = dist
                    else:
                        house_dist[pos] = min(house_dist[pos], dist)
            
            pointer -= 1
        
        return max(house_dist.values())