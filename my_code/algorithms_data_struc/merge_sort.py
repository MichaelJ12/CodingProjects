nums: list = [5, 2, 9, 1, 5, 6]

def merge_sort(nums) -> list:
    if len(nums) <= 1:
        return nums

    split = len(nums) // 2

    left_split = nums[:split]
    right_split = nums[split:]

    left = merge_sort(left_split)
    right = merge_sort(right_split)

    merged = []
    i = 0
    j = 0 

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1  

    while i < len(left):
        merged.append(left[i])
        i += 1
        
    while j < len(right):
        merged.append(right[j])
        j += 1
        
    return merged

print(merge_sort(nums))
