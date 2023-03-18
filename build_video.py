import pygame.camera
import os 
from PIL import Image
from moviepy.editor import VideoFileClip, concatenate_videoclips
import pygame.camera
import time

pygame.camera.init()
print(pygame.camera.list_cameras())
cam = pygame.camera.Camera("FaceTime HD Camera (Built-in)",(2880,1620))
cam.start()
img = cam.get_image()
time.sleep(2)
pygame.image.save(img,"awful_image.jpg")
time.sleep(2)
image = Image.open('awful_image.jpg')
new_image = image.resize((1920, 1080))
new_image.save('image.jpg')
time.sleep(2)
os.system("ffmpeg -r 1 -i image.jpg -vcodec mpeg4 -y movie.mp4")
clip1 = VideoFileClip("pai.mp4")
clip2 = VideoFileClip("movie.mp4")
final_clip = concatenate_videoclips([clip1, clip2])
final_clip.write_videofile("video.mp4")
