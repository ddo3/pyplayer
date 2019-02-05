import pyglet
import numpy as np
from typing import List
import os

class PyPlayer:
    def __init__(self) -> None:
        self.song_queue = []
        self.queue_size = 10
        self.current_song_num = -1
        self.temp_song_playing = False
        self.queue_songs_playing = False
        self.player = pyglet.media.Player()
        self.player_temp = pyglet.media.Player()

    @staticmethod
    def print_all_songs() -> None:
        print()
        print("All Songs:")
        for file in os.listdir('./'):
            if '.mp3' in file or '.mp4' in file:
                print(file)

    @staticmethod
    def search_for_song(song_name: str) -> str:
        name = song_name.lower()
        for file in os.listdir('./'):
            if name in file.lower():
                return file
        return None

    def play_queue_song(self) -> None:
        if(len(self.song_queue) > 0):
            self.player.play()
        else:
            print('No songs in queue')

    def start_song_again(self) -> None:
        if self.temp_song_playing :
            self.player_temp.play()
        elif self.queue_songs_playing:
            self.player.play()
        else:
            print('No songs have been queued to play.')

    def play_temp_song(self, song_name: str) -> None:
        filename = self.search_for_song(song_name)
        #temp_song_playing
        if(filename != None):
            self.temp_song_playing = True
            #global current_song_num
            #song_queue.append( filename)
            #current_song_num = current_song_num + 1
            songSource = pyglet.media.load(filename)
            self.player_temp.queue(songSource)
            self.player_temp.play()
        else:
            self.temp_song_playing = False
            print('Couldnt find that song')

    def pause_temp_song(self) -> None:
        self.player_temp.pause()

    def stop_temp_song(self) -> None:
        self.player_temp.pause()
        self.player_temp = pyglet.media.Player()
        self.temp_song_playing = False

    def stop(self) -> None:
        if self.temp_song_playing:
            self.stop_temp_song()
        elif self.queue_song_playing:
            self.player.pause()
        else:
            print('No songs are playing.')

    def change_queue_size(self, size: int) -> None:
        self.queue_size = size

    @staticmethod
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
    playerObject = PyPlayer()
    print('Welcome to PyPlayer!')
    print()
    PyPlayer.possible_actions()

    while True:
        ans = input('What do you want to do? \n')

        if ans == 'x':
            print('See you later!')
            break
        elif ans == 'help':
            playerObject.possible_actions()
        elif ans == 'play':
            playerObject.start_song_again()
        elif 'play' in ans:
            second_command = ans.split()[1]
            playerObject.play_temp_song(second_command)
        elif ans == 'stop':
            playerObject.stop()
        elif ans == 'pause':
            playerObject.pause_temp_song()
        elif ans == 'q':
            playerObject.print_all_songs()

        print()

if __name__ == '__main__':
    main()
