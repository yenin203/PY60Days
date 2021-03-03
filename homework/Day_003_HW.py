import numpy as np
V1 = 20000
V0 = 20

GdB = V0 * np.log10(V1 / V0)
answer1 = GdB
# print(GdB)
GdB30 = 30
GdB50 = 50
answer2 = (np.power(10, (GdB30 /V0)) * V0) / (np.power(10, (GdB50 /V0)) * V0)
# print(answer1)
# print(answer2)
# print((np.power(10, (GdB /V0)) * V0))
# print((np.power(10, (GdB30 / V0)) * V0))
# print((np.power(10, (GdB50 / V0)) * V0))
