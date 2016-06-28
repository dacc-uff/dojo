import unittest

class TestRomanNumbers(unittest.TestCase):
    def test_1(self):
        self.assertEqual(arabic_to_roman(1), 'I')

    def test_2(self):
        self.assertEqual(arabic_to_roman(2), 'II')

    def test_3(self):
        self.assertEqual(arabic_to_roman(3), 'III')

    def test_4(self):
        self.assertEqual(arabic_to_roman(4), 'IV')

    def test_5(self):
        self.assertEqual(arabic_to_roman(5), 'V')

    def test_10(self):
        self.assertEqual(arabic_to_roman(10), 'X')

    def test_9(self):
        self.assertEqual(arabic_to_roman(9), 'IX')

    def test_1000(self):
        self.assertEqual(arabic_to_roman(1000), 'M')

    def test_500(self):
        self.assertEqual(arabic_to_roman(500),'D')

    def test_1501(self):
        self.assertEqual(arabic_to_roman(1501), 'MDI')

    def test_8(self):
        self.assertEqual(arabic_to_roman(8), 'VIII')

    def test_90(self):
        self.assertEqual(arabic_to_roman(90), 'XC')

    def test_404(self):
        self.assertEqual(arabic_to_roman(404), 'CDIV')

    def test_42(self):
        self.assertEqual(arabic_to_roman(42), 'XLII')
    def test_944(self):
        self.assertEqual(arabic_to_roman(944), 'CMXLIV')

    def test_2000(self):
        self.assertEqual(arabic_to_roman(2000), 'MM')

    def test_2999(self):
        self.assertEqual(arabic_to_roman(2999), 'MMCMXCIX')

    def test_244(self):
        self.assertEqual(arabic_to_roman(244), 'CCXLIV')

    def test_2440(self):
        self.assertEqual(arabic_to_roman(2440), 'MMCDXL')

    def test_3333(self):
        self.assertEqual(arabic_to_roman(3333), 'MMMCCCXXXIII')

    def test_1400(self):
        self.assertEqual(arabic_to_roman(1400), 'MCD')

def arabic_to_roman(number):

    string_num = ''

    a,number = divmod(number,1000)
    string_num += 'M'*a
    if number >= 900:
        string_num += 'CM'
        number -= 900
    a,number = divmod(number,500)
    string_num += 'D'*a
    if number >= 400:
        string_num += "CD"
        number -= 400
    a,number = divmod(number,100)
    string_num += 'C'*a
    if number >= 90:
        string_num += "XC"
        number -= 90
    a,number = divmod(number,50)
    string_num += 'L'*a
    if number >= 40:
        string_num += "XL"
        number -= 40
    a,number = divmod(number,10)
    string_num += 'X'*a
    if number >= 9:
        string_num += "IX"
        number -= 9
    a,number = divmod(number,5)
    string_num += 'V'*a
    if number >= 4:
        string_num += "IV"
        number -= 4
    a,number = divmod(number,1)
    string_num += 'I'*a

    return string_num

def main():
    arabic_to_roman(2444)

if __name__ == '__main__':
    unittest.main()
    main()
