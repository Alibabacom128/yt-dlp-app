import yt_dlp

def download_video(url, output_format='mp4'):
    options = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }
    
    if output_format == 'mp3':
        options.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        })

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Enter YouTube URL: ")
    format_choice = input("Enter format (mp4/mp3): ").strip().lower()
    download_video(video_url, format_choice)
