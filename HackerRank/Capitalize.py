"""
Make sure names are capitalized
"""
def solve(name):

    name_list = list(name)
    name_list[0] = name_list[0].upper()


    for index, letter in enumerate(name_list):
        if letter == " ":
            name_list[index + 1] = name_list[index + 1].upper()

    name = ''.join(name_list)
    return name



if __name__ == "__main__":
    print(solve("nathan pillai"))
