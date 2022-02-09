x = 12

# 12  = 00001100
# ~12 = 11110011

# 13 = 00001101
# one's complinebt = 11110010
# plus one         = 11110011
# this is two's compliment
# 13's two's compliment = -13 (11110011) = ~12

print(x)
print(~x)


x = 0b00001111
y = 0b00110011

print(bin(x | y))  # OR
print(bin(x & y))  # AND
print(bin(x ^ y))  # XOR


x = 0b00000100
print(bin(x << 2))
print(bin(x >> 2))
