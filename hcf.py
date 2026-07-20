def search(lst, element):
    if element in lst:
        return lst.index(element)
    else:
        return "Element not found"

numbers = [10, 20, 30, 40, 50]

x = int(input("Enter the element to search: "))

result = search(numbers, x)

print(result)
