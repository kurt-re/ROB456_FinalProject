
def createAdjMatrix(world):
    """Takes in nxn world where 1 is an obstacle and
    0 is clear and returns an Adjacency Matrix, which
    represents connected vertices, where connected means 
    both are unoccupied and horizontal/vertical to eachother.
    
    Adjacency Matrix represents a 4-connected world,
    so if vertices are clear then it is possible to move
    up, down, left, and right between them.
    
    Assumes world is square and vertices are 
    numbered left to right, top to bottom"""
    
    #Create matrix that is necessary size
    #Number of total vertices
    numVertex = (len(world)**2)
    
    #Create rows
    adjMat = [0]*(numVertex)
    
    #Create columns
    for k in range(len(adjMat)):
        adjMat[k] = [0]*(numVertex)
        
    #Run through all vertices    
    for vertex in range(numVertex):
        
        #Find Vertex Coordinates
        vertCoord = vertToCoord(vertex, world)

        
        #Check to see if vertex is unoccupied (0). If it is occupied (1), adjacency
        #matrix will stay all zeros
        if world[vertCoord[0]][vertCoord[1]] == 0:

            #Find Vertex number of four neighboring vertices [up, down, right, left]
            neighborVert = [0]*4
            neighborVert[0] = vertex - len(world)
            neighborVert[1] = vertex + len(world)
            neighborVert[2] = vertex + 1
            neighborVert[3] = vertex - 1
            
            #Check if vertex is in column 0 or 19, if so take away 
            #either the "right" vertex or "left" vertex to prevent
            #The code from saying vertices on opposite sides of the grid
            #are adjacent

            if vertCoord[1] == 0:
                neighborVert[3] = -1
            elif vertCoord[1] == len(world)-1:
                neighborVert[2] = -1
                
                #Kurt is a loser
                    
            
            #Check if you can get to neighboring vertices from original vertex
            for i in range(4):
                
                #Check if neighboring vertex is in range of possible vertices
                if neighborVert[i] >= 0 and neighborVert[i] <= numVertex:
                    
                    #Find coordinates of neighboring vertex
                    coord = vertToCoord(neighborVert[i], world)
                    
                    #Verify that neighboring coordinates are within bounds
                    if coord[0] <= len(world) and coord[1] <= len(world):
                        
                        #Check occupancy of neighboring vertex
                        occ = world[coord[0]][coord[1]]
                    else:
                        occ = 1
                    
                    #If unoccupied, populate Adj Matrix with a one in row of 
                    #original vertex and column of neighboring vertex
                    if occ == 0:
                        adjMat[vertex][neighborVert[i]] = 1
        
    #Return Adjacency Matrix
    return adjMat
