from .bank import Bank
from globalCode.classSInt import SInt

class AdvanceBank(Bank):

    def __init__(self, childInBatteries = 0):
        self.voltageMaxLength = 12
        super().__init__(inBatteries = childInBatteries)

    def findMaxVoltage(self):
        
        if self.bank.isEmpty():
            return

        numOfBattery = len(self.bank)
        remainBatteries = numOfBattery - 1

        # Sets the first number, as it will always be greater then nothing :-)
        potentialVoltage = SInt(self.bank[0])
        
        # Searches through all the batteries in the bank
        for curBattery in range(1, numOfBattery):
            
            # Gets the current voltage
            voltage = self.bank[curBattery]

            self._removeSmallVoltage(potentialVoltage, voltage, remainBatteries)
            remainBatteries = remainBatteries - 1

        
        self.setMaxVoltage(potentialVoltage)   
       
    def _removeSmallVoltage(self, potentialVoltage, voltage, spotsRemaing):
       
        # Adds battery if it's the only one
        if potentialVoltage.isEmpty():
            potentialVoltage.append(voltage)
        
        # Adds battery if near the end and don't have the required number of batteries
        elif (len(potentialVoltage) + spotsRemaing <= self.voltageMaxLength):
            potentialVoltage.append(voltage)

        # Checks if the voltage is greater then the last stored battery
        elif potentialVoltage[-1] < voltage:
            potentialVoltage.pop()
            self._removeSmallVoltage(potentialVoltage, voltage, spotsRemaing)

        # Adds the battery if the are not all ready 12 batteries
        elif len(potentialVoltage) < self.voltageMaxLength:
            potentialVoltage.append(voltage)

        return potentialVoltage
