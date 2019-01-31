def m4p1(p):
    inversion_count = 0;

    for i in range(0, len(p)):
        for k in range(i + 1, len(p)):
            if(p[i] > p[k]):
                inversion_count += 1;

    return inversion_count;

def m4p2(p):
    descent_count = 0;

    for i in range(0, len(p) - 1):
        if(p[i] > p[i + 1]):
            descent_count += 1;

    return descent_count;

def m4p3(n):
    perm_count = 0;

    #for i in Permutations(n):

'''
def m4p4(p, cl):
    sequence = [];
    count = 0;

    for i in p:
        for j in p:
            if(i > j):
                if(i - j == cl[count]):
                    sequence.append(i-j);
                    count += 1;
            else:
                if(j - i == cl[count]):
                    sequence.append(j - i);
                    count += 1;

            if(len(sequence) == len(cl)):
                return sequence == cl;

    return sequence == cl;
'''

def m4p4(p, cl):
    complete_list = [];
    count = 0;
    current = 0;

    for i in range(0, len(p)):
        current = i;
        for j in range(i, len(p)):
            if(count >= len(cl) - 1):
                for c in complete_list:
                    print(c)
                return True;

            if(cl[count] > cl[count + 1]):
                if(p[current] > p[j]):
                    complete_list.append((p[current], p[j]));
                    count += 1;
                    current = j;
                    continue;


            if(cl[count] < cl[count + 1]):
                if(p[current] < p[j]):
                    complete_list.append((p[current], p[j]));
                    count += 1;
                    current = j;
                    continue;





def m4p5(p):
    for i in range(0, len(p) - 1):
        if(p[i] > p[i + 1]):
            for j in range(i + 1, len(p)):
                if(p[i] > p[j]):
                    p[i], p[j] = p[j], p[i];
                    i += 1;
                else:
                    break;
    return p;

def m4p7(p):
    std_list = [0] * len(p);

    for i in range(0, len(p)):
        count = len(p);
        for j in range(0, len(p)):
            if(p[i] < p[j]):
                count -= 1;
        std_list[i] = count;

    return std_list;

def main():
    #print(m4p1(([2,4,1,5,3])));
    #print(m4p2(([2, 4, 1, 5, 3])));
    #print(m4p4([1,5,2,4,3], [3,1,2]));
    #print(m4p4([6, 13, 9, 17, 15, 2, 4, 14, 12, 3, 16, 10, 1, 8, 5, 18, 7, 11], [1, 3, 2, 4]));
    #print(m4p5(([5,3,2,6,1,4])));
    #print(m4p5([3, 22, 17, 9, 15, 5, 4, 13, 23, 11, 21, 19, 6, 7, 16, 18, 10, 12, 14, 2, 8, 20, 1]));
    #print(m4p7([1,3,7,5]));


if __name__ == '__main__':
    main();