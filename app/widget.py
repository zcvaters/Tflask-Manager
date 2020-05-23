from threading import Timer

class Timr:

    def __init__(self, currTime =0):
        self.currTime = currTime
        self.mins = 0

    def getTime(self):
        return self.currTime
    
    def timeSet(self):
        # Increases the time in one minute intervals
        # TODO: create a countdown/ more detailed description
        self.currTime = self.currTime * 60
        z = Timer(self.currTime, self.status)
        z.start()

    def status(self):
        print("Timer Complete")

if __name__ == "__main__":
    currTime = int(input())
    t = Timr(currTime)
    t.timeSet()