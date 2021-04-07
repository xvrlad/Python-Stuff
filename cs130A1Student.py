import csv

# Question 01
def get_longest_common_name(vernacular_names):
    common_names_list = vernacular_names.split("|")
    longest_name = common_names_list[0]
    if longest_name.isspace() or longest_name == "":
        return None
    for list_index in range(1,len(common_names_list)):
        if len(common_names_list[list_index]) > len(longest_name):
            longest_name = common_names_list[list_index]
    return longest_name

# Question 02
def get_classification_hierarchy(classification_ranks, classifications):
    classification_ranks_list = classification_ranks.split("|")
    classifications_list = classifications.split("|")
    if len(classification_ranks_list) != len(classifications_list):
        print("ERROR: Invalid input, classification ranks do not match classifications!")
        return []
    return [(rank, class_name) for (rank, class_name) in zip(classification_ranks_list,classifications_list)]

# Question 03
def get_biostatus(biostatus_string):
    interested_cases = ["Endemic", "Non-endemic", "Exotic", "Indigenous"]
    biostatus_list = biostatus_string.split("|")
    for case in biostatus_list:
        if case in interested_cases:
            return case
    return "N/A"

# Question 04
class Ave:
    def __init__(self, scientific_name, common_name, biostatus, classification_hierarchy):
        self.__scientific_name = scientific_name
        self.__common_name = common_name
        self.__biostatus = biostatus
        self.__classification_hierarchy = classification_hierarchy

    def __str__(self):
        return f"{self.__common_name}, Status = {self.__biostatus}"

    def __repr__(self):
        return f"Ave<{self.__scientific_name}>"

    def __lt__(self, other):
        return other.__scientific_name > self.__scientific_name

    def __eq__(self, other):
        return other.__scientific_name == self.__scientific_name and other.__common_name == self.__common_name and other.__biostatus == self.__biostatus and other.__classification_hierarchy == self.__classification_hierarchy

    def find_in_classification_hierarchy(self, classification_rank):
        for hierarchy_tuple in self.__classification_hierarchy:
            if classification_rank in hierarchy_tuple:
                return hierarchy_tuple[1]
        return None

    def lowest_classification_rank(self):
        return self.__classification_hierarchy[0][0]

    def get_scientific_name(self):
        return self.__scientific_name

    def get_common_name(self):
        return self.__common_name

    def get_biostatus(self):
        return self.__biostatus

# Question 05
class BirdDatasetReader:

    def __init__(self, csv_filename):
        self.__csv_filename = csv_filename

    # Question 01
    def get_longest_common_name(self, vernacular_names):
        common_names_list = vernacular_names.split("|")
        longest_name = common_names_list[0]
        if longest_name.isspace() or longest_name == "":
            return None
        for list_index in range(1, len(common_names_list)):
            if len(common_names_list[list_index]) > len(longest_name):
                longest_name = common_names_list[list_index]
        return longest_name

    # Question 02
    def get_classification_hierarchy(self, classification_ranks, classifications):
        classification_ranks_list = classification_ranks.split("|")
        classifications_list = classifications.split("|")
        if len(classification_ranks_list) != len(classifications_list):
            print("ERROR: Invalid input, classification ranks do not match classifications!")
            return []
        return [(rank, class_name) for (rank, class_name) in zip(classification_ranks_list, classifications_list)]

    # Question 03
    def get_biostatus(self, biostatus_string):
        interested_cases = ["Endemic", "Non-endemic", "Exotic", "Indigenous"]
        biostatus_list = biostatus_string.split("|")
        for case in biostatus_list:
            if case in interested_cases:
                return case
        return "N/A"

    def read_birds_dataset(self):
        # TODO: start from here and fully implement this method
        try:
            ave_list = []

            csvfile = open(self.__csv_filename, mode='r')
            csv_dict_reader = csv.DictReader(csvfile)
            for data_row_dictionary in csv_dict_reader:
                common_name = self.get_longest_common_name(data_row_dictionary["VernacularNamesForScientific"])
                classification_hierarchy = self.get_classification_hierarchy(data_row_dictionary["ClassificationRanks"], data_row_dictionary["Classification"])
                biostatus = self.get_biostatus(data_row_dictionary["Biostatus"])
                if common_name == None:
                    common_name = data_row_dictionary["ScientificName"]
                ave_list.append(Ave(data_row_dictionary["ScientificName"], common_name, biostatus, classification_hierarchy))
            ###
            index = 1
            for row in csv_dict_reader:
                if index <= 10:
                    print(index, row['ScientificName'])
                index += 1
            ###
            csvfile.close()
            return ave_list
        except FileNotFoundError:
            print(f"ERROR: File '{self.__csv_filename}' not found!")
            return []

# Question 06
def consistency_check(all_aves):
    index = 0
    passed_check = True
    for ave_object in all_aves:
        index += 1
        lowest_classification = ave_object.find_in_classification_hierarchy(ave_object.lowest_classification_rank())
        if not ave_object.get_scientific_name() == lowest_classification:
            print(f"Inconsistency found for bird #{index} in the list! {ave_object.get_scientific_name()} vs {lowest_classification}")
            passed_check = False
    return passed_check

# Question 07
def print_histogram_of_biostatuses(all_aves):
    histogram_dict = {}
    for ave_object in all_aves:
        if ave_object.get_biostatus() not in histogram_dict:
            histogram_dict[ave_object.get_biostatus()] = 0
        histogram_dict[ave_object.get_biostatus()] += 1
    print("Histogram of biostatus entries:")
    histogram_key_list = list(histogram_dict.keys())
    histogram_key_list.sort()
    for key in histogram_key_list:
        print(f"{key:<12}: {histogram_dict[key]}")
    return

# Question 08
def get_birds_with_specific_classification(all_aves, classification_rank, classification):
    specific_aves = []
    for ave_object in all_aves:
        family = ave_object.find_in_classification_hierarchy(classification_rank)
        if classification == family:
            specific_aves.append(ave_object)
    return specific_aves

# Question 09
def find_bird_by_scientific_name_binary_search(all_aves_sorted, scientific_name):
    return_tuple = None, 0
    min_index = 0
    max_index = len(all_aves_sorted) - 1
    if max_index < min_index:
        return return_tuple
    mid_index_count = 0
    while (min_index <= max_index):
        mid_index = (max_index + min_index) // 2
        mid_index_count += 1
        if all_aves_sorted[mid_index].get_scientific_name() == scientific_name:
            return_tuple = all_aves_sorted[mid_index], mid_index_count
            return return_tuple
        elif all_aves_sorted[mid_index].get_scientific_name() < scientific_name:
            min_index = mid_index + 1
        elif all_aves_sorted[mid_index].get_scientific_name() > scientific_name:
            max_index = mid_index - 1
    return return_tuple



# Below are a number of unit tests which your code has to fulfill. If you are interested in how this works, consider
# looking at the documentation of the Python unittest module. However, you don't have to change anything below here,
# just make sure that when you execute this class through Python command line or an IDE like IDLE, you receive the
# message:
# Ran 2 tests in x.xxx seconds.
# OK

import unittest

class TestBirdsMethods(unittest.TestCase):

    def test_0_read_csvfile(self):
        csv_filename = 'NZOR-BirdsTaxonomicExcerpt_15only.csv'
        reader = BirdDatasetReader(csv_filename)
        all_aves = reader.read_birds_dataset()
        self.assertEqual(repr(all_aves), "[Ave<Callaeas cinerea>, Ave<Hirundapus>, Ave<Leucocarbo colensoi>, Ave<Egretta alba>, Ave<Vanellus miles>, Ave<Thalasseus>, Ave<Anthus novaeseelandiae>, Ave<Callaeas>, Ave<Rallus pectoralis muelleri>, Ave<Procellaria>, Ave<Emeidae>, Ave<Puffinus puffinus puffinus>, Ave<Phalaropus fulicarius>, Ave<Porzana>, Ave<Anas>]")

    def test_1_find_all_birds(self):
        csv_filename = 'NZOR-BirdsTaxonomicExcerpt.csv'
        reader = BirdDatasetReader(csv_filename)
        all_aves = reader.read_birds_dataset()
        all_aves_sorted = sorted(all_aves)
        largest_number_of_search_steps = -1000
        smallest_number_of_search_steps = 1000
        index = 0
        for ave in all_aves:
            bird, nr_search_steps = find_bird_by_scientific_name_binary_search(all_aves_sorted, ave.get_scientific_name())
            index += 1
            if nr_search_steps > largest_number_of_search_steps:
                largest_number_of_search_steps = nr_search_steps
            if nr_search_steps < smallest_number_of_search_steps:
                smallest_number_of_search_steps = nr_search_steps
        self.assertEqual(largest_number_of_search_steps, 11)
        self.assertEqual(smallest_number_of_search_steps, 1)

if __name__ == "__main__":
    unittest.main(verbosity=0)