#If the heart rate of the user falls below a certain threshold,
#send in Ronnie to motivate them.

#import the sound player
#import PulseSensor_timer.c
import time

class Motivate:

    def process_heart_rate(self, age):
        #figure out if the heart rate has fallen below certain threshold

        resting_heart_rate = 80
        max_heart_rate = 220 - age
        heart_rate_reserve = max_heart_rate - resting_heart_rate
        bpm_threshold = (heart_rate_reserve * .7) + resting_heart_rate

        #while (getBPM() != None):

            #bpm = getBPM()

            #if (bpm < bpm_threshold):

                #play_sound()
                sleep(15)

def main():
    Motivate.process_heart_rate()

main()