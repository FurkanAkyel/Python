from pytube import YouTube

SAVE_PATH = "C:\\YoutubeDown"

link = input("İndirmek istediğiniz videonun linki : ")

try:
    yt = YouTube(link)
except Exception as e:
    print(f"Bağlantı hatası: {e}")
    exit()

# En yüksek kalitedeki mp4 videoyu al
mp4_streams = yt.streams.filter(file_extension='mp4', progressive=True)

if not mp4_streams:
    print("MP4 formatında uygun video bulunamadı.")
    exit()

d_video = mp4_streams.order_by('resolution').last()

try:
    d_video.download(output_path=SAVE_PATH)
    print("Video başarıyla indirildi!")
except Exception as e:
    print(f"Hata oluştu: {e}")
