# import libraries
import osmnx as ox
import networkx as nx
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import osmium as osm
import pandas as pd

# import data
# define class function
class OSMHandler(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_data = []

    def tag_inventory(self, elem, elem_type):
        for tag in elem.tags:
            self.osm_data.append([elem_type, 
                                   elem.id, 
                                   elem.version,
                                   elem.visible,
                                   pd.Timestamp(elem.timestamp),
                                   elem.uid,
                                   elem.user,
                                   elem.changeset,
                                   elem.location,
                                   len(elem.tags),
                                   tag.k, 
                                   tag.v])

    def node(self, n):
        self.tag_inventory(n, "node")

    def way(self, w):
        self.tag_inventory(w, "way")

    def relation(self, r):
        self.tag_inventory(r, "relation")

osmhandler = OSMHandler()
# scan the input file and fills the handler list accordingly
osmhandler.apply_file("munich_center.osm")

# transform the list into a pandas DataFrame
data_colnames = ['type', 'id', 'version', 'visible', 'ts', 'uid',
                 'user', 'chgset','location','ntags', 'tagkey', 'tagvalue']
df_osm = pd.DataFrame(osmhandler.osm_data, columns=data_colnames)

# find target
target = df_osm[df_osm['tagkey'] == 'target']
# find source
source = df_osm[df_osm['tagkey'] == 'source']

# get footway data using bbox [11.5430,48.1249,11.6104,48.1510]
footways = ox.graph_from_bbox(48.1391,48.1319, 11.5698,11.5604, network_type='walk')
# footways = ox.graph.graph_from_xml('munich_center.osm')
# plot the graph
# ox.plot_graph(footways)

# define origin and desination locations
# sample point based on target and source 
origin_point = ( 48.135710, 11.565572) 
destination_point = (48.138244, 11.561798)

# plot graph and origin - destination
fig, ax = ox.plot_graph(footways, show=False)
ax.scatter(origin_point[1], origin_point[0], c='red', s=100, label='orig', marker='o')
ax.scatter(destination_point[1], destination_point[0], c='lime', s=100, label='dest', marker='o')
ax.annotate('origin-point', (origin_point[1], origin_point[0]), color = 'white')
ax.annotate('destination-point', (destination_point[1], destination_point[0]),color = 'white')
plt.show()

# get the nearest nodes to the locations 
origin_node = ox.get_nearest_node(footways, origin_point) 
destination_node = ox.get_nearest_node(footways, destination_point)

# printing the closest node id to origin and destination points 
origin_node, destination_node

points_list = list(footways.edges())

nodesNumber = footways.number_of_nodes()
footways.number_of_nodes(),footways.number_of_edges()

nodes_list= []
for point in points_list:
    v,u = point[0],point[1]
    nodes_list.append(v)
    nodes_list.append(u)

nodes_set = set(nodes_list)

reverse_nodes_dict = dict(enumerate(nodes_set))
nodes_dict = dict(zip(nodes_set,range(0,nodesNumber)))

new_points_list = []
for point in points_list:
    v,u = point[0],point[1]
    newV, newU = nodes_dict[v],nodes_dict[u]
    new_node = (newV, newU)
    new_points_list.append(new_node)

nodes_dict[origin_node],nodes_dict[destination_node]

#### Algorithm missing

# visualization
# getting coordinates of the nodes
# we will store the longitudes and latitudes in following list 
long = [] 
lat = []  
for i in route:
     point = footways.nodes[i]
     long.append(point['x'])
     lat.append(point['y'])

def plot_path(lat, long, origin_point, destination_point):
    

    # adding the lines joining the nodes
    fig = go.Figure(go.Scattermapbox(
        name = "Path",
        mode = "lines",
        lon = long,
        lat = lat,
        marker = {'size': 10},
        line = dict(width = 4.5, color = 'blue')))
    # adding source marker
    fig.add_trace(go.Scattermapbox(
        name = "Source",
        mode = "markers",
        lon = [origin_point[1]],
        lat = [origin_point[0]],
        marker = {'size': 12, 'color':"red"}))
     
    # adding destination marker
    fig.add_trace(go.Scattermapbox(
        name = "Destination",
        mode = "markers",
        lon = [destination_point[1]],
        lat = [destination_point[0]],
        marker = {'size': 12, 'color':'green'}))
    
    # getting center for plots:
    lat_center = np.mean(lat)
    long_center = np.mean(long)
    # defining the layout using mapbox_style
    fig.update_layout(mapbox_style="stamen-terrain",
        mapbox_center_lat = 30, mapbox_center_lon=-80)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                      mapbox = {
                          'center': {'lat': lat_center, 
                          'lon': long_center},
                          'zoom': 13})
    fig.show()

plot_path(lat, long, origin_point, destination_point)


