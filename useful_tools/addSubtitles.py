'''
This script is to add subtitles into a mp4 video file.

Before using this script, you need to make sure the following things:
1: make sure which video you use
2: make sure that you have completed subtitles.srt file

'''


from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
import numpy as np
from PIL import Image
from tkinter import filedialog as fd


def open_file_selection() -> chr:
    filetypes = (
        ('video file', '*.mp4')
                )
    # mac or windows
    files = fd.askopenfilenames(
        filetypes=filetypes,
        initialdir='/Users/phionabasemera/Documents/pdfscrapper'
    )
    print(files)
    return files


# Function to determine the dominant background color
def get_dominant_color(frame):
    # Resize the frame to speed up processing
    small_frame = Image.fromarray(frame).resize((50, 50))
    # Convert frame to numpy array
    arr = np.array(small_frame)
    # Reshape array to be a list of RGB colors
    reshaped_arr = arr.reshape((arr.shape[0] * arr.shape[1], 3))
    # Get the average color of the frame
    avg_color = reshaped_arr.mean(axis=0)
    return avg_color


# Function to decide font color based on background color
def choose_font_color(background_color):
    # Simple thresholding to decide font color
    brightness = np.mean(background_color)
    if brightness > 128:
        return 'black'  # If the background is bright, use a dark font color
    else:
        return 'white'  # If the background is dark, use a light font color


# Define a generator function that returns a styled TextClip for each subtitle
def make_styled_text_clip(txt, frame):
    background_color = get_dominant_color(frame)
    font_color = choose_font_color(background_color)

    return TextClip(
        txt,
        fontsize=24,  # Font size
        color=font_color,  # Font color based on background
        font='Arial',  # Font type
        stroke_color='black',  # Stroke color for better contrast
        stroke_width=2  # Stroke width
    )


# Load the video file
video_file = open_file_selection()
video = VideoFileClip(video_file)

# Load the subtitles from the SRT file
subtitles = SubtitlesClip("subtitles.srt", lambda txt: make_styled_text_clip(txt, video.get_frame(0)))

# Create a list to hold composite clips with subtitles
clips = []

# Go through the video frame-by-frame and add styled subtitles
for start, end, txt in subtitles.subtitles:
    # Extract a frame near the subtitle time for background analysis
    frame = video.get_frame(start)

    # Create a styled TextClip based on the frame
    text_clip = make_styled_text_clip(txt, frame).set_duration(end - start).set_start(start).set_pos(
        ('center', 'bottom'))

    # Add the styled subtitle to the list of clips
    clips.append(text_clip)

# Create the final video with all subtitle clips
final_video = CompositeVideoClip([video] + clips)

# Write the output video file
final_video.write_videofile("output_" + video.filename + ".mp4", codec="libx264", fps=video.fps)
