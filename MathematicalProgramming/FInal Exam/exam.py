def Ep1(n):
    lis = [];

    for i in range(2, n + 1):
        for j in range(2, n + 1):
            value = i**j;
            lis.append(value)

    return len(set(lis));



def Ep2(n, x, y, s):
    import random;

    death_toll = 0;

    for i in range(1000):
        posX = x;
        posY = y;

        for i in range(s):
            if(posX > n or posY > n or posX < 0 or posY < 0):
                death_toll += 1;
                break;

            direction = random.randint(0, 3);

            #UP
            if(direction == 0):
                posY += 1;

            #DOWN
            elif(direction == 1):
                posY -= 1;

            #RIGHT
            elif(direction == 2):
                posX += 1;

            #LEFT
            elif(direction == 3):
                posX -= 1;

            #print('dir: ' + str(direction) + ', (' + str(posX) + ', ' + str(posY) + ')')


    return death_toll/1000;

import random;
def Ep3(n,x,y,s):
    return sum([Ep3_recursive(n, x, y, s, random.randint(0, 3)) for i in range(1000)])/1000;

def Ep3_recursive(n, x, y, s, direction):
    if(s == 0):
        return 0;

    if(x > n or x < 0 or y > n or y < 0):
        return 1;

    #UP
    if(direction == 0):
        y += 1;

    #DOWN
    elif(direction == 1):
        y -= 1;

    #RIGHT
    elif(direction == 2):
        x += 1;

    #LEFT
    elif(direction == 3):
        x -= 1;

    return Ep3_recursive(n, x, y, s - 1, random.randint(0, 3));







def Ep6(perm):
    stack = [];
    output = [];

    while(len(perm) > 0):
        if(len(stack) == 0):
            stack.append(perm[0]);
            del perm[0];

        elif(len(stack) == 1 and perm[0] < stack[0]):
            stack.append(perm[0]);
            del perm[0];

        elif(len(stack) == 2):
            if(perm[0] < stack[0]):
                if(perm[0] < stack[1]):
                    output.append(perm[0]);
                    del perm[0];

                elif(perm[0] > stack[1]):
                    output.append(stack[1]);
                    stack[1] = perm[0];
                    del perm[0];

            elif(perm[0] > stack[0]):
                output.append(stack[1]);
                output.append(stack[0]);

                stack = [];
                stack.append(perm[0]);
                del perm[0];

    if(len(stack) == 1):
        output.append(stack[0]);
    elif(len(stack) == 2):
        output.append(stack[1]);
        output.append(stack[0]);
        stack = [];

    return output;


def main():
    #print(Ep1(500));
    #print(Ep2(10, 9, 9, 3 ));
    print(Ep3(10, 9, 9, 3 ));
    #print(Ep6([6,4,2,5,8,3,7,1]));

if __name__ == '__main__':
    main();