def maopaosort(alist):
    n = len(alist)
    for i in range(n-1):
        count = 0
        for j in range(n-1-i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                count += 1
        if count == 0:
            break
    return alist

def quick_sort(alist):
    n = len(alist)
    for i in range(n):
        left, right = i, n-1
        flag = 0
        count = alist[right]
        while left < right:
            while flag == left and alist[left] > count:
                alist[left], alist[right] = alist[right], alist[left]
                count = alist[right]
            left += 1
            flag = right
            while flag == left and alist[left] < count:
                right -= 1
                count = alist[right]
            while flag == right and alist[left] > count:
                alist[right], alist[left] = alist[left], alist[right]
                count = alist[left]
            right -= 1
            flag = left
            while flag == right and alist[left] < count:
                left += 1
                count = alist[left]
        print(i)
        print("*")
        print(alist)

if __name__ =="__main__":
    alist = [54, 26, 93, 77, 43, 44, 44, 31, 44, 55, 20]