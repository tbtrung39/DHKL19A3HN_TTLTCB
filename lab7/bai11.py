cpp_students = set(map(int, input("Nhập các số thứ tự sinh viên thi C++ (cách nhau bằng dấu cách): ").split()))
java_students = set(map(int, input("Nhập các số thứ tự sinh viên thi Java (cách nhau bằng dấu cách): ").split()))
python_students = set(map(int, input("Nhập các số thứ tự sinh viên thi Python (cách nhau bằng dấu cách): ").split()))

print("Sinh viên thi C++:", cpp_students)
print("Sinh viên thi Java:", java_students)
print("Sinh viên thi Python:", python_students)

only_cpp = cpp_students.difference(java_students).difference(python_students)
only_java = java_students.difference(cpp_students).difference(python_students)
only_python = python_students.difference(cpp_students).difference(java_students)

cpp_java = cpp_students.intersection(java_students).difference(python_students)
cpp_python = cpp_students.intersection(python_students).difference(java_students)
java_python = java_students.intersection(python_students).difference(cpp_students)

all_three = cpp_students.intersection(java_students).intersection(python_students)

print("\nSinh viên thi riêng C++:", only_cpp)
print("Sinh viên thi riêng Java:", only_java)
print("Sinh viên thi riêng Python:", only_python)

print("\nSinh viên thi C++ và Java:", cpp_java)
print("Sinh viên thi C++ và Python:", cpp_python)
print("Sinh viên thi Java và Python:", java_python)

print("\nSinh viên thi cả 3 ngôn ngữ:", all_three)
