
def quicksort(sequence):
    length =len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.appends(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)


print(quicksort([5,6,676,243,7776,8897,554,666,789]))

