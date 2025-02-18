from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route("/")
def home():
    return "YouTube Downloader is Running!"

@app.route("/download", methods=["POST"])
def download_video():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    ydl_opts = {"outtmpl": "/app/downloads/%(title)s.%(ext)s"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    return jsonify({"status": "Downloaded", "title": info["title"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
