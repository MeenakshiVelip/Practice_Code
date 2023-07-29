#use dict to create graph 
# Vertices/Nodes - a,b,c,d,e
# tutorialspoint
from PIL import Image
Graph = {
    'a':['b','c'],
    'b':['a','d'],
    'c':['a','d'],
    'd':['e'],
    'e':['d']
}

#print the graph
print(Graph)
image = Image.open('Graph_img.jpg')
image.show()