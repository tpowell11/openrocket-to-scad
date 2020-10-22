# Openrocket file specification
# 1: Structure
A .ork file is actually a zip, which contains that file "rocket.ork". Unlike the previous level, this .ork is just a reextended XML file. Renaming it will reveal the rest of the structure. 
## 1.1: High Level Tags / Meta tags
### 1.1.1: openrocket
This tag contains all other tags in the file, with the exeption of `<?xml>.` This tags attributes holds the file version (see the offical OpenRocket repo for details), and which version of the program it was created with. 
### 1.1.2: rocket
This tag contains all of the rocket components.
### 1.1.3: name
Holds the name of the rocket in the tag's text, for example `<name>Name</name>`
### 1.1.4: motorconfiguration
The tag's atributes are a `configid`, which appears to be a registry format key, and a bool regarding weather the particular configuration is the default.
### 1.1.5: referencetype
Unsure as to what this does
## 1.2: Rocket components
### 1.2.1: subcomponents
`<subcompoents>` acts as the container for all compoents that are children of another component. The exeption being when it's only parent is `<rocket>`, then it is just a container for parts.
### 1.2.2: stage
For each stage defined in the editor, it's components will be held in a `<stage>` tag.
## 1.3: Rocket Parts
All of the below parts must be contained in a `<subcomponents>` tag.
### 1.3.1: nosecone
`<nosecone>` is defined by:
```xml
<name>Nose cone</name>
<finish>normal</finish>
<material type="bulk" density="500.0">Basswood</material>
<length>0.22</length>
<thickness>0.002</thickness>
<shape>power</shape>
<shapeclipped>false</shapeclipped>
<shapeparameter>0.4</shapeparameter>
<aftradius>0.075</aftradius>
<aftshoulderradius>0.0</aftshoulderradius>
<aftshoulderlength>0.0</aftshoulderlength>
<aftshoulderthickness>0.0</aftshoulderthickness>
<aftshouldercapped>false</aftshouldercapped>
```
A note about the `<shape>` tag: most of its values are the same as the field in the editor, exept for power, paraolic, and Haak series. These are truncated as power, parabolic, and haak, respectivley.
### 1.3.2 bodytube
`<bodytube>`is defined by:
```xml
<bodytube>
<name>Body tube</name>
<finish>normal</finish>
<material type="bulk" density="680.0">Cardboard</material>
<length>0.3</length>
<thickness>0.002</thickness>
<radius>auto</radius>
```
### 1.3.3 transition
`<transition>` is defined by:
```xml 
<transition>
<name>Transition</name>
<finish>normal</finish>
<material type="bulk" density="500.0">Basswood</material>
<length>0.11</length>
<thickness>0.002</thickness>
<shape>haack</shape>
<shapeclipped>true</shapeclipped>
<shapeparameter>0.3</shapeparameter>
<foreradius>auto</foreradius>
<aftradius>0.05</aftradius>
<foreshoulderradius>0.0</foreshoulderradius>
<foreshoulderlength>0.0</foreshoulderlength>
<foreshoulderthickness>0.0</foreshoulderthickness>
<foreshouldercapped>false</foreshouldercapped>
<aftshoulderradius>0.0</aftshoulderradius>
<aftshoulderlength>0.0</aftshoulderlength>
<aftshoulderthickness>0.0</aftshoulderthickness>
<aftshouldercapped>false</aftshouldercapped>
</transition>
```
### 1.3.4 freeformfinset
### 1.3.5 trapezoidfinset
### 1.3.6 ellipticalfinset
### 1.3.7 tubefinset
## 1.4: Simulation components
Simulation components include `<masscomponent>, <shockcord>, /motormount/<motor>`
### 1.4.1: masscomponent
A masscomponent is a point mass which effects simulations defined by
```xml
<masscomponent>
    <name>Unspecified</name>
    <position type="top">0.11</position>
    <packedlength>0.05</packedlength>
    <packedradius>0.0225</packedradius>
    <radialposition>0.0</radialposition>
    <radialdirection>0.0</radialdirection>
    <mass>0.061</mass>
    <masscomponenttype>masscomponent</masscomponenttype>
</masscomponent>
```