import tv

def main():
   # object creation
   tv1 = tv.TV()

   # object usage
   tv1.show_status()
   tv1.turn_on()
   tv1.show_status()
   tv1.show_channels()
   tv1.set_channels(["TVP1", "TVP2", "Filmbox", "TVN", "Discovery", "Polsat", "MTV"])
   tv1.show_channels()
   tv1.set_channel(7)
   tv1.increase_volume()
   tv1.increase_volume()
   tv1.increase_volume()
   tv1.increase_volume()
   tv1.increase_volume()
   tv1.increase_volume()
   tv1.show_status()
   tv1.set_channel(61)
   tv1.decrease_volume()
   tv1.decrease_volume()
   tv1.decrease_volume()
   tv1.show_status()
   tv1.turn_off()
   tv1.show_status()

if __name__ == "__main__":
   main() 