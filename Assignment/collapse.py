# Evan Henley
# EAH0102
# August 29, 2021

# This method collapses any non-negative integer value, provided as a string,
# into a single digit.

def collapse(value):
    
    if (isinstance(value,str) and (value.isnumeric()) and (len(value) < 51)):
        
        storedVal = value
        
        while (len(storedVal) > 1):
            tempVal = 0
            
            for character in storedVal: 
            
                tempVal += int(character)
            
            storedVal = str(tempVal)
            
            
        return storedVal
    
    else:
        return None