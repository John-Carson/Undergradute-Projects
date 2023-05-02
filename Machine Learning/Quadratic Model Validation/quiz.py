import numpy as np

p1 = np.array([3,250])

p2 = np.array([1,235])

p3 = np.array([3,195])

max_x = 5
min_x = 1

max_y = 250
min_y = 150

x_mean = 2.5
x_std = 1.38

y_mean = 212.5
y_std = 32.5

def get_distance(p1, p2):
    return np.sqrt(np.sum((p1-p2)**2))

def normalize(p):
    return np.array([ (p[0] - min_x) / (max_x - min_x), (p[1] - min_y) / (max_y - min_y) ])

def standardize(p):
    return np.array([ (p[0] - x_mean) / x_std, (p[1] - y_mean) / y_std ])

def three_distance(p1, p2):
    return np.sqrt(np.sum((p1-p2)**2))


p1_std = standardize(p1)
p2_std = standardize(p2)
p3_std = standardize(p3)

print(get_distance(p1_std, p2_std))
print(get_distance(p1_std, p3_std))


