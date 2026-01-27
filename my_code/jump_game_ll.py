nums: list = [2, 3, 1, 1, 4]
#       index[0, 1, 2, 3, 4] = 5

# You start at index 0. 
# The minimum jumps to reach the last index is 2 (0 -> 1 -> 4)

def jump_game(nums) -> int:
    current_end = 0
    jumps: int = 0

    print(f"begin start: {current_end}")
    print("-" * 40)
    farthest = current_end
    
    for i in range(len(nums) -1):
        print(f"index: {i} value: {nums[i]}")
        print(f"current end start: {current_end}")
        print(f"farhest start: {farthest}")
        
        farthest = max(farthest, i + nums[i])
        print(f"{farthest} = {farthest}, {i} + {nums[i]}")
        print("-" * 40)
        
        if i == current_end:
            current_end = farthest
            jumps += 1
            print(f"jump = {jumps}")
            print("-" * 40)
        if current_end >= len(nums) -1:
            print("we are done")
            print("=" * 40)
            return jumps
    return jumps

jumps = jump_game(nums)

print(f"final number of jumps: {jumps}")

