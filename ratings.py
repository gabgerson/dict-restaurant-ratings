"""Restaurant rating lister."""


# put your code here
def ratings_dictionary(file_name):

    data_file = open(file_name)

    restaurant_ratings = {}
    for line in data_file:
        line = line.rstrip()
        items = line.split(':')
        key = items[0]
        value = int(items[1])
        restaurant_ratings[key] = restaurant_ratings.get(key, 0) + value

    for k, v in sorted(restaurant_ratings.items()):
        print(k, v)

ratings_dictionary("scores.txt")
