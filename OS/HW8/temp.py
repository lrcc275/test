import cv2
import matplotlib.pyplot as plt

# 1. 读取彩色图像
image = cv2.imread('pic.jpg')

# 2. 将彩色图像从BGR颜色空间转换为HSV颜色空间
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 3. 对亮度（V通道）进行直方图均衡化
hsv_image[:, :, 2] = cv2.equalizeHist(hsv_image[:, :, 2])

# 4. 将处理后的图像从HSV颜色空间转换回BGR颜色空间
equalized_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# 5. 绘制直方图均衡化前后的彩色图像
plt.figure(figsize=(12, 6))

# 原始彩色图像
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

# 均衡化后的彩色图像
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB))
plt.title('Equalized Image')


#plt.tight_layout()
plt.savefig("result.jpg")
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()