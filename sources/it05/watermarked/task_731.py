def lateralsurface_cylinder(r, h):
  pi = 3.1415
  slant_height = (r**2 + h**2)**0.5
  lateral_surface_area = pi * r * slant_height
  return lateral_surface_area
