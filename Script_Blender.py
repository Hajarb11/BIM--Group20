### Import libraries to allow blender to work with Python ###
### Importing function from blenderbim library to store file, and to allow us to extract information from the model we've opened ###

import bpy
from blenderbim.bim.ifc import IfcStore

### Function to store file in a variable called 'file' ###
file = IfcStore.get_file()

### STRUCTURAL ELEMENTS VARIABLE DEFINITION ###

beams = file.by_type('IfcBeam')
walls = file.by_type('IfcWall')
columns = file.by_type('IfcColumn')
slabs = file.by_type('IfcSlab')

### COUNT STRUCTURAL ELEMENTS ###

print('Number of beams = {length}'.format(length=len(beams)))
print('Number of walls = {length}'.format(length=len(walls)))
print('Number of columns = {length}'.format(length=len(columns)))
print('Number of slabs = {length}'.format(length=len(slabs))) 

### ATTRIBUTES FOR FIRST FIVE BEAMS ###

count = 1

for beam in beams[:6]:
    print('Details of beam number {}'.format(count))
    print('The Name of the beam is: {}'.format(beam.Name))
    print('The Global ID of the beam is: {}'.format(beam.id()))
    print('The Tag of the beam is: {}'.format(beam.Tag))
    print('The Object Type of the beam is: {}'.format(beam.ObjectType))
    print('\n \n')
    count+=1
    
### FUNCTION FOR PROPERTY SET "NAME" IN BEAM ###

for beam in beams:
##Using for loop to search the column/array 'IsDefinedBy' which contains property sets for all types of elements
    for definition in beams.IsDefinedBy:
    ##Using if function to filter properties which we need 
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition
            print(property_set.Name)
            
            
### NAMES OF ALL THE PROPERTIES ASSOCIATED WITH A BEAM ###

for beam in beams:
    for definition in beam.IsDefinedBy:
        for properties in definition.RelatingPropertyDefinition.HasProperties:
            print(properties.Name)
        
### TOTAL BEAM LENGTH IN PROJECT ###

total_beam_length = 0

for beam in beams:
    for definition in beam.IsDefinedBy:
        for properties in definition.RelatingPropertyDefinition.HasProperties:
            if properties.Name == 'Length':
                total_beam_length += properties.NominalValue.wrappedValue

print('The total length of all the beams in the project is: {}'.format(total_beam_length))

### MATERIAL PROPERTIES OF A BEAM ### 

for beam in beams:
    for relAssociatesMaterial in beam.HasAssociations:
        print(relAssociatesMaterial.RelatingMaterial.Name)

