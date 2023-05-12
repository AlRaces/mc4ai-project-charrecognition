import numpy as np

names = np.array([str(i) for i in range(10)] + [chr(65 + i)
                                                for i in range(26)] + [(chr(97 + i)) for i in range(26)])

print(names.shape)
np.save("./names.npy", names)
