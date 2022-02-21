from math import sin, cos, sqrt, radians, asin
import sys

def a_star(start_city, end_city):

    destinations = getEdges()
    heuristics = heuristic(end_city)
    cities = readCoordinates()
    
    open_set = set({start_city})
    closed_set = set()
    distances = {}
    parents = {}
    distances[start_city] = 0
    parents[start_city] = start_city
    
    
    while len(open_set) > 0:
        currentNode = None

        for nextNode in open_set:
            if currentNode == None or distances[nextNode] + heuristics[nextNode] < distances[currentNode] + heuristics[currentNode]:
                currentNode = nextNode

        if currentNode == end_city or cities[currentNode] == None:
                 pass
        else:
            for (city, miles) in destinations[currentNode].items():
                if city not in open_set and city not in closed_set:
                    open_set.add(city)
                    parents[city] = currentNode
                    distances[city] = distances[currentNode] + miles
                else:
                    if distances[city] > distances[currentNode] + miles:
                        distances[city] = distances[currentNode] + miles
                        parents[city] = currentNode

                        if city in closed_set:
                            closed_set.remove(city)
                            open_set.add(city)
            
        if currentNode == None:
            print('Dne')
            return None

        if currentNode == end_city:
            path = []

            while parents[currentNode] != currentNode:
                path.append(currentNode)
                currentNode = parents[currentNode]

            path.append(start_city)

            path.reverse()
 
            print("From city: " + start_city)
            print("To city: " + end_city)
            print("Best Route:", " - ".join(["{}"]*len(path)).format(*path))
            print("Total Distance:", format(distances[end_city], '.2f'))   
            return path
        open_set.remove(currentNode)
        closed_set.add(currentNode)
    print('path dne')
    return None


    
def get_neighbors(nextNode):
    if nextNode in Graph_nodes:
        return Graph_nodes[nextNode]
    else:
        return None
    
def heuristic(endCity):
    coordinates = readCoordinates()
    endNode = coordinates[endCity]

    heuristic_distance = {}
    for it_cities in coordinates:
        heuristic_distance[it_cities] = distance(coordinates[it_cities], endNode)
    print(heuristic_distance)
    return heuristic_distance

    

def readCoordinates():
    coordinates = open('coordinates.txt', 'r')
    city_coordinates = coordinates.readlines()

    lv_cities = {}

    for it_city in city_coordinates:
        temp_city = it_city.strip().split(":")
        temp_coordinate = temp_city[1].replace("(", "").replace(")", "").split(",")
        lv_cities[temp_city[0]] = temp_coordinate

    return lv_cities


def getEdges():
    mapfile = open('map.txt', 'r')
    city_edges = mapfile.readlines()

    lv_distance = {}
    
    for it_city in city_edges:
        temp_city = it_city.strip().split("-")
        temp_destination = temp_city[1].split(",")
        temp_city_distance = {}
        for it_destination in temp_destination:
            temp_city_destination = it_destination.replace(")", "").split("(")
            temp_city_distance[temp_city_destination[0]] = float(temp_city_destination[1])
        lv_distance[temp_city[0]] = temp_city_distance   
    return lv_distance
    

def distance(city1, city2):
    R = 3958.8

    lat1 = radians(float(city1[0]))
    long1 = radians(float(city1[1]))
    lat2 = radians(float(city2[0]))
    long2 = radians(float(city2[1]))

    dlong = long2 - long1
    dlat = lat2 - lat1

    a = sin(dlat /2)**2 + cos(lat1) * cos(lat2) * sin(dlong / 2)**2
    c = 2 * asin(sqrt(a))
    distance = (R * c)
    return distance



if __name__ == "__main__":

    #inputStart = sys.argv[1]
    #inputEnd = sys.argv[2]
    a_star("SanJose", "LongBeach")
