def getPolygon():
    with open("Calloutarea.kml", "r") as f:
        s = f.read()

        start = "<coordinates>"
        finish = "</coordinates>"

        dataString = (s[s.index(start) + len(start): s.index(finish)])
        points = dataString.split()
        verticies = [(float(point.split(",")[0]),(point.split(",")[1])) for point in points]
        verticies.append(verticies[0])

        lines = []
        count = len(verticies)
        
        for x in range(count-1):
            lines.append((verticies[x],verticies[x+1]))
        
        return(lines)
        
