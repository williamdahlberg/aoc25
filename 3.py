
def find_biggest_in_bank(bank):
    biggest_ix = 0
    biggest_battery = "0"
    for ix, battery in enumerate(bank):
        if battery > biggest_battery:
            biggest_battery = battery
            biggest_ix = ix
        
        if biggest_battery == 9:
            break
    return biggest_ix, biggest_battery
    

values = []
for bank in map(str.strip, open('3.input')):
    first_big_ix, first_big_value = find_biggest_in_bank(bank)
    if first_big_ix != len(bank) - 1:
        second_big_ix, second_big_value = find_biggest_in_bank(bank[first_big_ix + 1:])
        values.append(int(f"{first_big_value}{second_big_value}"))
    else:
        prev_big_ix, prev_big_value = find_biggest_in_bank(bank[:-1])
        values.append(int(f"{prev_big_value}{first_big_value}"))

print(sum(values))