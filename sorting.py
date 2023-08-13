from typing import List, TypeVar

T = TypeVar('T')

def bubble_sort(container: List[T], field: str) -> List[T]:
    """
    This function implements bubble sort.
    Args:
        container: A list of objects that we want to sort.
        field: The field that will be used for sorting.
    Returns:
        The sorted list.
    """
    did_swap = False
    while True:
        for i in range(1, len(List)):
            if container[i-1] > container[i]:
                x = container[i-1]
                container[i-1] = container[i]
                container[i] = x
                did_swap = True
            if not did_swap:
                break
            did_swap = False



def insertion_sort(container: List[T], field: str) -> List[T]:
    pass

def selection_sort(container: List[T], field: str) -> List[T]:
    pass

def binary_search(container: List[T], field: str, target):
    pass