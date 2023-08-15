import cv2
import numpy as np

# İki görüntüyü yükle (gri tonlamalı olarak)
img1 = cv2.imread('cla_foto.webp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('p_harfi.png', cv2.IMREAD_GRAYSCALE)

# SIFT detektörünü oluştur
sift = cv2.SIFT_create()

# İlk görüntüdeki anahtar noktaları ve açıklama vektörlerini bul
kp1, des1 = sift.detectAndCompute(img1, None)

# İkinci görüntüdeki anahtar noktaları ve açıklama vektörlerini bul
kp2, des2 = sift.detectAndCompute(img2, None)

# FLANN tabanlı eşleştiriciyi oluştur
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)



# Eşleştirmeleri Lowe'nin oran testine göre filtreleyin ve iyi eşleşmeleri seçin
good_matches = []
for m, n in matches:
    if m.distance < 0.4 * n.distance:
        good_matches.append(m)

# İyi eşleşmeleri görselleştirin
img3 = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imshow('Matches', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
