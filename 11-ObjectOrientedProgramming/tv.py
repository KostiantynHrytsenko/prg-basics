# tv.py file
# class definition
class TV:
   def __init__(self):
      self.is_on = False
      self.channel_no = 1
      self.channels = []
      self.volume = 5
   def turn_off(self):
      self.is_on = False
   def set_channel(self, new_channel_no):
      self.channel_no = new_channel_no
   def set_channels(self, channels_list):
      self.channels = channels_list
   def increase_volume(self):
      if self.volume < 10:
       self.volume += 1
   def decrease_volume(self):
      if self.volume > 0:
       self.volume -= 1
   def show_channels(self):
      j = 1
      for i in self.channels:
         print(f"{j}.{self.channels[j-1]}")
         j+=1
   def turn_on(self):
      self.is_on = True
   def show_status(self):
      if(self.is_on):
        if(self.channel_no <= len(self.channels)):
         print(f"TV is on, channel {self.channel_no}, ({self.channels[self.channel_no - 1]}), volume:{self.volume}")
        else:
           print(f"TV is on, channel {self.channel_no}, volume:{self.volume}")
      else:   
        print("TV is off")