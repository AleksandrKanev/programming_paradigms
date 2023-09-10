def sort_list_imperative(numbers):
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
          
    return numbers

def sort_list_declarative(numbers: list):
    numbers.sort(reverse=True)
    return numbers


numbers = [1,2,3,5,4,4]
numbers1 = [1,2,3,5,4,4]
print(sort_list_imperative(numbers))
print(sort_list_declarative(numbers1))