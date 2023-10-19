def reverse_list(arr):
    new_arr = []
    for i in range(len(arr) - 1,-1,-1):
        new_arr.append(arr[i])
    return new_arr

def reverse_list2(arr):
    for i in range(len(arr)//2):
        s = arr[i]
        arr[i] = arr[len(arr) - i - 1]
        arr[len(arr) - i - 1] = s
        print(arr)

    return arr
        

if __name__ == "__main__":
    # print(reverse_list([7,8,9])) # [3,2,1]
    # print(reverse_list([5,6,7,8])) # [4,3,2,1]
    print(reverse_list2([6,8,9]))
