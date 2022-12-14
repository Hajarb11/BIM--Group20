### Import ifcopenshell in Python to allow us to work with IFC files
### Importing function from blenderbim library to store file, and to allow us to extract information from the model we've opened

def funtion_ifc(dir)

    import ifcopenshell

    ### Function to store file in a variable called 'file'
    file = ifcopenshell.open(dir)

    ### Functions to define various structural elements in the model
    beams = file.by_type('IfcBeam')
    walls = file.by_type('IfcWall')
    columns = file.by_type('IfcColumn')
    slabs = file.by_type('IfcSlab')

    ###Function Used to count the number of Structural Elements
    print('Number of beams = {length}'.format(length=len(beams)))
    print('Number of walls = {length}'.format(length=len(walls)))
    print('Number of columns = {length}'.format(length=len(columns)))
    print('Number of slabs = {length}'.format(length=len(slabs))) 

    ###Function that prints the attributes for the first five beams in the project. The same can be repeated for all other elements
    count = 1

    for beam in beams[:6]:
        print('Details of beam number {}'.format(count))
        print('The Name of the beam is: {}'.format(beam.Name))
        print('The Global ID of the beam is: {}'.format(beam.id()))
        print('The Tag of the beam is: {}'.format(beam.Tag))
        print('The Object Type of the beam is: {}'.format(beam.ObjectType))
        print('\n \n')
        count+=1
    
    ###Writing a function to get "Names" of all the properties associated with a beam

    for beam in beams:
    ###Using for loop to search the column/array 'IsDefinedBy' which contains property sets for all types of elements
        for definition in beams.IsDefinedBy:
        ###Using if function to filter properties which we need 
            if definition.is_a('IfcRelDefinesByProperties'):
                property_set = definition.RelatingPropertyDefinition
                print(property_set.Name)
            
            
    ###Writing a function to get "Names" of all the properties associated with a beam. Using these names, we can output any property we desire

    for beam in beams:
        for definition in beam.IsDefinedBy:
            for properties in definition.RelatingPropertyDefinition.HasProperties:
                print(properties.Name)
        
    ###Writing a function to get total combined length of all beams in the file
    total_beam_length = 0

    for beam in beams:
        for definition in beam.IsDefinedBy:
            for properties in definition.RelatingPropertyDefinition.HasProperties:
                if properties.Name == 'Length':
                    total_beam_length += properties.NominalValue.wrappedValue

    print('The total length of all the beams in the project is: {}'.format(total_beam_length))

