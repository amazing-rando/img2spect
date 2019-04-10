from PIL import Image
from scipy import ndimage
from scipy.io import wavfile
import numpy as np
import os, sys

#Get user input.
filename = sys.argv[1]

#Import image file as grayscale numpy array.
img = Image.open(filename).convert("L")
img = np.array(img)
img = ndimage.rotate(img, -90)
w, h = img.shape

#Transform image data to frequency domain.
wav = np.fft.irfft(img, h * 2, axis = 1).reshape((w * h * 2))

#Save as WAV file.
wavfile.write(os.path.splitext(filename)[0] + ".wav", 44100, wav)
