import numpy as np
import pandas as pd

if __name__ == '__main__':

    # ----------------------Fives Analysis--------------------------

    a_collection = np.arange(1, 43, 1)
    b_collection = np.arange(1, 43, 1)
    c_collection = np.arange(1, 43, 1)
    d_collection = np.arange(1, 43, 1)
    e_collection = np.arange(1, 43, 1)

    # Create list with all pairs
    pairs = []
    for a in a_collection:
        for b in b_collection:
            for c in c_collection:
                for d in d_collection:
                    for e in e_collection:
                        pairs.append([a, b, c, d, e])

    print('List with all pairs created')

    # Delete doubles
    new_pairs = []
    for pair in pairs:
        if pair[0] != pair[1] and pair[1] != pair[2] and pair[2] != pair[3] and pair[3] != pair[4] \
                and pair[0] != pair[2] and pair[0] != pair[3] and pair[1] != pair[3] and pair[0] != pair[4] \
                and pair[1] != pair[4] and pair[2] != pair[4]:
            new_pairs.append(pair)

    pairs = new_pairs

    print('Deleted duplicate values')

    # Delete fives
    for pair in pairs:
        pair.sort()

    pairs.sort()

    unic_pairs_numbers = np.arange(0, 102080160, 120)
    new_pairs = []
    for number in unic_pairs_numbers:
        new_pairs.append(pairs[number])

    pairs = new_pairs

    print('Deleted fives')

    np.savetxt("all_fives_p1.csv",
               pairs[0:425334],
               delimiter=", ",
               fmt='% s')

    np.savetxt("all_fives_p2.csv",
               pairs[425335::],
               delimiter=", ",
               fmt='% s')


