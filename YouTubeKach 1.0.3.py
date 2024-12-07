from pytubefix import YouTube
from moviepy.editor import *
from pytubefix.cli import on_progress
import os 


def afterMain():
    while True:
        waiting = input(f"\nОтлично! Нажмите Enter, чтобы закрыть программу. Нажмите 1 если хотите еще что-то скачать.  \n")
        if len(waiting) < 1:
            quit()
        else:
            main()
def main():
    def folder_for_download():
     # check for destination to save file 
        print(r"Чтобы ввести путь, куда качать (такого плана: D:\download) нажмите 1") 
        print('Нажмите 2, чтобы скачать в папку, которая указана в настройках программы (текстовом файле file.txt)')
        choice = input('Нажимайте 1/2, потом Enter>>')
        if choice == '1':
            destination = str(input("Вбивайте путь сюда или жмите Enter, чтобы скачать в папку программы>> ")) or '.'
        else:
            with open('file.txt', 'r') as file:
                destination = file.read()
        return destination


    url = input('Введите URL видео, которое хотите скачать:  ')
    print('Чтобы скачать видео 📷 быстро и в хорошем качестве нажмите 1')
    print('Чтобы скачать аудио 🔊 ролика как можно быстрее нажмите 2')
    print('Чтобы скачать аудио 📀 в наилучшем качестве нажмите 3 ')
    print('Чтобы скачать видео 📽 в наилучшем качестве (Warning! Это долго и тяжело для вашего процессора) нажмите 4 ')
    yes_or_no = input('Введите 1/2/3/4>>:  ')

    if yes_or_no == '2':
        try:
            video = YouTube(url)
            stream = video.streams.filter(only_audio=True).first()
            title = stream.title.replace("?","")
            print(f'Качаю -={title}=-')
            destination = folder_for_download()

            stream.download(filename=f"{title}.mp3", output_path=destination)
            print("The video is downloaded in MP3")
        except KeyError:
            print("Unable to fetch video information. Please check the video URL or your network connection.")
    
    elif yes_or_no == '1':
        yt = YouTube(url, on_progress_callback = on_progress)

        title = yt.title.replace("?","")
        print(f'Качаю -={title}=-')

        destination = folder_for_download()
 
        ys = yt.streams.get_highest_resolution()

        ys.download(filename=f'{title}.mp4', output_path=destination)

    elif yes_or_no == '4':
        yt = YouTube(url, on_progress_callback = on_progress)

        title = yt.title.replace("?","")
        print(f'Качаю -={title}=-')

        destination = folder_for_download()
 
        # ys = yt.streams.get_highest_resolution()
        # ys = yt.streams.filter(res='720p').first()
        # ys = yt.streams.filter(res='720p').desc().first()
        # ys = yt.streams.filter(progressive=True).last()
        # ys = yt.streams.filter(res='1080p').desc().first() получаем самое высокое качество видео без звука
        ys = yt.streams.filter(res='1080p').desc().first()
        ys.download(filename=f'{title}.mp4', output_path=destination)

        # Отдельно скачивание аудио
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(filename=f"{title}.mp3", output_path=destination)

        videoclip = VideoFileClip(filename=fr'{destination}/{title}.mp4')
        audioclip = AudioFileClip(filename=fr'{destination}/{title}.mp3')

        new_audioclip = CompositeAudioClip([audioclip])
        videoclip.audio = new_audioclip
        # videoclip.write_videofile(filename=fr'New_{destination}/{title}.mp4')
        videoclip.write_videofile(filename=fr'{destination}/{title}_vovkina_proga.mp4')
        videoclip.close()
        new_audioclip.close()
        os.remove(fr"{destination}/{title}.mp4")
        os.remove(fr"{destination}/{title}.mp3")


    else:
        yt = YouTube(url, on_progress_callback = on_progress)
        title = yt.title.replace("?","")
        print(f'Качаю {title}')
        destination = folder_for_download()
        ys = yt.streams.get_highest_resolution()
        ys.download(filename=f'{title}.mp4', output_path=destination)
        # Load the mp4 file
        video = VideoFileClip(filename=fr'{destination}/{title}.mp4')

        # Extract audio from video
        video.audio.write_audiofile(filename=fr'{destination}/{title}.mp3')
        video.close()
        os.remove(fr"{destination}/{title}.mp4")

        
while True:
    main()
    afterMain()
