from Song import Song
import random

class Playlist:
  def __init__(self):
    self.__first_song = None


  def add_song(self, title):
    # adds song by reassigning relationships by going through a while loop
    current_song = self.__first_song
    new_song = Song(title)

    # if playlist is empty
    if current_song == None:
      self.__first_song = new_song
      return

    while current_song.get_next_song() != None:
      current_song = current_song.get_next_song()

    current_song.set_next_song(Song(title))


  def find_song(self, title):
    # Uses while loop to keep track and return the index
    current_song = self.__first_song
    current_ind = 0

    # if playlist is empty
    if current_song == None:
      return "Playlist is empty. No songs to find."

    # if title is not equal and we're not at the end, continue
    while current_song.get_title() != title and current_song.get_next_song() != None:
      current_song = current_song.get_next_song()
      current_ind += 1
    
    # if we reached the end and didn't find it
    if current_song.get_title() != title and current_song.get_next_song() == None:
      return -1
    else:
      # we found it
      return current_ind

 
  def remove_song(self, title):
    # Keep track of previous song as well so that we can easily reassign relationship in while loop
    previous_song = None
    current_song = self.__first_song

    # if playlist is empty
    if current_song == None:
      print('Playlist is empty. No songs to remove.')
      return

    # if we're not at the end and title is not equal, then continue
    while current_song.get_title() != title and current_song.get_next_song() != None:
      previous_song = current_song
      current_song = current_song.get_next_song()

    # If I reach the end of the linked list 
    if current_song.get_title() != title and current_song.get_next_song() == None:
      print(f'Could not find song title {title} in the playlist.')
    
    # When code enters here, that means we've found the song
    next_song = current_song.get_next_song()
    previous_song.set_next_song(next_song)


  def length(self):
    #uses while loop and a counter to find length of the linked list
    current_song = self.__first_song
    counter = 1

    # if playlist is empty
    if current_song == None:
      return 0

    #use counter to keep track of length
    while current_song.get_next_song() != None:
      current_song = current_song.get_next_song()
      counter += 1
    
    return counter 


  def print_songs(self):
    current_song = self.__first_song
    counter = 1

    # if playlist is empty
    if current_song == None:
      print("Your playlist has no songs!")
      return
    
    
    while current_song.get_next_song() != None:
      print(f"{counter}. {current_song}")

      current_song = current_song.get_next_song()
      counter += 1
    
    # Print last song
    print(f"{counter}. {current_song}")

  def insert_song(self, title, index):
      # Checking if the input is valid
      self_len = self.length()
      if index + 1 > self_len:
        print("ERROR: index is out of range")
        return
      
      current_song = self.__first_song
      current_ind = 0
      
      #Loop until the indeces are equal
      while current_ind != index:
        current_song = current_song.get_next_song()
        current_ind += 1
      
      # we found the song in the current index,
      song_to_insert = Song(title)
      next_song = current_song.get_next_song()
      
      # Reassign relationships
      song_to_insert.set_next_song(next_song)
      current_song.set_next_song(song_to_insert)

  def reverse(self):

    # If playlist is empty or 1
    if self.__first_song == None or self.__first_song.get_next_song() == None:
      return
  
    # Recursive Function helper
    def recur(prev, curr):
      # If the last value, return it
      if curr.get_next_song() == None:
        curr.set_next_song(prev)
        return curr
      else:
        #otherwise, keep going and processes changes
        new_curr = curr.get_next_song()
        curr.set_next_song(prev)
        return recur(curr, new_curr)

    self.__first_song = recur(None, self.__first_song)
    
    



  
