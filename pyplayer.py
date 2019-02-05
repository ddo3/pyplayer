import pyglet
import numpy as np
from typing import List
import os

song_queue = []
queue_size = 10
current_song_num = 0
#need a queue of songs

#in this queue, we will start from the begining, and

player = pyglet.media.Player()

def search_for_song(song_name: str) -> str:
    for file in os.listdir('./'):
        if song_name in file:
            return file
    return None

def play_queue_song() -> None:
    if(len(song_queue) > 0):
        player.play()
    else:
        print('No songs in queue')

def play_song(song_name: str) -> None:
    filename = search_for_song(song_name)
    if(filename != None):
        global current_song_num
        song_queue.append( filename)
        current_song_num = current_song_num + 1
        songSource = pyglet.media.load(filename)
        player.queue(songSource)
        player.play()
    else:
        print('Couldnt find that song')

def stop_song() -> None:
    player.pause()

def change_queue_size(size: int) -> None:
    queue_size = size

def possible_actions() -> None:
    print('Here are some actions:')
    print('q    : print the songs queue')
    print('size : print the size of the queue')
    print('size {num}: change the size of the queue')
    print('shuffle : shuffle the songs in the queue')
    print('new songs: pick new songs from the queue')
    print('play {song name}: play specific song')
    print('play : starts playing songs in the queue')
    print('play {song num} : plays song at this number in queue')
    print('stop : stops playing current song')
    print('curr song num: gets the number of the current song playing')
    print('x : stop the PyPlayer ')
    print('help : show actions again')

def main() -> None:

    print('Welcome to PyPlayer!')
    print()
    possible_actions()

    while True:
        ans = input('What do you want to do? \n')

        if ans == 'x':
            print('See you later!')
            break
        elif ans == 'help':
            possible_actions()
        elif ans == 'play':
            play_queue_song()
        elif 'play' in ans:
            second_command = ans.split()[1]
            play_song(second_command)
        elif ans == 'stop':
            stop_song()

if __name__ == '__main__':
    main()
