def get_data(string):
    # create a new temp dictionary for each iteration with blank strings so there's no confusion and overwriting old data
    temp = {
        "name": " ",
        "id": " ",
        "nametype": " ",
        "recclass": " ",
        "mass": " ",
        "fall": " ",
        "year": " ",
        "reclat": " ",
        "reclong": " ",
        "geolocation": " ",
        "states": " ",
        "counties": " "
    }

    # go through and separate the data values into the correct keys then get the new, trimmed string
    temp["name"], string = separate_data(string)
    temp["id"], string = separate_data(string)
    temp["nametype"], string = separate_data(string)
    temp["recclass"], string = separate_data(string)
    temp["mass"], string = separate_data(string)
    temp["fall"], string = separate_data(string)
    temp["year"], string = separate_data(string)
    temp["reclat"], string = separate_data(string)
    temp["reclong"], string = separate_data(string)
    temp["geolocation"], string = separate_data(string)
    temp["states"], string = separate_data(string)
    temp["counties"], string = separate_data(string)

    # return temp dictionary into the all_data dictionary (nested)
    return temp


# filter the data according to the specifications, return empty when value is missing or has incorrect data
def get_recent(year_dict):
    if year_dict["year"] == "N/A":
        return
    if 2013 <= int(year_dict["year"]) <= 2022:
        return year_dict
    else:
        return


# filter the data according to the specifications, return empty when value is missing or has incorrect data
def get_large(mass_dict):
    if mass_dict["mass"] == "N/A":
        return
    if float(mass_dict["mass"]) >= 2900000.0:
        return mass_dict
    else:
        return


# function used to read values from text file and put it into temp keys
def separate_data(passed_string):
    new_string = ""
    while passed_string[0] != "\t":
        if passed_string[0] != "\n":
            new_string += passed_string[0]
            passed_string = passed_string[1:]
        else:
            break

    if new_string == "":
        new_string = "N/A"
    if passed_string[0] != "\n":
        passed_string = passed_string[1:]
    return new_string, passed_string
