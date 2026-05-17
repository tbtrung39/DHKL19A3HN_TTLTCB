n = int(input("Nhập n (bậc ma trận đơn vị): "))

identity_matrix = []
for i in range(n):
    hang = []
    for j in range(n):
        if i == j:
            hang.append(1)
        else:
            hang.append(0)
    identity_matrix.append(hang)

print("Ma trận đơn vị bậc", n, ":")
for i in range(len(identity_matrix)):
    print(identity_matrix[i])
