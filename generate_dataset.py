<<<<<<< HEAD
import Augmentor
p = Augmentor.Pipeline("animals")
p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
p.rotate(probability=0.2, max_left_rotation=10, max_right_rotation=10)
p.flip_left_right(probability=0.3)
p.flip_top_bottom(0.1)
p.crop_random(probability=0.1, percentage_area=0.5)
p.zoom(probability=0.3, min_factor=1.1, max_factor=1.6)
p.resize(probability=1.0, width=120, height=120)
p.sample(30000)
# print(os.getcwd())
=======
import Augmentor
p = Augmentor.Pipeline("animals")
p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
p.rotate(probability=0.2, max_left_rotation=10, max_right_rotation=10)
p.flip_left_right(probability=0.3)
p.flip_top_bottom(0.1)
p.crop_random(probability=0.1, percentage_area=0.5)
p.zoom(probability=0.3, min_factor=1.1, max_factor=1.6)
p.resize(probability=1.0, width=120, height=120)
p.sample(30000)
# print(os.getcwd())
>>>>>>> e354189448834a19363cb47b2e6566d23968bb73
