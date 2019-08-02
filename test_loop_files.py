import ffmpeg
from pathlib import Path
import os


library_directory = r"C:\Users\Jordan\Documents\GitHub\ffmpeg\videos"
new_library_path = r"C:\Users\Jordan\Documents\GitHub\ffmpeg\done"
video_format_setting = ".mp4"
audio_setting = "aac"
bitrate_setting = "128k"

for each_file in os.listdir(library_directory):
    file = Path(os.path.join(library_directory, each_file))
    input_file = str(file)
    if file.suffix != video_format_setting:
        probe = ffmpeg.probe(input_file)
        new_file_name = f"done/{file.stem}{video_format_setting}"
        input_steam = ffmpeg.input(filename=input_file)
        out_put = ffmpeg.output(input_steam["0"], input_steam["1"], input_steam["1"], new_file_name,
                                **{"c:v": "libx264"}, **{"c:a:0": "copy"}, **{"c:a:1": audio_setting},
                                **{"b:a:1": bitrate_setting}, ac=2)
        out_put = ffmpeg.overwrite_output(out_put)
        out_put = out_put.global_args('-loglevel', 'info', "-strict", "-2")
        print(" ".join(ffmpeg.compile(out_put)))
        ffmpeg.run(out_put)
