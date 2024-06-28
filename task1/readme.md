## Video Processing Script

Write a script that accepts 3 command line arguments: an input filename of an MP4 video, a start timestamp, and an end timestamp in seconds. The script should generate a GIF from the video segment between these timestamps, applying a watermark of the Edge Video logo at the bottom right corner of the GIF. The process should be optimized for speed and minimal memory usage. Consider edge cases such as invalid timestamps or files.

Include error handling for various edge cases and document your approach to optimizing the GIF creation process.

## Setup:
create a virtual env using virtualenv im using python3.10
start it with source env/bin/activate
run pip install requirements.txt in the main directory to install dependencies

## Sample command:
task1.py sample.mp4 1 5

## Approach

1. **Initial Setup**: Started by adding the task directly to ChatGPT, which provided a reference to `moviepy` and generated a basic script to start with.
2. **Exploration**: Explored `moviepy` documentation to find useful functions and options for implementing the feature and improving efficiency. Also explored other libraries and decided that `moviepy` would be the best option.
3. **GIF Conversion**: Wrote a function to convert the video file into a GIF file.
4. **Watermark Addition**: Wrote another function to add a watermark to the GIF file.
5. **Error Handling**: Added error handling for essential functions and other possible errors, including checking if the inputs are correct, the file is available, the file is an MP4, timestamps are logically correct, and not larger than the file itself.

## Optimizations

1. **Watermark Efficiency**: Initially wrote `add_watermark_with_moviepy`, but found it inefficient. Created another function named `add_watermark` using the PIL library to add the watermark to each frame and then convert it back to the original GIF. This approach was much faster and produced better results.
2. **Memory and File Size**: Removed audio while loading the file in memory since GIFs do not have audio.
3. **Frame Rate Reduction**: Reduced the frame rate to 15, as GIFs generally have lower frame rates (between 10-24 fps). This helped reduce the number of frames to process while adding the watermark.
4. **Quality Reduction**: Reduced the quality of the GIFs to 360p, as GIFs are not high quality. This helped reduce the GIF file size by more than 50%. The `moviepy` resize function is broken in the latest package version. You can remove it if the script does not work.
5. **Codec Options**: Decided to use `imageio` as the codec, but two other options are available which can speed up the process even further.

## Development Notes

I use Cursor IDE, which has integrated ChatGPT. The history was lost while working on the task, but my questions to ChatGPT were mostly related to `moviepy` and figuring out other approaches for conversions, which I also googled for research.

## Error Handling

- **File Validation**: Checks if the input file exists and is an MP4 file.
- **Timestamp Validation**: Ensures the start and end timestamps are valid and logically correct.
- **Frame Processing**: Handles errors during frame processing and skips problematic frames.

## Conclusion

This script efficiently processes video files to create watermarked GIFs, with optimizations for speed and memory usage. It includes robust error handling to manage various edge cases.
