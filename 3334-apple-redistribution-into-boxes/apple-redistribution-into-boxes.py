class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        
        boxes = 0
        for cap in capacity:
            total_apples -= cap
            boxes += 1
            if total_apples <= 0:
                return boxes
        
        return boxes
