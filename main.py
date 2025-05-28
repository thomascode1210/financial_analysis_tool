def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Đã sắp xếp
    pivot = arr[len(arr) // 2]  # Chọn phần tử làm chốt
    left = [x for x in arr if x < pivot]  # Nhỏ hơn chốt
    middle = [x for x in arr if x == pivot]  # Bằng chốt
    right = [x for x in arr if x > pivot]  # Lớn hơn chốt
    return quicksort(left) + middle + quicksort(right)

# Ví dụ sử dụng
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print("Danh sách đã sắp xếp:", sorted_arr)
