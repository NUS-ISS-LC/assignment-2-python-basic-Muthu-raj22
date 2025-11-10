def find(s, n):

    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if(s[i]+s[j]==n):
                return [i,j]

nums = [3,2,4]
target = 5
print(find(nums, target))
