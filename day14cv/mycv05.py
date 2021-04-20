import cv2
 
# 이미지 읽기
img = cv2.imread('bts.jpg', 1)


print(img)
print("shape:", img.shape)

for i in img:
    for j in i:
        j[0] = 0
        j[2] = 0
        
 
# 이미지 화면에 표시
cv2.imshow('Image', img)
cv2.waitKey()
# 이미지 윈도우 삭제
cv2.destroyAllWindows()
 
# 이미지 다른 파일로 저장
cv2.imwrite('BTS2.jpg', img)
