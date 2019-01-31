def problem_one(n):
    u = 0;

def problem_two(n):
    current = 1;
    prev = 1;

    sum = 0;

    while(prev < n):
        prev, current = current, current + prev;

        if(current % 2 == 0):
            sum += current;

    return sum;

def main():
    print(problem_two(10))

if __name__ == '__main__':
    main();