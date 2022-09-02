"""
Template for Programming Assignment 
Family Trees

In this assignment we create a Python module to implement some
basic family tree software, where users can look up various relationships
that exist in the database, as well as merging two family tree databases
that may contain overlapping information.



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

from familytree_codebase import read_family, person_index, father, mother, children, grandchildren, greatgrandchildren


# Assignment 2

# Task 1
def grandparent(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: A list containing the names of all grandparent of person that
            are stored in the database.
    
    For example:
    
    >>> hobbits = read_family('hobbit-family.txt')
    >>> sorted(grandparent('Frodo Baggins', hobbits))
    ['Fosco Baggins', 'Gorbadoc Brandybuck', 'Mirabella Took', 'Ruby Bolger']
    >>> sorted(grandparent('Doderic Brandybuck', hobbits))
    ['Saradas Brandybuck']
    >>> sorted(grandparent('Hilda Bracegirdle', hobbits))
    []
    
    """
    
    pass

# Task 2
def siblings(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: A list containing the names of all siblings of person that
            are stored in the database.
    
    For example:
    
    >>> hobbits = read_family('hobbit-family.txt')
    >>> sorted(siblings('Frodo Baggins', hobbits))
    []
    >>> sorted(siblings('Daisy Baggins', hobbits))
    []
    >>> sorted(siblings('Drogo Baggins', hobbits))
    ['Dora Baggins', 'Dudo Baggins']
    >>> sorted(siblings('Dudo Baggins', hobbits))
    ['Dora Baggins', 'Drogo Baggins']
    
    """
    
    pass

# Task 3
def cousins(person, family):
    """
    Input: A person's name (person) and a family tree database (family)
            as specified above.
    Output: A list containing the names of all cousins of person that
            are stored in the database.
    
    For example:
    
    >>> hobbits = read_family('hobbit-family.txt')
    >>> sorted(cousins('Frodo Baggins', hobbits))
    ['Daisy Baggins', 'Merimac Brandybuck', 'Milo Burrows', 'Saradoc Brandybuck', 'Seredic Brandybuck']
    
    """
    pass

# Task 4
def direct_ancestor(p1, p2, family):
    """
    Input: Two names (p1, p2) and a family tree database (family).
    Output: One of the following three string outputs (where p1 and
            p2 are the given input strings, and n is a non-negative integer):
            "p1 is a direct ancestor of p2, n generations apart."
            "p2 is a direct ancestor of p1, n generations apart."
            "p1 is not a direct ancestor or descendant of p2."

    For example:

    >>> hobbits = read_family('hobbit-family.txt')
    >>> direct_ancestor('Frodo Baggins', 'Frodo Baggins', hobbits)
    'Frodo Baggins is a direct ancestor of Frodo Baggins, 0 generations apart.'
    >>> direct_ancestor('Frodo Baggins', 'Gormadoc Brandybuck', hobbits)
    'Gormadoc Brandybuck is a direct ancestor of Frodo Baggins, 5 generations apart.'
    
    <Paragraph on problem, challenges, and overall approach.>

    """
    pass

# Task 5
def cousin_degree(p1, p2, family):
    """
    Input: Two names (p1, p2) and a family tree database (family).
    Output: A number representing the minimum distance cousin relationship between p1 and p2, as follows:
            -   0 if p1 and p2 are siblings
            -   1 if p1 and p2 are cousins
            -   n if p1 and p2 are nth cousins, as defined at https://www.familysearch.org/blog/en/cousin-chart/
            -   -1 if p1 and p2 have no cousin or sibling relationship
    
    For example:
    >>> hobbits = read_family("hobbit-family.txt")
    >>> cousin_degree('Minto Burrows', 'Myrtle Burrows', hobbits)
    0
    >>> cousin_degree('Estella Bolger', 'Meriadoc Brandybuck', hobbits)
    3
    >>> cousin_degree('Frodo Baggins', 'Bilbo Baggins', hobbits)
    -1
    
    <Paragraph on problem, challenges, and overall approach.>

    """
    pass
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
