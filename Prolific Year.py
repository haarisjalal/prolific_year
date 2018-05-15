Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}
    
def getting_all_years(dictionary):
    years = []
    for titles in dictionary:
        years.append(dictionary[titles])
    return years
    

def most_counts(dictionary):
    """
    Takes a dict formatted like Beatles_Discography example above 
    and returns the year in which the most albums were released.
    """
    list1 = getting_all_years(dictionary)
    counts = {}
    for items in list1:
        if items in counts:
            counts[items] += 1
        else:
            counts[items] = 1
    return counts

def most_prolific(dictionary):
    return max(most_counts(dictionary), key=most_counts(dictionary).get)

