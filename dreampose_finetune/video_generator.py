import cv2
import os
import re
# frame paths
image_folder = './demo/results'

# video output path
video_name = './demo/results/video.mp4'

# frame per second
fps = 24

# get frame list
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

# sorted
images.sort(key=lambda x: int(re.findall(r'\d+', x)[0]))

# get the width and depth of the image
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# video objective
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

# generation
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

# play
cv2.destroyAllWindows()
video.release()
