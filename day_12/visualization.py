from string import ascii_lowercase
import matplotlib.pyplot as plt
import numpy as np

alphabet = 'S' + ascii_lowercase + 'E'
with open('input.txt', 'r') as f:
    data = f.readlines()

data = [l.replace('\n', '') for l in data]
data = [[k for k in w] for w in data]

for i, row in enumerate(data):
    for j, val in enumerate(row):
        data[i][j] = int(val.replace(val, str(alphabet.index(val))))


print(f"Width {len(data[0])}, height {len(data)}")
X = np.arange(1, len(data[0])+1)
Y = np.arange(1, len(data)+1)
X, Y = np.meshgrid(X, Y)
z = np.array(data)


fig = plt.figure()
ax = plt.axes(projection='3d')

surf = ax.plot_surface(X, Y, z, rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
ax.set_title('Surface plot')
plt.show()
