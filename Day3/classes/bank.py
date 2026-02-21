from globalCode.classSInt import SInt

class Bank():

    def __init__(self, inBatteries = 0):
        self.setBank(inBatteries)
        self.maxVoltage = SInt(0)
    
    # Checks that the Interger value given is a valid bank number
    def _validatedBank(self, inBatteries):

        # Attempts to convert the batteries to an integer value
        try:
            intBatteries = int(inBatteries)
        except (ValueError, TypeError):
            return 0

        # Checks that there are no 0 voltage in Batteries
        if "0" in str(intBatteries):
            return 0

        return intBatteries

    def setBank(self, inBatteries):
        intBank = self._validatedBank(inBatteries)
        self.bank = SInt(intBank)


    def setMaxVoltage(self, newVoltage):

        tmpVoltage = newVoltage
        if not isinstance(newVoltage, SInt):
            if isinstance(newVoltage, int):
                tmpVoltage = SInt(newVoltage)
            else:
                return

        self.maxVoltage = tmpVoltage

    def getMaxVoltage(self):
        return self.maxVoltage


    def findMaxVoltage(self):
        
        if self.bank.isEmpty():
            return

        numOfBattery = len(self.bank)

        potentialVoltage = SInt(10)
        potentialVoltage[0] = self.bank[0]
        
        for curBattery in range(1, numOfBattery):
            voltage = self.bank[curBattery]
            if voltage > potentialVoltage[0]:
                if (numOfBattery - curBattery) > 1:
                    potentialVoltage[0] = voltage
                    potentialVoltage[1] = 0
                else:
                    potentialVoltage[1] = voltage
            elif voltage > potentialVoltage[1]:
                potentialVoltage[1] = voltage
        
        self.setMaxVoltage(potentialVoltage)   
            

