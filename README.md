# Openrocket to SCAD (DOES NOT WORK YET)
This is a python utility to convert openrocket .ork files to SCAD files. Openrocket files are actually zipped [xml](openrocketFileDocumentation.md), so using some simple python libraries it is easy to parse, and match scad snippets to xml elements/
## Requirements
 - Python
 - `xml.etree.ElementTree`
 - `os`
 - `zipfile`
 - `shutil`
All of these should come packages with modern versions of python
## Instructions
1. Run the Python file
2. Enter the filename or the path to the .ork file
3. Unless the -o option is used, the generated file will be `out.scad`