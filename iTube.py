#!/usr/env/bin python3

from pytube import YouTube
from pytube import Playlist
from tqdm import tqdm
from termcolor import colored
import pyfiglet
import os
import time
import shutil
import re

def banner():
    os.system("cls")
    ascii_banner = pyfiglet.figlet_format("iTube")
    print(colored("###################################################################", "blue", attrs=['bold']))
    print(colored(ascii_banner + "	                                                  ", "blue", attrs=['bold']))
    print(colored(""" Coded by: 0xmarWan7A                    								   	
 Github: https://github.com/0xmarWan7A/           				 """ , "blue", attrs=['bold']))
    print(colored("###################################################################",  "blue", attrs=['bold']))
    print("")

banner()

def progress_bar():
    for i in tqdm(range(100), ascii=True, desc="Downloading... "):
        time.sleep(0.05)

def remove_special_characters(character):
    if character.isalnum() or character == ' ' or character == '-' or character == '&' or character == '[' or character == ']':
        return True
    else:
        return False

print(colored("[+] Welcome to iTube script for downloading videos from YouTube " , "blue", attrs=['bold']))
print(colored("\n\nSelect your option: " , "blue", attrs=['bold']))
print(colored("\n[1] Playlist" , "blue"))
print(colored("[2] Video\n", "blue"))
selector = int(input(colored("Enter the number of select ===> " , "red" , attrs=['bold'])))
if selector == 1:
    os.system("cls")
    banner()
    def YT_playlist_downloader():
        link = str(input(colored("[+] Enter the playlist link : ", "red", attrs=['bold'])))
        playlist = Playlist(link)
        
        urls = playlist.video_urls
        print(colored("\n[+] Number of videos : " + str(len(urls)) , "yellow"))
        for url in urls:
            try:
                server = YouTube(url, on_progress_callback=progress_bar())
            except Exception as e:
                print(colored(e, "red", attrs=['bold']))

            video_title = server.title
            video_author = server.author
            video_length = int(server.length / 60) 
            video_viewers = server.views

            print(colored(f"""
[+] Video Title: {video_title}
[+] Video Author: {video_author}
[+] Video Length: {str(video_length)} min
[+] Video Viewers: {video_viewers} views
""", "blue", attrs=['bold']))

            try:
                server.streams.get_highest_resolution().download()
                path = os.getcwd()
                new_path = f"D:/youtube/"
                video_title1 = "".join(filter(remove_special_characters, video_title))
                video_path =  path + "\\" + video_title1 + ".mp4"
                shutil.move(video_path, new_path)
                print(colored("\n[+] Video has been downloaded Successfully", "green", attrs=['bold']))
                print(colored("=" * 100 , "blue"))
            except Exception as e:
                print(colored(e, "red", attrs=['bold']))
        print(colored("\n[+] Playlist has been downloaded Successfully", "green", attrs=['bold']))
    YT_playlist_downloader()   

elif selector == 2:
    os.system("cls")
    banner()
    def YT_video_downloader():
        link = str(input(colored("[+] Enter the video link : ", "red", attrs=['bold'])))

        try:
            server = YouTube(link, on_progress_callback=progress_bar())
        except Exception as e:
            print(colored(e, "red", attrs=['bold']))

        video_title = server.title
        video_author = server.author
        video_length = int(server.length / 60) 
        video_viewers = server.views

        print(colored(f"""
    [+] Video Title: {video_title}
    [+] Video Author: {video_author}
    [+] Video Length: {str(video_length)} min
    [+] Video Viewers: {video_viewers} views
    """, "blue", attrs=['bold']))

        try:
            server.streams.get_highest_resolution().download()   
            path = os.getcwd()
            new_path = "D:/youtube/"
            video_title1 = "".join(filter(remove_special_characters, video_title))
            video_path =  path + "\\" + video_title1 + ".mp4"
            shutil.move(video_path, new_path)
            print(colored("\n[+] Video has been downloaded Successfully", "green", attrs=['bold']))
        except Exception as e:
            print(colored(e, "red", attrs=['bold']))

    YT_video_downloader()

else:
    print(colored("[-] Enter correct number !!" , "red", attrs=['bold']))
    pass


