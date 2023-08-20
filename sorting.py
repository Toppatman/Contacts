from typing import List, Literal
from person import Person

def bubble_sort(people: List[Person], field: Literal['name', 'phone']):
    """
    This function implements bubble sort.
    Args:
        people: A list of objects that we want to sort.
        field: The field that will be used for sorting.
    Returns:
        The sorted list.
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


def insertion_sort(people: List[Person], field: str) -> List[Person]:
    
    pass

def selection_sort(people: List[Person], field: str) -> List[Person]:

    pass

def binary_search(people: List[Person], field: str, target) -> int:
    pass