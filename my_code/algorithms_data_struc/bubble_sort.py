numbers = [7, 2, 5, 3, 9]

for i in range(len(numbers) - 1):
    print(f"\nPass {i + 1}:")
    already_sorted = True
    for j in range(len(numbers) - i -1):
        ranges = range(len(numbers) - i -1)
        print(f"{j} in {ranges} = {range(len(numbers))} - {i} - {1}")
        print("=" * 50)
        
        print(f"{numbers[j]} > {numbers[j+1]}")
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            print(numbers)
            already_sorted = False
    print(f"After pass {i + 1}: {numbers}")
    
    if already_sorted:
        print("sorted!")
        break