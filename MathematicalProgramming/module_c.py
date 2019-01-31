def mCp3(x, y):
    counter = 0
    for i in range(0,len(x)):
        if x[i] != y[i]:
            counter += 1
    return counter

def mCp4(x, y):
    counter = 0

    for i in range(0, len(x)):
        if x[i] != y[i]:
            counter += 1

    loop_one = counter;
    counter = 0;

    for i in range(len(x)):
        if(x[i] != y[i]):
            for j in range(i, len(y) - 1):
                y[j] = y[j + 1];

            counter += 1;
            y[len(y) - 1] = 0;

            if (x[i] == 1):
                counter += 1;
                y[i] = 1;

            if (x[i] == 0):
                counter += 1;
                y[i] = 0;

    if (counter < loop_one):
        return counter;
    else:
        return loop_one;

def mCp7(L, J):
    lowest = 0
    nearestNeig = 0
    Jtuple = [tuple(l) for l in J] * len(J)
    J.append(0);

    for i in range(0, len(J[0]) - 1):
        for j in range(0, len(L) - 1):
            dist = mCp3(L[j][0], J[0])

            if lowest == 0:
                lowest = dist
                nearestNeig = L[j]

            elif lowest > dist:
                lowest = dist
                nearestNeig = L[j]

        J[1] = nearestNeig[1]
        lowest = 0

    return list(tuple((list(J[0]), J[1])));

def main():
    print(mCp4([1, 0, 1, 0], [1, 1, 0, 1]));
    print(mCp4([1, 0, 1, 0, 0, 0, 1, 0, 0], [1, 1, 0, 1, 0, 1, 1, 0, 1]));

    L = [([1, 1, 1], 2), \
         ([0, 0, 0], 1), \
         ([1, 0, 1], 2), \
         ([0, 0, -1], 1)]

    J = [[1, 1, 0]]

    print(mCp7(L, J));
    #print(mCp7([([0, 0], 6), ([0, 0], 0), ([1, 0], 4), ([1, 0], 6), ([1, 1], 5), ([0, 0], 1), ([0, 1], 5), ([0, 0], 5), ([0, 1], 5), ([0, 1], 3)], [[1, 1], [0, 0], [1, 0], [1, 0], [0, 1], [0, 1], [0, 0], [0, 1], [0, 1], [1, 0]]));


main();