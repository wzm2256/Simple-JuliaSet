import numpy as np
import torch
import matplotlib.pyplot as plt

B = 2

# Several choices of c lead to different types of Julia sets.
# c = -0.75
c = np.complex(-0.391, -0.578)
# c = np.complex(-0.123, 0.754)
# c = -1.

# Other parameters
pixel = 6000
norm = 5
Iteration = 500

# Initialize..
x = np.linspace(-B, B, pixel)
y = np.linspace(-B, B, pixel)

xx, yy = np.meshgrid(x, y)
yy = yy[::-1, :]

xx = np.expand_dims(xx, -1)
yy = np.expand_dims(yy, -1)

Z_np = np.concatenate([xx, yy], axis=-1)


# Convert the computation to GPU using torch if possible.
# if you have a cuda-compatible GPU, uncomment the 2nd line below.
Z = torch.tensor(Z_np, device='cpu', dtype=torch.float, requires_grad=False)
# Z = torch.tensor(Z_np, device='cuda', dtype=torch.float, requires_grad=False)

Z = torch.view_as_complex(Z)

# Iteration teration
for i in range(Iteration):
    Z = Z * Z + c

Mask = torch.abs(Z).cpu().numpy() < norm
M = Mask.astype(np.int)

plt.imsave(str(c) + '.png', M, cmap='gray')