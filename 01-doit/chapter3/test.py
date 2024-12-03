# class Cal:
#     def __init__(self):
#         self.value = 0

#     def add(self, val):
#         self.value += val


# # class UpgradeCal(Cal) :
# #     def minus(self, val) :
# #         self.value -= val

# # cal = UpgradeCal()
# # cal.add(10)
# # cal.minus(7)

# # print(cal.value)


# class MaxLimitCal(Cal):
#     def add(self, val):
#         self.value += val

#         if self.value > 100:
#             self.value = 100


# cal2 = MaxLimitCal()
# cal2.add(50)
# cal2.add(60)
# print(cal2.value)


# print(all([1, 2, abs(-3) - 3]))
# print(chr(ord("a")) == "a")

# a = list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3]))
# print(a)

# print(round(17/3, 4))


a = list(filter(lambda x : x > 0, [1, -3, 2, 0]))
print(a)