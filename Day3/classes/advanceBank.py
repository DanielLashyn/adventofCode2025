from .bank import Bank
from globalCode.classSInt import SInt

class AdvanceBank(Bank):


    def findMaxVoltage(self):
        
        if self.bank.isEmpty():
            return

        numOfBattery = len(self.bank)
        remainBatteries = numOfBattery - 1

        # Sets the first number, as it will always be greater then nothing :-)
        potentialVoltage = SInt(0)
        potentialVoltage[0] = self.bank[0]
        
        # Searches through all the batteries in the bank
        for curBattery in range(1, numOfBattery):
            
            # Gets the current voltage
            voltage = self.bank[curBattery]
            #If remaing length = spots avilbabe:
                #then append
            #else:
            self._removeSmallVoltage(potentialVoltage, voltage, remainBatteries)
            remainBatteries = remainBatteries - 1


#Check if the voltage is greater then voltage last in digit:
                # True: set that current Voltage to 0 and check next digit
                # False: If there is a spot then add that digit to the last avilable digit otherwise ignore it
            '''if voltage > potentialVoltage[0]:
                if (numOfBattery - curBattery) > 1:
                    potentialVoltage[0] = voltage
                    potentialVoltage[1] = 0
                else:
                    potentialVoltage[1] = voltage
            elif voltage > potentialVoltage[1]:
                potentialVoltage[1] = voltage
        '''
        print(potentialVoltage)
        self.setMaxVoltage(potentialVoltage)   
       
    def _removeSmallVoltage(self, potentialVoltage, voltage, spotsRemaing):
       
        
        if potentialVoltage.isEmpty():
            potentialVoltage.append(voltage)
        elif (len(potentialVoltage) + spotsRemaing <= 12):
            potentialVoltage.append(voltage)

        elif potentialVoltage[-1] < voltage:
            potentialVoltage.pop()
            self._removeSmallVoltage(potentialVoltage, voltage, spotsRemaing)

        elif len(potentialVoltage) < 12:
            potentialVoltage.append(voltage)

        return potentialVoltage
