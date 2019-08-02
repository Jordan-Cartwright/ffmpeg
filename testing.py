import ffmpeg
from pathlib import Path
import json

folder_path = Path(r"C:\Users\Jordan\Documents\GitHub\ffmpeg\videos\big_buck_bunny_720p_1mb.mp4")
input_file = str(folder_path)

probe = ffmpeg.probe(input_file)
# print(json.dumps(probe, indent=2))

# for stream in probe['streams']:
#     print(stream)

# convert the input file to a stream object
input_stream = ffmpeg.input(filename=input_file)

# Produces the output stream object, but doesn't run it yet.
out_put = ffmpeg.output(input_stream["0"], input_stream["1"], input_stream["1"], "done/out_put_test.mkv",
                        **{"c:v": "libx264"}, **{"c:a:0": "copy"}, **{"c:a:1": "aac"},
                        **{"b:a:1": "128k"}, ac=2)

# Adds -y to the ffmpeg command
out_put = ffmpeg.overwrite_output(out_put)

# Set some global args, note args go to the whole command line on a stream.
# We could use the progress parameter here and get them web sockets going
out_put = out_put.global_args('-loglevel', 'info', "-strict", "-2")

print(json.dumps(ffmpeg.compile(out_put), indent=2))
print(" ".join(ffmpeg.compile(out_put)))
# ffmpeg.run(out_put)
