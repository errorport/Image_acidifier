import numpy as np
import cv2
import collections as col
import sys

image_path = sys.argv[1]

frame = cv2.imread(image_path, 1)
for y in range(frame.shape[0]):
	for x in range(frame.shape[1]):
		I = sum(frame[y,x])
		p = frame[y,x]
		if I < 100:
			frame[y,x-I//5:x+I//5,0]+=p[0]//10
		frame[y-I//5:y,x,2]=p[2]
		frame[y-I:y,x,0]+=p[0]//30
		if I > 0x88:
			frame[y,x:x+I,0]-=p[0]//15
			frame[y,x:x+I,2]-=p[2]//15
			frame[y,x:x+I,1]+=p[1]//50
		p = [g*g//255 for g in p]

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow('frame', frame)

image_name, image_type = image_path.split('.')
image_name = image_name+"_acidified"
image_path = image_name+"."+image_type
print("Saving: ", image_path)
cv2.imwrite(image_path, frame)

while(True):
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
