
# 11 盛最多水的容器container-with-most-water

题目描述
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

图片描述：

![image.png](attachment:image.png)


示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49


## 方法一：暴力法   通过47/50  超时 时间复杂度O(n^2)


```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        output = 0
        n = len(height)
        for i in range(0,n-1):
            for j in range(i,n):
                temp = min(height[i],height[j])
                if (temp*(j-i)) > output:
                    output = temp*(j-i)
        return output
s1 = Solution()
print(s1.maxArea([1,8,6,2,5,4,8,3,7]))
```

    49
    

## 方法二：动态规划 时间复杂度 O(n)

两头向内检索

$ output = max(output,min(height[i],height[j])*(j-i)) $

由于面积由短的柱子决定，所以只需要将短的方向向内检索即可


```python
class Solution2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        output = 0
        i,j = 0,n-1
        while i < j:
            output = max(output,min(height[i],height[j])*(j-i))
            if height[i]<height[j]:
                i = i+1
            else:
                j=j-1
        return output
    
s2 = Solution2()
print(s2.maxArea([1,8,6,2,5,4,8,3,7]))
```

    49
    
