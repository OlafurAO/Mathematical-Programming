def m1p1(n):
    return sum([i for i in range(1, n) if i % 3 == 0 or i % 5 == 0]);

def m1p2(n):
    current = 1;
    prev = 1;
    sum = 0;

    while prev < n:
        curr_fibo = current + prev;

        if (curr_fibo % 2 == 0 and curr_fibo < n):
            sum += curr_fibo;

        temp = current;
        current += prev;
        prev = temp;

    return sum;

def m1p3(n):
    for i in range(n-1, 2, -1):
        prime_found = True;

        for k in range(i, 2, -1):
            if(i % k == 0 and i != k and i != 1 and k != 1):
                prime_found = False;
                break;

        if(prime_found):
            return i;
    '''
    highest_prime = 0;
    i = 1;

    while(i < n):
        if(n % i == 0):
            highest_prime = i;
        i += 1;
    return highest_prime;
    '''

def m1p4(n):
    highest_pali = 0;
    highest = 0;

    for i in range(1, n + 1):
        highest *= 10;
        highest += 9;

    lowest = int(highest / 10) + 1;

    for i in range(highest, lowest - 1, -1):
        for k in range(i, lowest - 1, -1):
            if (i * k < highest_pali):
                break;

            multiply = i * k;
            reversed = 0;
            temp = multiply;

            while (temp != 0):
                reversed = reversed * 10 + temp % 10;
                temp = int(temp / 10);

            if (reversed == multiply):
                highest_pali = multiply;

    return highest_pali;

def m1p5(n):
    num = 1;

    while True:
        divisable = True;
        for i in range(1, n):
            if(num % i != 0):
                divisable = False;
                break;

        if(divisable):
            return num;
        num += 1;





def m1p6(n):
    return sum([i for i in range(1, n + 1)])**2 - \
           sum([i ** 2 for i in range(1, n + 1)]);

def m1p7(n):
    u = 0;

def m1p8(n, k):
    n = str(n);
    greatest_product = 0;
    current_product = 1;

    for i in range(0, len(n) - k + 1):
        for j in range(i, i + k):
            current_product *= int(n[j]);

        if(current_product > greatest_product):
            greatest_product = current_product;

        current_product = 1;

    return greatest_product;


def m1p9(n):
    for a in range(1, int(n / 3) + 1):
        for b in range(a + 1, int(n / 2) + 1):
            c = n - a - b
            if (a**2 + b**2 == c**2):
                return (a, b, c);

def m1p10(n):
    sum = 0;

    for i in range(2, n):
        prime_check = True;
        for k in range(2, n):
            if(i % k == 0 and i != k):
                prime_check = False;
                break;

        if(prime_check):
            sum += i;

    return sum;

def m1p11(M, k):
    greatest_product = 0;
    product_horizontal = 1;
    product_diagonal = 1;
    product_vertical = 1;
    count = 0;

    #Horizontal
    for i in M:
        for j in i:
            if(count >= k):
                break;

            product_horizontal *= j;
            count += 1;

        if(product_horizontal > greatest_product):
            greatest_product = product_horizontal;

        product_horizontal = 1;
        count = 0;

    #Vertical
    for i in range(0, len(M[0])):
        for j in M:
            if(count >= k):
                break;

            product_vertical *= j[i];
            count += 1;

        if(product_vertical > greatest_product):
            greatest_product = product_vertical;

        product_vertical = 1;
        count = 0;

    #Diagonal
    for i in range(0, len(M)**2 - 1, len(M)):
        for j in M:
            if(count >= k):
                break;

            product_diagonal *= j[i]
            count += 1;
            #print(product_diagonal);

        if(product_diagonal > greatest_product):
            greatest_product = product_diagonal;

    return greatest_product;

def main():
    print('m1p1(50): ' + str(m1p1(50))); #yes
    print('m1p2(50): ' + str(m1p2(50))); #yes
    print('m1p3(50): ' + str(m1p3(500000))); #nope
    print('m1p4(3): ' + str(m1p4(3))); #yes

    print('m1p5(4): ' + str(m1p5(4))); #nope
    print('m1p6(3): ' + str(m1p6(3))); #yes
    print('m1p7(15): ' + str(m1p7(15))); #yes
    print('m1p8(1234567, 4): ' + str(m1p8(1234567, 2)));
    print('m1p9(12): ' + str(m1p9(12))); #yes
    print('m1p10(250): ' + str(m1p10(15))); #yes
    print('m1p11([[3, 1, 1], [1, 3, 2], [1, 2, 3]], 2): ' + str(m1p11([[3, 1, 1], [1, 3, 2], [1, 2, 3]], 2)));  # yes


if __name__ == '__main__':
    main();