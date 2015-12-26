# This function calculates median of the given list of numbers
# Example [3, 6, 20, 99, 10, 15] => 12.5
# Example [3, 2, 5, 8, 1, 20,7] => 5

def median(list):
    sorted_list = sorted(list)
    count = len(sorted_list)
    idx = int(count/2)

    if count%2 == 0:
        return (sorted_list[idx] + sorted_list[idx-1]) / 2
    else:
        return sorted_list[idx]


