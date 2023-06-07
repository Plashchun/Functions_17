def change(lst):
 lst[0], lst[-1] = lst[-1], lst[0]
lst = [5, 8, 14, 1, 89]
change(lst)
print(lst)

def to_dict(lst):
    return {element: element for element in lst}
print(to_dict([5, 6, 8, 9]))


def sum_range(start, end):
    if start > end:
        end, start = start, end
    return sum(range(start, end + 1))
print(sum_range(1, 4))