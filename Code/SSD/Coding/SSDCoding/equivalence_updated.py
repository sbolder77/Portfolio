"""CODE SOURCE: https://shorturl.at/qDMP7"""

def equivalence_partition(iterable, relation):
    """Partitions a set of objects into equivalence classes

    Args:
        iterable: collection of objects to be partitioned
        relation: equivalence relation. I.e. relation(o1,o2) evaluates to True
            if and only if o1 and o2 are equivalent

    Returns: classes, partitions
        classes: A sequence of sets. Each one is an equivalence class
        partitions: A dictionary mapping objects to equivalence classes
    """
    classes = []
    partitions = {}
    for obj in iterable:  # for each object
        # find the class it is in
        found = False
        for cla in classes:
            if relation(next(iter(cla)), obj):  # is it equivalent to this class?
                cla.add(obj)
                partitions[obj] = cla
                found = True
                break
        if not found:  # it is in a new class
            classes.append(set([obj]))
            partitions[obj] = classes[-1]
    return classes, partitions

def equivalence_enumeration(iterable, relation):
    """Partitions a set of objects into equivalence classes

    Same as equivalence_partition() but also numbers the classes.

    Args:
        iterable: collection of objects to be partitioned
        relation: equivalence relation. I.e. relation(o1,o2) evaluates to True
            if and only if o1 and o2 are equivalent

    Returns: classes, partitions, ids
        classes: A sequence of sets. Each one is an equivalence class
        partitions: A dictionary mapping objects to equivalence classes
        ids: A dictionary mapping objects to the indices of their equivalence classes
    """
    classes, partitions = equivalence_partition(iterable, relation)
    ids = {}
    for ind, cla in enumerate(classes):
        for obj in cla:
            ids[obj] = ind
    return classes, partitions, ids

def check_equivalence_partition(classes, partitions, relation):
    """Checks that a partition is consistent under the relationship"""
    for obj, cla in partitions.items():
        for _cla in classes:
            assert (obj in _cla) ^ (not _cla is cla)
    for cla1 in classes:
        for obj1 in cla1:
            for cla2 in classes:
                for obj2 in cla2:
                    assert (cla1 is cla2) ^ (not relation(obj1, obj2))

def test_equivalence_partition():
    """First function to set objects to perform checks"""
    relation = relate()
    classes, partitions = equivalence_partition(
        range(-3, 5),
        relation
    )
    check_equivalence_partition(classes, partitions, relation)
    for cla in classes:
        print(cla)
    for obj, cla1 in partitions.items():
        print(obj, ':', cla1)

def relate():
    """Function to be called from other functions for lambda"""
    return lambda x, y: (x - y) % 4 == 0

if __name__ == '__main__':
    test_equivalence_partition()
