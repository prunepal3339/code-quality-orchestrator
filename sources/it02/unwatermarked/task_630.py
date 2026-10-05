def get_coordinates(coord):
    x, y = coord
    return [[x-1, y-1], [x-1,y], [x, y- 1], [ x+1, y - 1],[ x + 1, y ],[ x + 2, y ], [ x , y + 1], 
            [ x - 1,  y + 2], [ x, y +  2],  [ x +  1,   y + 3]]
