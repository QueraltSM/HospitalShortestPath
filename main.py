def print_result(src,dest,path,distances):
    print str(src)+" -> "+str(dest)

    final_path = ""
    for hospital in path:
        final_path += hospital+" -> "
    print "\nShortest path:\n", final_path[:-3]
    print "Minimum cost = "+str(distances[dest])+" km"

def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')
    if src == dest:
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        print_result(src,dest,path,distances)
    else :
        if not visited:
            distances[src]=0
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        visited.append(src)
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,dest,visited,distances,predecessors)

graph = {
        'Hospital Universitario de Gran Canaria Doctor Negrin':
        {'Clinica Centro - Las Palmas': 2.5,
        'Clinica del Carmen':3.1,
        'Hospital Pediatrico Dr. Agustin Zubillaga': 1.3},

        'Clinica Centro - Las Palmas':
        {'Hospital Universitario de Gran Canaria Doctor Negrin': 2.5,
        'Hospital San Jose': 2,
        'Hospitales San Roque': 0.8,
        'Hospitales La Paloma': 3.7},

        'Hospital Pediatrico Dr. Agustin Zubillaga':
        {'Hospital Universitario de Gran Canaria Doctor Negrin': 1.3,
        'Hospitales La Paloma': 3.3},

        'Clinica del Carmen':
        {'Hospital Universitario de Gran Canaria Doctor Negrin': 3.1,
        'Hospital Vithas Santa Catalina': 1.2},

        'Hospital Vithas Santa Catalina':
        {'Clinica del Carmen':1.2,
        'Hospital La Paloma':0.25,
        'HPS - Hospital Perpetuo Socorro':4.1},

        'Hospital La Paloma':
        {'Hospital Pediatrico Dr. Agustin Zubillaga': 3.3,
        'Clinica Centro - Las Palmas': 3.7,
        'Hospital Vithas Santa Catalina': 0.25},

        'Hospitales San Roque':
        {'HPS - Hospital Perpetuo Socorro':1.7,
        'Clinica Centro - Las Palmas':0.8},

        'HPS - Hospital Perpetuo Socorro':
        {'Hospital San Jose':0.85,
        'Hospitales San Roque':1.7,
        'Hospital Vithas Santa Catalina':4.1},

        'Hospital San Jose':
        {'Clinica Centro - Las Palmas':2,
        'HPS - Hospital Perpetuo Socorro':0.85}}


dijkstra(graph,'Hospital San Jose','Hospital Universitario de Gran Canaria Doctor Negrin')
