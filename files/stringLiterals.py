print("\u1010")
print()
print()
print("keyboard          = \N{KEYBOARD}")
print("Raisin Hand       = \N{HAPPY PERSON RAISING ONE HAND}")
print("Dil wali akhan    = \N{Smiling Face with Heart-Shaped Eyes}")
print("Kissie to Missie  = \N{Face throwing a kiss}")

print(end="\n\n")
print("Converting between numbers and strings", end="\n\n")

print("dead (in base 16) = ", int('dead',16))

amount, space, currency = "123.45 USD".partition(" ")
print("amount   = ", amount)
print("space    = ", space)
print("currency = ", currency)
print()
a, c = "123.45 USD".split(" ")
print("a = ", a)
# print("b = ", b)
print("c = ", c)