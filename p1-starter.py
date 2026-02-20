# Name: Sofia Samai
# Student ID:
# Email: sbsamai@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.
# e.g.:
# Asked ChatGPT hints for debugging and suggesting the general structure of the code
# Did your use of GenAI on this assignment align with your goals and guidelines in 
#    your Gen AI contract? If not, why?

import os
import csv


def read_penguins(filename:str):
 
    source_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(source_dir, filename)
    f = open(full_path)
    csv_f = csv.reader(f)

    return csv_f


# function 1

def avg_female_adelie_bill_length(filename:str):
    total = 0
    count = 0

    csv_f = read_penguins(filename)

    headers = next(csv_f)
    for row in csv_f:
        species = row[1]
        sex = row[7]
        bill_length = row[3]

        if (
            species == "Adelie" and
            sex == "female" and
            bill_length != "NA" and
            bill_length != ""
        ):
            total += float(bill_length)
            count += 1

    if count == 0:
        return None
    avg_bill = total / count
    return avg_bill



# # function 2

def dream_male_weight(filename:str):
    count = 0

    csv_f = read_penguins(filename)

    for row in csv_f:
        sex = row[7]
        island = row[2]
        body_mass = row[6]

        if (
            sex == "male" and
            island == "Dream" and
            body_mass != "NA" and 
            body_mass != ""

        ):
            if float(body_mass) >= 4500:
                count += 1
    return count


# alia's functions

# function 1

def female_chinstrap_birthyear_2008(filename:str):
       count = 0
       for row in csv_f:
            sex = row[7]
            species = row[1]
            birth_year = row[8]

        if (
            sex == "female" and
            species == "Chinstrap" and
            birth_year == 2008
        ):
        return count


# function 2


def gentoo_female_avg_flipper_after_2007(filename:str):
    total = 0
    count = 0

    for row in csv_f:
        sex = row[7]
        species = row[1]
        flipper_length = row[5]
        birth_year = row[8]

        if (
            sex == "female" and
            species == "Gentoo" and
            flipper_length != "NA" and 
            flipper_length != "" and
            birth_year > 2007

        ):
            total += float(flipper_length)
            count += 1

    if count == 0:
        return None
    avg_flipper_length = total / count
    return avg_flipper_length
        


# write outputs to a .txt file


def write_results_to_file(input_filename, output_file = "penguin_results.txt"):
    
    source_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(source_dir, output_file)

    avg_bill_female = avg_female_adelie_bill_length(input_filename)
    dream_males = dream_male_weight(input_filename)

    with open(output_path, "w") as csv_f:
        csv_f.write(f"The results of the first two functions are as follows: ")
        csv_f.write(f"The average bill length of female Adelie penguins is: {avg_bill_female:.2f} mm\n")
        csv_f.write(f"The number of male penguins on Dream Island that weight more than 4500 g is: {dream_males}\n")
        csv_f.write("\n\n")


import unittest

class TestPenguinFunctions(unittest.TestCase):


    # function 1 test cases
    def setUp(self):
        self.filename = "penguin_subset1.csv"
        self.filename2 = "penguin_subset2.csv"

    # general case
    def test_general_avg_female_adelie_bill_length(self):

        self.assertAlmostEqual(avg_female_adelie_bill_length(self.filename), 38.37, places=2) # hard code value you find using a calculator
   
    # edge case
    def test_edge_avg_female_adelie_bill_length(self):

        self.assertNotEqual(avg_female_adelie_bill_length(self.filename), 38.73) # wrong value including males
    # function 2 test cases

    # general case

    def test_general_dream_male_weight(self):
        self.assertEqual(dream_male_weight(self.filename2), 2)


    # edge case
    def test_edge_dream_male_weight(self):
      self.assertNotEqual(dream_male_weight(self.filename2),4) # wrong value from all islands

    def write_to_file(self):
        write_results_to_file(self.filename)


def main():
    filename = "penguins.csv"
    write_results_to_file(filename)
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
