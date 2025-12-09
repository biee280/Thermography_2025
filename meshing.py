import pygmsh
import gmsh

with pygmsh.occ.Geometry() as geom:
    geom.characteristic_length_min = 3
    geom.characteristic_length_max = 3

    rectangle_2d = geom.add_rectangle([-1.0, -1.0, 0.0], 100, 100)
    disk_2d = geom.add_disk([50, 50], 10)
    
    geom.translate(disk_2d, [0, 0, 2])

    box_volume = geom.extrude(rectangle_2d, [0, 0, 5]) 
    
    disk_volume = geom.extrude(disk_2d, [0, 0, 2]) 
    
    sample = geom.boolean_difference(box_volume[1], disk_volume[1])

    mesh = geom.generate_mesh()
    gmsh.option.setNumber("Mesh.SaveGroupsOfNodes", 1)

    elementTypes, elementTags, nodeTags = gmsh.model.mesh.getElements(2, 14)
    surface_nodes = set(nodeTags[0])
    pygmsh.write("mesh.inp")

print('done')