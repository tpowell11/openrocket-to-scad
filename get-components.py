#Converter by Tom Powell
#SCAD Nosecone Library by Garrett Goss

import os #file io
import xml.etree.ElementTree as ET #xml handling
import zipfile #ork is just zipped xml
import shutil #for removing temp directory
class BodyTube(object):
    "Holds the physical values for any <bodytube>"
    length = 0
    wall_thickness = 0  
    radius = 0
    pass
class NoseCone(object):
    "Holds the physcial attributes for any <nosecone>"
    length=0
    thickness = 0
    #parameters for the nosecone generator
    generator = ""
    generator_parameter = 0
    generator_end_radius = 0 
    generator_is_clipped = False
    #parameters for the shoulder generator
    shoulder_length = 0
    shoulder_radius = 0 
    shoulder_thickness = 0
    shoulder_capped = False
    pass
class standardFinset(object):
    "contains standard auti fins"
    pass
class freeformFinset(object):
    "contains freeform fins"
    finpoints = []
    pass
class Transition(object):
    "holds the physcial values for <transition>"
    length = 0
    thickness = 0
    #Shape generator parameters
    generator = ""
    generator_is_clipped = False
    generator_parameter = 0
    #fore
    fore_radius = "" #it's weird, there'll be a class methof soon enough
    fore_shoulder_radius = 0 
    fore_shoulder_length = 0
    fore_shoulder_thickness = 0
    fore_shoulder_capped = False
    #aft
    aft_radius = ""
    aft_shoulder_radius = 0
    aft_shoulder_length = 0
    aft_shoulder_thickness = 0 
    aft_shoulder_capped = False
    pass
class Launch_Lug(object):
    "Storage class for launch lug"
    position = 0
    radius = 0
    length = 0 
    thickness = 0
    radialdirection = 0 
    pass
#---------------------------
#functions
def setupTempDir():
    "makes a dir for the xml extraction, if it already exists it is removed"
    if os.path.isdir("temp/") == True:
        shutil.rmtree("temp/")
    else: 
        os.mkdir("temp/")#make temp directory

def extractXml(filename):
    "unzips the ork, and parses the internal file as a xml"
    try:
        setupTempDir()
        target = zipfile.ZipFile(filename) #open the zip/ork
        target.extractall('temp') #extract to the temp directory
        tree = ET.parse('temp/rocket.ork')
        root = tree.getroot()
    except FileNotFoundError: 
        print("cant find that file, exiting")
        exit()
    return root

def cleanup():
    "cleans up any leftover temporary files after execution"
    shutil.rmtree("temp/")

def parse(root):
    elements = []
    profile = [] #final profile of the rocket 
    v1outline = []
    v2outline = []
    v3outline = []
    v3positions = []
    #gets the number of top level components, builds the highest level outline
    for item in root.findall("rocket/subcomponents/stage/subcomponents/"):
        v1outline.append(item.tag) #get all of the highest-level physical components
    print("\ntop-level components", v1outline)

    #gets the number of bodytubes and builds the 2nd level outline 
    tubesCT = v1outline.count('bodytube')
    print("\nthere are %s bodytubes" %tubesCT) #cool print syntax
    for x in range(tubesCT):
        print('\ntube number', str(x+1))
        for item in root.findall("rocket/subcomponents/stage/subcomponents/bodytube["+ str(x+1) +"]/"):
            print("\t",[item.tag, item.text])
            v2outline.append(item.tag)

def getComponent(component):
    "gets the requested component"
    
#---------------------------
#MAIN
def main():
    print("Openrocket to SCAD \u00a9 Tom Powell\nEnter the name of a ORK file:\n")
    while (1):
        try:
            inp = input(">")
            parse(extractXml(inp))
            selection = input("what component are you looking for? :\n")
            getComponent(selection)
        except KeyboardInterrupt:
            cleanup()
            print("Exitied")
            exit()
if __name__ == "__main__":
    main()
    pass
