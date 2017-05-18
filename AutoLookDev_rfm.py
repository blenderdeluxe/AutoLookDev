#AutoLookDev (ALD) was created by Valentin DAVID and is an open source script, making it freely usable, modifiable and distributable.
#AutoLookDev is intended to boost your workflow with Maya 2017 and RenderMan 21 / Arnold 4
#Contact : vdavid.pro@gmail.com
#If you're interested in seeing my work, please visit https://www.artstation.com/artist/vdavid
#See also : https://github.com/vdavidcg

import maya.cmds as cmds
from maya import mel
import mtoa.utils
import webbrowser
import time
import os

# **************** GLOBAL VARIABLES ****************
version_nbr = "AutoLookDev for Renderman v1.1.0"

black_level = 0.015
grey_level = 0.18
white_level = 0.7

macbethA1 = [0.175,0.078,0.053] #Dark skin
macbethA2 = [0.558,0.279,0.212] #Light skin
macbethA3 = [0.105,0.188,0.328] #Blue sky
macbethA4 = [0.107,0.150,0.051] #Foliage
macbethA5 = [0.227,0.212,0.429] #Blue flower
macbethA6 = [0.114,0.509,0.413] #Bluish green
macbethB1 = [0.745,0.202,0.030] #Orange
macbethB2 = [0.060,0.102,0.386] #Purplish blue
macbethB3 = [0.558,0.080,0.114] #Moderate red
macbethB4 = [0.109,0.042,0.138] #Purple
macbethB5 = [0.332,0.497,0.042] #Yellow green
macbethB6 = [0.768,0.356,0.020] #Orange Yellow
macbethC1 = [0.021,0.048,0.283] #Blue
macbethC2 = [0.047,0.292,0.061] #Green
macbethC3 = [0.445,0.037,0.041] #Red
macbethC4 = [0.839,0.571,0.005] #Yellow
macbethC5 = [0.521,0.078,0.287] #Magenta
macbethC6 = [0.000,0.235,0.376] #Cyan
macbethD1 = 0.888
macbethD2 = 0.591
macbethD3 = 0.366
macbethD4 = 0.191
macbethD5 = 0.091
macbethD6 = 0.032

ALD_ID = "ALD_UI"

ald_update_url = "https://github.com/vdavidcg/AutoLookDev/"
ald_readme_url = "https://github.com/vdavidcg/AutoLookDev/blob/master/README.TXT"
webbrowser_new = 2

folderA = "C:/Users/"
folderB = "/Documents/maya/AutoLookDev/hdri_array"
folderC = "/Documents/maya/AutoLookDev/lookdev_hdri"
folderD = "/Documents/maya/AutoLookDev"
username_envvar = os.environ["USERNAME"]
hdri_array_folder = folderA + username_envvar + folderB
lookdev_hdri_folder = folderA + username_envvar + folderC
autolookdev_folder = folderA + username_envvar + folderD
hdri_nodes = []


# **************** FUNCTIONS ****************
def init_ald_interface(*arg):
	try :
		cmds.deleteUI(ALD_ID)
	except RuntimeError :
		pass
	cmds.window(ALD_ID, title="AutoLookDev", width=300, tlb = 1)
	MasterLayout = cmds.columnLayout(adjustableColumn=True, width=300)
	cmds.text(label=version_nbr,h=20,bgc=(0,0.6,0.9))
	cmds.text(label="",h=1,bgc=(.9,0.447,0))
	SlaveLayout0 = cmds.rowColumnLayout(numberOfColumns=3)
	cmds.button(label="Create simple camera rig", width=200, enable=True, command=simple_camera_rig)
	cmds.button(label="Hide",width=50,command=hide_camera_rig)
	cmds.button(label="Delete", width=50, enable=True, command=delete_simple_camera_rig)
	cmds.button(label="Create complete camera rig", width=200, enable=True, command=complete_camera_rig)
	cmds.button(label="Hide",width=50,command=hide_camera_rig)
	cmds.button(label="Delete", width=50, enable=True, command=delete_complete_camera_rig)
	cmds.button(label="Create Macbeth Color Checker", width=200, enable=True, command=create_macbeth)
	cmds.button(label="Hide",width=50,command=hide_macbeth)
	cmds.button(label="Delete", width=50, enable=True, command=delete_macbeth)
	cmds.setParent('..')
	cmds.frameLayout(label="Lighting", collapsable=1,mh=0,cl=1)
	SlaveLayout1 = cmds.rowColumnLayout(numberOfColumns=3)
	cmds.button(label="Create 3 point light rig", width=200, enable=True, command=create_3pt_lightrig)
	cmds.button(label="Hide",width=50,command=hide_3pt_lightrig)
	cmds.button(label="Delete", width=50, enable=True, command=delete_3pt_lightrig)
	cmds.button(label="Import Lookdev HDRI", width=200, enable=True, command=import_3pt_hdri)
	cmds.button(label="Hide",width=50,command=hide_3pt_hdri)
	cmds.button(label="Delete", width=50, enable=True, command=delete_3pt_hdri)
	cmds.button(label="Create Cyclo", width=200, enable=True, command=create_cyclo)
	cmds.button(label="Hide",width=50,command=hide_cyclo)
	cmds.button(label="Delete", width=50, enable=True, command=delete_cyclo)
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.frameLayout(label="HDRI Array", collapsable=1,mh=0,cl=1)
	SlaveLayout1b = cmds.rowColumnLayout(numberOfColumns=3)
	cmds.button(label="Import HDRI Array", width=200, enable=True, command=import_hdri_array)
	cmds.button(label="Hide",width=50,command=hide_hdri_array)
	cmds.button(label="Delete", width=50, enable=True, command=delete_hdri_array)
	cmds.setParent('..')
	SlaveLayout1c = cmds.rowColumnLayout(numberOfColumns=1)
	cmds.button(label="Prepare for batch rendering",width=300,command=prepare_hdri_array)
	cmds.button(label="Open HDRI Array folder",width=300,command=open_hdri_array_folder)
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.frameLayout(label="Turn", collapsable=1,mh=0,cl=1)
	SlaveLayout2 = cmds.rowColumnLayout(numberOfColumns=2)
	cmds.button(label="Create turn locator", enable=True, width=250, command=create_turn_loc)
	cmds.button(label="Delete", enable=True, width=50, command=delete_turn_loc)
	cmds.setParent('..')
	SlaveLayout3 = cmds.rowColumnLayout(numberOfColumns=3)
	cmds.button(label="%d frames" % 50, width=100, enable=True, command=lambda *args: change_frames_number(50, *args))
	cmds.button(label="%d frames" % 100, width=100, enable=True, command=lambda *args: change_frames_number(100, *args))
	cmds.button(label="%d frames" % 150, width=100, enable=True, command=lambda *args: change_frames_number(150, *args))
	cmds.setParent('..')
	SlaveLayout4 = cmds.rowColumnLayout(numberOfColumns=2)
	cmds.text(label="Custom frame number : ", width=200)
	cmds.textField(width=100, enterCommand=lambda *args: change_frames_number(int(args[0])), changeCommand=lambda *args: change_frames_number(int(args[0])))
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.frameLayout(label="Geometry", collapsable=1,mh=0,cl=1)
	SlaveLayout5 = cmds.rowColumnLayout(numberOfColumns=2)
	cmds.button(label="Attach Subdiv Scheme",width=150,command=ald_subdiv_scheme)
	cmds.button(label="Detach Subdiv Scheme",width=150,command=ald_detach_subdiv_scheme)
	cmds.setParent('..')
	cmds.setParent('..')
	SlaveLayout6 = cmds.frameLayout(label="Help", collapsable=1,mh=0,cl=1)
	cmds.button(label="Check for updates",command=ald_update)
	cmds.button(label="Online Help",command=ald_readme)
	cmds.button(label="Open AutoLookDev folder",width=300,command=open_autolookdev_folder)
	#EDIT WINDOW
	cmds.window(ALD_ID, edit=True,resizeToFitChildren=True)
	cmds.showWindow()
	
def ald_update(*arg):
	webbrowser.open(ald_update_url)
	
def ald_readme(*arg):
	webbrowser.open(ald_readme_url)

def create_macbeth(*arg):
	#Delete pre-existing ald_macbeth
	delete_macbeth()
	#Create Macbeth ramps
	cmds.shadingNode("ramp",asTexture=True,name="ald_rampCol1")
	cmds.shadingNode("place2dTexture",asUtility=True,name="ald_rampCol1_place2dTexture")
	cmds.connectAttr("ald_rampCol1_place2dTexture.outUV","ald_rampCol1.uvCoord")
	cmds.connectAttr("ald_rampCol1_place2dTexture.outUvFilterSize","ald_rampCol1.uvFilterSize")
	cmds.setAttr("ald_rampCol1.type",1)
	cmds.setAttr("ald_rampCol1.interpolation",0)

	cmds.shadingNode("ramp",asTexture=True,name="ald_rampCol2")
	cmds.shadingNode("place2dTexture",asUtility=True,name="ald_rampCol2_place2dTexture")
	cmds.connectAttr("ald_rampCol2_place2dTexture.outUV","ald_rampCol2.uvCoord")
	cmds.connectAttr("ald_rampCol2_place2dTexture.outUvFilterSize","ald_rampCol2.uvFilterSize")
	cmds.setAttr("ald_rampCol2.type",1)
	cmds.setAttr("ald_rampCol2.interpolation",0)

	cmds.shadingNode("ramp",asTexture=True,name="ald_rampCol3")
	cmds.shadingNode("place2dTexture",asUtility=True,name="ald_rampCol3_place2dTexture")
	cmds.connectAttr("ald_rampCol3_place2dTexture.outUV","ald_rampCol3.uvCoord")
	cmds.connectAttr("ald_rampCol3_place2dTexture.outUvFilterSize","ald_rampCol3.uvFilterSize")
	cmds.setAttr("ald_rampCol3.type",1)
	cmds.setAttr("ald_rampCol3.interpolation",0)

	cmds.shadingNode("ramp",asTexture=True,name="ald_rampCol4")
	cmds.shadingNode("place2dTexture",asUtility=True,name="ald_rampCol4_place2dTexture")
	cmds.connectAttr("ald_rampCol4_place2dTexture.outUV","ald_rampCol4.uvCoord")
	cmds.connectAttr("ald_rampCol4_place2dTexture.outUvFilterSize","ald_rampCol4.uvFilterSize")
	cmds.setAttr("ald_rampCol4.type",1)
	cmds.setAttr("ald_rampCol4.interpolation",0)

	cmds.setAttr("ald_rampCol1.colorEntryList[0].color",macbethA1[0],macbethA1[1],macbethA1[2],type="float3")
	cmds.setAttr("ald_rampCol1.colorEntryList[0].position",0)
	cmds.setAttr("ald_rampCol1.colorEntryList[1].color",macbethA2[0],macbethA2[1],macbethA2[2],type="float3")
	cmds.setAttr("ald_rampCol1.colorEntryList[1].position",.167)
	cmds.setAttr("ald_rampCol1.colorEntryList[2].color",macbethA3[0],macbethA3[1],macbethA3[2],type="float3")
	cmds.setAttr("ald_rampCol1.colorEntryList[2].position",.333)
	cmds.setAttr("ald_rampCol1.colorEntryList[3].color",macbethA4[0],macbethA4[1],macbethA4[2],type="float3")
	cmds.setAttr("ald_rampCol1.colorEntryList[3].position",0.5)
	cmds.setAttr("ald_rampCol1.colorEntryList[4].color",macbethA5[0],macbethA5[1],macbethA5[2],type="float3")
	cmds.setAttr("ald_rampCol1.colorEntryList[4].position",.667)
	cmds.setAttr("ald_rampCol1.colorEntryList[5].color",macbethA6[0],macbethA6[1],macbethA6[2],type="float3")
	cmds.setAttr("ald_rampCol1.colorEntryList[5].position",.833)

	cmds.setAttr("ald_rampCol2.colorEntryList[0].color",macbethB1[0],macbethB1[1],macbethB1[2],type="float3")
	cmds.setAttr("ald_rampCol2.colorEntryList[0].position",0)
	cmds.setAttr("ald_rampCol2.colorEntryList[1].color",macbethB2[0],macbethB2[1],macbethB2[2],type="float3")
	cmds.setAttr("ald_rampCol2.colorEntryList[1].position",.167)
	cmds.setAttr("ald_rampCol2.colorEntryList[2].color",macbethB3[0],macbethB3[1],macbethB3[2],type="float3")
	cmds.setAttr("ald_rampCol2.colorEntryList[2].position",.333)
	cmds.setAttr("ald_rampCol2.colorEntryList[3].color",macbethB4[0],macbethB4[1],macbethB4[2],type="float3")
	cmds.setAttr("ald_rampCol2.colorEntryList[3].position",0.5)
	cmds.setAttr("ald_rampCol2.colorEntryList[4].color",macbethB5[0],macbethB5[1],macbethB5[2],type="float3")
	cmds.setAttr("ald_rampCol2.colorEntryList[4].position",.667)
	cmds.setAttr("ald_rampCol2.colorEntryList[5].color",macbethB6[0],macbethB6[1],macbethB6[2],type="float3")
	cmds.setAttr("ald_rampCol2.colorEntryList[5].position",.833)

	cmds.setAttr("ald_rampCol3.colorEntryList[0].color",macbethC1[0],macbethC1[1],macbethC1[2],type="float3")
	cmds.setAttr("ald_rampCol3.colorEntryList[0].position",0)
	cmds.setAttr("ald_rampCol3.colorEntryList[1].color",macbethC2[0],macbethC2[1],macbethC2[2],type="float3")
	cmds.setAttr("ald_rampCol3.colorEntryList[1].position",.167)
	cmds.setAttr("ald_rampCol3.colorEntryList[2].color",macbethC3[0],macbethC3[1],macbethC3[2],type="float3")
	cmds.setAttr("ald_rampCol3.colorEntryList[2].position",.333)
	cmds.setAttr("ald_rampCol3.colorEntryList[3].color",macbethC4[0],macbethC4[1],macbethC4[2],type="float3")
	cmds.setAttr("ald_rampCol3.colorEntryList[3].position",0.5)
	cmds.setAttr("ald_rampCol3.colorEntryList[4].color",macbethC5[0],macbethC5[1],macbethC5[2],type="float3")
	cmds.setAttr("ald_rampCol3.colorEntryList[4].position",.667)
	cmds.setAttr("ald_rampCol3.colorEntryList[5].color",macbethC6[0],macbethC6[1],macbethC6[2],type="float3")
	cmds.setAttr("ald_rampCol3.colorEntryList[5].position",.833)

	cmds.setAttr("ald_rampCol4.colorEntryList[0].color",macbethD1,macbethD1,macbethD1,type="float3")
	cmds.setAttr("ald_rampCol4.colorEntryList[0].position",0)
	cmds.setAttr("ald_rampCol4.colorEntryList[1].color",macbethD2,macbethD2,macbethD2,type="float3")
	cmds.setAttr("ald_rampCol4.colorEntryList[1].position",.167)
	cmds.setAttr("ald_rampCol4.colorEntryList[2].color",macbethD3,macbethD3,macbethD3,type="float3")
	cmds.setAttr("ald_rampCol4.colorEntryList[2].position",.333)
	cmds.setAttr("ald_rampCol4.colorEntryList[3].color",macbethD4,macbethD4,macbethD4,type="float3")
	cmds.setAttr("ald_rampCol4.colorEntryList[3].position",0.5)
	cmds.setAttr("ald_rampCol4.colorEntryList[4].color",macbethD5,macbethD5,macbethD5,type="float3")
	cmds.setAttr("ald_rampCol4.colorEntryList[4].position",.667)
	cmds.setAttr("ald_rampCol4.colorEntryList[5].color",macbethD6,macbethD6,macbethD6,type="float3")
	cmds.setAttr("ald_rampCol4.colorEntryList[5].position",.833)
	
	#Create alpha ramps
	cmds.shadingNode("ramp",asTexture=True,name="ald_rampAlpha1")
	cmds.shadingNode("place2dTexture",asUtility=True,name="ald_rampAlpha1_place2dTexture")
	cmds.connectAttr("ald_rampAlpha1_place2dTexture.outUV","ald_rampAlpha1.uvCoord")
	cmds.connectAttr("ald_rampAlpha1_place2dTexture.outUvFilterSize","ald_rampAlpha1.uvFilterSize")
	cmds.setAttr("ald_rampAlpha1.interpolation",0)
	cmds.setAttr("ald_rampAlpha1.colorEntryList[0].color",0,0,0,type="float3")
	cmds.setAttr("ald_rampAlpha1.colorEntryList[0].position",0)
	cmds.setAttr("ald_rampAlpha1.colorEntryList[1].color",1,1,1,type="float3")
	cmds.setAttr("ald_rampAlpha1.colorEntryList[1].position",.75)
	cmds.shadingNode("ramp",asTexture=True,name="ald_rampAlpha2")
	cmds.shadingNode("place2dTexture",asUtility=True,name="ald_rampAlpha2_place2dTexture")
	cmds.connectAttr("ald_rampAlpha2_place2dTexture.outUV","ald_rampAlpha2.uvCoord")
	cmds.connectAttr("ald_rampAlpha2_place2dTexture.outUvFilterSize","ald_rampAlpha2.uvFilterSize")
	cmds.setAttr("ald_rampAlpha2.interpolation",0)
	cmds.setAttr("ald_rampAlpha2.colorEntryList[0].color",0,0,0,type="float3")
	cmds.setAttr("ald_rampAlpha2.colorEntryList[0].position",0)
	cmds.setAttr("ald_rampAlpha2.colorEntryList[1].color",1,1,1,type="float3")
	cmds.setAttr("ald_rampAlpha2.colorEntryList[1].position",.25)
	cmds.shadingNode("ramp",asTexture=True,name="ald_rampAlpha3")
	cmds.shadingNode("place2dTexture",asUtility=True,name="ald_rampAlpha3_place2dTexture")
	cmds.connectAttr("ald_rampAlpha3_place2dTexture.outUV","ald_rampAlpha3.uvCoord")
	cmds.connectAttr("ald_rampAlpha3_place2dTexture.outUvFilterSize","ald_rampAlpha3.uvFilterSize")
	cmds.setAttr("ald_rampAlpha3.interpolation",0)
	cmds.setAttr("ald_rampAlpha3.colorEntryList[0].color",0,0,0,type="float3")
	cmds.setAttr("ald_rampAlpha3.colorEntryList[0].position",0)
	cmds.setAttr("ald_rampAlpha3.colorEntryList[1].color",1,1,1,type="float3")
	cmds.setAttr("ald_rampAlpha3.colorEntryList[1].position",.5)
	#Create grid
	cmds.shadingNode("grid",asTexture=True,name="ald_grid")
	cmds.shadingNode("place2dTexture",asUtility=True,name="ald_grid_place2dTexture")
	cmds.connectAttr("ald_grid_place2dTexture.outUV","ald_grid.uvCoord")
	cmds.connectAttr("ald_grid_place2dTexture.outUvFilterSize","ald_grid.uvFilterSize")
	cmds.setAttr("ald_grid_place2dTexture.repeatU",6)
	cmds.setAttr("ald_grid_place2dTexture.repeatV",4)
	cmds.setAttr("ald_grid.lineColor",0,0,0,type="float3")
	cmds.setAttr("ald_grid.fillerColor",1,1,1,type="float3")
	#Create color blend nodes
	cmds.shadingNode ("blendColors",asUtility=True,name="ald_blendColors1")
	cmds.shadingNode ("blendColors",asUtility=True,name="ald_blendColors2")
	cmds.shadingNode ("blendColors",asUtility=True,name="ald_blendColors3")
	cmds.shadingNode ("blendColors",asUtility=True,name="ald_blendColors4")
	#Create color remap node
	cmds.shadingNode("remapColor",asUtility=True,name="ald_remap_grid")
	cmds.setAttr("ald_remap_grid.inputMin",1)
	cmds.setAttr("ald_remap_grid.inputMax",0)
	#Merge ramps
	cmds.connectAttr("ald_rampCol1.outColor","ald_blendColors1.color1",force=True)
	cmds.connectAttr("ald_rampCol2.outColor","ald_blendColors1.color2",force=True)
	cmds.connectAttr("ald_rampAlpha1.outColor.outColorR","ald_blendColors1.blender",force=True)

	cmds.connectAttr("ald_rampCol3.outColor","ald_blendColors2.color1",force=True)
	cmds.connectAttr("ald_rampCol4.outColor","ald_blendColors2.color2",force=True)
	cmds.connectAttr("ald_rampAlpha2.outColor.outColorR","ald_blendColors2.blender",force=True)

	cmds.connectAttr("ald_blendColors1.output","ald_blendColors3.color1",force=True)
	cmds.connectAttr("ald_blendColors2.output","ald_blendColors3.color2",force=True)
	cmds.connectAttr("ald_rampAlpha3.outColor.outColorR","ald_blendColors3.blender",force=True)

	cmds.connectAttr("ald_grid.outColor","ald_remap_grid.color",force=True)
	cmds.connectAttr("ald_grid.outColor","ald_blendColors4.color1",force=True)
	cmds.connectAttr("ald_blendColors3.output","ald_blendColors4.color2",force=True)
	cmds.connectAttr("ald_remap_grid.outColorR","ald_blendColors4.blender",force=True)

	PxrSurface_ald_macbeth = cmds.shadingNode("PxrSurface", asShader=True, name="PxrSurface_ald_macbeth")
	cmds.connectAttr("ald_blendColors4.output","PxrSurface_ald_macbeth.diffuseColor",force=True)

	#Create Macbeth geometry and assign shader
	cmds.polyPlane(sx=6,sy=4,n="ald_macbeth_p")
	cmds.setAttr("ald_macbeth_p.scaleZ",.666667)
	cmds.setAttr("ald_macbeth_p.rotateX",90)
	cmds.makeIdentity(apply=True,s=1)
	cmds.hyperShade(assign=PxrSurface_ald_macbeth)
	#Disable cast shadows
	cmds.setAttr("ald_macbeth_p.castsShadows",0)
	

def delete_macbeth(*arg):
	try:
		cmds.delete("ald_rampCol1")
		cmds.delete("ald_rampCol1_place2dTexture")
		cmds.delete("ald_rampCol2")
		cmds.delete("ald_rampCol2_place2dTexture")
		cmds.delete("ald_rampCol3")
		cmds.delete("ald_rampCol3_place2dTexture")
		cmds.delete("ald_rampCol4")
		cmds.delete("ald_rampCol4_place2dTexture")
		cmds.delete("ald_rampAlpha1")
		cmds.delete("ald_rampAlpha1_place2dTexture")
		cmds.delete("ald_rampAlpha2")
		cmds.delete("ald_rampAlpha2_place2dTexture")
		cmds.delete("ald_rampAlpha3")
		cmds.delete("ald_rampAlpha3_place2dTexture")
		cmds.delete("ald_grid")
		cmds.delete("ald_grid_place2dTexture")
		cmds.delete("ald_blendColors1")
		cmds.delete("ald_blendColors2")
		cmds.delete("ald_blendColors3")
		cmds.delete("ald_blendColors4")
		cmds.delete("ald_remap_grid")
		cmds.delete("PxrSurface_ald_macbeth")
		cmds.delete("PxrSurface_ald_macbethSG")
		cmds.delete("ald_macbeth_p")
	except ValueError:
		pass
	

def complete_camera_rig(*arg):
	delete_complete_camera_rig()
	#Create Renderman PxrSurface shaders
	#Black ball shader
	PxrSurface_ald_blackball = cmds.shadingNode("PxrSurface", asShader=True, name="PxrSurface_ald_blackball")
	cmds.setAttr("PxrSurface_ald_blackball.diffuseColorR",black_level)
	cmds.setAttr("PxrSurface_ald_blackball.diffuseColorG",black_level)
	cmds.setAttr("PxrSurface_ald_blackball.diffuseColorB",black_level)
	cmds.setAttr("PxrSurface_ald_blackball.diffuseBackColorR",black_level)
	cmds.setAttr("PxrSurface_ald_blackball.diffuseBackColorG",black_level)
	cmds.setAttr("PxrSurface_ald_blackball.diffuseBackColorB",black_level)
	#Grey ball shader
	PxrSurface_ald_greyball = cmds.shadingNode("PxrSurface", asShader=True, name="PxrSurface_ald_greyball")
	#White ball shader
	PxrSurface_ald_whiteball = cmds.shadingNode("PxrSurface", asShader=True, name="PxrSurface_ald_whiteball")
	cmds.setAttr("PxrSurface_ald_whiteball.diffuseColorR",white_level)
	cmds.setAttr("PxrSurface_ald_whiteball.diffuseColorG",white_level)
	cmds.setAttr("PxrSurface_ald_whiteball.diffuseColorB",white_level)
	cmds.setAttr("PxrSurface_ald_whiteball.diffuseBackColorR",white_level)
	cmds.setAttr("PxrSurface_ald_whiteball.diffuseBackColorG",white_level)
	cmds.setAttr("PxrSurface_ald_whiteball.diffuseBackColorB",white_level)
	#Chrome ball shader
	PxrSurface_ald_chromeball = cmds.shadingNode("PxrSurface", asShader=True, name="PxrSurface_ald_chromeball")
	cmds.setAttr("PxrSurface_ald_chromeball.diffuseGain",0)
	cmds.setAttr("PxrSurface_ald_chromeball.specularFresnelMode",0)
	cmds.setAttr("PxrSurface_ald_chromeball.specularFaceColor",1,1,1,type="float3")
	cmds.setAttr("PxrSurface_ald_chromeball.specularEdgeColor",1,1,1,type="float3")
	cmds.setAttr("PxrSurface_ald_chromeball.specularRoughness",0)
	cmds.setAttr("PxrSurface_ald_chromeball.specularIor",0,0,0,type="float3")
	cmds.setAttr("PxrSurface_ald_chromeball.specularExtinctionCoeff",1,1,1,type="float3")
	#Create 50mm camera
	cmds.camera(fl=50, name="ald_camera")
	#Create balls geometries and assign shaders
	cmds.polySphere(name="ald_blackball_p")
	cmds.polySphere(name="ald_greyball_p")
	cmds.polySphere(name="ald_whiteball_p")
	cmds.polySphere(name="ald_chromeball_p")
	cmds.select("ald_blackball_p",r=True)
	cmds.hyperShade(assign=PxrSurface_ald_blackball)
	cmds.select("ald_greyball_p",r=True)
	cmds.hyperShade(assign=PxrSurface_ald_greyball)
	cmds.select("ald_whiteball_p",r=True)
	cmds.hyperShade(assign=PxrSurface_ald_whiteball)
	cmds.select("ald_chromeball_p",r=True)
	cmds.hyperShade(assign=PxrSurface_ald_chromeball)
	#Disable cast shadows render stats
	cmds.setAttr("ald_blackball_pShape.castsShadows",0)
	cmds.setAttr("ald_greyball_pShape.castsShadows",0)
	cmds.setAttr("ald_whiteball_pShape.castsShadows",0)
	cmds.setAttr("ald_chromeball_pShape.castsShadows",0)
	#Create Locator and lock transforms
	cmds.spaceLocator(name="distanceFromCamera_loc")
	cmds.setAttr("distanceFromCamera_loc.tx", lock=True)
	cmds.setAttr("distanceFromCamera_loc.ty", lock=True)
	cmds.setAttr("distanceFromCamera_loc.rx", lock=True)
	cmds.setAttr("distanceFromCamera_loc.ry", lock=True)
	cmds.setAttr("distanceFromCamera_loc.rz", lock=True)
	cmds.setAttr("distanceFromCamera_loc.sx", lock=True)
	cmds.setAttr("distanceFromCamera_loc.sy", lock=True)
	cmds.setAttr("distanceFromCamera_loc.sz", lock=True)
	#Create Macbeth color chart
	create_macbeth()
	#Parent balls to locator
	cmds.select("ald_blackball_p", replace=True)
	cmds.select("ald_greyball_p", add=True)
	cmds.select("ald_whiteball_p", add=True)
	cmds.select("ald_chromeball_p", add=True)
	cmds.select("ald_macbeth_p", add=True)
	cmds.select("distanceFromCamera_loc", add=True)
	cmds.parent()
	cmds.select(clear=True)
	cmds.select("distanceFromCamera_loc", replace=True)
	cmds.select("ald_camera1", add=True)
	cmds.parent()
	cmds.select(clear=True)
	#Translate locator to default position
	cmds.setAttr("distanceFromCamera_loc.translateZ",-50)
	#Attach Subdiv Scheme Attribute
	cmds.select("ald_blackball_p", replace=True)
	cmds.select("ald_greyball_p", add=True)
	cmds.select("ald_whiteball_p", add=True)
	cmds.select("ald_chromeball_p", add=True)
	ald_subdiv_scheme()
	cmds.select(clear=True)
	#Set expressions to match distance from camera and scale balls
	cmds.expression(s="ald_blackball_p.translateX = distanceFromCamera_loc.translateZ / 3.333333")
	cmds.expression(s="ald_blackball_p.translateY = distanceFromCamera_loc.translateZ / -6.25")
	cmds.expression(s="ald_blackball_p.scaleX = distanceFromCamera_loc.translateZ / -50")
	cmds.expression(s="ald_blackball_p.scaleY = distanceFromCamera_loc.translateZ / -50")
	cmds.expression(s="ald_blackball_p.scaleZ = distanceFromCamera_loc.translateZ / -50")

	cmds.expression(s="ald_greyball_p.translateX = distanceFromCamera_loc.translateZ / 4")
	cmds.expression(s="ald_greyball_p.translateY = distanceFromCamera_loc.translateZ / -6.25")
	cmds.expression(s="ald_greyball_p.scaleX = distanceFromCamera_loc.translateZ / -50")
	cmds.expression(s="ald_greyball_p.scaleY = distanceFromCamera_loc.translateZ / -50")
	cmds.expression(s="ald_greyball_p.scaleZ = distanceFromCamera_loc.translateZ / -50")

	cmds.expression(s="ald_whiteball_p.translateX = distanceFromCamera_loc.translateZ / 5")
	cmds.expression(s="ald_whiteball_p.translateY = distanceFromCamera_loc.translateZ / -6.25")
	cmds.expression(s="ald_whiteball_p.scaleX = distanceFromCamera_loc.translateZ / -50")
	cmds.expression(s="ald_whiteball_p.scaleY = distanceFromCamera_loc.translateZ / -50")
	cmds.expression(s="ald_whiteball_p.scaleZ = distanceFromCamera_loc.translateZ / -50")

	cmds.expression(s="ald_chromeball_p.translateX = distanceFromCamera_loc.translateZ / 6.666666")
	cmds.expression(s="ald_chromeball_p.translateY = distanceFromCamera_loc.translateZ / -6.25")
	cmds.expression(s="ald_chromeball_p.scaleX = distanceFromCamera_loc.translateZ / -50")
	cmds.expression(s="ald_chromeball_p.scaleY = distanceFromCamera_loc.translateZ / -50")
	cmds.expression(s="ald_chromeball_p.scaleZ = distanceFromCamera_loc.translateZ / -50")
	
	cmds.expression(s="ald_macbeth_p.scaleX = distanceFromCamera_loc.translateZ / -16.667")
	cmds.expression(s="ald_macbeth_p.scaleY = distanceFromCamera_loc.translateZ / -16.667")
	cmds.expression(s="ald_macbeth_p.scaleZ = distanceFromCamera_loc.translateZ / -16.667")
	cmds.expression(s="ald_macbeth_p.translateX = distanceFromCamera_loc.translateZ * 0.225")
	cmds.expression(s="ald_macbeth_p.translateY = distanceFromCamera_loc.translateZ / -9.25")
	
	#Create an offset
	cmds.select("ald_blackball_p", replace=True)
	cmds.select("ald_greyball_p", add=True)
	cmds.select("ald_whiteball_p", add=True)
	cmds.select("ald_chromeball_p", add=True)
	cmds.select("ald_macbeth_p", add=True)
	cmds.group(name="ald_balls_os")
	cmds.select("ald_balls_os.rotatePivot")
	cmds.move(0,0,-50, rotatePivotRelative=True)
	cmds.select("ald_balls_os.scalePivot")
	cmds.move(0,0,-50, rotatePivotRelative=True)
	cmds.select(clear=True)
	

def delete_complete_camera_rig(*arg):
	try:
		cmds.select(clear=True)
		cmds.select("ald_camera1")
		cmds.delete()
		cmds.delete("PxrSurface_ald_blackballSG")
		cmds.delete("PxrSurface_ald_chromeballSG")
		cmds.delete("PxrSurface_ald_greyballSG")
		cmds.delete("PxrSurface_ald_whiteballSG")
		cmds.delete("PxrSurface_ald_blackball")
		cmds.delete("PxrSurface_ald_greyball")
		cmds.delete("PxrSurface_ald_whiteball")
		cmds.delete("PxrSurface_ald_chromeball")
	except ValueError:
		pass

def simple_camera_rig(*arg):
	#Delete pre-existing rig
	delete_simple_camera_rig()
	# Create Renderman PxrSurface shaders
	# Grey ball shader
	PxrSurface_ald_greyball = cmds.shadingNode("PxrSurface", asShader=True, name="PxrSurface_ald_greyball")
	# Chrome ball shader
	PxrSurface_ald_chromeball = cmds.shadingNode("PxrSurface", asShader=True, name="PxrSurface_ald_chromeball")
	cmds.setAttr("PxrSurface_ald_chromeball.diffuseGain",0)
	cmds.setAttr("PxrSurface_ald_chromeball.specularFresnelMode",0)
	cmds.setAttr("PxrSurface_ald_chromeball.specularFaceColor",1,1,1,type="float3")
	cmds.setAttr("PxrSurface_ald_chromeball.specularEdgeColor",1,1,1,type="float3")
	cmds.setAttr("PxrSurface_ald_chromeball.specularRoughness",0)
	cmds.setAttr("PxrSurface_ald_chromeball.specularIor",0,0,0,type="float3")
	cmds.setAttr("PxrSurface_ald_chromeball.specularExtinctionCoeff",1,1,1,type="float3")
	#Create 50mm camera
	cmds.camera(fl=50, name="ald_camera")
	#Create balls geometries and assign shaders
	cmds.polySphere(name="ald_greyball_p")
	cmds.polySphere(name="ald_chromeball_p")
	cmds.select("ald_greyball_p",r=True)
	cmds.hyperShade(assign=PxrSurface_ald_greyball)
	cmds.select("ald_chromeball_p",r=True)
	cmds.hyperShade(assign=PxrSurface_ald_chromeball)
	#Disable cast and receive shadows render stats
	cmds.setAttr("ald_greyball_pShape.castsShadows",0)
	cmds.setAttr("ald_chromeball_pShape.castsShadows",0)
	#Create Locator and lock transforms
	cmds.spaceLocator(name="distanceFromCamera_loc")
	cmds.setAttr("distanceFromCamera_loc.tx", lock=True)
	cmds.setAttr("distanceFromCamera_loc.ty", lock=True)
	cmds.setAttr("distanceFromCamera_loc.rx", lock=True)
	cmds.setAttr("distanceFromCamera_loc.ry", lock=True)
	cmds.setAttr("distanceFromCamera_loc.rz", lock=True)
	cmds.setAttr("distanceFromCamera_loc.sx", lock=True)
	cmds.setAttr("distanceFromCamera_loc.sy", lock=True)
	cmds.setAttr("distanceFromCamera_loc.sz", lock=True)
	#Create Macbeth color chart
	create_macbeth()
	#Parent balls and macbeth to locator
	cmds.select("ald_greyball_p", r=True)
	cmds.select("ald_chromeball_p", add=True)
	cmds.select("ald_macbeth_p", add=True)
	cmds.select("distanceFromCamera_loc", add=True)
	cmds.parent()
	cmds.select(clear=True)
	cmds.select("distanceFromCamera_loc", replace=True)
	cmds.select("ald_camera1", add=True)
	cmds.parent()
	cmds.select(clear=True)
	#Translate locator to default position
	cmds.setAttr("distanceFromCamera_loc.translateZ",-50)
	#Attach Subdiv Scheme Attribute
	cmds.select("ald_greyball_p", r=True)
	cmds.select("ald_chromeball_p", add=True)
	mel.eval('execRmanMenuItem("SubdivAttr")')
	#cmds.displaySmoothness(divisionsU=3, divisionsV=3, pointsWire=16, pointsShaded=4, polygonObject=3)
	cmds.select(clear=True)
	#Set expressions to match distance from camera and scale balls
	cmds.expression(s="ald_greyball_p.translateX = distanceFromCamera_loc.translateZ / 3.333333")
	cmds.expression(s="ald_greyball_p.translateY = distanceFromCamera_loc.translateZ / -6.25")
	cmds.expression(s="ald_greyball_p.scaleX = distanceFromCamera_loc.translateZ / -50")
	cmds.expression(s="ald_greyball_p.scaleY = distanceFromCamera_loc.translateZ / -50")
	cmds.expression(s="ald_greyball_p.scaleZ = distanceFromCamera_loc.translateZ / -50")

	cmds.expression(s="ald_chromeball_p.translateX = distanceFromCamera_loc.translateZ / 4")
	cmds.expression(s="ald_chromeball_p.translateY = distanceFromCamera_loc.translateZ / -6.25")
	cmds.expression(s="ald_chromeball_p.scaleX = distanceFromCamera_loc.translateZ / -50")
	cmds.expression(s="ald_chromeball_p.scaleY = distanceFromCamera_loc.translateZ / -50")
	cmds.expression(s="ald_chromeball_p.scaleZ = distanceFromCamera_loc.translateZ / -50")
	
	cmds.expression(s="ald_macbeth_p.scaleX = distanceFromCamera_loc.translateZ / -16.667")
	cmds.expression(s="ald_macbeth_p.scaleY = distanceFromCamera_loc.translateZ / -16.667")
	cmds.expression(s="ald_macbeth_p.scaleZ = distanceFromCamera_loc.translateZ / -16.667")
	cmds.expression(s="ald_macbeth_p.translateX = distanceFromCamera_loc.translateZ * 0.275")
	cmds.expression(s="ald_macbeth_p.translateY = distanceFromCamera_loc.translateZ / -9.25")
	#Create an offset
	cmds.select("ald_greyball_p", r=True)
	cmds.select("ald_chromeball_p", add=True)
	cmds.select("ald_macbeth_p", add=True)
	cmds.group(name="ald_balls_os")
	cmds.select("ald_balls_os.rotatePivot")
	cmds.move(0,0,-50, rotatePivotRelative=True)
	cmds.select("ald_balls_os.scalePivot")
	cmds.move(0,0,-50, rotatePivotRelative=True)
	cmds.select(clear=True)
	
def delete_simple_camera_rig(*arg):
	try:
		cmds.select(clear=True)
		cmds.select("ald_camera1")
		cmds.delete()
		cmds.delete("PxrSurface_ald_chromeballSG")
		cmds.delete("PxrSurface_ald_greyballSG")
		cmds.delete("PxrSurface_ald_greyball")
		cmds.delete("PxrSurface_ald_chromeball")
	except ValueError:
		pass

def create_turn_loc(*arg):
	delete_turn_loc()
	cmds.spaceLocator(name="ald_turn_loc")
	cmds.setAttr("ald_turn_locShape.localScaleX",5)
	cmds.setAttr("ald_turn_locShape.localScaleY",5)
	cmds.setAttr("ald_turn_locShape.localScaleZ",5)
	cmds.currentTime(1)
	cmds.setKeyframe("ald_turn_loc", attribute="rotateY")
	cmds.currentTime(101)
	cmds.setAttr("ald_turn_loc.rotateY",360)
	cmds.setKeyframe("ald_turn_loc", attribute="rotateY")
	cmds.selectKey(clear=True)
	cmds.selectKey("ald_turn_loc", time=(1,101), attribute="rotateY")
	cmds.keyTangent(itt="linear", ott="linear")
	cmds.currentTime(1)
	cmds.playbackOptions(min=1, max=100)
	cmds.selectKey(clear=True)
	cmds.select(clear=True)

def delete_turn_keys(*arg):
	cmds.currentTime(1)
	cmds.cutKey("ald_turn_loc", time=(0,999999), attribute="rotateY", option="keys")
	cmds.selectKey(clear=True)
	cmds.select(clear=True)

def change_frames_number(*arg):
	frame_nb = arg[0]
	cmds.select("ald_turn_loc", r=True)
	delete_turn_keys()
	cmds.currentTime(1)
	cmds.setAttr("ald_turn_loc.rotateY",0)
	cmds.setKeyframe("ald_turn_loc", attribute="rotateY")
	cmds.currentTime(frame_nb + 1)
	cmds.setAttr("ald_turn_loc.rotateY",360)
	cmds.setKeyframe("ald_turn_loc", attribute="rotateY")
	cmds.selectKey("ald_turn_loc", time=(1,frame_nb + 1), attribute="rotateY")
	cmds.keyTangent(itt="linear", ott="linear")
	cmds.currentTime(1)
	cmds.playbackOptions(min=1, max=frame_nb)
	cmds.selectKey(clear=True)
	cmds.select(clear=True)
	
def delete_turn_loc(*arg):
	try:
		cmds.select("ald_turn_loc",r=True)
		cmds.delete()
	except ValueError:
		pass

def create_cyclo(*arg):
	delete_cyclo()
	#Create Cyclo
	ald_cyclo_p = cmds.polyPlane(w=100,h=100,sx=3,sy=3,n="ald_cyclo_p")
	ald_extrude = cmds.polyExtrudeEdge("ald_cyclo_p.e[21:23]",divisions=2)
	cmds.rename(ald_extrude,"ald_extrude")
	cmds.setAttr("ald_extrude.localTranslate",0,0,66)
	cmds.displaySmoothness("ald_cyclo_p",divisionsU=3,divisionsV=3,pointsWire=16,pointsShaded=4,polygonObject=3)
	cyclo_uv = cmds.polyProjection("ald_cyclo_p.f[9:14]",ch=1,type="Planar",ibd=1,md="z")
	cmds.setAttr(cyclo_uv[0]+".projectionHeight",100)
	cmds.DeleteHistory("ald_cyclo_p")
	cmds.select(clear=True)
	#Assign grey shader
	PxrSurface_ald_cyclo = cmds.shadingNode("PxrSurface", asShader=True, name="PxrSurface_ald_cyclo")
	cmds.setAttr("PxrSurface_ald_cyclo.diffuseColor",0.18,0.18,0.18)
	cmds.setAttr("PxrSurface_ald_cyclo.diffuseBackColor",0.18,0.18,0.18)
	cmds.select("ald_cyclo_p")
	cmds.hyperShade(assign=PxrSurface_ald_cyclo)
	#Assign grid texture
	cmds.shadingNode("grid",asTexture=True,name="ald_cyclo_grid")
	cmds.shadingNode("place2dTexture",asUtility=True,name="ald_cyclo_grid_place2dTexture")
	cmds.connectAttr("ald_cyclo_grid_place2dTexture.outUV","ald_cyclo_grid.uvCoord")
	cmds.connectAttr("ald_cyclo_grid_place2dTexture.outUvFilterSize","ald_cyclo_grid.uvFilterSize")
	cmds.setAttr("ald_cyclo_grid_place2dTexture.repeatU",32)
	cmds.setAttr("ald_cyclo_grid_place2dTexture.repeatV",32)
	cmds.setAttr("ald_cyclo_grid.lineColor",.2,.2,.2,type="float3")
	cmds.setAttr("ald_cyclo_grid.fillerColor",.18,.18,.18,type="float3")
	cmds.setAttr("ald_cyclo_grid.uWidth",.05)
	cmds.setAttr("ald_cyclo_grid.vWidth",.05)
	cmds.connectAttr("ald_cyclo_grid.outColor","PxrSurface_ald_cyclo.diffuseColor",f=True)
	cmds.select("ald_cyclo_p",r=True)
	ald_subdiv_scheme()
	
def delete_cyclo(*arg):
	try:
		cmds.select("ald_cyclo_p",r=True)
		cmds.delete()
		cmds.delete("ald_cyclo_grid")
		cmds.delete("PxrSurface_ald_cyclo")
		cmds.delete("ald_cyclo_grid_place2dTexture")
	except ValueError:
		pass

def create_3pt_lightrig(*arg):
	#Delete if already exists
	delete_3pt_lightrig()
	#Create Lightrig
	ald_key_l = cmds.shadingNode("PxrDiskLight",asLight=True)
	ald_fill_l = cmds.shadingNode("PxrRectLight",asLight=True)
	ald_rim_l = cmds.shadingNode("PxrDiskLight",asLight=True)
	ald_dome_l = cmds.shadingNode("PxrDomeLight",asLight=True)
	cmds.rename(ald_key_l,"ald_key_l")
	cmds.rename(ald_fill_l,"ald_fill_l")
	cmds.rename(ald_rim_l,"ald_rim_l")
	cmds.rename(ald_dome_l,"ald_dome_l")
	create_cyclo()
	#Create and parent locator
	ald_lightrig_loc = cmds.spaceLocator(name="ald_lightrig_loc")
	cmds.group("ald_key_l","ald_fill_l","ald_dome_l","ald_rim_l","ald_cyclo_p","ald_lightrig_loc",name="ald_3pt_lightrig_grp")
	cmds.parent("ald_key_l","ald_fill_l","ald_rim_l","ald_dome_l","ald_lightrig_loc")
	#Place lights
	#key_light
	cmds.setAttr("ald_key_l.t",-7.848,6.428,6.972)
	cmds.setAttr("ald_key_l.r",-42.673,-39.612,16.015)
	cmds.setAttr("ald_key_l.s",2.349,2.349,2.349)
	#fill_light
	cmds.setAttr("ald_fill_l.t",13.785,9.472,11.033)
	cmds.setAttr("ald_fill_l.r",-27.129,51.779,1.383)
	cmds.setAttr("ald_fill_l.s",12.227,12.227,12.227)
	#rim_light
	cmds.setAttr("ald_rim_l.t",11.798,4.226,-18.848)
	cmds.setAttr("ald_rim_l.r",12.639,148.583,42.984)
	cmds.setAttr("ald_rim_l.s",1,1,1)
	#Set lights intensity
	cmds.setAttr("ald_key_lShape.intensity",90)
	cmds.setAttr("ald_fill_lShape.intensity",1)
	cmds.setAttr("ald_rim_lShape.intensity",200)
	cmds.setAttr("ald_dome_l.intensity",.2)
	
def delete_3pt_lightrig(*arg):
	try:
		cmds.delete("ald_3pt_lightrig_grp")
		cmds.delete("PxrSurface_ald_cyclo")
		cmds.delete("PxrSurface_ald_cycloSG")
		cmds.delete("ald_cyclo_grid")
		cmds.delete("ald_cyclo_grid_place2dTexture")
		cmds.delete("ald_lightrig_loc")
		cmds.delete("ald_key_l")
		cmds.delete("ald_fill_l")
		cmds.delete("ald_rim_l")
		cmds.delete("ald_dome_l")
		cmds.delete("ald_cyclo_p")
	except ValueError:
		pass
		
def ald_subdiv_scheme(*arg):
	sel = cmds.ls(selection=True)
	for object in sel :
		mel.eval('execRmanMenuItem("SubdivAttr")')
		mel.eval('rmanSetAttr("' + object + '","rman__torattr___subdivScheme","0");')
	cmds.select(sel,r=True)

def ald_detach_subdiv_scheme(*arg):
	sel = cmds.ls(selection=True)
	for object in sel :
		try :
			mel.eval('rmanSetAttr("' + object + '","rman__torattr___subdivScheme","100");')
		except RuntimeError :
			pass
	cmds.select(sel,r=True)

def hide_camera_rig(*arg):
	test_vis = cmds.getAttr("distanceFromCamera_loc.visibility")
	if test_vis == True:
		cmds.setAttr("distanceFromCamera_loc.visibility",0)
	elif test_vis == False:
		cmds.setAttr("distanceFromCamera_loc.visibility",1)
		
def hide_3pt_hdri(*arg):
	test_vis = cmds.getAttr("ald_lookdev_grp.visibility")
	if test_vis == True:
		cmds.setAttr("ald_lookdev_grp.visibility",0)
	elif test_vis == False:
		cmds.setAttr("ald_lookdev_grp.visibility",1)

def hide_cyclo(*arg):
	test_vis = cmds.getAttr("ald_cyclo_p.visibility")
	if test_vis == True:
		cmds.setAttr("ald_cyclo_p.visibility",0)
	elif test_vis == False:
		cmds.setAttr("ald_cyclo_p.visibility",1)

def hide_macbeth(*arg):
	test_vis = cmds.getAttr("ald_macbeth_p.visibility")
	if test_vis == True:
		cmds.setAttr("ald_macbeth_p.visibility",0)
	elif test_vis == False:
		cmds.setAttr("ald_macbeth_p.visibility",1)

def hide_hdri_array(*arg):
	test_vis = cmds.getAttr("ald_hdri_array_grp.visibility")
	if test_vis == True:
		cmds.setAttr("ald_hdri_array_grp.visibility",0)
	elif test_vis == False:
		cmds.setAttr("ald_hdri_array_grp.visibility",1)
		
def hide_3pt_lightrig(*arg):
	test_vis = cmds.getAttr("ald_3pt_lightrig_grp.visibility")
	if test_vis == True:
		cmds.setAttr("ald_3pt_lightrig_grp.visibility",0)
	elif test_vis == False:
		cmds.setAttr("ald_3pt_lightrig_grp.visibility",1)

def import_hdri_array(*arg):
	delete_hdri_array()
	list_hdri = cmds.getFileList(folder=hdri_array_folder)
	hdri_nodes = []
	for hdri in list_hdri:
		# concatenate file path
		hdri_fullstr = hdri_array_folder + "/" + hdri
		PxrDomeLight = cmds.shadingNode("PxrDomeLight",asLight=True)
		renamed_PxrDomeLight = cmds.rename(PxrDomeLight,"PxrDomeLight_"+hdri)
		#hide hdri
		cmds.setAttr(renamed_PxrDomeLight+".visibility",0)
		#set hdri file paths
		try:
			cmds.setAttr(renamed_PxrDomeLight+".lightColorMap",hdri_fullstr,type="string")
		except PluginError:
			pass
		global hdri_nodes
		hdri_nodes.append(renamed_PxrDomeLight)
	#group hdri domelights	
	cmds.group(hdri_nodes,name="ald_hdri_array_grp")
	
def delete_hdri_array(*arg):
	try :
		cmds.delete("ald_hdri_array_grp")
	except ValueError:
		pass

def prepare_hdri_array(*arg):
	#hide all hdri
	for hdri in hdri_nodes:
		cmds.setAttr(hdri+".visibility",0)
	cmds.currentTime(1)
	current_frame = 1
	for hdri in hdri_nodes:
		#make visible
		cmds.currentTime(current_frame-1)
		cmds.setAttr(hdri+".visibility",0)
		cmds.setAttr(hdri+".intensity",0)
		cmds.setKeyframe(hdri,attribute="visibility")
		cmds.setKeyframe(hdri,attribute="intensity",ott="stepnext")
		cmds.currentTime(current_frame)
		cmds.setAttr(hdri+".visibility",1)
		cmds.setAttr(hdri+".intensity",1)
		cmds.setKeyframe(hdri,attribute="visibility")
		cmds.setKeyframe(hdri,attribute="intensity",ott="stepnext")
		cmds.currentTime(current_frame+1)
		cmds.setAttr(hdri+".visibility",0)
		cmds.setAttr(hdri+".intensity",0)
		cmds.setKeyframe(hdri,attribute="visibility")
		cmds.setKeyframe(hdri,attribute="intensity",ott="stepnext")
		current_frame += 1
	cmds.currentTime(1)
	cmds.playbackOptions(min=1, max=current_frame-1)
	cmds.selectKey(clear=True)
	cmds.select(clear=True)
	#render settings
	cmds.setAttr("defaultRenderGlobals.endFrame",current_frame-1)
	cmds.setAttr("defaultRenderGlobals.outFormatControl",0)
	cmds.setAttr("defaultRenderGlobals.animation",1)
	cmds.setAttr("defaultRenderGlobals.putFrameBeforeExt",1)
	cmds.setAttr("defaultRenderGlobals.extensionPadding",2)
	cmds.confirmDialog(t="Done !",m="Ready for batch rendering")

def import_3pt_hdri(*arg):
	delete_3pt_hdri()
	list_hdri = cmds.getFileList(folder=lookdev_hdri_folder)
	for hdri in list_hdri:
		# concatenate file path
		hdri_fullstr = lookdev_hdri_folder + "/" + hdri
		PxrDomeLight = cmds.shadingNode("PxrDomeLight",asLight=True)
		renamed_PxrDomeLight = cmds.rename(PxrDomeLight,"ald_lookdev_PxrDomeLight")
		#set hdri file path
		try:
			cmds.setAttr(renamed_PxrDomeLight+".lightColorMap",hdri_fullstr,type="string")
		except PluginError:
			pass
		global hdri_nodes
		hdri_nodes.append(renamed_PxrDomeLight)
	# group hdri domelights	
	cmds.group(hdri_nodes,name="ald_lookdev_grp")
	
def delete_3pt_hdri(*arg):
	try:
		cmds.delete("ald_lookdev_grp")
	except ValueError:
		pass

def open_autolookdev_folder(*arg):
	os.startfile(autolookdev_folder)

def open_lookdev_hdri_folder(*arg):
	os.startfile(lookdev_hdri_folder)
		
def open_hdri_array_folder(*arg):
	os.startfile(hdri_array_folder)
	


# **************** INIT ****************
def init_ald_rfm(*arg):
	#Create AutoLookDev directories
	if not os.path.exists(autolookdev_folder):
		os.makedirs(autolookdev_folder)
	if not os.path.exists(lookdev_hdri_folder):
		os.makedirs(lookdev_hdri_folder)
	if not os.path.exists(hdri_array_folder):
		os.makedirs(hdri_array_folder)
	mel.eval('rmanLoadPlugin')
	mel.eval('rmanChangeToRenderMan')
	init_ald_interface()

init_ald_rfm()