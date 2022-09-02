from familytree_codebase import read_family, person_index, father, mother, children, grandchildren, greatgrandchildren
duck_tree = read_family('hobbit-family.txt')

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
    grandparent = []
    first_father = father(person, family)
    first_mother = mother(person, family)

    if first_father != None:
        second_father = father(first_father, family)
        second_mother = mother(first_father, family)
        if second_father != None:
            grandparent.append(second_father)
        if second_mother != None:
            grandparent.append(second_mother)
    
    if first_mother != None:
        second_father = father(first_mother, family)
        second_mother = mother(first_mother, family)
        if second_father != None:
            grandparent.append(second_father)
        if second_mother != None:
            grandparent.append(second_mother)

    return grandparent

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
    siblings=[]
    father_person = father(person,family)
    mother_person = mother(person,family)

    for i in range(len(family)):
        if family[i][1]==father_person and family[i][2] == mother_person:
            if family[i][0] != person:
                siblings.append(family[i][0])    
    
    return siblings

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
    cousins = []
    gplist = grandparent(person, family)
    for grand_parent in gplist:
        clist = grandchildren(grand_parent, family)
        for child in clist:
            if child not in cousins:
                cousins.append(child)
    cousins.remove(person)

    return cousins

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
    list_father_p1 = []
    list_father_p2 = []
    ori_p1 = p1
    ori_p2 = p2

    while True:
        p1 = father(p1,family)
        if p1 != None:
            list_father_p1.append(p1)
        else:
            break

    while True:
        p2 = father(p2,family)
        if p2 != None:
            list_father_p2.append(p2)
        else:
            break

    if len(list_father_p1)>len(list_father_p2):
        print(list_father_p1)
        print(list_father_p2)
        exit()
        if ori_p2 in list_father_p1:
            index = list_father_p1.index(ori_p2)
            print(f'{ori_p1} is a direct ancestor of {ori_p2}, {index+1} generations apart.')
        else:
            print(f'{ori_p1} is not a direct ancestor or descendant of {ori_p2}.')
    elif len(list_father_p1)<len(list_father_p2):
        if ori_p1 in list_father_p2:
            index = list_father_p1.index(ori_p1)
            print(f'{ori_p2} is a direct ancestor of {ori_p1}, {index+1} generations apart.')
        else:
            print(f'{ori_p2} is not a direct ancestor or descendant of {ori_p1}.')
    else:
        print(f'{ori_p1} is a direct ancestor of {ori_p2}, 0 generations apart.')

# direct_ancestor('Frodo Baggins', 'Gormadoc Brandybuck', duck_tree)

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
    n = 0

    while True:    
        p1 = father(p1,family)
        # print(p1)
        child_temp = [p1]
        for i in range(n+1):
            child = []
            for anak in child_temp:
                if children(anak, family)!=None:
                    child += children(anak, family)
            child_temp = child
            # print(n, child)
        for chill in child :
            if chill == p2:
                return print(n)
            elif p1 == None:
                return print(-1)
        n+=1
