# chem_mystery
This is an open-source project to convert chemical compound schematics to a data structure that can be used for further processing.

# Design documentation
This project will take chemical compound schematics that fulfill the below criteria:

- The "carbon" atoms are represented as "C" instead of intersections of two bonds (lines) or as a single dot.
- The atoms currently supported are: C (carbon), H (hydrogen), O (oxygen), S (sulphur), and N (nitrogen).
- We currently support the following bonds:
  - Single covalent bonds
  - Double covalent bonds
  - Triple covalent bonds
- For optimal results the atom symbol should not touch the bond lines but be really close to it.
- We would also recommend not including lone pairs for better results. We will compute lone pair information and add it in the database 😄

The project abides by Doxygen style comments structure to generate API documentation. As a consequence any contributions to the project should abide by Doxygen comment style. 

The output will follow the datastructure design as described below:

# Datastructure design
The database has the following classes:

- Bond: (Base class)
  - From: atom
  - To: atom
- Single bond: (Derived from bond)
  - From: atom
  - To: atom
- Double bond: (Derived from bond)
  - From: atom
  - To: atom
- Triple bond: (Derived from bond)
  - From: atom
  - To: atom

- atom:
  - Element:
  - x:
  - y:
  - Valence atoms:
  - Number of electrons:
  - Atomic weight: 
  - Free electrons:
  - List of bonds: <list of Bonds>

- molecule
  - Name:
  - Molecular weight:
  - Leading carbon:
  - Hashmap for element-number_of_atoms:
  - List of atom and bonds: (We will store this as a adjacency list, because the graph will most likely be sparse)
  
# Step by step workflow:
  
### Step 1 - Atom recognition
  The first step is to recognize the elementary atoms from the picture and store the atoms x and y corrdinates. This would require a letter recognition model that encircles the atom using the rectangle. The x and y coordinates are obtained by computing the midpoint of the box. We will do this using a custom fast compute ML model designed for this use case. We will first try to use a light mobilenet variant for transfer learning
  
### Step 2 - Bond recognition
  The next step is to identify bonds. We will try using a custom line identifying model and train it to differentiate between single, double and triple bonds. The bonds will follow a radial proximity rule i.e. the end points of the bonds will be mapped to the atom if the atom is within certain radius of the endpoint. The exact radius will be defined after analyzing the average distance from the bond and the standard devition of the dataset.
  
### Step 3 - Database construction
  This involves populating the class objects with the collected data and making API to access the information from the atoms and molecules.
  
# Future usecases:
  - IUPAC nomenclature
  - Educational Applications that link structures with properties
  - Analyzing similarilities between structures
  - Making a huge database of chemical structures
  - Simulating reactions (Will need more information and functionality integrated)
  

