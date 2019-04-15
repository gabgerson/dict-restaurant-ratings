"""Restaurant rating lister."""


# put your code here
def ratings_dictionary(file_name):
    """Makes a dictionary of restaurants and corresponding ratings. 

    Function ger input from file and from user. Prints the restaurants and 
    ratings in sorted alphabetical order.  
    """
    data_file = open(file_name)

    user_restaurant = input("Add a new restaurant: ")
    user_score = input("Add score for the new resuarant: ")
    restaurant_ratings = {}

    for line in data_file:
        line = line.rstrip()
        items = line.split(':')
        key = items[0]
        value = int(items[1])
        restaurant_ratings[key] = restaurant_ratings.get(key, 0) + value

    restaurant_ratings[user_restaurant] = user_score

    for k, v in sorted(restaurant_ratings.items()):
        print(k, v)

ratings_dictionary("scores.txt")
