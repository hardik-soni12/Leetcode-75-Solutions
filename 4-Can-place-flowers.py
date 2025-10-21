'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, 
flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the 
no-adjacent-flowers rule and false otherwise.

'''

'''
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
'''

def can_place_flowers(flowerbed, n):

    count = 0
    for i, flower in enumerate(flowerbed):
        if flower == 0:
            leftside = (i==0) or flowerbed[i-1] == 0
            rightside = (i==len(flowerbed)-1) or flowerbed[i+1] == 0
            if leftside and rightside:
                flowerbed[i] = 1
                count += 1
            
            if count >= n:
                return True
            
    return count>= n

flowerbed = [0,1,0]
n = 1
print(can_place_flowers(flowerbed, n))