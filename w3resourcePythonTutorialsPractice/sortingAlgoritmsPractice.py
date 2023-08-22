def merge(left, right):

    print("Merge Function")
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break
    print('result',result)
    return result

def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    print('Merge Sort Function')
    print(array)
    if len(array) < 2:
        return array

    midpoint = len(array) // 2
    print(midpoint)

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

list2=[534,67,8,4,5,6,7,8,9,2,2,3,45,5,666]
# print(len(list2))

finaleList=merge_sort(list2)
print(finaleList)