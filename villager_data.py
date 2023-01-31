"""Functions to parse a file containing villager data."""

# filename = open('villagers.csv')

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    data = open(filename)
    # species_set = set()
    
    # for line in data:
    #     species = line.split("|")[1]
    #     species_set.add(species)

    species_set = set(line.split("|")[1] for line in data)

    return species_set


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    data = open(filename)
    # species_set = set(line.split("|")[1])


    villagers = []
    if search_string == "all":
        for species in data:
            species = species.split("|")[1]
            species_set = set(species)
            for name in data:
                name = name.split("|")[0]
                species_set.add(name)
                # villagers += species

    # else:
    #     for search_string in species_set:
    #         search_string = []
    #     for line in data:
    #         if line[1] == search_string:
    #             search_string.append(line[0])
    #             villagers += search_string
        



    print(species)
get_villagers_by_species('villagers.csv', "all")
    

    # TODO: replace this with your code

    # return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code

    return []


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
