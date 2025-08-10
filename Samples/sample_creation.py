# Units: Millimeters (mm)
import cadquery as cq
from cadquery.vis import show

# Define the dimensions of the box
box_length = 100.0
box_width = 100.0
box_height = 5

# Define the dimensions of the circular void
void_radius = 10.0
void_height = 1.5 # The actual height/depth of the circular void
void_z_offset = 1.5 # Distance from the bottom of the box to the bottom of the void

# Create the main box object
# We start on the XY plane. The .box() method creates a box centered at the origin.
# So, the bottom of the box will be at Z = -box_height / 2.
box = cq.Workplane("XY").box(box_length, box_width, box_height)

# Calculate the Z-position for the center of the void cylinder.
# The void_cylinder is created centered on its own height by default.
# 1. Start from the bottom of the box: -box_height / 2
# 2. Add the offset from the bottom: + void_z_offset
# 3. Add half of the void's depth to get to its center: + (void_height / 2)
void_center_z = (-box_height / 2) + void_z_offset + (void_height / 2)

# Create the cylinder that will form the void
# Use the new 'void_height' for the cylinder's height
void_cylinder = cq.Workplane("XY").cylinder(void_height, void_radius)

# Translate the void cylinder to its desired position within the box
# We only need to translate along the Z-axis, as X and Y are already centered.
void_cylinder = void_cylinder.translate((0, 0, void_center_z))

# Cut the cylinder from the box to create the void
# The .cut() method subtracts the second object from the first
result = box.cut(void_cylinder)

result.export(f"sample_1_r_{void_radius}_h_{void_height}_d_{void_z_offset}.step", "STEP")
print("exported")

cylinder = cq.Workplane("XY").cylinder(void_height, void_radius)
cylinder = cylinder.translate((0, 0, void_center_z))

# Cut the cylinder from the box to create the void
# The .cut() method subtracts the second object from the first
result_2 = cylinder

result_2.export(f"sample_1_cyliner.step", "STEP")
print("exported")



