import random
A = [random.randint(1, 99999) for _ in range(1000)]
list_cach_1 = A.copy()
list_cach_2 = A.copy()

# CÁCH 1: Sử dụng hàm sorted() 
sorted_list_1 = sorted(list_cach_1)

# CÁCH 2: Không sử dụng hàm sorted() 
def manual_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

sorted_list_2 = manual_sort(list_cach_2)

# --- KIỂM TRA KẾT QUẢ ---
print("Kết quả 10 phần tử đầu tiên sau khi sắp xếp:")
print(f"Cách 1 (hàm sorted): {sorted_list_1[:10]}")
print(f"Cách 2 (không sd hàm sorted): {sorted_list_2[:10]}")

if sorted_list_1 == sorted_list_2:
    print("=> Cả hai cách đều cho kết quả chính xác!")