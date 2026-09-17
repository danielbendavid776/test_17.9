valid_ranks = []
while True:
    try:
        rank = int(input('enter rank: '))
        if rank == -999 and len(valid_ranks) >= 10:
            break
        if rank == -999 and len(valid_ranks) < 10:
            print('need at least 10 valid ranks, keep entering')
        elif rank < 1 or rank > 5:
            print('not in range, skip')
        else:
            valid_ranks.append(rank)
    except ValueError:
        print('invalid input, skip')



average = sum(valid_ranks) / len(valid_ranks)
highest = max(valid_ranks)

print(f'number of valid ranks: {len(valid_ranks)}')
print(f'average rank: {average:.2f}')
print(f'highest rank :{highest}')
print('done')
