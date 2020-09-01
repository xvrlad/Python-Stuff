#q1
def count_code(n):
    total = 0
    i = 0
    count = 2
    count += 1 
    while i < n:
        count +=1 
        total += total
        count +=1 
        j = n - 1
        count += 1
        while j >= 0:
            count += 1
            total /= 2
            count += 1
            total -= 1
            count += 1
            j -= 2
            count += 1
        count += 1
        i += 2
        count += 1
    count += 1
    return total, count

#q3
def get_quartiles(list_of_numbers):
    """Returns the lower and upper quartiles of a set of numbers"""
    try:
        list_copy = sorted(list(list_of_numbers))
        lower_quartile_index = len(list_copy) // 4
        upper_quartile_index = (len(list_copy) * 3) // 4

        lower_quartile = list_copy[lower_quartile_index]
        upper_quartile = list_copy[upper_quartile_index]
    except IndexError:
        return None
    return lower_quartile, upper_quartile

#q4
##needs finishing
def insertion_sort(a_list):	
    for index in range(1, len(a_list)):
        item_to_insert = a_list[index]
        i = index - 1
        while i >= 0 and len(a_list[i]) < len(item_to_insert):
            a_list[i + 1] = a_list[i]
            i -= 1
        a_list[i + 1] = item_to_insert
    return

def main():
    d = ['eyebolts', 'timarau', 'embow', 'sculpted', 'readout']
##    d = ['sculpted', 'eyebolts', 'timarau', 'readout', 'embow']
    insertion_sort(d)
    print(d)
    return

main()
