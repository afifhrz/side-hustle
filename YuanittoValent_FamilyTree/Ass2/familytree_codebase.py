"""
Codebase for Programming Assignment 2
Family Trees

In this assignment we create a Python module to implement some
basic family tree software, where users can look up various relationships
that exist in the database.


We represent each entry in a family tree database as a list of three
strings [name, father, mother], where name is a person's name, father
is the name of their father, and mother is the name of their mother.
Where a particular relationship is unknown, the value None is used.
For example:

>>> duck_tree = [['Fergus McDuck', None, None],
...           ['Downy ODrake', None, None],
...           ['Quackmore Duck', None, None],
...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
...           ['Huey Duck', None, 'Della Duck'],
...           ['Dewey Duck', None, 'Della Duck'],
...           ['Louie Duck', None, 'Della Duck']]


The file hobbit-family.txt is also provided for testing. The database
used in this file has been compiled using the info at
http://lotrproject.com/hobbits.php. Character names are by J.R.R. Tolkein.

For more information see the function documentations below and the
assignment sheet.

"""
import copy

#Q1
def read_family(filename):
    """
    Input: A filename (filename) containing a family tree database where
    each line is in the form name, father, mother
    Output: A family tree database containing the contents of the file
    in the format specified above.
    
    For example:

    >>> hobbits = read_family('hobbit-family.txt')
    >>> len(hobbits)
    119
    >>> hobbits[118]
    ['Sancho Proudfoot', 'Olo Proudfoot', None]

     """
    
    family = []
    
    f = open(filename, "r")
    
    for line in f:
        entry = line.strip().split(",")
        for i in range(3):
            entry[i] = entry[i].strip()
            if entry[i] == '':
                entry[i] = None
        family += [entry]
    
    return family


#Q2
def person_index(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: The index value of the person's entry in the family tree,
            or None if they have no entry.

    For example:
    >>> duck_tree = [['Fergus McDuck', None, None],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> person_index('Dewey Duck', duck_tree)
    8
    >>> person_index('Daffy Duck', duck_tree)
    
    """
    for i in range(len(family)):
        if family[i][0] == person:
            return i
    return None

#Q3
def father(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: The name of person's father, or None if the information is
            not in the database.

    For example:
    >>> duck_tree = [['Fergus McDuck', None, None],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> father('Della Duck', duck_tree)
    'Quackmore Duck'
    >>> father('Huey Duck', duck_tree)

    >>> father('Daffy Duck', duck_tree)
    
    """
    p = person_index(person, family)
    if p != None:
        return family[p][1]
    else:
        return None

#Q4
def mother(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: The name of person's mother, or None if the information is
            not in the database.

    For example:
    >>> duck_tree = [['Fergus McDuck', None, None],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> mother('Hortense McDuck', duck_tree)
    'Downy ODrake'
    >>> mother('Fergus McDuck', duck_tree)

    >>> mother('Daffy Duck', duck_tree)
    
    """
    p = person_index(person, family)
    if p != None:
        return family[p][2]
    else:
        return None

#Q5
def children(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: A list containing the names of all of person's children.
    
    For example:
    >>> duck_tree = [['Fergus McDuck', None, None],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> sorted(children('Della Duck', duck_tree))
    ['Dewey Duck', 'Huey Duck', 'Louie Duck']
    >>> children('Donald Duck', duck_tree)
    []
    >>> sorted(children('Fergus McDuck', duck_tree))
    ['Hortense McDuck', 'Scrooge McDuck']
    >>> children('Donald Mallard', duck_tree)
    []
    
    """
    children = []
    for p in family:
        if p[1] == person or p[2] == person:
            children.append(p[0])
    return children

#Q6
def grandchildren(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: A list containing only the names of the grandchildren of person
        that are stored in the database.
    
    For example:
    >>> duck_tree = [['Fergus McDuck', 'Dingus McDuck', 'Molly Mallard'],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck']]
    >>> sorted(grandchildren('Quackmore Duck', duck_tree))
    ['Dewey Duck', 'Huey Duck', 'Louie Duck']
    >>> sorted(grandchildren('Downy ODrake', duck_tree))
    ['Della Duck', 'Donald Duck']
    >>> grandchildren('Della Duck', duck_tree)
    []
    
    """

    grandchildren = []

    clist = children(person, family)

    for child in clist:
        grandchildren += children(child, family)
    
    return grandchildren

#Q7 
def greatgrandchildren(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: A list containing only the names of the great-grandchildren of person
        that are stored in the database.
    
    For example:
    >>> duck_tree = [['Fergus McDuck', 'Dingus McDuck', 'Molly Mallard'],
    ...           ['Downy ODrake', None, None],
    ...           ['Quackmore Duck', None, None],
    ...           ['Donald Duck','Quackmore Duck','Hortense McDuck'],
    ...           ['Della Duck', 'Quackmore Duck', 'Hortense McDuck'],
    ...           ['Hortense McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Scrooge McDuck', 'Fergus McDuck', 'Downy ODrake'],
    ...           ['Huey Duck', None, 'Della Duck'],
    ...           ['Dewey Duck', None, 'Della Duck'],
    ...           ['Louie Duck', None, 'Della Duck'],
    ...           ['Quackmore Duck', 'Humperdink Duck', 'Elvira Coot']]
    >>> sorted(greatgrandchildren('Quackmore Duck', duck_tree))
    []
    >>> sorted(greatgrandchildren('Humperdink Duck', duck_tree))
    ['Dewey Duck', 'Huey Duck', 'Louie Duck']
    >>> sorted(greatgrandchildren('Elvira Coot', duck_tree))
    ['Dewey Duck', 'Huey Duck', 'Louie Duck']
    
    """
    grandchildren_list = grandchildren(person, family)
    greatgrandchildren_list = []
    for gchild in grandchildren_list:
        greatgrandchildren_list += children(gchild, family)
    
    return greatgrandchildren_list




if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
