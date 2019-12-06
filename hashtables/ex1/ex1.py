#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # insert weights to hash table with index as value
    for i, weight in enumerate(weights):
        # print(i, weight)
        hash_table_insert(ht, weight, i)
    # check to see if hashtable contains a entry for limit - weight
    for i, weight in enumerate(weights):
        # index we are looking for will be the difference of limit and the current weight
        index = limit - weight
        # If we found one, capture the value and return as a tuple
        if hash_table_retrieve(ht, index) is not None:
            other_index = hash_table_retrieve(ht, index)
            # return larger weight first in tuple
            if other_index > i:
                return (other_index, i)
            else:
                return (i, other_index)
    # return hash_table_retrieve(ht, 6)



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


weights_3 = [4, 6, 10, 15, 16]
answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
print(answer_3)
