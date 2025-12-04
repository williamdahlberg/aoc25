
jolts = []
for bank in map(str.strip, open('3.input')):
    base_jolt = bank[-12:]
    jolt = base_jolt
    min_ix = -1
    for ix, battery in enumerate(base_jolt):
        found = False
        base_bank_ix = len(bank) - 12 + ix
        for test_ix in range(base_bank_ix - 1, min_ix, -1):
            if bank[test_ix] >= battery:
                found = True
                battery = bank[test_ix]
                jolt = jolt[:ix] + bank[test_ix] + jolt[ix + 1:]
                min_ix = test_ix
        if not found:
            min_ix = base_bank_ix

    jolts.append(int(jolt))
print(sum(jolts))