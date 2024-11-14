import csv

def load_playlist(playlist_path):
    tracks = set()
    with open(playlist_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="\t")
        next(reader, None)  # Skip the header line if it exists
        for row in reader:
            if len(row) > 2:
                track_title = row[2].strip().lower()
                artist = row[3].strip().lower()
                tracks.add((track_title, artist))
    return tracks