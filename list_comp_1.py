# list comprehension
def square_numbers(n):
    
    print([x**2 for x in range(n)])


    # so what list comprehensions is, its a simpler way to make lists in python , it makes 
    # list = []
    # for x in range(n):
    #     list.append(x**2)

    # print(list)
    #  make this long code into the one line code above
        

# square_numbers(10)

def remove_spaces():
    list = [' apple', 'banana ', 'cherry   ']
    new_list = [elem.strip() for elem in list]
    print(new_list)

# remove_spaces()

# nested list comprehension

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# to transpose the matrix we can use nested list comprehension

transposed = [[row[i] for row in matrix ] for i in range(4)]

print(transposed)
