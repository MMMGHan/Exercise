# 输入一个列表和要查询的元素，输出元素所在位置
def halfsearch(alist,x):
    num_list = sorted(alist)
    left, right = 0, len(num_list)
    while left < right:
        mid = (left + right) // 2
        if num_list[mid] > x:
            right = mid
        elif num_list[mid] < x:
            left = mid + 1
        else:
            return mid

if __name__ == "__main__":
    alist = [54, 26, 93, 77, 43, 44, 44, 31, 44, 55, 20]
    print(halfsearch(alist, 44))
