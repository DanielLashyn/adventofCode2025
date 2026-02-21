from globalCode.classSInt import SInt

class Bank():

    def __init__(self, inBatteries = 0):
        self.setBank(inBatteries)
        print(type(self.bank))
        print(self.bank)
        print(self.bank[0:3])
        self.bank[2:] = 9

        print(self.bank)

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


