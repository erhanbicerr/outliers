import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.randint(5000, 10000, 5000)
plt.hist(incomes, 50)
plt.show()
print("Old Mean =", np.mean(incomes))
print("Old Median =", np.median(incomes))
print("Old Std =", incomes.std())

incomes = np.append(incomes, [1000000000])
print("New Mean =", np.mean(incomes))
print("New Median =", np.median(incomes))
print("New Std =", incomes.std())
