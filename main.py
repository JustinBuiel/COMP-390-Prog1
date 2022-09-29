import utility_functions


def main():
    # initialize variables
    all_data = {}
    year_filtered = {}
    mass_filtered = {}
    name_label = "NAME"
    mass_label = "MASS (g)"
    year_label = "YEAR"
    # start reading data and clear the first line
    data = open("meteorite_landings_data.txt")
    data.readline()

    # main loop of reading a new line and getting all the data into the all_data dictionary
    while 1:
        line = data.readline()
        if line == "":
            break
        # dynamically create keys for each new dictionary that is returned
        all_data[len(all_data)] = utility_functions.get_data(line)

    data.close()

    # filter the data into the 2 new dictionaries for easy printing
    for i in iter(all_data):
        year_filtered[len(year_filtered)] = utility_functions.get_recent(all_data[i])
        mass_filtered[len(mass_filtered)] = utility_functions.get_large(all_data[i])

    # remove any datapoints that didn't match the specifications
    year_filtered = {
        key: value for key, value in year_filtered.items() if value is not None
    }
    mass_filtered = {
        key: value for key, value in mass_filtered.items() if value is not None
    }

    count = 1
    # print the two tables formatted neatly
    print(f'{name_label:<24}{mass_label:<20}')
    print("========================================")
    for i in mass_filtered:
        print(f'{count:<4}{mass_filtered[i]["name"]:<24}{mass_filtered[i]["mass"]:<20}')
        count += 1

    print("\n\n")
    count = 1
    print(f'{name_label:<26}{year_label:<14}')
    print("====================================")
    for i in year_filtered:
        print(f'{count:<4}{year_filtered[i]["name"]:<26}{year_filtered[i]["year"]:<14}')
        count += 1


if __name__ == '__main__':
    main()
