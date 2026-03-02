
def removeDuplicates(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    k = 1
    for i in range(len(nums)):
        if nums[k-1] != nums[i]:
            nums[k] = nums[i]
            k += 1
    return nums


nums = list(map(int,input("enter the numbers : ").split(",")))
print(removeDuplicates(nums))