import os
import sys
import ffmpeg
from tqdm import tqdm


def match_track(file_name, tracks):
    file_name = file_name.lower()
    for track_title, artist in tracks:
        if track_title in file_name or artist in file_name:
            return True
    return False


def process_files(input_dir: str,
                  output_dir: str,
                  input_formats,
                  output_format,
                  tracks=None,
                  use_playlist=False,
                  recursive=False,
                  bitrate="320k", ):
    # Collect all files to process
    if recursive:
        file_list = []
        for root, _, files in os.walk(input_dir):
            for file in files:
                if any(file.lower().endswith(ext.lower()) for ext in input_formats):
                    file_list.append(os.path.join(root, file))
    else:
        file_list = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if
                     any(f.lower().endswith(ext.lower()) for ext in input_formats)]

    if use_playlist and tracks is None:
        print("Playlist is enabled but no tracks loaded.")
        sys.exit(1)

    file_iterator = tqdm(file_list, desc="Converting files")


    for input_file in file_iterator:
        file_name = os.path.splitext(os.path.basename(input_file))[0]
        if use_playlist:
            if not match_track(file_name, tracks):
                continue
        output_file = os.path.join(output_dir, file_name + f".{output_format}")
        convert_file(input_file, output_file, output_format=output_format, bitrate=bitrate)


def convert_file(input_file, output_file, output_format="wav", bitrate="320k"):
    try:
        if output_format == "mp3":
            stream = ffmpeg.input(input_file).output(output_file, audio_bitrate=bitrate)
        else:
            stream = ffmpeg.input(input_file).output(output_file)

        stream = stream.global_args('-loglevel', 'quiet')
        stream.run(overwrite_output=True)
    except ffmpeg.Error as e:
        print(f"Error converting {input_file}: {e.stderr.decode()}")