#import vlc

song_queue = []
queue_size = 10
current_song_num = 0
#need a queue of songs

#in this queue, we will start from the begining, and

#User can have the choice of playing random songs, or playing the whole queue_size


#p = vlc.MediaPlayer("file:///path/to/track.mp3")
#p.play()

#def start_application() -> None:
    #

#def play_song() -> None:
#def stop_song() -> None:

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
    #cmd = sys.argv[1]
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


if __name__ == '__main__':
    main()
