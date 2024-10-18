from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import time


def create_timer_presentation(min_timer: int) -> None:
    """
    Create a PowerPoint file including each slide with every one-second countdown.

    min_timer: int
        Number of minutes for the countdown timer.

    Return: None
    """

    # Create a PowerPoint presentation object
    presentation = Presentation()

    # Set slide width and height to 1920x1080 (in inches: 1920 px = 20 inches, 1080 px = 11.25 inches)
    presentation.slide_width = Inches(20)  # 1920px width
    presentation.slide_height = Inches(11.25)  # 1080px height

    # Start timer to track execution time
    start_time = time.time()

    # Total duration in seconds ( minutes = 600 seconds)
    total_seconds = min_timer * 60

    # Loop to create 600 slides, one for each second
    for i in range(total_seconds, -1, -1):
        # Create a new blank slide
        slide = presentation.slides.add_slide(presentation.slide_layouts[5])  # Layout 5 is a blank slide

        # Calculate the minutes and seconds
        minutes = i // 60
        seconds = i % 60
        time_str = f"{minutes:02}:{seconds:02}"

        # Add the timer text box
        text_box = slide.shapes.add_textbox(Inches(16), Inches(9.75), Inches(3), Inches(1))
        text_frame = text_box.text_frame
        text_frame.text = time_str

        # Customize the text style (font size, alignment, color)
        paragraph = text_frame.paragraphs[0]
        paragraph.font.size = Pt(44)
        paragraph.font.bold = True
        paragraph.alignment = PP_ALIGN.RIGHT
        paragraph.font.color.rgb = RGBColor(0, 0, 0)  # Black color for the font
        paragraph.font.name = 'EB Garamond'  # Set font to EB Garamond

    # Save the presentation
    presentation.save(f"{min_timer}_minute_timer_presentation.pptx")

    # End timer to track execution time
    end_time = time.time()
    print(f'Presentation created in {end_time - start_time:.2f} seconds.')
    print('Presentation saved as "10_minute_timer_presentation.pptx".')


if __name__ == '__main__':
    min_timer = int(input("Enter the number of minutes for the countdown timer: "))
    create_timer_presentation(min_timer)
