# Advanced BIM - Group 20
## Group Members
#### 1. Umair Abid Mughal
#### 2. Hajar Benjdya
#### 3. Eloise Catherine Helene Birkeland

## Question 2: Markdown File describing our Use Case

### Describe the use case you have chosen
Our use case is Structural Use Case and a bit of code validation to go along with it. To elaborate, our goal is to formulate a process which will enable us to extract structural elements from an IFC model, and generate a simplified structural model, which can be read and utilized for Structural Analysis in any FEM software.  
	
### Who is the use case for?
The use case primarily for Structural Engineers and consultants, who are required to extrapolate useful information for 'Structural Analysis' from IFC models. Moreover, this usecase is also useful for analysis of existing structure, especially in cases where existing design needs to be changed or additional construction is planned on the existing structure. This tool is also useful for validating the conformance of materials and elements with specified codes, before a structure is built. 
	
### What disciplinary (non BIM) expertise did you use to solve the use case?
To address this usecase, a working knowledge of Structural Analysis and Design is required. Additionally, working knowledge of FEM software and python is also a pre-requisite for solving this use case  
	
### What IFC concepts did you use in your script (would you use in your script)
Finding lengths of various Ifc element arrays, calling a Ifc file to extract information from it, using the called Ifc file to extract element attributes and element properties such as lengths. Using the Ifc file to display the element count for various structural elements and also displaying their attributes. Also, getting location of various elements will be required to enable them to be used with an FEM software. 

	
### What disciplinary analysis does it require?
Structural Analysis and Code Validation

### What building elements are you interested in?
Primarily, the following elements will serve as adequate inputs for Structural Use Case: Beams, Columns, Walls, Slabs & Roof

### What (use cases) need to be done before you can start your use case?
Architectual IFC model

### What is the input data for your use case?
Dimensions of the structural elements, Material usage of various elements, Location of the structural elements, Load Data such as wind, gravity, seismic and live loads, Element joints/connections data

### What other use cases are waiting for your use case to complete?
Code Validation, LCA, Fire
