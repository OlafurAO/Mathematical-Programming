def m3p1(L):
    x_sum = 0;
    y_sum = 0;

    for i in L:
        x_sum += i[0];
        y_sum += i[1];

    x_sum = float(round(x_sum/len(L), 2))
    y_sum = float(round(y_sum/len(L), 2))

    return (x_sum, y_sum);

def m3p2(p, q):
    import math;
    sum = 0;

    for i in range(0, len(p)):
        sum += (q[i] - p[i])**2;

    sum = math.sqrt(sum);
    sum = float(round(sum, 2))

    return sum;

def m3p3(p,q):
    sum = 0;

    for i in range(0, len(p)):
        result = p[i] - q[i];

        if (result < 0):
            sum += -result;
        else:
            sum += result;

    return float(round(sum, 2));

def m3p4(sites, gridsize, B, f = 1/2, g = 1, d = m3p3):
    initial_grid = initialize_grid(gridsize);
    complete_grid = [];
    initial_grid_count = 0;
    row_list = [];

    equation_p1 = 0;
    equation_p2 = 0;
    total = 0;

    for x in range(0, gridsize[0]):
        for y in range(0, gridsize[1]):
            total = 0;

            for site in sites:
                cell = d(initial_grid[initial_grid_count], site);

                if(cell > B):
                    total += 1 / (cell)**f
                else:
                    total += ((1 - 0)) * B**(g-f) / (2 * B - cell)**g

            total = float(round(total, 2));

            row_list.append(total);
            initial_grid_count += 1;

        complete_grid.append(row_list);
        row_list = [];

    return complete_grid;

def initialize_grid(size):
    grid = [];
    cell = ();
    x = 0;
    y = 0;

    for i in range(0, size[0]):
        for i in range(0, size[1]):
            cell = (x, y);
            grid.append(cell);
            y += 1;

        x += 1;
        y = 0;

    return grid;

def m3p5(sites, gridsize, B):
    initial_grid = initialize_grid(gridsize);
    grid = m3p4(sites, gridsize, B);

    result = [];
    highest_value = 0;

    for i in grid:
        for j in i:
            if(j > highest_value):
                highest_value = j;

    for i in initial_grid:
        if(grid[i[0]][i[1]] == highest_value):
            result.append(i);

    return set(result);

def main():
    #print(m3p1([(17,3), (3,15), (27,19), (22,21), (18,25)]));
    #print(m3p2((1,1), (3,2)));
    #print(m3p3((1,1), (3,2)));
    #print(m3p4([(27, 3), (12, 21), (7, 25), (29, 3), (9, 19), (22, 14), (11, 8)], (30, 30), 6));
    #print(m3p5([(2, 9), (5, 18), (26, 4), (4, 6), (20, 28)], (30, 30), 9));
    print(m3p5([(0, 0), (2, 2)], (3, 3), 1))


if __name__ == '__main__':
    main();