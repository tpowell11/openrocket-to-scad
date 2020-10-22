# Openrocket to SCAD
This is a python utility to convert openrocket .ork files to SCAD files. Openrocket files are actually zipped [xml](openrocketFileDocumentation.md), so using some simple python libraries it is easy to parse, and match scad snippets to xml elements/
## Requirements
 - Python
 - `xml.etree.ElementTree`
 - `os`
## Instructions
1. Rename a given .ork file to .zip
2. Extract contents
3. In a terminal copy /extracted/rocket.xml to the directory where the python file is.
4. `python .\openrocket-to-scad.py`
5. A conversion.log and rocket.scad file will be generated.