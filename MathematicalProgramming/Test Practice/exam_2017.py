def problem_one(n):
    if(n <= 0):
        return 1;
    if(n == 1):
        return 0;
    if(n == 2):
        return 2;

    return problem_one_recursive(1, 0, 2, 3, 2, n);

def problem_one_recursive(t1, t2, t3, current, count, n):
    if(count == n):
        return current;

    t1, t2, current, t3  = t2, t3, t3 + 3 * t2 + t1, current;
    t3 = current;

    return problem_one_recursive(t1, t2, t3, current, count + 1, n);

def problem_two(n):
    T = [1, 0, 2] + [0] * (n - 2)

    for i in range(3, n + 1):
        T[i] = T[i - 1] + 3 * T[i - 2] + T[i - 3];

    return T[n];

def problem_three():
    u = 0;

def problem_four():
    u = 0;

def problem_six(fucking_random_num):
    pop = [];
    fuck_andrey = [];

    while(len(fucking_random_num) > 0):
        if(len(fuck_andrey) == 0):
            fuck_andrey.append(fucking_random_num[0]);
            del fucking_random_num[0];

        elif(fuck_andrey[0] > fucking_random_num[0]):
            #fuck_andrey[0], fucking_random_num[0], =
            fuck_andrey.insert(0, fucking_random_num[0]);
            del fucking_random_num[0]

        elif(fuck_andrey[0] <= fucking_random_num[0]):
            pop.append(fuck_andrey);
            fuck_andrey = [];
            fuck_andrey.insert(0, fucking_random_num[0]);
            del fucking_random_num[0];

        print(fuck_andrey)

    pop.append(fuck_andrey);

    new_list = [];

    for i in pop:
        for j in i:
            new_list.append(j);

    fuck_andrey = [];
    fucking_random_num = [];

    return (new_list, fuck_andrey, fucking_random_num);

def problem_eight(n, L):
    grid = [[]] * n

    for i in range(n):
        grid[i] = [0] * n

    for i in L:
        grid[i[0]][i[1]] = 1;

    grid = grid[::-1]

    for i in grid:
        print(i)

    neighbour_count = 0;

    for i in grid:





def main():
    #print(problem_one(6));
    #print(problem_two(6));
    #print(problem_three(3));
    #print(problem_six([5,1,2,4,3]));
    print(problem_eight(10, [(1,1),(2,2)]));

if __name__ == '__main__':
    main();