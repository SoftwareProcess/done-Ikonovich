import unittest
import Assignment.collapse as collapse


class CollapseTest(unittest.TestCase):

    # Happy path:  nominal value within bounds
    def test100_100_ShouldCollapseSingleDigit(self):
        value = '5'
        expectedResult = '5'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    # Happy path: value contains 5 digits
    def test_ShouldCollapseFiveDigits(self):
        value = '11121'
        expectedResult = '6'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    # Happy path: Initial sum contains multiple digits
    def test_ShouldCollapseMultipleDigitInitialSum(self):
        value = '123456789'
        expectedResult = '9'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
      
    #  Happy path: value contains 50 digits
    def test_ShouldCollapseFiftyDigits(self):
        value = '15948305706294801849230528214092429723429482193121'
        expectedResult = '6'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    # Happy path: value is all zeroes
    def test_ShouldCollapseAllZeroes(self):
        value = '000000'
        expectedResult = '0'
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)

    #  Sad path: value is non-numeric
    def test_ShouldNotCollapseNonNumeric(self):
        value = 'abc'
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)

    # Sad path: value is over 50 digits
    def test_ShouldNotCollapseFiftyOneDigits(self):
        value = '159483057062948018492305282140924297234294821931215'
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    # Sad path: value is 0 digits
    def test_ShouldNotCollapseZeroDigits(self):
        value = ''
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    # Sad path: No input parameter
    def test_ShouldNotCollapseValueNone(self):
        value = None
        expectedResult = None
        actualResult = collapse.collapse(None)
        self.assertEqual(expectedResult, actualResult)
        
    # Sad path: value less than 0
    def test_ShouldNotCollapseValueBelowZero(self):
        value = '-5'
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)
        
    # Sad path: value is not string
    def test_ShouldNotCollapseValueNotString(self):
        value = 1
        expectedResult = None
        actualResult = collapse.collapse(value)
        self.assertEqual(expectedResult, actualResult)