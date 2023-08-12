import cv2
source="road.jpg"
destination='new-image.jpg'
image = cv2.imread(source,cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",image)
cv2.waitKey(0)

scale_percentage=50
width=int(image.shape[1]*scale_percentage/100)
height=int(image.shape[0]*scale_percentage/100)

tuple=(width,height)
output = cv2.resize(image,tuple)

cv2.imwrite(destination,output)
cv2.waitKey(0)