from shapely.geometry import Point, Polygon
import extractKml


#get command line arguments, polygon.kml & points.csv
polygon = extractKml.getPolygon()

#take csv and define points array
pointArray = [[2,2], [3,3], [4,4], [1.5,4]]

#take kml and define polygon
#kml data is verticies and polygon requires lines. 
polygon = Polygon([(0,0), (4,0), (4,4), (0,4)])


#itterate over array; is inside the polygon?
for point in pointArray:

    point = Point(point[0],point[1])
    if polygon.contains(point):
        #record point as inside
        print("The point is inside")
    else:
        #record point as outside.
        print("The point is outside")
