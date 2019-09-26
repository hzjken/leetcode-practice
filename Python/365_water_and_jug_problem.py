class Solution:
    def canMeasureWater(self, x, y, z):
        if x == 0:
            return z in {0, y}
        if y == 0:
            return z in {0, x}
        
        vol_set = set()
        min_jug = min(x, y)
        max_jug = max(x, y)
        max_vol = min_jug + max_jug
        queue = [0]
        
        while queue != []:
            size = queue.pop(0)
            if size not in vol_set and 0 <= size <= max_vol:
                vol_set.add(size)
            
                if size + min_jug <= max_vol:
                    queue.append(size+min_jug)
                if size + max_jug <= max_vol:
                    queue.append(size+max_jug)
                if max_jug - size >= 0:
                    queue.append(min_jug - ((max_jug - size) % min_jug))
                if min_jug - size >= 0:
                    queue.append(max_jug - ((min_jug - size) % max_jug))
        
        return z in vol_set