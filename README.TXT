****** INSTALL ******

1. Copy and paste "AutoLookDev.py" in your scripts folder (usually "C:\Users\user\Documents\maya\2017\prefs\scripts")
2. Open Maya
3. Open the script editor
4. In an empty Python tab paste the following code :

from AutoLookDev import init_ald
init_ald()

6. File > Save Script to Shelf
7. To modify the icon use the shelf editor
8. If you wish to modify the default black and white values, please feel free to edit AutoLookDev.py :

black_level = 0.015   > Change this value
white_level = 0.7   > Change this value

9. You can also change the Macbeth Color Checker values, although I do NOT recommend it. These values were picked from
http://www.babelcolor.com/colorchecker-2.htm#CCP2_images From X-Rite L*a*b* D50 (formulations AFTER Nov. 2014) sRGB TIF 16bits
If you think the default values are wrong please send me an email !


******

#AutoLookDev (ALD) was created by Valentin DAVID and is an open source script, making it freely usable, modifiable and distributable.
#AutoLookDev is intended to boost your workflow with Maya 2017 and RenderMan 21
#If you have any suggestions, features request or bug enquiries please shoot me an email !
#Contact : vdavid.pro@gmail.com
#If you're interested in seeing my work, please visit https://www.artstation.com/artist/valentindavid
