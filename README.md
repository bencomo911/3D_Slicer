# 3D_Slicer
The 3D Slicer Application is a proprietary software for the W.M. Keck Center for 3D Innovation. It combines a Python Qt frontend with a MATLAB backend to generate G-code from STL files primarily for 3D printing workflows. 

## Project Overview
3D Slicer is a desktop application that follows conventional slicing software workflows: it slices 3D models (STL files) into layers and generates G-code for 3D printers to process.The goal of developing this proprietary software is to test the newly researched infills in the lab. The GUI is built with PyQt5 providing user friendly controls for slicing customizations such as layer height, shell thickness, infill density, print speed, and infill type. The slicing computations are performed by a MATLAB backend script (`main.m`) accessed through the MATLAB Engine API for Python. 
MATLAB backend link: [here](https://github.com/wjk199511140034/AMebius-slicer/blob/master/main.m).

## Features
* **Interactive GUI** with parameter adjustments.
* **MATLAB backend integration** for G-code generation and slicing.
* **File Ingestion**: Reads data from stl file.
* **G-Code Output**: Outputs a G-code file readable by 3D printers and other CNC machines. 
* Slicing parameter customization: layer height, shell thickness, infill density, print speed
* API error handling and parameter validation.



