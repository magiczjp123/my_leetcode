def bubble_sort(nums):
    while True:
        swapped = False
        for n in range(len(nums)-1):
            if nums[n] > nums[n+1]:
                nums[n], nums[n+1] = nums[n+1], nums[n]
                swapped = True
        if swapped == False:
            break
    return nums

def bubble_sort_2(nums):
    n = len(nums)-1
    while True:
        swapped = False
        for i in range(n):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True
        n = n -1
        if swapped == False:
            break
    return nums

def bubble_sort_3(nums):
    n = len(nums)
    while True:
        newn = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                newn = i+1
        n = newn
        if n <= 1:
            break
    return nums


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    l1 = nums[:len(nums)//2]
    l2 = nums[len(nums)//2:]

    l1 = merge_sort(l1)
    l2 = merge_sort(l2)

    return merge(l1, l2)


def merge(l1, l2):
    l3 = list()

    while(l1 and l2):
        if(l1[0] > l2[0]):
            l3.append(l2[0])
            l2.pop(0)
        else:
            l3.append(l1[0])
            l1.pop(0)

    while(l1):
        l3.append(l1[0])
        l1.pop(0)

    while(l2):
        l3.append(l2[0])
        l2.pop(0)

    return l3


def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

def fib(n):
    if n == 0 or n == 1:
        return 1

    return fib(n-1)+fib(n-2)


def str_reverse(s):
    # reverse a string "abcde" to "edcba", recursively
    if len(s) <= 1:
        return s
    return str_reverse(s[1:]) + s[0]


print(merge_sort([5,1,4,3,10,21,2,8]))
for n in range(10):
    print(fib(n))
print(str_reverse('abcdefg'))