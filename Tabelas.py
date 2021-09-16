from enum import Enum


class Funct(Enum):
    ADD = "100000"
    SUB = "100010"
    OR = "100101"
    AND = "100100"
    SLT = "101010"
    SLL = "000000"
    BNE = "000101"
    BEQ = "000100"
    J = "000010"
    JR = "001000"
    LW = "100011"
    SW = "101011"
    ADDI = "001000"
    ANDI = "001100"
    DIV = "011010"
    MULT = "011000"
    SB = "101000"
    SH = "101001"

    def __str__(self):
        return '{0}'.format(self.name)


class Registradores(Enum):
    zero = "00000"
    at = "00001"
    v0 = "00010"
    v1 = "00011"
    a0 = "00100"
    a1 = "00101"
    a2 = "00110"
    a3 = "00111"
    t0 = "01000"
    t1 = "01001"
    t2 = "01010"
    t3 = "01011"
    t4 = "01100"
    t5 = "01101"
    t6 = "01110"
    t7 = "01111"
    s0 = "10000"
    s1 = "10001"
    s2 = "10010"
    s3 = "10011"
    s4 = "10100"
    s5 = "10101"
    s6 = "10110"
    s7 = "10111"
    t8 = "11000"
    t9 = "11001"

    def __str__(self):
        return '{0}'.format(self.name)
