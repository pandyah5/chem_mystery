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

The project abides by Doxygen style comments structure to generate API documentation. As a consequence any contributions to the project should abide by Doxygen comment style. 

The output will follow the datastructure design as described below:

# Datastructure design
The database has the following classes:

- Bond: (Base class)
  - From:
  - To:
- Single bond: (Derived from bond)
  - From:
  - To:
- Double bond: (Derived from bond)
  - From:
  - To:
- Triple bond: (Derived from bond)
  - From:
  - To:

- atom:
  - Element:
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
  

