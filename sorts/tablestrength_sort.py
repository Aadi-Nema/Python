def max_table_weight(test_cases):
    results = []
    for legs in test_cases:
        # Sort the leg strengths in descending order
        legs.sort(reverse=True)
        
        max_weight = 0
        # Calculate the maximum weight for each number of legs
        for i in range(len(legs)):
            # The weight each leg would bear if using the first (i + 1) legs
            weight = legs[i] * (i + 1)
            # Update the maximum weight
            max_weight = max(max_weight, weight)
        
        results.append(max_weight)
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    test_cases = []
    
    index = 1
    for _ in range(T):
        N = int(data[index])  # Read number of legs
        index += 1
        legs = list(map(int, data[index].split()))  # Read leg strengths
        test_cases.append(legs)
        index += 1
    
    results = max_table_weight(test_cases)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
