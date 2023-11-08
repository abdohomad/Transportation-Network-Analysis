from graph_manager import GraphManager
import networkx as nx
import tkinter as tk
from haversine import haversine
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from folium import plugins
import folium
import webbrowser
from tkinter import Canvas, messagebox
import matplotlib.pyplot as plt
import csv
import ast
from geopy.geocoders import Nominatim


data = [
    ('New York City, New York', 'Boston, Massachusetts', 635),
    ('New York City, New York', 'Boston, Massachusetts', 635),
    ('New York City, New York', 'Detroit, Michigan', 692),
    ('New York City, New York', 'Chicago, Illinois', 1132),
    ('New York City, New York', 'Washington, D.C.', 2414),
    ('New York City, New York', 'Philadelphia, Pennsylvania', 2272),
    ('Los Angeles, California', 'Bakersfield, California', 112),
    ('Los Angeles, California', 'Phoenix, Arizona', 364),
    ('Los Angeles, California', 'San Diego, California', 120),
    ('Los Angeles, California', 'Santa Barbara, California', 92),
    ('Chicago, Illinois', 'Columbus, Ohio', 272),
    ('Chicago, Illinois', 'Indianapolis, Indiana', 173),
    ('Chicago, Illinois', 'St. Louis, Missouri', 262),
    ('Chicago, Illinois', 'Des Moines, Iowa', 323),
    ('Houston, Texas', 'El Paso, Texas', 674),
    ('Houston, Texas', 'New Orleans, Louisiana', 348),
    ('Houston, Texas', 'San Antonio, Texas', 197),
    ('Houston, Texas', 'Dallas, Texas', 225),
    ('Phoenix, Arizona', 'Tucson, Arizona', 117),
    ('Phoenix, Arizona', 'Mesa, Arizona', 12),
    ('Phoenix, Arizona', 'Las Vegas, Nevada', 256),
    ('Phoenix, Arizona', 'Flagstaff, Arizona', 137),
    ('Philadelphia, Pennsylvania', 'New York City, New York', 82),
    ('Philadelphia, Pennsylvania', 'Baltimore, Maryland', 96),
    ('Philadelphia, Pennsylvania', 'Washington, D.C.', 123),
    ('Philadelphia, Pennsylvania', 'Newark, New Jersey', 80),
    ('Dallas, Texas', 'Houston, Texas', 225),
    ('Dallas, Texas', 'Fort Worth, Texas', 31),
    ('Dallas, Texas', 'Oklahoma City, Oklahoma', 205),
    ('Dallas, Texas', 'San Antonio, Texas', 274),
    ('San Jose, California', 'San Francisco, California', 42),
    ('San Jose, California', 'Oakland, California', 33),
    ('San Jose, California', 'Fresno, California', 120),
    ('San Jose, California', 'Sacramento, California', 109),
    ('Austin, Texas', 'Houston, Texas', 197),
    ('Austin, Texas', 'San Antonio, Texas', 75),
    ('Austin, Texas', 'Fort Worth, Texas', 190),
    ('Austin, Texas', 'Dallas, Texas', 189),
    ('Jacksonville, Florida', 'Tampa, Florida', 186),
    ('Jacksonville, Florida', 'Miami, Florida', 338),
    ('Jacksonville, Florida', 'Orlando, Florida', 127),
    ('Jacksonville, Florida', 'Atlanta, Georgia', 258),
    ('San Francisco, California', 'San Jose, California', 42),
    ('San Francisco, California', 'Oakland, California', 8),
    ('San Francisco, California', 'Sacramento, California', 76),
    ('San Francisco, California', 'Fresno, California', 155),
    ('Indianapolis, Indiana', 'Columbus, Ohio', 172),
    ('Indianapolis, Indiana', 'Chicago, Illinois', 170),
    ('Indianapolis, Indiana', 'Fort Wayne, Indiana', 111),
    ('Indianapolis, Indiana', 'Louisville, Kentucky', 112),
    ('Columbus, Ohio', 'Indianapolis, Indiana', 172),
    ('Columbus, Ohio', 'Cleveland, Ohio', 142),
    ('Columbus, Ohio', 'Cincinnati, Ohio', 100),
    ('Columbus, Ohio', 'Pittsburgh, Pennsylvania', 185),
    ('Fort Worth, Texas', 'Dallas, Texas', 32),
    ('Fort Worth, Texas', 'Austin, Texas', 146),
    ('Fort Worth, Texas', 'Oklahoma City, Oklahoma', 203),
    ('Charlotte, North Carolina', 'Atlanta, Georgia', 250),
    ('Charlotte, North Carolina', 'Columbia, South Carolina', 90),
    ('Charlotte, North Carolina', 'Raleigh, North Carolina', 140),
    ('Charlotte, North Carolina', 'Greensboro, North Carolina', 70),
    ('Charlotte, North Carolina', 'Winston-Salem, North Carolina', 90),
    ('Charlotte, North Carolina', 'Nashville, Tennessee', 230),
    ('Seattle, Washington', 'Spokane, Washington', 280),
    ('Seattle, Washington', 'Portland, Oregon', 180),
    ('Seattle, Washington', 'Tacoma, Washington', 30),
    ('Raleigh, North Carolina', 'Greensboro, North Carolina', 80),
    ('Raleigh, North Carolina', 'Fayetteville, North Carolina', 60),
    ('Raleigh, North Carolina', 'Columbia, South Carolina', 220),
    ('Raleigh, North Carolina', 'Richmond, Virginia', 140),
    ('Raleigh, North Carolina', 'Washington, D.C.', 270),
    ('Baton Rouge, Louisiana', 'New Orleans, Louisiana', 80),
    ('Baton Rouge, Louisiana', 'Shreveport, Louisiana', 210),
    ('Oklahoma City, Oklahoma', 'Kansas City, Missouri', 350),
    ('Oklahoma City, Oklahoma', 'Dallas, Texas', 205),
    ('Oklahoma City, Oklahoma', 'Wichita, Kansas', 160),
    ('Oklahoma City, Oklahoma', 'Tulsa, Oklahoma', 107),
    ('Oklahoma City, Oklahoma', 'Fort Worth, Texas', 204),
    ('Oklahoma City, Oklahoma', 'Memphis, Tennessee', 382),
    ('Oklahoma City, Oklahoma', 'Little Rock, Arkansas', 333),
    ('Oklahoma City, Oklahoma', 'Kansas City, Kansas', 355),
    ('Oklahoma City, Oklahoma', 'St.Louis, Missouri', 430),
    ('Oklahoma City, Oklahoma', 'Houston, Texas', 430),
    ('Oklahoma City, Oklahoma', 'Des Moines, Iowa', 358),
    ('Kansas City, Missouri', 'Oklahoma City, Oklahoma', 350),
    ('Kansas City, Missouri', 'Des Moines, Iowa', 189),
    ('Kansas City, Missouri', 'St. Louis, Missouri', 248),
    ('Kansas City, Missouri', 'Wichita, Kansas', 198),
    ('Kansas City, Missouri', 'Omaha, Nebraska', 187),
    ('Kansas City, Missouri', 'Tulsa, Oklahoma', 236),
    ('Kansas City, Missouri', 'Little Rock, Arkansas', 303),
    ('Denver, Colorado', 'Salt Lake City, Utah', 516),
    ('Denver, Colorado', 'Albuquerque, New Mexico', 447),
    ('Denver, Colorado', 'Boise, Idaho', 500),
    ('Denver, Colorado', 'Oklahoma City, Oklahoma', 526),
    ('Denver, Colorado', 'Kansas City, Missouri', 600),
    ('El Paso, Texas', 'Albuquerque, New Mexico', 269),
    ('El Paso, Texas', 'Phoenix, Arizona', 347),
    ('El Paso, Texas', 'Austin, Texas', 554),
    ('El Paso, Texas', 'Oklahoma City, Oklahoma', 500),
    ('El Paso, Texas', 'San Antonio, Texas', 547),
    ('Washington, D.C.', 'Baltimore, Maryland', 38),
    ('Washington, D.C.', 'Philadelphia, Pennsylvania', 123),
    ('Washington, D.C.', 'Richmond, Virginia', 110),
    ('Washington, D.C.', 'Raleigh, North Carolina', 257),
    ('Detroit, Michigan', 'Chicago, Illinois', 282),
    ('Detroit, Michigan', 'Columbus, Ohio', 170),
    ('Detroit, Michigan', 'Indianapolis, Indiana', 250),
    ('Detroit, Michigan', 'Cleveland, Ohio', 169),
    ('Detroit, Michigan', 'Cincinnati, Ohio', 243),
    ('Boston, Massachusetts', 'New York City, New York', 215),
    ('Nashville, Tennessee', 'Memphis, Tennessee', 200),
    ('Nashville, Tennessee', 'Louisville, Kentucky', 173),
    ('Nashville, Tennessee', 'Indianapolis, Indiana', 260),
    ('Nashville, Tennessee', 'Atlanta, Georgia', 216),
    ('Nashville, Tennessee', 'St. Louis, Missouri', 250),
    ('Memphis, Tennessee', 'Nashville, Tennessee', 200),
    ('Memphis, Tennessee', 'Louisville, Kentucky', 167),
    ('Memphis, Tennessee', 'Little Rock, Arkansas', 137),
    ('Memphis, Tennessee', 'St. Louis, Missouri', 210),
    ('Portland, Oregon', 'Seattle, Washington', 173),
    ('Portland, Oregon', 'Boise, Idaho', 344),
    ('Portland, Oregon', 'Sacramento, California', 527),
    ('Portland, Oregon', 'San Francisco, California', 633),
    ('Las Vegas, Nevada', 'Los Angeles, California', 236),
    ('Las Vegas, Nevada', 'Henderson, Nevada', 13),
    ('Las Vegas, Nevada', 'Phoenix, Arizona', 298),
    ('Louisville, Kentucky', 'Nashville, Tennessee', 167),
    ('Louisville, Kentucky', 'Cincinnati, Ohio', 98),
    ('Louisville, Kentucky', 'Indianapolis, Indiana', 112),
    ('Louisville, Kentucky', 'Lexington, Kentucky', 74),
    ('Baltimore, Maryland', 'Washington, D.C.', 38),
    ('Baltimore, Maryland', 'Philadelphia, Pennsylvania', 106),
    ('Baltimore, Maryland', 'Arlington, Virginia', 40),
    ('Milwaukee, Wisconsin', 'Chicago, Illinois', 92),
    ('Milwaukee, Wisconsin', 'Madison, Wisconsin', 77),
    ('Milwaukee, Wisconsin', 'Minneapolis, Minnesota', 337),
    ('Milwaukee, Wisconsin', 'Detroit, Michigan', 278),
    ('Milwaukee, Wisconsin', 'Green Bay, Wisconsin', 117),
    ('Milwaukee, Wisconsin', 'St. Paul, Minnesota', 321),
    ('Albuquerque, New Mexico', 'Phoenix, Arizona', 392),
    ('Albuquerque, New Mexico', 'El Paso, Texas', 266),
    ('Albuquerque, New Mexico', 'Mesa, Arizona', 343),
    ('Albuquerque, New Mexico', 'Tucson, Arizona', 324),
    ('Albuquerque, New Mexico', 'Colorado Springs, Colorado', 323),
    ('Albuquerque, New Mexico', 'Denver, Colorado', 447),
    ('Albuquerque, New Mexico', 'Oklahoma City, Oklahoma', 543),
    ('Albuquerque, New Mexico', 'Arlington, Texas', 596),
    ('Albuquerque, New Mexico', 'Dallas, Texas', 617),
    ('Albuquerque, New Mexico', 'Tulsa, Oklahoma', 679),
    ('Tucson, Arizona', 'Phoenix, Arizona', 114),
    ('Tucson, Arizona', 'Mesa, Arizona', 108),
    ('Tucson, Arizona', 'Chandler, Arizona', 115),
    ('Fresno, California', 'Sacramento, California', 157),
    ('Fresno, California', 'San Jose, California', 150),
    ('Fresno, California', 'Oakland, California', 171),
    ('Fresno, California', 'Stockton, California', 83),
    ('Sacramento, California', 'San Francisco, California', 86),
    ('Sacramento, California', 'Oakland, California', 86),
    ('Sacramento, California', 'San Jose, California', 119),
    ('Sacramento, California', 'Fresno, California', 157),
    ('Sacramento, California', 'Reno, Nevada', 131),
    ('Mesa, Arizona', 'Phoenix, Arizona', 12),
    ('Mesa, Arizona', 'Chandler, Arizona', 5),
    ('Mesa, Arizona', 'Gilbert, Arizona', 6),
    ('Mesa, Arizona', 'Scottsdale, Arizona', 9),
    ('Mesa, Arizona', 'Tempe, Arizona', 5),
    ('Atlanta, Georgia', 'Charlotte, North Carolina', 245),
    ('Atlanta, Georgia', 'Raleigh, North Carolina', 311),
    ('Atlanta, Georgia', 'Nashville, Tennessee', 213),
    ('Atlanta, Georgia', 'Birmingham, Alabama', 147),
    ('Long Beach, California', 'Los Angeles, California', 20),
    ('Long Beach, California', 'Anaheim, California', 14),
    ('Long Beach, California', 'Santa Ana, California', 17),
    ('Omaha, Nebraska', 'Wichita, Kansas', 191),
    ('Omaha, Nebraska', 'Kansas City, Missouri', 186),
    ('Omaha, Nebraska', 'Minneapolis, Minnesota', 274),
    ('Omaha, Nebraska', 'Des Moines, Iowa', 129),
    ('Miami, Florida', 'Hialeah, Florida', 5),
    ('Miami, Florida', 'Miami Gardens, Florida', 12),
    ('Miami, Florida', 'Miami Beach, Florida', 5),
    ('Miami, Florida', 'Fort Lauderdale, Florida', 27),
    ('Oakland, California', 'San Francisco, California', 11),
    ('Oakland, California', 'San Jose, California', 31),
    ('Oakland, California', 'Fremont, California', 17),
    ('Oakland, California', 'Hayward, California', 15),
    ('Oakland, California', 'Berkeley, California', 6),
    ('Oakland, California', 'Richmond, California', 12),
    ('Minneapolis, Minnesota', 'St. Paul, Minnesota', 9),
    ('Minneapolis, Minnesota', 'Bloomington, Minnesota', 13),
    ('Minneapolis, Minnesota', 'Eagan, Minnesota', 9),
    ('Oklahoma City, Oklahoma', 'Tulsa, Oklahoma', 105),
    ('Wichita, Kansas', 'Tulsa, Oklahoma', 159),
    ('Pittsburgh, Pennsylvania', 'Cleveland, Ohio', 134),
    ('Detroit, Michigan', 'Cleveland, Ohio', 95),
    ('Columbus, Ohio', 'Cleveland, Ohio', 143),
    ('Kansas City, Missouri', 'Wichita, Kansas', 156),
    ('Oklahoma City, Oklahoma', 'Wichita, Kansas', 166),
    ('Dallas, Texas', 'Arlington, Texas', 20),
    ('Fort Worth, Texas', 'Arlington, Texas', 8),
    ('Baton Rouge, Louisiana', 'New Orleans, Louisiana', 79),
    ('Fresno, California', 'Bakersfield, California', 106),

]


def create_graph():

    graph_manager = GraphManager()

    for row in data:
        start_city, end_city, distance = row
        graph_manager.add_city(start_city)
        graph_manager.add_city(end_city)
        graph_manager.add_connection(start_city, end_city, distance)
    return graph_manager


def get_coordinates(city):
    city_coordinates = {
        'New York City, New York': (40.7128, -74.0060),
        'Los Angeles, California': (34.0522, -118.2437),
        'Chicago, Illinois': (41.8781, -87.6298),
        'Houston, Texas': (29.7604, -95.3698),
        'Phoenix, Arizona': (33.4484, -112.0740),
        'Philadelphia, Pennsylvania': (39.9526, -75.1652),
        'San Antonio, Texas': (29.4241, -98.4936),
        'San Diego, California': (32.7157, -117.1611),
        'Dallas, Texas': (32.7767, -96.7970),
        'San Jose, California': (37.3541, -121.9552),
        'Austin, Texas': (30.2672, -97.7431),
        'Jacksonville, Florida': (30.3322, -81.6557),
        'San Francisco, California': (37.7749, -122.4194),
        'Indianapolis, Indiana': (39.7684, -86.1581),
        'Columbus, Ohio': (39.9612, -82.9988),
        'Fort Worth, Texas': (32.7555, -97.3308),
        'Charlotte, North Carolina': (35.2271, -80.8431),
        'Seattle, Washington': (47.6062, -122.3321),
        'Denver, Colorado': (39.7392, -104.9903),
        'El Paso, Texas': (31.7619, -106.4850),
        'Washington, D.C.': (38.8951, -77.0369),
        'Boston, Massachusetts': (42.3601, -71.0589),
        'Detroit, Michigan': (42.3314, -83.0458),
        'Nashville, Tennessee': (36.1627, -86.7816),
        'Memphis, Tennessee': (35.1495, -90.0490),
        'Portland, Oregon': (45.5051, -122.6750),
        'Oklahoma City, Oklahoma': (35.4634, -97.5151),
        'Las Vegas, Nevada': (36.1699, -115.1398),
        'Louisville, Kentucky': (38.2527, -85.7585),
        'Baltimore, Maryland': (39.2904, -76.6122),
        'Milwaukee, Wisconsin': (43.0389, -87.9065),
        'Albuquerque, New Mexico': (35.0844, -106.6504),
        'Tucson, Arizona': (32.2226, -110.9747),
        'Fresno, California': (36.7468, -119.7726),
        'Sacramento, California': (38.5816, -121.4944),
        'Kansas City, Missouri': (39.0997, -94.5786),
        'Mesa, Arizona': (33.4152, -111.8315),
        'Atlanta, Georgia': (33.7490, -84.3880),
        'Long Beach, California': (33.7701, -118.1937),
        'Omaha, Nebraska': (41.2565, -95.9345),
        'Raleigh, North Carolina': (35.7796, -78.6382),
        'Miami, Florida': (25.7617, -80.1918),
        'Oakland, California': (37.8044, -122.2711),
        'Minneapolis, Minnesota': (44.9778, -93.2650),
        'Tulsa, Oklahoma': (36.1540, -95.9928),
        'Cleveland, Ohio': (41.4993, -81.6944),
        'Wichita, Kansas': (37.6872, -97.3301),
        'Arlington, Texas': (32.7357, -97.1081),
        'New Orleans, Louisiana': (29.9511, -90.0715),
        'Bakersfield, California': (35.3733, -119.0187),
        'Tampa, Florida': (27.9506, -82.4572),
        'Honolulu, Hawaii': (21.3069, -157.8583),
        'Aurora, Colorado': (39.7294, -104.8319),
        'Anaheim, California': (33.8366, -117.9143),
        'Santa Ana, California': (33.7455, -117.8677),
        'St. Louis, Missouri': (38.6270, -90.1994),
        'Riverside, California': (33.9534, -117.3962),
        'Corpus Christi, Texas': (27.8006, -97.3964),
        'Lexington, Kentucky': (38.0406, -84.5037),
        'Stockton, California': (37.9577, -121.2908),
        'Pittsburgh, Pennsylvania': (40.4406, -79.9959),
        'St. Paul, Minnesota': (44.9537, -93.0892),
        'Anchorage, Alaska': (61.2181, -149.9003),
        'Cincinnati, Ohio': (39.1031, -84.5120),
        'Henderson, Nevada': (36.0395, -114.9817),
        'Greensboro, North Carolina': (36.0726, -79.7910),
        'Plano, Texas': (33.0198, -96.6989),
        'Newark, New Jersey': (40.7357, -74.1724),
        'Toledo, Ohio': (41.6639, -83.5552),
        'Fort Wayne, Indiana': (41.0793, -85.1394),
        'St. Petersburg, Florida': (27.7676, -82.6403),
        'Laredo, Texas': (27.5306, -99.4803),
        'Jersey City, New Jersey': (40.7282, -74.0776),
        'Chandler, Arizona': (33.3062, -111.8413),
        'Madison, Wisconsin': (43.0731, -89.4012),
        'Lubbock, Texas': (33.5779, -101.8552),
        'Scottsdale, Arizona': (33.4942, -111.9261),
        'Reno, Nevada': (39.5296, -119.8138),
        'Buffalo, New York': (42.8864, -78.8784),
        'Gilbert, Arizona': (33.3528, -111.7890),
        'Glendale, Arizona': (33.5387, -112.1858),
        'North Las Vegas, Nevada': (36.1989, -115.1175),
        'Winston-Salem, North Carolina': (36.0999, -80.2442),
        'Chesapeake, Virginia': (36.7682, -76.2875),
        'Norfolk, Virginia': (36.8508, -76.2859),
        'Boise, Idaho': (43.6150, -116.2023),
        'Richmond, Virginia': (37.5407, -77.4360),
        'Baton Rouge, Louisiana': (30.4515, -91.1871),
        'Spokane, Washington': (47.6588, -117.4260),
        'Des Moines, Iowa': (41.5868, -93.6250),
        'Montgomery, Alabama': (32.3792, -86.3077),
        'Modesto, California': (37.6391, -120.9969),
        'Fayetteville, North Carolina': (35.0527, -78.8784),
        'Tacoma, Washington': (47.2529, -122.4443),
        'Shreveport, Louisiana': (32.5252, -93.7502),
        'San Bernardino, California': (34.1083, -117.2898)
    }

    return city_coordinates.get(city, [0, 0])


def draw_graph(graph_manager):
    G = graph_manager.get_graph()

    # Create a Folium map centered at a specific location
    map_center = get_coordinates("Jefferson City")
    m = folium.Map(location=map_center, zoom_start=7)

    # Create markers for cities
    for node in G.nodes():
        city_coords = get_coordinates(node)
        if city_coords != [0, 0]:
            folium.Marker(location=city_coords, popup=node).add_to(m)

    # Create lines for connections
    for edge in G.edges():
        start, end = edge
        start_coords = get_coordinates(start)
        end_coords = get_coordinates(end)
        if start_coords != [0, 0] and end_coords != [0, 0]:
            folium.PolyLine([start_coords, end_coords], color="blue").add_to(m)

    m.save("city_map.html")

    G = graph_manager.get_graph()

    canvas = Canvas(root, width=900, height=800)
    canvas.pack()

    pos = nx.spring_layout(G)

    for node in G.nodes():
        x, y = pos[node]
        x, y = x * 300 + 400, y * 300 + 300  # Scale and position nodes
        canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="lightblue")
        canvas.create_text(x, y, text=node)

    for edge in G.edges():
        start, end = edge
        x1, y1 = pos[start]
        x2, y2 = pos[end]
        x1, y1 = x1 * 300 + 400, y1 * 300 + 300
        x2, y2 = x2 * 300 + 400, y2 * 300 + 300
        canvas.create_line(x1, y1, x2, y2, fill="blue")


def show_all_cities_on_map():
    draw_graph(graph_manager)
    webbrowser.open("city_map.html")


def find_shortest_path():
    start_city = start_city_entry.get()
    end_city = end_city_entry.get()

    shortest_path, shortest_distance = graph_manager.get_shortest_path_with_intermediate_hops(
        start_city, end_city)

    if shortest_path:
        result_label.config(
            text=f"Shortest Path: {shortest_path}\nShortest Distance: {shortest_distance:.2f} miles")
        # draw_graph(graph_manager, cities_to_display=shortest_path)
        map_center = get_coordinates("Kansas City")
        m = folium.Map(location=map_center, zoom_start=7)

        # Create a line to represent the path
        path_coords = [get_coordinates(city) for city in shortest_path]
        folium.PolyLine(locations=path_coords, color="red").add_to(m)

        # Add markers for cities
        for city in shortest_path:
            city_coords = get_coordinates(city)
            if city_coords != [0, 0]:
                folium.Marker(location=city_coords, popup=city).add_to(m)

        m.save("city_map_with_path.html")
        webbrowser.open("city_map_with_path.html")

    else:
        result_label.config(
            text=f"No path found from {start_city} to {end_city}.")


root = tk.Tk()
root.title("City Path Finder")
start_city_label = tk.Label(root, text="Start City:")
start_city_label.pack()
start_city_entry = tk.Entry(root)
start_city_entry.pack()
end_city_label = tk.Label(root, text="End City:")
end_city_label.pack()
end_city_entry = tk.Entry(root)
end_city_entry.pack()
find_button = tk.Button(root, text="Find Shortest Path",
                        command=find_shortest_path)
find_button.pack()
show_all_cities_button = tk.Button(root, text="Show All Cities on Map",
                                   command=show_all_cities_on_map)
show_all_cities_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
graph_manager = create_graph()

root.mainloop()
