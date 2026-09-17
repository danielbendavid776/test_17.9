def special_percentile(precent ,numbers):
    after_sorted = sorted(numbers)
    position = precent/ 100 * len(after_sorted)
    index = int(position)
    return after_sorted[index]
print(special_percentile(25,[50,10,40,30,20]))
print(special_percentile(50,[9,1,7,3]))


