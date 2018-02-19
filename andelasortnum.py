def my_sort(numbers):
     odd  = [n for n in numbers if n % 2 != 0]
     even = [n for n in numbers if n % 2 == 0]
     return sorted(odd) + sorted(even)

b = [1,2,3,4,5,6,7,8,9,10]

print my_sort(b)
