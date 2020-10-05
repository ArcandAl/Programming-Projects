import time
from time import sleep

'''
PID control algortihm for 
controlling a smoker
'''

class PID(object):

    def __init__(self, propGain, integGain, derivGain, curTime):

        self.lastError = 0.0
        self.lastTime = curTime

        self.propGain = propGain    # how aggressively PID reacts to current error with setting gain
        self.integGain = integGain
        self.derivGain = derivGain
        self.integError = 0.0

    def pidAlgorithm(self, input, setpoint, curTime):
        elapsedTime = curTime - self.lastTime

        instanteneousError = setpoint - input   # proportional

        self.integError = self.integError + (instanteneousError + self.lastError) * elapsedTime
        cumulativeError = self.integError

        rateOfError = (instanteneousError - self.lastError) / elapsedTime

        propOutput = self.propGain * instanteneousError
        integOutput = self.integGain * cumulativeError
        derivOutput = self.derivGain * rateOfError

        self.lastError = instanteneousError
        self.lastTime = curTime

        return propOutput, integOutput, derivOutput
