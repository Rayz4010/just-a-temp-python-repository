nums=[]
x=0
while x<10:
    a=input("Enter the number: ")
    x=x+1
nums.append(a)
target=int(input("Enter the target: "))
def sums(nums,target):
    for x in range (len(nums)):
     for y in range (x+1,len(nums)):
      if nums[x]+nums[y]==target:
            return x,y
l=sums(nums,target)
print(l)