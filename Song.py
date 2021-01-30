class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None

  def get_title(self):
    return self.__title
  

  def set_title(self, title):
    if not isinstance(title, str):
      return print(f"ERROR: Failed to set title, {title} is not type string")
      
    if not title.istitle():
      return print(f"ERROR: Failed to set title, {title} is not title case")
      
    self.__title = title


  def get_next_song(self):
    return self.__next_song


  def set_next_song(self, next_song):
    if not isinstance(next_song, Song) and next_song is not None:
      return print(f"ERROR: Failed to set next song, {next_song} is not type Song")
    
    self.__next_song = next_song


  def __str__(self):
    return self.get_title()


  def __repr__(self):
    return f"{self.get_title()} -> {self.get_next_song().get_title()}"
