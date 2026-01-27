nums: list = [7, 2, 5, 3, 9]
#            [0, 1, 2, 3, 4]
def selection_sort(nums) -> None:
    sorted = []


    for i in range(len(nums) - 1):
        print(i)
        value_min = min(nums)
        value_index = nums.index(value_min)
        
        nums.pop(value_index)
        sorted.append(value_min)
        print(value_min)
        print(nums)
        print(sorted)
        print("_" * 40)
    
    if nums:
        last = max(nums)
        print(last)
        # last = nums.index(last)
        sorted.append(last)
        nums.pop(0)
       
        print("we got the last number")
        print(nums)
        print(sorted)
        print("=" * 40)
        
def selection_sort_classic(nums) -> None:
       

    for i in range(len(nums) - 1):
        print(nums) 
        print("index:", nums[i])
        value_min = min(nums[i:])
        index_min = i + nums[i:].index(value_min)

      
        print(f"value: {value_min} index: {index_min}")
        nums[i], nums[index_min] = nums[index_min], nums[i]
        print(f"{nums[index_min], nums[i]} = {nums[i], nums[index_min]}")
        print(nums) 
        print("-" * 40)

if __name__ ==  "__main__":
    # print(selection_sort(nums))
    print(selection_sort_classic(nums))
