import yt_dlp

SAVE_PATH = "C:\\YoutubeDown"
link = input("İndirmek istediğiniz videonun linki: ")

ydl_opts = {
    'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
    'format': 'bestvideo+bestaudio/best',
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print("Video başarıyla indirildi!")
except Exception as e:
    print(f"Hata oluştu: {e}")
