import os

# Networking

host = "localhost"
port = 8888

# Client

frame_rate = 30

# Window

background_color = 0, 0, 0
window_size = 650, 585
window_caption = "Raanana Tira Project"

# Matrix

matrix_height = 9
matrix_width = 4
row_height = 65
cell_width = 130
left_margin = 95
top_margin = 10

# Files

install_dir = os.path.dirname(__file__)
obstacles_glob = os.path.join(install_dir, '../client/res/obstacles/obstacle*.png')
road_glob = os.path.join(install_dir, '../client/res/bg/bg*.png')
cars_dir = os.path.join(install_dir, '../client/res/cars')

# Player

max_lives = 3
max_players = 4
