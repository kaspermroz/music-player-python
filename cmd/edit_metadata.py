from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

audio = EasyID3("")
audio['title'] = ""
audio['artist'] = ""
audio['date'] = "2020"
audio.save()

audio = MP3("")
print(audio.tags)
