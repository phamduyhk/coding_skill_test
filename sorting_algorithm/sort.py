import random 
import time

def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
    return arr


def sellect_sort(arr):
    for ind, ele in enumerate(arr):
        min_ind = min(range(ind, len(arr)), key=arr.__getitem__)
        arr[ind], arr[min_ind] = arr[min_ind], ele
    return arr


def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        ele = arr[i]
        while arr[j] > ele and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = ele
    return arr



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # ここで分割を行う
    left = arr[:mid]
    right = arr[mid:]

    # 再帰的に分割を行う
    left = merge_sort(left)
    right = merge_sort(right)

    # returnが返ってきたら、結合を行い、結合したものを次に渡す
    return merge(left, right)


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged


def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    # データの状態に左右されないためにrandom.choice()を用いることもある。
    # ref = random.choice(arr)
    ref = arr[0]
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right

def quick_sort_2(arr):
    left = 0
    right = len(arr)
    
    def sort(arr,left,right):
        if left < right:
            i = left
            j = right
            mid = int((left+right)/2)
            pivot = arr[mid]
            while(True):
                while(arr[i]<pivot): i+=1
                while(arr[j]>pivot): j-=1
                if i>=j: break
                # swap i, j
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i += 1
                j -= 1
            sort(arr,left,i-1)
            sort(arr, j+1, right)

    return arr




def count_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    count = [0] * (max_num - min_num + 1)
    for ele in arr:
        count[ele - min_num] += 1

    return [ele for ele, cnt in enumerate(count, start=min_num) for __ in range(cnt)]


if __name__ == "__main__":
    arr = [random.randint(0,100) for i in range(20)]
    print("Array: ", arr)
    start = time.time()
    sorted_arr = quick_sort_2(arr)
    end = time.time()
    print("Sorted array: ", sorted_arr)
    print("Quick Sort Executed time: ", end-start)

    start = time.time()
    sorted_arr = merge_sort(arr)
    end = time.time()
    print("Merge Sort Executed time: ", end-start)

    start = time.time()
    sorted_arr = insert_sort(arr)
    end = time.time()
    print("Insert Sort Executed time: ", end-start)
