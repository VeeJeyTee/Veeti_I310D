def calculate_volume_of_sphere(radius):
  '''Calculate the volume of a sphere.'''
  pi = 3.14
  volume = 4/3 * pi * (radius)**3
  return volume

radius_1 = 30
volume_1 = calculate_volume_of_sphere(radius_1)
print(f"The volume of a sphere with a radius of {radius_1} is: {volume_1}")

radius_2 = 40 
volume_2 = calculate_volume_of_sphere(radius_2)
print(f"The volume of a sphere with a radius of {radius_2} is: {volume_2}")
