import numpy as np
import cv2
from PIL import Image
from random import *
import sys

# ! ADJUST GRID PIXELS
N = 20

if(len(sys.argv) != 2 and len(sys.argv) != 3):
	print("\nScript must be run in this way :\n\npython " + sys.argv[0] + " picture.jpg")
	print("\n\nIf you want to add awesome eyes to your picture just run :")
	print("\npython faces.py picture.jpg eye.png\n\n")
	print("Try again !")
	exit(0)


def twoMaxs(lnp):
	"""
		Return 0-based index of the two max values
	"""
	index1 = 0
	index2 = 0
	cnt = 0
	maxArea = 0
	maxArea2 = 0
	for (ex, ey, ew, eh) in lnp:
		if(ew * eh >= maxArea):
			index1 = cnt
			maxArea = ew * eh
		cnt += 1
	

	cnt = 0
	for (ex, ey, ew, eh) in lnp:
		if(index1 == cnt):
			cnt += 1
			continue
		if(ew * eh >= maxArea2):
			index2 = cnt
			maxArea2 = ew * eh
		cnt +=1
	
	return (index1, index2)

def abs(x):
	if(x >= 0):
		return x
	else:
		return -x


fName = sys.argv[1]
dirFile = "pics/"
ff = dirFile + fName
eyeFile = "eyes/eye.png"


if(len(sys.argv) == 3):
	eyeFile = "eyes/" + sys.argv[2]

face_cascade = cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')
eye_cascade = cv2.CascadeClassifier('xml/haarcascade_eye.xml')


img = cv2.imread(ff)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

print("Faces detected : "  + str(len(faces)))
#print(faces)

finalEyes = []

for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
	roi_gray = gray[y: y + h, x: x + w]
	roi_color = img[y: y + h, x: x + w]
	eyes = eye_cascade.detectMultiScale(roi_gray)
	print(eyes)
	maxS = twoMaxs(eyes)
	cnt = 0
	
	for (ex, ey, ew, eh) in eyes:
		if(len(eyes) < 2):
			continue
		if( (cnt == maxS[0]) or (cnt == maxS[1]) ):	
			#if(ew > 21): # magic
			finalEyes.append((ex + x, ey + y, ew, eh))
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		cnt += 1


finalEyes.sort(key=lambda tup: tup[0])

print("Eyes detected : "  + str(len(finalEyes)))
#print(finalEyes)


source = Image.open(ff)

width = source.size[0]
height = source.size[1]


visited = [[0 for x in range(width)] for y in range(height)]
grid = [[ [0, 0, 0] for x in range(width)] for y in range(height)]

data = list(source.getdata())

x = -1
y = 0
for k in range(len(data)):
	if(k % width == 0):
		x += 1
		y = 0

	grid[x][y][0] = data[k][0]
	grid[x][y][1] = data[k][1]
	grid[x][y][2] = data[k][2]	
	y += 1

# Generating eyeGrid



eyeSource = Image.open(eyeFile)
eyeW = eyeSource.size[0]
eyeH = eyeSource.size[1]

#print("EYE : ", eyeW, eyeH)

eyeGrid = [[ [0, 0, 0] for x in range(eyeW)] for y in range(eyeH)]
eyeData = list(eyeSource.getdata())
x = -1
y = 0

for k in range(len(eyeData)):
	if(k % eyeW == 0):
		x += 1
		y = 0
	eyeGrid[x][y][0] = eyeData[k][0]
	eyeGrid[x][y][1] = eyeData[k][1]
	eyeGrid[x][y][2] = eyeData[k][2]
	y += 1

# ---- 




img = Image.new( 'RGB', (width, height), "white") 
pixels = img.load()

currEye = 0
for i in range(img.size[0]):
	for j in range(img.size[1]):
		if(len(sys.argv) == 3):
			if(currEye < len(finalEyes)):
				# centering the eyes:
				startPixW = finalEyes[currEye][0] + abs(eyeW - finalEyes[currEye][2]) / 2
				startPixH = finalEyes[currEye][1] + abs(eyeH - finalEyes[currEye][3]) / 2
				if((j == startPixH) and (i == startPixW)):
					print(finalEyes[currEye][0], finalEyes[currEye][1])
					print(startPixW, startPixH)
					currEye += 1
					for k in range(eyeW):
						xx = i + k
						for l in range(eyeH):
							yy = j + l
							r = eyeGrid[l][k][0]
							g = eyeGrid[l][k][1]
							b = eyeGrid[l][k][2]
							if((yy < height) and (xx < width)):
								pixels[xx, yy] = (r, g, b)
								visited[yy][xx] = 1

		if(visited[j][i]):
			continue
		r = grid[j][i][0]
		g = grid[j][i][1]
		b = grid[j][i][2]

		for k in range(N):

			xx = i + k
			for l in range(N):
				yy = j + l
				if((yy < height) and (xx < width)):
					pixels[xx, yy] = (r, g, b)
					visited[yy][xx] = 1				
		#pixels[i, j] = (grid[j][i][0], grid[j][i][1], grid[j][i][2]) 

toSave = "tmp_" + fName

img.save(dirFile + toSave)
print("Picture saved : " + dirFile + toSave)
img.show()
#print(finalEyes)
print("END.")
