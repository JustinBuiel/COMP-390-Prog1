This is individual programming project 1; get the biggest meteors from the dataset.

The main driver program iterates through the dataset, passing each line to the utility functions get_data and separate_data to create a dictionary of dictionaries of all the data.

The data is carefully separated  by each value while placing "N/A" in place of any missing data to avoid any confusion.

Then the all_data dictionary is combed through to find the datapoints that satisfy the specifications of 2013 and newer AND 2,900,000g and larger, separately, dictionary comprehension is used to remove any null values leftover after the filtering is complete
