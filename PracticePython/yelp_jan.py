
# neighborhood of houses, max only 2 houses, optimal reward
# cant hit two houses next to each other

# neighborhood of houses --> arr of nodes
# nodes have value property
# return val ===> Max (int)



def house_robber(arr):

    max_1 = None
    max_2 = None

    for val in arr:

        if max_1 == None:
            max_1 = val
            max_2 = val

        if max_1 < val:
            max_2 = max_1
            max_1 = val
            print(f"max_1: {max_1}")
            print(f"max_2: {max_2}")
            continue

        if max_2 < val:
            max_2 = val

        print(f"max_1: {max_1}")
        print(f"max_2: {max_2}")

    return (sum([max_1,max_2]))

if __name__ == "__main__":

    arr = [1,2,3]
    print(house_robber(arr))
