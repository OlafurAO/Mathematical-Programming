def problem_one(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1;

    return problem_one_recursive(0, 1, 1, 0, 3, n);


def problem_one_recursive(t1, t2, t3, sum, count, n):
    if(count == n):
        return sum;

    sum = t1 + t2 + t3;
    t1, t2, t3 = t2, t3, sum;

    return problem_one_recursive(t1, t2, t3, sum, count + 1, n);

def problem_two(n):
    if(n < 0):
        return 0;

    memo = {0: 0, 1: 0, 2: 1};

    if n in memo:
        return memo[n];
    else:
        value = problem_two(n - 1) + problem_two(n - 2) + problem_two(n - 3);
        memo.update({ n: value});
        return memo[n];

def problem_three(n):
    T = [0, 0, 1] + [0] * (n - 2);

    for i in range(3, n + 1):
        T[i] = T[i - 1] + T[i - 2] + T[i - 3];

    return T[n]

def problem_four(n):
    if n <= 1:
        return 0;

    t3, t2, t1 = 1, 0, 0

    for i in range(3,n+1):
        t3, t2, t1 = t3 + t2 + t1, t3, t2;

    return t3;

def problem_five(n):



def main():
    print(problem_one(8));
    print(problem_two(8));
    print(problem_three(8));
    print(problem_four(8));

if __name__ == '__main__':
    main();