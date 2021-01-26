from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    current_song = self.__first_song
    new_song = Song(title)

    if current_song == None:
      self.__first_song = new_song
      return

    while current_song.get_next_song() != None:
      current_song = current_song.get_next_song()

    current_song.set_next_song(Song(title))


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 
  def find_song(self, title):
    current_song = self.__first_song
    current_ind = 0

    if current_song == None:
      return "Playlist is empty. No songs to find."

    while current_song.get_title() != title and current_song.get_next_song() != None:
      current_song = current_song.get_next_song()
      current_ind += 1
    
    if current_song.get_title() != title and current_song.get_next_song() == None:
      return -1
    else:
      return current_ind

 
  def remove_song(self, title):
    pass
    previous_song = None
    current_song = self.__first_song

    if current_song == None:
      print('Playlist is empty. No songs to remove.')
      return

    while current_song.get_title() != title and current_song.get_next_song() != None:
      previous_song = current_song
      current_song = current_song.get_next_song()

    # If I reach the end of the linked list 
    if current_song.get_title() != title and current_song.get_next_song() == None:
      print(f'Could not find song title {title} in the playlist.')
    
    # When code enters here, that means we've found the song
    next_song = current_song.get_next_song()
    previous_song.set_next_song(next_song)

  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    pass
    current_song = self.__first_song
    counter = 1

    if current_song == None:
      return 0

    while current_song.get_next_song() != None:
      current_song = current_song.get_next_song()
      counter += 1
    
    return counter 

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    pass

  