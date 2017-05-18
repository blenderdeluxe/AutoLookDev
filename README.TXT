#CURRENT VERSION : v1.1

****** INSTALL ******

1. Copy and paste "AutoLookDev_rfm.py" in your scripts folder (usually "C:\Users\%USERPROFILE%\Documents\maya\2017\prefs\scripts")
2. Open Maya
3. Open the script editor
4. In an empty Python tab paste the following code :

from AutoLookDev_rfm import init_ald_rfm
init_ald_rfm()

6. File > Save Script to Shelf
7. To modify the icon use the shelf editor

****** Setting up HDRI folders ******

1. In AutoLookDev's help menu, click "Open AutoLookDev folder"
2. There should be two folders :
	"hdri_array" : should contain any hdri you want to batch render with
	"lookdev_hdri" : should contain a neutral hdri, such as a three point lighting.

****** Adapting ALD to your needs
	
1. If you wish to modify the default black and white values, please feel free to edit AutoLookDev.py :
black_level = 0.015   > Change this value
white_level = 0.7   > Change this value
grey_level = 0.18	> Why would you ?

2. You can also change the Macbeth color checker values, although I do not recommend it. These values were picked from
http://www.babelcolor.com/colorchecker-2.htm#CCP2_images From X-Rite L*a*b* D50 (formulations AFTER Nov. 2014) sRGB TIF 16bits.
If you think the default values are wrong please create a new Issue on Github.

******

#AutoLookDev (ALD) was created by Valentin DAVID and is an open source script, making it freely usable, modifiable and distributable.
#AutoLookDev is intended to boost your workflow with Maya 2017 and RenderMan 21
#Contact : vdavid.pro@gmail.com
#If you're interested in seeing my work, please visit https://www.artstation.com/artist/vdavid
#Features request / bug reports : https://github.com/vdavidcg/AutoLookDev/issues
#See also :  https://github.com/vdavidcg
