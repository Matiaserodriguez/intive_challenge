# Challenge: 
# Coding question - Triplets

# Given a log file of user_id, timestamp & page visited find the 10 most common triplets, where a triplet is an occurrence of 3 pages 
# visited sequentially by the same user.

# Tips

# We are looking to see how the candidate writes code, so they should choose the language 
# they are most familiar with and write code that is readable and maintainable.

# If the candidate thinks this is some massively parallel log parsing / analysis problem, 
# tell them it's just for one log file and that they can assume that the data fits in memory. 
# If they try to do the math to figure out how many unique combinations there might be, it's ok (and counts as a bonus for the candidate),
#  but don't let them dwell on this for too long.

# We are not looking for them to write a sort algorithm, 
# so if they want to use any off-the-shelf sorting to get the top 10, it is acceptable. 
# They can also create some data structure to keep track of the top 10, and that's also acceptable


import itertools

# since there are no logs given I've created them, similar as a json file.
given_logs = [
    {'user_id': 'a', 'timestamp': 1932850073, 'page_visited': 'facebook.com'},
    {'user_id': 'a', 'timestamp': 1932850074, 'page_visited': 'twitter.com'},
    {'user_id': 'a', 'timestamp': 1932850075, 'page_visited': 'instagram.com'},
    {'user_id': 'a', 'timestamp': 1932850076, 'page_visited': 'facebook.com'},
    {'user_id': 'a', 'timestamp': 1932850077, 'page_visited': 'twitter.com'},
    {'user_id': 'a', 'timestamp': 1932850078, 'page_visited': 'instagram.com'},
    {'user_id': 'a', 'timestamp': 1932850079, 'page_visited': 'facebook.com'},
    {'user_id': 'a', 'timestamp': 1932850080, 'page_visited': 'twitter.com'},
    {'user_id': 'a', 'timestamp': 1932850081, 'page_visited': 'instagram.com'},
    {'user_id': 'a', 'timestamp': 1932850079, 'page_visited': 'facebook.com'},
    {'user_id': 'a', 'timestamp': 1932850080, 'page_visited': 'twitter.com'},
    {'user_id': 'a', 'timestamp': 1932850081, 'page_visited': 'instagram.com'},
    {'user_id': 'a', 'timestamp': 1932850082, 'page_visited': 'facebook.com'},
    {'user_id': 'a', 'timestamp': 1932850083, 'page_visited': 'twitter.com'},
    {'user_id': 'a', 'timestamp': 1932850084, 'page_visited': 'instagram.com'},
    {'user_id': 'a', 'timestamp': 1932850085, 'page_visited': 'facebook.com'},
    {'user_id': 'a', 'timestamp': 1932850086, 'page_visited': 'twitter.com'},
    {'user_id': 'a', 'timestamp': 1932850087, 'page_visited': 'instagram.com'},
    {'user_id': 'a', 'timestamp': 1932850088, 'page_visited': 'facebook.com'},
    {'user_id': 'a', 'timestamp': 1932850089, 'page_visited': 'twitter.com'},
    {'user_id': 'a', 'timestamp': 1932850090, 'page_visited': 'instagram.com'},
    {'user_id': 'a', 'timestamp': 1932850091, 'page_visited': 'facebook.com'},
    {'user_id': 'a', 'timestamp': 1932850092, 'page_visited': 'twitter.com'},
    {'user_id': 'a', 'timestamp': 1932850093, 'page_visited': 'instagram.com'},
    {'user_id': 'a', 'timestamp': 1932850094, 'page_visited': 'facebook.com'},
    {'user_id': 'a', 'timestamp': 1932850095, 'page_visited': 'twitter.com'},
    {'user_id': 'a', 'timestamp': 1932850096, 'page_visited': 'instagram.com'},
    {'user_id': 'a', 'timestamp': 2037623191, 'page_visited': 'spotify.com'},
    {'user_id': 'a', 'timestamp': 2037623192, 'page_visited': 'youtube.com'},
    {'user_id': 'a', 'timestamp': 2037623193, 'page_visited': 'linkedin.com'},
    {'user_id': 'b', 'timestamp': 2037623191, 'page_visited': 'spotify.com'},
    {'user_id': 'b', 'timestamp': 2037623192, 'page_visited': 'youtube.com'},
    {'user_id': 'b', 'timestamp': 2037623193, 'page_visited': 'linkedin.com'},
]

def main():

    # asks the user for the name of the user they would like to search for.
    user_id = input('What\'s the user\'s report you are looking for? ')

    # gets the specific logs from the given user.
    filtered_user = filter_user(given_logs, user_id)

    # sorts the list using the timestamp.
    sorted_list = sort_list(filtered_user)

    # cont_triples will use the get_triples function to store those values
    # from sorted_list into the sorted_triples_dictionary
    sorted_triples_dictionary = count_triples(get_triples, sorted_list)

    times_counter = 0

    # prints the required information by accessing the items on the finished dictionary.
    for i in sorted_triples_dictionary.items():
        print(f'The "{i[0]}" triple has been reached by the user {user_id}, {i[1]} times.')
        times_counter += 1
        if times_counter == 10:
            break


def filter_user(array, user):
    '''@array: takes an array and loop over the elements of it.
    @user: the specific user ID looking the information for.
    This function filters and returns an array with the searched user's info'''
    
    returned_array = []

    for i in array:
        if i['user_id'] == user:
            returned_array.append(i)
    
    return returned_array

def sort_list(array):
    '''@array: will take a array and sort it by the timestamp.
    It returns a sorted array from the given array.'''

    sorted_array = sorted(array, key = lambda user_logs: user_logs['timestamp'])

    return sorted_array

def get_triples(array, count = 3):
    '''@array: takes the sorted array for getting the triples.
    @count: it will start on 3 if no parameters are given
    This function will get an array and take the first 3 values of the 
    'page_visited' key, returning them in a new array.'''

    counts = []

    for i in itertools.islice(array, count):
        pages = i['page_visited']
        counts.append(pages)
    
    return counts

def count_triples(get_triples, array):
    '''@get_triples: will use that function in order to get the logic.
    @array: given sorted array
    This function counts the triples on the given array by using the get_triples function,
    and returns a sorted dictionary with its key-value pair in descending order.
    The key will be the triple, and the value will be the number of repetitions.'''

    triples_array = []

    while len(array) != 0:
        for _ in array:
            triples_array.append(get_triples(array))
            array.pop(0)

    triples_dictionary = {tuple(item):triples_array.count(item) for item in triples_array}

    sorted_dic = dict(sorted(triples_dictionary.items(), key=lambda item: item[1], reverse = True))

    # This will remove the last two items of the dictionary because
    # the tuples will have 1 and 2 items but not three as expected.
    sorted_dic.popitem()
    sorted_dic.popitem()

    return sorted_dic

if __name__ == '__main__':
    main()