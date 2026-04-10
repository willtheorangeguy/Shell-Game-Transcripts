"""
This script uses yt-dlp to download audio, by year, from the
Shell Game podcast playlist.
"""

import yt_dlp

def download_playlist(playlist_url):
    """
    Downloads all audio from the podcast site.
    """
    ydl_opts = {
        "format": "bestaudio",
        "noplaylist": False,
        "ignoreerrors": True,
        "download_archive": "downloaded.log",
        "outtmpl": "%(upload_date>%Y)s/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "0",
            }
        ],
        'concurrent-fragments': True,
        'no-mtime': True,
#       'playlistend': 10
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


if __name__ == "__main__":
    playlist = "https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/d3d3abca-191a-4010-8160-b3530112d393/c639b22c-ee8c-43dd-86c1-b3530112d3a3/podcast.rss"
    download_playlist(playlist)
    print("Downloaded all audio from the Shell Game podcast website.")
