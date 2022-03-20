import cv2
import glob

NEW_IMAGE_SIZE = 320
for img_path in glob.glob("../img/*.png"):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (NEW_IMAGE_SIZE, NEW_IMAGE_SIZE),
                     interpolation=cv2.INTER_LINEAR)

    num = int(img_path.split("/")[-1].split(".")[0])
    cv2.imwrite(f"./new_images/im{num}.jpg", img)
