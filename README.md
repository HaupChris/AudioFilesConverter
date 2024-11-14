# AudioFilesConverter

A command-line tool to convert audio files from one format to another using ffmpeg. This comes handy for hobby DJs, needing to convert their music for different equipment. All processing happens on your local machine, no content is uploaded.

## Quality Disclaimer
Converting from a lossy format (e.g., MP3) to a lossless format (e.g., FLAC or WAV) will not improve audio quality. The quality is limited by the source file, and lost data cannot be recovered through conversion.

## Features

- **Batch Conversion**: Convert multiple audio files from one format to another.
- **Playlist Filtering**: Optionally convert only the files specified in a playlist.
- **Recursive Processing**: Convert files in subdirectories recursively.
- **Customizable Formats**: Specify input and output formats.


## Requirements

- **Python 3.10**
- **ffmpeg**: Must be installed and accessible in your system's PATH.
- Python packages listed in `requirements.txt`.

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/HaupChris/AudioFilesConverter
cd AudioFilesConverter
```
2. **Install the required Python packages:**
```
pip install -r requirements.txt
```

## Usage
```bash
python main.py --input-dir INPUT_DIR --output-dir OUTPUT_DIR --output-format OUTPUT_FORMAT [options]
```

### Required Arguments
- --input-dir: Directory containing audio files to convert.
- --output-dir: Directory where converted files will be saved.
- --output-format: Desired output format (e.g., mp3, wav).

### Optional Arguments
- --input-formats: List of input formats to convert from (default: flac). Example: --input-formats flac wav aiff.
- --playlist: Path to a playlist file (tab-separated values).
- --use-playlist: Enable filtering using the playlist.
- --recursive: Recursively search for audio files in subdirectories.
- --bitrate: Bitrate for output files (default: 320k for mp3).


## Examples
## Convert all FLAC files in a directory to MP3
```
python main.py --input-dir /path/to/input 
                   --output-dir /path/to/output 
                   --output-format mp3 
                   --input-formats flac 
```

### Convert FLAC and WAV files recursively to WAV
```
python main.py --input-dir /path/to/input 
                   --output-dir /path/to/output 
                   --output-format wav 
                   --input-formats flac wav 
                   --recursive 
```

### Convert files matching a playlist
```
python main.py --input-dir /path/to/input 
                   --output-dir /path/to/output 
                   --output-format mp3 
                   --playlist /path/to/playlist.txt 
                   --use-playlist 
                   --recursive 
```


## Playlist File Format
The playlist file should be a tab-separated values file with at least four columns. The script uses the third column as the track title and the fourth column as the artist. Such playlist files can usually be exported from Rekordbox.

Example (playlist.txt)
```
Index   TrackID   Title           Artist
1       123       Song Title One  Artist One
2       456       Song Title Two  Artist Two

```