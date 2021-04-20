import cv2

# 이미지 90도 회전
 
# 이미지 읽기
img = cv2.imread('bts.jpg', 1)


print(img)
print("shape:", img.shape)

img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        
 
# 이미지 화면에 표시
cv2.imshow('Image', img90)
cv2.waitKey()
# 이미지 윈도우 삭제
cv2.destroyAllWindows()



