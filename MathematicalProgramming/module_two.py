def m2p1(n):
    if(n <= 1):
        pass;
    if(n == 2):
        pass;

    return m2p1_recursive(n - 1, 0, 0, 1, 0);

def m2p1_recursive(og_n, n0, n1, n2, count):
    if(count == og_n - 1):
        return n2;
    else:
        param_0 = n1;
        param_1 = n2;
        if(count != 0):
            param_2 = n2 + n1 + n0;
        else:
            param_2 = 1;
        return m2p1_recursive(og_n, param_0, param_1, param_2, count + 1);

memo = {0:0, 1:0, 2:1};

def m2p2(n):
    if(n < 0):
        return 0;

    if(n in memo):
        return memo[n]
    else:
        value = m2p2(n - 1) + m2p2(n - 2) + m2p2(n - 3);
        memo.update({n: value});
        return memo[n];

def m2p3(n):
    T = [0,0,1] + [0] * (n-1);

    for i in range(3,n + 1):
        T[i] = T[i - 1] + T[i - 2] + T[i - 3];

    return T[n]

def m2p4(n):
    num1 = 0;
    num2 = 0;
    num3 = 1;

    for i in range(3, n + 1):
        num3, num2, num1 = num3 + num2 + num1, num3, num2

    return num3;

def m2p5(n, L):
    split_list = [1] + [0] * n;

    for i in L:
        for k in range(i, n + 1):
            split_list[k] += split_list[k - i]

    return split_list[n];

def m2p6(k):
    num_list = range(1, k);
    split_list = [1] + [0] * k;

    for i in num_list:
        for k in range(i, k + 1):
            split_list[k] += split_list[k - i]

    return split_list[k];


def m2p7(k):
    num_of_ways = 0;

    while True:
        for i in Prime():
            bla = 0;


    return num_of_ways;

def m2p9(M):
    current_sum = 0;
    current_pos = [0, 0]

    while(current_pos != [len(M) - 1, len(M) - 1]):
        for i in range()



def m2p9(M):
    current_pos = [0, 0];
    sum = M[current_pos[0]][current_pos[0]];
    '''S
    while current_pos != [len(M) - 1, len(M) - 1]:
        if(current_pos[1] == len(M) - 1):
            current_pos = [current_pos[0] + 1, current_pos[1]];
            sum += M[current_pos[0]][current_pos[1]];
            print(sum)
            continue;

        if(current_pos[0] == len(M) - 1):
            current_pos = [current_pos[0], current_pos[1] + 1];
            sum += M[current_pos[0]][current_pos[1]];
            print(sum)
            continue;

        if(M[current_pos[0]][current_pos[1] + 1] < M[current_pos[0] + 1][current_pos[1]]):
            if(current_pos[1] == len(M) - 1):
                

                for i in range()

            current_pos = [current_pos[0], current_pos[1] + 1]
            sum += M[current_pos[0]][current_pos[1]];

        elif(M[current_pos[0]][current_pos[1] + 1] > M[current_pos[0] + 1][current_pos[1]]):
            current_pos = [current_pos[0] + 1, current_pos[1]];
            sum += M[current_pos[0]][current_pos[1]];

    
        if(M[current_pos[0]][current_pos[1] + 1] + M[current_pos[0] + 1][current_pos[1] + 1]
           < M[current_pos[0] + 1][current_pos[1]] + M[current_pos[0] + 1][current_pos[1] + 1]):
            current_pos = [current_pos[0], current_pos[1] + 1];
            sum += M[current_pos[0]][current_pos[1]];

        elif(M[current_pos[0]][current_pos[1] + 1] + M[current_pos[0] + 1][current_pos[1] + 1]
          > M[current_pos[0] + 1][current_pos[1]] + M[current_pos[0] + 1][current_pos[1] + 1]):
            current_pos = [current_pos[0] + 1, current_pos[1]];
            sum += M[current_pos[0]][current_pos[1]];

        else:
            if(M[current_pos[0] + 1][current_pos[1]] < M[current_pos[0]][current_pos[1] + 1]):
                current_pos = [current_pos[0] + 1, current_pos[1]];
            else:
                current_pos = [current_pos[0], current_pos[1] + 1];
            sum += M[current_pos[0]][current_pos[1]];
        '''

    return sum;

def main():
    print('m2p1(8): ' + str(m2p1(8)));
    print('m2p2(8): ' + str(m2p2(8)));
    print('m2p3(8): ' + str(m2p3(8)));
    print('m2p4(8): ' + str(m2p4(8)));
    print('m2p5(5,[1,2,3]): ' + str(m2p5(5,[1,2,3])));
    print('m2p6(5): ' + str(m2p6(5)));
    print('m2p6(8): ' + str(m2p6(8)));
    print('m2p7(4): ' + str(m2p6(4)));

    print('m2p9([[1,1,9], [9,1,1], [9,9,1]): '  + str(m2p9([[1,1,9],
                                                            [9,1,1],
                                                            [9,9,1]])));
    '''
    print('m2p9([[1,2,9], [9,1,1], [9,9,1]): ' + str(m2p9([[1,2,9],
                                                           [9,1,1],
                                                           [9,9,1]])));
    '''

    print('m2p9(PE matrix): ' + str(m2p9([[131, 673, 234, 103, 18],
                                                           [201, 96,  342, 965, 150],
                                                           [630, 803, 746, 422, 111],
                                                           [537, 699, 497, 121, 956],
                                                           [805, 732, 524, 37, 331]])));


if __name__ == '__main__':
    main();