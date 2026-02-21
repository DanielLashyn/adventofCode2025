# Slicable Integer object

class SInt(int):
    def __new__(cls, value):
        if not isinstance(value, int):
            raise TypeError("SInt must be initialized with an int")
        return int.__new__(cls,value)
    
    def __getitem__(self,key):
        
        # Converts to string, slices, then returns int
        s = str(self)
        result = s[key]
        
        return int(result) if isinstance(result, str) else result
