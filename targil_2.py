def special_percentile(precent ,numbers):
    '''
     calculate percentile of numbers
    :param precent: int
    :param numbers: list
    :return: return the first number in the list that has the highest percentile
    '''
    after_sorted = sorted(numbers)
    position = precent/ 100 * len(after_sorted)
    index = int(position)
    return after_sorted[index]
print(special_percentile(25,[50,10,40,30,20]))
print(special_percentile(50,[9,1,7,3]))


