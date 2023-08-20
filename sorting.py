from typing import List, Literal
from person import Person

def bubble_sort(people: List[Person], field: Literal['name', 'phone']):
    """
    This function implements bubble sort.
    Args:
        people: A list of objects that we want to sort.
        field: The field that will be used for sorting.
    """
    while True:
        did_swap = False
        for i in range(1, len(people)):
            if getattr(people[i - 1], field) > getattr(people[i], field):
                temp = people[i - 1]
                people[i - 1] = people[i]
                people[i] = temp
                did_swap = True
        if not did_swap:
            break
        did_swap = False


def insertion_sort(people: List[Person], field: Literal['name', 'phone']) -> List[Person]:
    """
    This function implements insertion sort.
    Args:
        people: A list of objects that we want to sort.
        field: The field that will be used for sorting.
    """

    
    pass

def selection_sort(people: List[Person], field: Literal['name', 'phone']) -> List[Person]:
    """
    This function implements selection sort.
    Args:
        people: A list of objects that we want to sort.
        field: The field that will be used for sorting.
    """
    for i in range(len(people)):
        smallest = i
        for j in range(i + 1, len(people)):
            if getattr(people[j], field) < getattr(people[smallest], field):
                smallest = j
        people[i], people[smallest] = people[smallest], people[i]

def binary_search(people: List[Person], field: Literal['name', 'phone'], target) -> int:
    pass