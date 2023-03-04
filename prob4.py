# Suppose you are making a program for a Television remote control named “RickMote”. The TV
# channel provider has provided only 6 channels where the corresponding channel numbers are
# 0,2,3,6,7,9. This is a vital information as you might need to store the list of channel numbers in
# an instance variable. Now your task is to design the “RickMote” class in such a way that the
# expected output is produced for the given code below: [Hint:
#     • The channel numbers are not circular. So, channel number 0 is the first channel while 9
#     is the last. You cannot go below channel number 0 and beyond channel number 9.
#     • If power is turned off, there is no point in changing channel and volume.
#     • Increasing channel number means going to the next channel in the channel list and
#     decreasing it means going to the previous channel in the channel list.]

class RickMote:
    def __init__(self):
        self.lst = [0, 2, 3, 6, 7, 9]
        self.pow = 'OFF'
        self.channel = 0
        self.volume = 3

    def power(self):
        if (self.pow == 'OFF'):
            self.pow = 'ON'
        elif (self.pow == 'ON'):
            self.pow = 'OFF'

    def changeVolumeLevel(self, vol=None):
        if (self.pow == 'OFF'):
            print('powerr is turned off. Cannot change volume.')
        else:
            if (vol == None):
                self.volume += 1
            elif (vol != None):
                self.volume += vol

    def changeChannel(self, chl=None):
        if (self.pow == 'OFF'):
            print('powerr is turned off. Cannot change Channel')
        else:
            if (chl == None):
                idx = self.lst.index(self.channel)
                self.channel = self.lst[idx+1]
            else:
                if (chl in self.lst):
                    self.channel = chl
                else:
                    print('TV channel does not exist')

    def showInfo(self):
        print('ID Cable Box Status: \nCable Box is: {self.pow}')
        if (self.pow == 'ON'):
            print(f'Channel:{self.channel} \nVolume:{self.volume}')
        else:
            pass


oTV = RickMote()
oTV.power()
print("1.############################")
oTV.showInfo()
print("2.############################")
oTV.changeChannel()
oTV.changeVolumeLevel()
oTV.showInfo()
print("3.############################")
oTV.power()
oTV.showInfo()
print("4.############################")
oTV.power()
oTV.changeVolumeLevel(4)
oTV.changeChannel(3)
oTV.showInfo()
print("5.############################")
oTV.changeVolumeLevel(-2)
oTV.showInfo()
print("6.############################")
oTV.power()
oTV.changeChannel(9)
oTV.changeVolumeLevel(-1)
oTV.showInfo()
print("7.############################")
oTV.power()
oTV.changeChannel(11)
oTV.showInfo()
