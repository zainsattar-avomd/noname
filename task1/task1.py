import os, sys

from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
from PIL import Image


gif_path = "output.gif"
watermark_path = "edge_video_logo.png" 

def add_watermark():
    try:
        gif = Image.open(gif_path)
        watermark = Image.open(watermark_path).convert("RGBA")
    except Exception as e:
        print("Error opening files: {e}")
        return
    
    if watermark.width > gif.width or watermark.height > gif.height:
        print("Error: Watermark is larger than the GIF frames.")
        return
    
    frames = []
    for frame in range(gif.n_frames):
        # takes each frame from the gif and pastes the watermark at the bottom right
        try:
            gif.seek(frame)
            frame_image = gif.convert("RGBA")
            frame_image.paste(
                watermark, 
                (frame_image.width - watermark.width, frame_image.height - watermark.height),
                watermark
            )
            frames.append(frame_image)
        except Exception as e:
            print(f"Error processing frame {frame}: {e}")
            continue
    
    try:
        frames[0].save(gif_path, save_all=True, append_images=frames[1:], loop=0)
        print(f"Watermark added successfully to {gif_path}")
    except Exception as e:
        print(f"Error saving GIF: {e}")

def add_watermark_with_moviepy(video):
    try:
        #gif_clip = VideoFileClip("output.gif")
        logo = (ImageClip(watermark_path, duration=video.duration)
            .margin(right=8, top=8, opacity=0)
            .set_position("right","bottom"))
        
        final_clip = CompositeVideoClip([video, logo])
        final_clip.write_gif(gif_path, program='imageio', opt='nq',fps=15, logger='bar')
        print(f"GIF created successfully: {gif_path}")
    
    except Exception as e:
        print(f"Error creating GIF: {e}")


def create_gif(input_filename, start_timestamp, end_timestamp):
    
    if not os.path.isfile(input_filename):
        print(f"Error: File '{input_filename}' not found.")
        return None

    if start_timestamp < 0 or end_timestamp <= start_timestamp:
        print("Error: Invalid timestamps.")
        return None

    try:
        video = VideoFileClip(input_filename, audio=False).subclip(start_timestamp, end_timestamp)
        #video.resize(height=360) #reduce resolution for efficency and smaller gif size
        video.write_gif(gif_path, program='imageio', opt='nq',fps=15, logger='bar')
    except Exception as e:
        print(f"Error processing video: {e}")
        return None

    return video

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_filename> <start_timestamp in sec> <end_timestamp in sec>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    if not input_filename.lower().endswith('.mp4'):
        print("Error: Input file must be an MP4 file.")
        sys.exit(1)
    
    try:
        start_timestamp = float(sys.argv[2])
    except Exception as e:
        print(f"Start timestamp invalid: {e}")
    try:
        end_timestamp = float(sys.argv[3])
    except Exception as e:
        print(f"End timestamp invalid: {e}")
    
    video = create_gif(input_filename=input_filename, 
                       start_timestamp=start_timestamp, 
                       end_timestamp=end_timestamp)
    
    if video:
        add_watermark()
        #add_watermark_with_moviepy(video=video)
    else:
        print(f"GIF not created")


if __name__ == "__main__":
    main()