from pytubefix import YouTube
from moviepy.editor import *
from pytubefix.cli import on_progress
import os

# This is the part I would like you to look at. It was my way of constructing programs.
# I put everything in a main function and then add after_main function  to create a working loop.
# If you want to look at all code, it would be great
# (this is how I write apps, how I think in Python), but it's not necessary.
# It's the first  decision (main and after_main) that I came up with when I was writing my
# first program. And I stuck to it. But then AI told me that I use recursion,
# and it's not the best approach. I know what recursion is, but honestly speaking,
# I didn't think that I've been using it all the time )

def after_main():
    while True:
        waiting = input(f"\nExcellent! Press Enter to close the program. Press 1 if you want to download something else.  \n")
        if len(waiting) < 1:
            quit()
        else:
            main()
def main():
    def folder_for_download():
     # check for destination to save file
        print("Press 1 to enter the path where you want to download (for example: D:\download)")
        print('Press 2 to download to the folder specified in the program settings (text file file.txt)')
        choice = input('Enter 1/2, then Enter>>')
        if choice == '1':
            destination = str(input("Enter the path here or press Enter to download to the program folder>> ")) or '.'
        else:
            with open('file.txt', 'r') as file:
                destination = file.read()
        return destination


    url = input('Enter the URL of the video you want to download:  ')
    print('To download video quickly and in good quality, press 1')
    print('To download audio quickly, press 2')
    print('To download audio in the best quality, press 3 ')
    print('To download video in the best quality (Warning! This is long and heavy for your processor) press 4 ')
    yes_or_no = input('Enter 1/2/3/4>>:  ')

    if yes_or_no == '2':
        try:
            video = YouTube(url)
            stream = video.streams.filter(only_audio=True).first()
            title = stream.title.replace("?","")
            print(f'Downloading -={title}=-')
            destination = folder_for_download()

            stream.download(filename=f"{title}.mp3", output_path=destination)
            print("The video is downloaded in MP3")
        except KeyError:
            print("Unable to fetch video information. Please check the video URL or your network connection.")

    elif yes_or_no == '1':
        yt = YouTube(url, on_progress_callback = on_progress)

        title = yt.title.replace("?","")
        print(f'Downloading -={title}=-')

        destination = folder_for_download()

        ys = yt.streams.get_highest_resolution()

        ys.download(filename=f'{title}.mp4', output_path=destination)

    elif yes_or_no == '4':
        yt = YouTube(url, on_progress_callback = on_progress)

        title = yt.title.replace("?","")
        print(f'Downloading -={title}=-')

        destination = folder_for_download()

        ys = yt.streams.filter(res='1080p').desc().first()
        ys.download(filename=f'{title}.mp4', output_path=destination)

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
        print(f'Downloading {title}')
        destination = folder_for_download()
        ys = yt.streams.get_highest_resolution()
        ys.download(filename=f'{title}.mp4', output_path=destination)
        # Load the mp4 file
        video = VideoFileClip(filename=fr'{destination}/{title}.mp4')

        # Extract audio from video
        video.audio.write_audiofile(filename=fr'{destination}/{title}.mp3')
        video.close()
        os.remove(fr"{destination}/{title}.mp4")
