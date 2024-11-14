import argparse
import os
import sys

from src.converter import process_files
from src.playlist import load_playlist


def main():
    parser = argparse.ArgumentParser(description="Audio File Converter using ffmpeg")
    parser.add_argument('--input-dir', required=True, help="Input directory containing audio files")
    parser.add_argument('--output-dir', required=True, help="Output directory for converted files")
    parser.add_argument('--input-formats', nargs='+', default=['flac'],
                        help="List of input formats to convert from (e.g., flac wav)")
    parser.add_argument('--output-format', required=True, help="Output audio format (e.g., mp3, wav)")
    parser.add_argument('--playlist', help="Path to playlist file (tab-separated values)")
    parser.add_argument('--use-playlist', action='store_true', help="Enable filtering using playlist")
    parser.add_argument('--recursive', action='store_true', help="Recursively search in subdirectories")
    parser.add_argument('--bitrate', default='320k', help="Bitrate for output files (e.g., 320k for mp3)")

    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    tracks = None
    if args.use_playlist:
        if args.playlist is None:
            print("Playlist file must be specified when using --use-playlist")
            sys.exit(1)
        else:
            tracks = load_playlist(args.playlist)

    process_files(
        input_dir=args.input_dir,
        output_dir=args.output_dir,
        input_formats=args.input_formats,
        output_format=args.output_format,
        tracks=tracks,
        use_playlist=args.use_playlist,
        recursive=args.recursive,
        bitrate=args.bitrate
    )


if __name__ == "__main__":
    main()