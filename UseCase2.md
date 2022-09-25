# 1 Goal
The goal of the tool is to extract a simplified structural model from an IFC model to facilitate structural analysis using Rhino/Grasshopper tools. The tool will need to translate the incoming data to a format readable by the FEM plugin used in Grasshopper. 

# 2 Model Use (BIM uses) 
The whole use case is of type **03 Analyse** according to the Penn State document, where the subtype would be **03 Validate**, since the model would be used to validate the structural system. Our tool to help with this overall process is of type **04 Communicate** and either subprocess **02 Transform** or **03 Draw** since the architectural/structural model will be *transformed* to allow structural analysis model. 

## 2.1 Model benefits
Translation between tools that otherwise are not compatible provides value by facilitating more responsive design decisions where effects of changes can be immediately forecasted thus shortening design phases for better cost effectiveness.  Software based tools also reduce human documentation load and avoid introduction of errors when moving from one format to another by standardizing the translation method. 
By using relatively inexpensive and customizable FEM tools in a parametric environment both the complexity, required time can be reduced and the responsiveness of designing structures can be increased. 

## 2.2 Scope
The scope of the FEM analysis and translation includes extracting structural load bearing and stabilizing elements from the model as well as cross section, material, and physical properties from the elements. The tool will not automatically access dead loads from other geometry to be applied to the structure nor will it automatically apply other dynamic loads. It is assumed that this information often stays the same regardless of chances to the structural design and therefore do not need to be setup many times. 

## 2.3 Further development out of scope
One thing that would strengthen the tool, would be if it was able to do optimizations through iterations (so-called dynamic modelling) and then transferring this optimized structural system back into the arch model. This would mean that the model should be able to transform the FEM-data structure back into Revit or IFC, and change the original model -- alternatively, it should work so fast that the arch team wouldn’t have made any changes to the original in the time it would take to do a structural analysis. 
## 2.3.1 Making of structural report
Another feature that would save time, would be the automatic generation of a structural report documenting loads and other assumptions, as well as doing screenshots of the structural system on specific beams, columns, or walls. 

# 3 Process 
The generic process map for performing structural analysis can be seen in the BPMN below. For the generic process each step moving between tasks is heavily manual. 

![BPMN of full system](./GenericProcessMap_UseCase2_StructuralAnalysis.svg "Full BPMN-diagram of process")

Below the actual process map for the tool can be seen. Here the process is largely automated with only the definition of loads and last decision point (marked with an asterisk) being manual.

![BPMN of our tool](./ActualProcessMap_UseCase2_StructuralAnalysis.svg "Our BIM tool")

# 4 Information exchange
Since we require information about material properties of the construction materials as well as cross sections and CC-distances, both the LOG and LOI must be quite high. In theory, LOG could be low, if a high LOI is provided. However, differences in LOI and LOG might lead to confusion in the design team, why compliance between LOI and LOG is preferred. Generally, a LOG of 325 is required and a LOI of 400. The detailed specification of the information exchange requirements can be found in the attached [Excel-file](./ExchangeInformation_UseCase2_StructuralAnalysis.xlsx).

# 5 Our tool
The benefit of the tool is to make more complicated FEM design accessible and cheaper than it *normally* is. Usually, a great deal of time is spent in structural 3D modelling programs, where the structural system is built by itself, and no there is no direct transfer of data between the arch model and the structural data. Therefore, FEM and structural models are only used when there is a complex structural system to be analyzed. 
Automatically setting up structural string models would therefor allow for more complex solutions and/or quicker documentation for the structural system. Software based tools also reduce human documentation load and avoid introduction of errors when moving from one format to another by standardizing the translation method. 
The base tool shall remove the process of modelling one structural model for drawings and then having to do a separate model for calculations. The parametric environment in which the tool uses for the FEM analysis also allows designers to be more flexible with what happens with the structural model. At this point the plan is to use the Grasshopper environment *Alpaca4D* as the FEM tool of choice. 

# 6 IFC
The following table translates the elements from the information exchange requirements to IFC entities and their properties that will be the actual sources when extracting data from a model. For some reason, there is no entity called an IfcColumn, however, columns should be extracted as well, as they are an integrated part of the structural system. 

| IFC entity | EIR element | IFC properties |
| :--- | :--- | :---| 
| IfcWallStandardCase or IfcWall<br>(IfcWall doesn’t support material layers) | Exterior, interior and subgrade walls<br> as well as certain foundations | Type Name : Found directly as a property of the entity<br>Structural : Found through *Pset_WallCommon* under *LoadBearing*<br>Geometry : Found in *IfcProductDefinitionShape* as a *IfcPolyline* and *IfcExtrusion*<br><br>If concrete:<br>Strength class : Found in *Pset_ConcreteElementGeneral*<br>Reinforcement strength class : Found in *Pset_ConcreteElementGeneral*<br>Reinforcement ratio : Found in *Pset_ConcreteElementGeneral*<br>Other materials:<br>Strength class : Assumed defined in a custom property set |
| IfcSlab (or IfcPlate) | All slabs or elements with<br>much greater area than thickness | Type Name : Found directly as a property of the entity<br>Structural : Found through *Pset_SlabCommon* under *LoadBearing*<br>Geometry : Found in *IfcProductDefinitionShape* as a *IfcPolyline* and *IfcExtrusion*<br><br>If concrete:<br>Strength class : Found in *Pset_ConcreteElementGeneral*<br>Reinforcement strength class : Found in *Pset_ConcreteElementGeneral*<br>Reinforcement ratio : Found in *Pset_ConcreteElementGeneral*<br>Other materials:<br>Strength class : Assumed defined in a custom property set |
| IfcBeam or IfcMember | All beams<br>(includes truss elements) | Type Name : Found directly as a property of the entity<br> Structural : Found through *Pset_BeamCommon* under *LoadBearing*<br>Geometry : Multiple methods, found under *IfcProductDefinitonShape* as profiles or polylines most often<br>Material / strength : Found through inverse association to *IfcMaterial* |
| IfcColumn | All beams<br>(includes truss elements) | Type Name : Found directly as a property of the entity<br> Structural : Found through *Pset_ColumnCommon* under *LoadBearing*<br>Geometry : Multiple methods, found under *IfcProductDefinitonShape* as profiles or polylines most often<br>Material / strength : Found through inverse association to *IfcMaterial* |
| IfcRoof | All roofs<br>(decomposes to slab if no slope) | Type Name : Found directly as a property of the entity<br>Structural : Found through *Pset_SlabCommon* under *LoadBearing*<br>Geometry : Found in *IfcProductDefinitionShape* as a *IfcPolyline* and *IfcExtrusion*<br><br>If concrete:<br>Strength class : Found in *Pset_ConcreteElementGeneral*<br>Reinforcement strength class : Found in *Pset_ConcreteElementGeneral*<br>Reinforcement ratio : Found in *Pset_ConcreteElementGeneral*<br>Other materials:<br>Strength class : Assumed defined in a custom property set |

For all elements, if they have the property *Structural Usage* they can be defined according to the below table:

| Usage | Number | Description |
| :--- | :--- | :--- |
| 1 | Shear | Rigid planar surfaces that inherently resist lateral thrusts of shear |
| 2 | Bearing | Elements that support a load in addition to their own weight |
| 3 | Non-bearing | Elements that only support their own weight but no additional weight |
| 4 | Structural combined | Elements that serve more than one of the above purposes |

# 7 Delivery
The initial step of the tool broadly requires the extraction of two types of data from the IFC and would perhaps be structured with a function for each of these. The first function will search for and extract system lines from all the geometry that has the load bearing property or is defined as stabilizing. These system lines are what will form the basis of the model in grasshopper. We imagine that the geometry will be extracted as points from the IFC file and then built into lines, curves or regions with native grasshopper components. The second function will retrieve material and cross section properties from the elements. For example columns will need a cross section and physical properties (elasticity, compression strength, bending, shear and so on). The data for the structural elements is linked to the elements via Type name. 
Lastly load information is applied natively in Grasshopper using the FEM plugin. Throughout the process we will probably require the model in standard SI-units. The analyzing and processing of results can then proceed and presented. In principle the results and what happens with the model could change to meet the needs of the individual. 
