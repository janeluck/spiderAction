def createGenerator():
    for i in range(5):
        yield i

nums = createGenerator()
print(nums)
for j in nums:
    print(j)


