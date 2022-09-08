from data_structures.graph import Graph


def direct_flights(realms, stops):
    if realms.contains(stops[0]):
        curr_stop = realms.get_node(stops.pop(0))
        curr_neighbors = {neighbor.vertex: neighbor.weight for neighbor in realms.get_neighbors(curr_stop)}
        next_stop = realms.get_node(stops.pop(0))
        cost = 0
        while next_stop in curr_neighbors:
            cost += curr_neighbors[next_stop]
            if len(stops) == 0:
                return True, cost
            curr_stop = next_stop
            curr_neighbors = {neighbor.vertex: neighbor.weight for neighbor in realms.get_neighbors(curr_stop)}
            next_stop = realms.get_node(stops.pop(0))
        return False, 0
