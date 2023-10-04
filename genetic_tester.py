'''Main file for controlling genetic tester'''

#=====Imports=====#
import os
import math
import random

from human import Human


#=====Data=====#
human_list = []
Adam_genetic_code = []
Eve_genetic_code = []
John_genetic_code = []
Sarah_genetic_code = []
Daniel_genetic_code = []
Jessica_genetic_code = []
Phillip_genetic_code = []
Angelique_genetic_code = []

total_genetics = 1000
adam_start = 1
eve_start = 1001
john_start = 2001
sarah_start = 3001
daniel_start = 4001
jessica_start = 5001
phillip_start = 6001
angelique_start = 7001

for a in range(total_genetics):
    Adam_genetic_code.append(adam_start)
    adam_start += 1
    Eve_genetic_code.append(eve_start)  
    eve_start += 1
    John_genetic_code.append(john_start)
    john_start += 1
    Sarah_genetic_code.append(sarah_start)
    sarah_start += 1
    Daniel_genetic_code.append(daniel_start)
    daniel_start += 1
    Jessica_genetic_code.append(jessica_start)
    jessica_start += 1
    Phillip_genetic_code.append(phillip_start)
    phillip_start += 1
    Angelique_genetic_code.append(angelique_start)
    angelique_start += 1

# Create first humans
Adam = Human('Male', Adam_genetic_code, 1, 0, 0)
Eve = Human('Female', Eve_genetic_code, 2, 0, 0)
John = Human('Male', John_genetic_code, 3, 0, 0)
Sarah = Human('Female', Sarah_genetic_code, 4, 0, 0)
Daniel = Human('Male', Daniel_genetic_code, 5, 0, 0)
Jessica = Human('Female', Jessica_genetic_code, 6, 0, 0)
Phillip = Human('Male', Phillip_genetic_code, 7, 0, 0)
Angelique = Human('Female', Angelique_genetic_code, 8, 0, 0)

# Appends Adam and Eve into existence
human_list.append(Adam)
human_list.append(Eve)
human_list.append(John)
human_list.append(Sarah)
human_list.append(Daniel)
human_list.append(Jessica)
human_list.append(Phillip)
human_list.append(Angelique)


#=====Functions=====#

def run_existence():
    """Runs Program"""

    main_window()


def main_window():
    """The main menu"""

    while True:
        os.system("cls || clear")
        print_main_window_options()
        option = input("Option: ")

        # If option equals "1", view_human_list()
        if option == "1":
            view_human_list()

        # else if option equals "2", breed_humans()
        elif option == "2":
            breed_humans()

        # else if option equals "3", exit()
        elif option == "3":
            exit()


def print_main_window_options():
    """Prints the main window options"""

    print('''1. View human list
2. Breed humans
3. Exit
''')
    

def view_human_list():
    """Displays the human list"""
    
    os.system("cls || clear")
    display_all_humans()
    option = input("\nPress Enter to return.")


def display_all_humans():
    """Displays all humans"""

    # Prints header
    print(f"ID{' ' * 3}" 
          + f"SEX{' ' * 5}"
          + f"MOTHER{' ' * 2}"
          + f"FATHER")
    
    # Print human details
    for human in human_list:
        print(f"{human.human_id}{' ' * (5 - len(str(human.human_id)))}"
              + f"{human.sex}{' ' * (8 - len(human.sex))}"
              + f"{human.mother}{' ' * (8 - (len(str(human.mother))))}"
              + f"{human.father}")
        

def display_all_females(male_dna):
    """Display all females.
    
        :param list male_dna: list of male's dna
    """

    # Prints header
    print(f"ID{' ' * 3}" 
          + f"SEX{' ' * 5}"
          + f"MOTHER{' ' * 2}"
          + f"FATHER{' ' * 2}"
          + f"DNA MATCH")
    
    # Print human details
    for human in human_list:
        if human.sex == "Female":
            print(f"{human.human_id}{' ' * (5 - len(str(human.human_id)))}"
                + f"{human.sex}{' ' * (8 - len(human.sex))}"
                + f"{human.mother}{' ' * (8 - (len(str(human.mother))))}"
                + f"{human.father}{' ' * (8 - (len(str(human.father))))}"
                + f"{dna_match(male_dna, human.list_of_genetics)} %")
            

def female_list():
    """Returns a list of all females."""

    list = []

    for human in human_list:
        if human.sex == "Female":
            list.append(human)

    return list

            

def display_all_males(female_dna):
    """Display all females.
    
        :param list female_dna: List of female's dna.
    """

    # Prints header
    print(f"ID{' ' * 3}" 
          + f"SEX{' ' * 5}"
          + f"MOTHER{' ' * 2}"
          + f"FATHER{' ' * 2}"
          + f"DNA MATCH")
    
    # Print human details
    for human in human_list:
        if human.sex == "Male":
            print(f"{human.human_id}{' ' * (5 - len(str(human.human_id)))}"
                + f"{human.sex}{' ' * (8 - len(human.sex))}"
                + f"{human.mother}{' ' * (8 - (len(str(human.mother))))}"
                + f"{human.father}{' ' * (8 - (len(str(human.father))))}"
                + f"{dna_match(female_dna, human.list_of_genetics)} %")
            

def male_list():
    """Returns a list of all males"""

    list = []

    for human in human_list:
        if human.sex == "Male":
            list.append(human)

    return list
            

def dna_match(dna_1, dna_2):
    """Measures the match between two dna's
    
        :param list dna_1: DNA list 1.
        :param list dna_2: DNA list 2.

        :returns: a percentage of match

        :rtype: float.
    """
    # Matches. 1 for match, 0 for non match
    matches = []

    for a in dna_1:
        match_found = False

        for b in dna_2:
            if a == b:
                match_found = True
                matches.append(1)
                break

        if match_found ==  False:
            matches.append(0)
                

    sum = 0
    for numb in matches:
        if numb == 1:
            sum += 1

    percentage = (sum / len(matches)) * 100
    
    return percentage


def get_human_dna(human_id):
    """Gets the genetic code for a specific human.
    
        :returns: list of human's genetic code
        :rtype: list
    """
    for human in human_list:
        if human.human_id == human_id:
            return human.list_of_genetics
        

def breeder(human_id_1, human_id_2):
    """Creates a new human, by mixing DNA of two individuals, generating gender, and adding parent details.
    
        :returns: New human details

        :rtype: list.
    """
    human_1 = None
    human_2 = None
    father = None
    mother = None
    new_dna = None
    new_id = None
    gender = None
    new_human_details = []

    # Gets human 1's Details
    for human in human_list:
        if human_id_1 == human.human_id:
            human_1 = human
            break

    # Gets human 2's details
    for human in human_list:
        if human_id_2 == human.human_id:
            human_2 = human
            break

    # Scramble DNA of parents
    new_dna = genetic_mixer(human_1.list_of_genetics, human_2.list_of_genetics)

    # Checks sex of parents, then add their id as father and mother
    if human_1.sex == "Female":
        mother = human_1.human_id

    elif human_1.sex == "Male":
        father = human_1.human_id

    if human_2.sex == "Female":
        mother = human_2.human_id

    elif human_2.sex == "Male":
        father = human_2.human_id

    new_id = assign_new_id()

    gender = random_gender_generator()

    # Add the new human details
    new_human_details.append(gender)
    new_human_details.append(new_dna)
    new_human_details.append(new_id)
    new_human_details.append(mother)
    new_human_details.append(father)

    return new_human_details


def random_gender_generator():
    """Assigns a new sex"""

    genders = 2
    gender = random.randint(1, 2)

    if gender == 1:
        return "Male"
    
    elif gender == 2:
        return "Female"
    

def assign_new_id():
    """Assigns a new id that has not been used yet"""

    id = 1

    while True:
        id_exists = False

        for human in human_list:
            if human.human_id == id:
                id_exists = True
                id += 1
                break
        
        if id_exists == False:
            break

    return id
        

def genetic_mixer(human_1_dna, human_2_dna):
    """Mixes the DNA of two humans"""
    human_1 = []
    human_2 = []
    new_dna = []

    for h in human_1_dna:
        human_1.append(h)

    for h in human_2_dna:
        human_2.append(h)

    count = int(len(human_1) / 2)
    # Randomly select 50% of the DNA of human 1
    for i in range(int(count)):
        human_1_len = int(len(human_1))
        random_index = int(random.randint(0, (human_1_len - 1)))
        new_dna.append(human_1[random_index])
        del human_1[random_index]

    for i in range(count):
        human_2_len = int(len(human_2))
        random_index = int(random.randint(0, (human_2_len -1)))
        new_dna.append(human_2[random_index])
        del human_2[random_index]

    return new_dna


def breed_humans():
    """Menu for breeding humans"""

    first_human = None
    second_human = None
    
    while True:
        os.system("cls || clear")
        display_all_humans()
        first_human_option = input("\nEnter the first human you want to use for breeding: ")

        if first_human_option == "":
            return

        # Checks if human exists
        for human in human_list:
            if first_human_option == str(human.human_id):
                first_human = human
                break

        if first_human != None:
            break


    while True:

        if first_human.sex == "Female":
            os.system("cls || clear")
            display_all_males(get_human_dna(int(first_human_option)))
            second_human_option = input("\nPlease select a male to breed with: ")

            if second_human_option == "":
                return
            
            # Checks if human exists
            for human in human_list:
                if second_human_option == str(human.human_id):
                    second_human = human
                    break

            if second_human != None:
                break

        elif first_human.sex == "Male":
            os.system("cls || clear")
            display_all_females(get_human_dna(int(first_human_option)))
            second_human_option = input("\nPlease select a female to breed with: ")

            if second_human_option == "":
                return
            
            # Checks if human exists
            for human in human_list:
                if second_human_option == str(human.human_id):
                    second_human = human
                    break

            if second_human != None:
                break
    
    new_human = breeder(first_human.human_id, second_human.human_id)

    while True:
        os.system("cls || clear")
        print(f"""New human details:
Gender: {new_human[0]}
Id: {new_human[2]}
Mother: {new_human[3]}
Father: {new_human[4]}
""")
        
        option = input("Do you want to add this human to the human population? (Y/N)")

        if option.upper() == "Y":
            human = Human(new_human[0], new_human[1], new_human[2], new_human[3], new_human[4])
            human_list.append(human)
            return
        
        if option.upper() == "N":
            return
    


#=====Run Code=====#

run_existence()
