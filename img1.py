import cv2

imagem = cv2.imread('img/homer.png')
imagem[0, 0]=(0,255,0)
cv2.imshow('Homer', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
