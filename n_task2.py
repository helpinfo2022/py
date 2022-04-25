# Task 2
# Array Challenge
# Have the function ArrayChallenge(arr) take the array of integers stored in arr, and find the four largest elements
# and return their sum. For example: if arr is [4, 5, -2, 3, 1, 2, 6, 6] then the four largest elements in this array
# are 6, 6, 4, and 5 and the total sum of these numbers is 21, so your program should return 21. If there are less
# than four numbers in the array your program should return the sum of all the numbers in the array.
# Examples
# Input: {1, 1, 1, -5}
# Output: -2
# Input: {0, 0, 2, 3, 7, 1}
# Output: 13



def ArrayChallenge(arr):
    my_list=sorted(arr)
    four_num=[]
    i = 1
    while i <= 4:
        four_num.append(my_list[-i])
        i +=1

    result=0
    for my_count in four_num:
        result+=my_count

    print(result)

ArrayChallenge([4, 5, -2, 3, 1, 2, 6, 6]);
