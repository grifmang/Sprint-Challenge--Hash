#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    route = []
    cache = {}
    count = length - 2

    def get(key):
        return cache[key]

    for trip in tickets:
        if trip.source == 'NONE':
            route.append(trip.destination)
        else:
            if trip not in cache:
                cache[trip.source] = trip.destination
    
    for i in range(count):
        route.append(cache[route[-1]])

    route.append('NONE')
    return route

