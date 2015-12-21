# pixel-ART

Pixel-ART your friends' faces.


# Usage :

Place picture.jpg in the "pics/" folder. 

Run : 

python faces.py picture.jpg

Make sure :

- picture.jpg exists in your "pics/" folder.
- You have reading and writing permissions in "pics/" folder.

You'll find the result in your "pics/tmp_picture.jpg" file.

 
If you want to add awesome eyes to your picture just run :

python faces.py picture.jpg eye.png


# Quick description of the algorithm:  

The technique used to pixel art faces is simple and yet quite effective.

We colored each grid of N x N pixels with the same color. (N can be changed in faces.py)


For face and eyes detection we used the great OpenCV library.

For each face we found on the given picture, we wisely applied eyes detection.
(Since we usually find eyes on the face :v )  

If this script puts an eye on your mouth don't blame me. Instead, blame OpenCV.
If this script doesn't put any eye on your face; it doesn't mean you don't have eyes.
It simply means that OpenCV didn't find them or they were judged to be 
too small by the script.

Have fun Pixel-Arting your friends' faces.

More stuff can be found on k3nz0.com
