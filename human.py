'''This file contains the class that describes a human'''

#=====Imports=====#


#=====Classes=====#

class Human():

    def __init__(self, sex, list_of_genetics, human_id, mother, father):
        """Constructor for human class.
        
            :param string sex: "Male" or "Female".
            :param list list_of_geneteic: list of the genetics in the human.
            :param int human_id: The id by which the human is identified by.
            :param int mother: The id by which this human's mother is recognized by.
            :param int father: The id by which this human's father is recognized by.
        """
        self.sex = sex
        self.list_of_genetics = list_of_genetics
        self.human_id = human_id
        self.mother = mother
        self.father = father

