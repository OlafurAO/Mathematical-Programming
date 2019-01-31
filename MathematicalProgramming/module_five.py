def m5p3(U, S):
    index = 0;
    counter = 0;
    list_counter = 0;

    #print(len(U))

    while(index != len(U)):
        for i in S:
            for j in i:

                if(j == U[index]):
                    index += 1;
                    print(j);
                    print(i)
            if(index > 0 and list_counter > 0):
                counter += 1;

            list_counter += 1;

    return counter - 1;



def main():
    #print(m5p3([1, 2, 3, 4, 5], [[1, 2, 3], [2, 4], [3, 4], [4, 5]]));
    print(m5p3([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [[0, 2, 3, 4, 5, 6, 8, 11, 12, 16, 17], [1, 3, 4, 6, 7, 9, 10, 13, 14, 15, 16, 17], [0, 1, 2, 4, 6, 8, 9, 11, 13, 15, 16], [0, 1, 2, 8, 10, 11, 13, 14, 16, 17], [4, 5, 6, 7, 10, 14, 15, 16], [1, 2, 4, 5, 6, 8, 10, 12, 15, 16, 17], [0, 1, 3, 5, 7, 9, 11, 12, 13, 16]]));

if __name__ == '__main__':
    main();

