from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, concatenate_videoclips
from PIL import Image


# Function to resize the image using Pillow
def resize_image(image_path, width, height):
    img = Image.open(image_path)
    resized_img = img.resize((width, height), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resampling
    resized_img.save(image_path)  # Overwrite the original image


# Load the main video (your study with me video)
background_video = VideoFileClip("study_with_me_video.mp4")

# Define the countdown duration (in minutes)
countdown_minutes = 5  # Adjust as needed

# Total number of images (minutes * 60 seconds)
image_files = [f"60_minute_timer_images/slide_{i}.jpg" for i in range(1, countdown_minutes * 60 + 1)]  # Adjust the path to your images

# Specify the size of the countdown timer image after resizing
pip_image_width = 100  # Width of the countdown image (adjust as needed)
pip_image_height = 100  # Height of the countdown image (adjust as needed)

# Calculate the position for "right", "bottom" with 20px padding
position = (1920 - pip_image_width - 20, 1080 - pip_image_height - 20)  # Bottom-right corner with padding

# Set the time (in seconds) when the PiP should start (0:16 means 16 seconds)
start_time_seconds = 17

# Create a list to hold all the PiP clips
pip_clips = []

# Loop through all countdown images, resize them using Pillow, create PiP for each, and set the start time
for i, image_file in enumerate(image_files):
    # Resize the countdown image using Pillow (optional, adjust as needed)
    resize_image(image_file, pip_image_width, pip_image_height)

    # Load the resized image into MoviePy
    pip_image = ImageClip(image_file).set_duration(1)  # Each image lasts 1 second

    # Position the countdown timer in the bottom-right corner with padding
    pip_image = pip_image.set_position(position)

    # Set the start time for each PiP image (1 second per image)
    pip_image = pip_image.set_start(start_time_seconds + i)

    # Create a CompositeVideoClip to overlay the PiP image onto the background video
    pip_clip = CompositeVideoClip([background_video.subclip(start_time_seconds + i, start_time_seconds + i + 1), pip_image])

    pip_clips.append(pip_clip)

# Concatenate all PiP clips into one final video
final_video = concatenate_videoclips(pip_clips)

# Output the final video with the countdown
final_video.write_videofile("study_with_me_with_countdown.mp4", codec="libx264")
