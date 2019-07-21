import cv2
import os
import glob
def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 10 
       
        else:
            return

save_all_frames('images/report.mov', 'data5/temp/result_png', 'sample_video_img', 'png')
i=0
a=[0]*66
files = glob.glob("data5/temp/result_png/*.png")
for f in files:
    img = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
    print(img.mean())
    a[i]=img.mean()
    i+=1
plt.plot(a)
plt.show()
