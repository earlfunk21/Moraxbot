import sqlite3
import struct

class ComputerSystem:
    def __init__(self) -> None:
        with sqlite3.connect("database/ndatarep.db") as self.conn:
            self.cur = self.conn.cursor()

    def Decimal_Binary(self, n):
        self.cur.execute("SELECT Binary FROM NumericDataRepresentation WHERE Decimal=?", (n))
        return self.cur.fetchone()[0]
    
    def Binary_Hexadecimal(self, n):
        self.cur.execute("SELECT Hexadecimal FROM NumericDataRepresentation WHERE Binary={}".format(n))
        return self.cur.fetchone()[0]
    
    def Hexadecimal_Decimal(self, n):
        self.cur.execute("SELECT Decimal FROM NumericDataRepresentation WHERE Hexadecimal=?", (n))
        return self.cur.fetchone()[0]

    def Unpacked(self, digit):
        zone = "1111"
        posi = "1100"
        nega = "1101"
        binary = []
        if digit[0] == "+":
            sign = posi
        elif digit[0] == "-":
            sign = nega
        else:
            return "Invalid Decimal Digit"
        lastd = len(digit) - 1
        for n in range(1, len(digit)):
            BCD = str(self.Decimal_Binary(digit[n]))
            for _ in range(4):
                if len(BCD) < 4:
                    BCD = "0" + BCD
            if n == lastd:
                binary.append(sign)
                binary.append(BCD)
                return binary
            else:
                binary.append(zone)
                binary.append(BCD)
    
    def packed(self, digit):
        posi = "1100"
        nega = "1101"
        binary = []
        if digit[0] == "+":
            sign = posi
        elif digit[0] == "-":
            sign = nega
        else:
            return "Invalid Decimal Digit"
        digit = digit.replace(digit[0], "")
        for n in range(len(digit)):
            BCD = str(self.Decimal_Binary(digit[n]))
            for _ in range(4):
                if len(BCD) < 4:
                    BCD = "0" + BCD
            binary.append(BCD)
        binary.append(sign)
        return binary

    def hexadecimal(self, binary):
        hexadecimal = []
        for i in binary:
            hexadecimal.append(str(self.Binary_Hexadecimal(i)))
        return hexadecimal

    def truevalue(self, Hexadecimal=None, Octa=None, Binary=None, Decimal=None):
        if Hexadecimal:
            return self._Truevalue(Hexadecimal, base=16)
        elif Decimal:
            return self._Truevalue(Decimal, base=10)
        elif Octa:
            return self._Truevalue(Octa, base=8)
        elif Binary:
            return self._Truevalue(Binary, base=2)
        else:
            return "Invalid Option"
            
    def _Truevalue(self, numbers, base=None):
        if base is None:
            base = len(numbers) + 1
        expo = 0
        total = 0
        if isinstance(numbers, str):
            numbers = [int(self.Hexadecimal_Decimal(i)) for i in reversed(numbers)]
        elif isinstance(numbers, int):
            numbers = [int(i) for i in reversed(str(numbers))]
        else:
            return "It must be Integer or String"
        for i in numbers:
            total += i*(base**expo)
            expo += 1
        return total

