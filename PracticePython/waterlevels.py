


def water_levels(array):

    end = array[::-1][0]

    iterator = array[0]

    sum = 0

    for index, wall in enumerate(array):

        if wall == 0:
            iterator == array[index + 1]
            continue

        elif iterator < wall:
            iterator = wall

        elif wall > array[index + 1]:
            sum += wall - array[index + 1]


        print("iterator:", iterator + "at ", index)
        print("wall:", wall, "at", index )
        


        # print("index {}".format(index))
        # print("wall:", wall)

    print(sum)

water_levels([2,0,1,6,2,4,8,9])
