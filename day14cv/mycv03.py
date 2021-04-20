import cv2
 
# 이미지 읽기
img = cv2.imread('bts.jpg', cv2.IMREAD_GRAYSCALE)

img2 = cv2.resize(img, (28,28))


    
print(img)
print("shape:", img.shape)
 
# 이미지 화면에 표시
cv2.imshow('Image', img)
cv2.waitKey()
# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 
