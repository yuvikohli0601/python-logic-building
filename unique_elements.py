def find_unique_elements(nums):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x,0)+1
    return [x for x,c in freq.items() if c==1]

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(find_unique_elements(nums))
