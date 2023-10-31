def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Запросить у пользователя ввод чисел, разделенных пробелом
user_input = input("Введите числа, разделенные пробелом: ")
# Преобразовать введенные числа в список
arr = [int(num) for num in user_input.split()]

bubble_sort(arr)
print("Отсортированный массив:")
for i in range(len(arr)):
    print(arr[i], end=" ")
