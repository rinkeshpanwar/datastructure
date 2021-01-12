class Solution:
    def findMedianSortedArrays(self, nums1 ,nums2 ):
       print(nums1)
       print(nums2)
       nums3 = []
       for i in nums1:
           nums3.append(i)
       for i in nums2:
           nums3.append(i)
       nums3.sort()
       print(nums3)
       if len(nums3)%2==0:
           i1 = len(nums3)/2
           print(i1)
           i2 = i1-1
           print(i2)
           temp = nums3[i1]+nums3[i2]
           print(temp)
           divi = temp/2
           return divi
       else:
           index = len(nums3)//2
           return nums3[index]
s=Solution()
temp = s.findMedianSortedArrays([1,3],[2])
print(temp)