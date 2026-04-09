import time
import datetime
import pygame

def set_alarm (alarm_time: str):
  print(f"Alarm set for {alarm_time}")
  sound_file = "alarm.mp3"
  is__running = True

  while is__running:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)

    if current_time == alarm_time:
      print("WAKE UP! 😶")

      pygame.mixer.init()
      pygame.mixer.music.load(sound_file)
      pygame.mixer.music.play()

      while pygame.mixer.music.get_busy():
        time.sleep(1)

      is__running = False

    time.sleep(1)

if __name__ == "__main__":
  alarm_time = input("Enter the alarm time (HH:MM:SS): ")
  set_alarm(alarm_time)
