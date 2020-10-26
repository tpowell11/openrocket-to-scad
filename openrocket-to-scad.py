#Converter by Tom Powell
#SCAD Nosecone Library by Garrett Goss

import os #file io
import xml.etree.ElementTree as ET #xml handling
import zipfile #ork is just zipped xml
import shutil #for removing temp directory

#---------------------------
#GLOBALS
#make xml avalible
#rockettree = ET.parse("rocket.xml") #parse rockettree
#rocketroot = rockettree.getroot() #find rocketroot 
#--------------------------
#CLASSES
class BodyTube(object):
    "Holds the physical values for any <bodytube>"
    length = 0
    wall_thickness = 0  
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
#scad file preamble data
version = "v0.0\n"
renderParameters = "$fa = 50\n$fs = 50\n"
#---------------------------
#FUNCTIONS
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

def getNoseconeParameters(ext_root):
    "parses the parameters of the <nosecone> component"
    print("Getting Nosecone...")
    elements = []
    for item in ext_root.findall('rocket/subcomponents/stage/subcomponents/nosecone/'):
        if item.tag != "subcomponents":
            elements.append([item.tag, item.text]) #add tags / values to elements[]
    output = NoseCone()
    output.length = elements[2][1] #[field nubmer][0: tag; 1: value]
    output.thickness = elements[3][1]
    #shoulder generator params
    output.shoulder_radius = elements[8][1]
    output.shoulder_length = elements[9][1]
    output.shoulder_thickness = elements[10][1]
    output.shoulder_capped = elements[11][1]
    #nosecone generator params
    output.generator = elements[5][1]
    #output.generator_is_clipped = elements[5][1] ??????
    output.generator_parameter = elements[6][1]
    output.generator_end_radius = elements[7][1]
    return output 

def getBodytubeParameters(ext_root):
    "parses the parameters of the <bodytube> component"
    elements = []
    for item in ext_root.findall('rocket/subcomponents/stage/subcomponents/'):
        if item.tag != "subcomponents":
            elements.append([item.tag, item.text])

def getTransitionParameters(ext_root):
    "parses the parameters of the <transistion> component"
    elements = []
    for item in ext_root.findall('rocket/subcomponents/stage/subcomponents/nosecone/'):
        if item.tag != "subcomponents":
            elements.append([item.tag, item.text])
    output = Transition()
    output.length = elements[2][1]
    output.thickness = elements[3][1]
    output.generator = elements[4][1]
    output.generator_is_clipped = elements[5][1]
    output.fore_radius = elements[6][1]
    output.aft_radius = elements[7][1]
    #foreshoulder
    output.fore_shoulder_radius = elements[8][1]
    output.fore_shoulder_length = elements[9][1]
    output.fore_shoulder_thickness = elements[10][1]
    output.fore_shoulder_capped = elements[11][1]
    #aftshoulder
    output.aft_shoulder_radius = elements[12][1]
    output.aft_shoulder_length = elements[13][1]
    output.aft_shoulder_thickness = elements[14][1]
    output.aft_shoulder_capped = elements[15][1]
    return output

def getLaunchLugParameters(ext_root):
    "parses the parameters of the launchlug"
    elements = []
    for item in ext_root.findall('rocket/subcomponents/stage/subcomponents/bodytube/subcomponents/launchlug/'):
        elements.append([item.tag, item.text]) 
    output = Launch_Lug()
    output.position = elements[1][1]
    output.radius = elements[4][1]
    output.length = elements[5][1]
    output.thickness = elements[6][1]
    output.radialdirection = elements[7][1]
    return output

def generateNoseconeScad(ext_root):
    "returns the string to be printed to the scad file"
    print("Generating nosecone info...")
    noseconeGenerator = getNoseconeParameters(ext_root).generator
    noseconeShapeParameter = getNoseconeParameters(ext_root).generator_parameter
    noseconeRadius = getNoseconeParameters(ext_root).generator_end_radius
    noseconeLength = getNoseconeParameters(ext_root).length
    if noseconeGenerator == "power":
        return "cone_power_series(" + noseconeShapeParameter+","+ noseconeRadius +","+ noseconeLength + ");\n"
    elif noseconeGenerator == "haack":
        return "cone_haack(" + noseconeShapeParameter+","+noseconeRadius+","+noseconeLength+");\n"
    elif noseconeGenerator == "ogive":
        return "cone_ogive_tan(" + noseconeShapeParameter+","+noseconeRadius+","+noseconeLength+");\n"

def generateBodytubeScad():
    "retuens the string to be printed to the scad file for bodytube components"
    
def cleanup():
    "cleans up any leftover temporary files after execution"
    shutil.rmtree("temp/")

def build(infilename, outfilename="out"):
    outname = outfilename + ".scad"
    outfile = open(outname, "w")#file creation
    outfile.write("//Generated by ORK to SCAD " + version + "\n") #file title
    outfile.write(renderParameters) #the render settings for scad 
    outfile.write("include <rocketParts.scad>; //copackaged scad library\n")
    buildroot = extractXml(infilename) #get the etree.root to pass to other functions
    generateNoseconeScad(buildroot)

    outfile.close()#close file at end of write sequence
#---------------------------
#MAIN
def main():
    print("Openrocket to SCAD \u00a9 Tom Powell\n")
    while (1):
        try:
            inp = input(">")
            build(inp)
        except KeyboardInterrupt:
            cleanup()
            print("Exitied")
            exit()
if __name__ == "__main__":
    main()
    pass
