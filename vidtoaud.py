import moviepy.editor as mp
from tkinter.filedialog import askopenfilename

def vid_to_aud(filename):
    video = mp.VideoFileClip(filename)
    audio = video.audio
    audio.write_audiofile("demo.mp3")
    print("Success")

if __name__ == '__main__':
    filename = askopenfilename()
    vid_to_aud(filename)