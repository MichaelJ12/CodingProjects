nums = [2, 3, 1, 1, 4]

def can_reach_end(nums) -> bool:
    # Stack of positions to explore, start at index 0
    to_explore = [0]
    # Set of already visited positions to avoid infinite loops
    visited = set()

    while to_explore:
        # Take the last position from the stack to explore
        current = to_explore.pop()
        # Mark current position as visited
        visited.add(current)

        # Print current state for clarity
        print(f"Current index being explored: {current}")
        print(f"Indexes to explore next: {to_explore}")
        print(f"Visited indexes: {visited}")
        print("-" * 40)

        # Check if we reached the last index
        if current == len(nums) - 1:
            print(f"Reached the end at index {current} ✅")
            return True
        else:
            # Calculate the forward jump
            forward_pos = current + nums[current]
            if 0 <= forward_pos < len(nums) and forward_pos not in visited:
                to_explore.append(forward_pos)
                print(f"Forward jump to index {forward_pos} (value: {nums[forward_pos]}) added to explore list")

            # Calculate the backward jump
            backward_pos = current - nums[current]
            if 0 <= backward_pos < len(nums) and backward_pos not in visited:
                to_explore.append(backward_pos)
                print(f"Backward jump to index {backward_pos} (value: {nums[backward_pos]}) added to explore list")

            print("=" * 40)  # Separator for readability

    # If stack is empty and end was never reached
    print("Cannot reach the end ❌")
    return False

can_reach_end(nums)


