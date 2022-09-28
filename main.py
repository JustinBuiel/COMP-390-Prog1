import utility_functions


def main():
    data = open("meteorite_landings_data.txt")
    data.readline()
    all_data = {}
    year_filtered = {}
    mass_filtered = {}
    name_label = "NAME"
    mass_label = "MASS (g)"
    year_label = "YEAR"

    while 1:
        line = data.readline()
        if line == "":
            break
        all_data[len(all_data)] = utility_functions.get_data(line)

    data.close()

    for i in iter(all_data):
        year_filtered[len(year_filtered)] = utility_functions.get_recent(all_data[i])
        mass_filtered[len(mass_filtered)] = utility_functions.get_large(all_data[i])

    year_filtered = {
        key: value for key, value in year_filtered.items() if value is not None
    }

    mass_filtered = {
        key: value for key, value in mass_filtered.items() if value is not None
    }

    print(f'{name_label:<24}{mass_label:<20}')
    print("========================================")

    for i in mass_filtered:
        print(f'{mass_filtered[i]["name"]:<24}{mass_filtered[i]["mass"]:<20}')

    print("\n\n")

    print(f'{name_label:<26}{year_label:<14}')
    print("====================================")
    for i in year_filtered:
        print(f'{year_filtered[i]["name"]:<26}{year_filtered[i]["year"]:<14}')


if __name__ == '__main__':
    main()
