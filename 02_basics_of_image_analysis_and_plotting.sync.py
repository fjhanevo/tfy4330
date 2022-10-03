# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import matplotlib.pyplot as plt
import numpy as np
import tifffile
from scipy.ndimage import rotate

# %% [markdown]
# ## Henter bilder og beskjærer dem

# %%
bildedata0 = plt.imread("bilde0.tif")
bildedata1 = plt.imread("bilde1.tif")
bildedata2 = plt.imread("bilde2.tif")

bildedata0_c = bildedata0[875:1170, 400:1600]
bildedata1_rotate = rotate(bildedata1,90)
bildedata1_c_rotate = bildedata1_rotate[850:1200, 150:1600]
bildedata2_rotate = rotate(bildedata2, 45)
bildedata2_c_rotate = bildedata2_rotate[1100:1500, 550:2200]

# %% [markdown]
# ## Skalering av data
# %%
tif0 = tifffile.TiffFile("bilde0.tif")
tif1 = tifffile.TiffFile("bilde1.tif")
tif2 = tifffile.TiffFile("bilde2.tif")

# %%
skala0 = tif0.fei_metadata['EScan']['PixelWidth']
skala1 = tif1.fei_metadata['EScan']['PixelWidth']
skala2 = tif2.fei_metadata['EScan']['PixelWidth']

# %% [markdown]
# ## Lager plot med alle bildene
# %%
fig, axarr = plt.subplots(3,1)

extent0 = [0, skala0 * bildedata0_c.shape[1] * 10**6, 0 , skala0 * bildedata0_c.shape[0] * 10**6]
extent1 = [0, skala1 * bildedata1_c_rotate.shape[1] * 10**6, 0 , skala1 * bildedata1_c_rotate.shape[0] * 10**6]
extent2 = [0, skala2 * bildedata2_c_rotate.shape[1] * 10**6, 0 , skala2 * bildedata2_c_rotate.shape[0] * 10**6]

# %%
ax0 = axarr[0]
ax1 = axarr[1]
ax2 = axarr[2]

# %%
ax0.imshow(bildedata0_c, extent=extent0)
ax1.imshow(bildedata1_c_rotate, extent=extent1)
ax2.imshow(bildedata2_c_rotate, extent=extent2)

# %%
plt.savefig("bilde.jpg")
fig

# %% [markdown]
# ## Legge til en skalebar
# %%
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import matplotlib.font_manager as fm
import matplotlib.patheffects as patheffects
fontprops = fm.FontProperties(size=18)
# %%
scalebar_kwargs = {'size': 5, 'label': '5 um', 'loc': 4, 'frameon': False, 'color': 'white', 'size_vertical': 0.2, 'label_top': False, 'fontproperties': fontprops}
scalebar0 = AnchoredSizeBar(transform=ax0.transData, **scalebar_kwargs)
scalebar0.txt_label._text.set_path_effects([patheffects.withStroke(linewidth=2, foreground='black', capstyle="round")])
ax0.add_artist(scalebar0)
# %%
scalebar1 = AnchoredSizeBar(transform=ax1.transData, **scalebar_kwargs)
scalebar1.txt_label._text.set_path_effects([patheffects.withStroke(linewidth=2, foreground='black', capstyle="round")])
ax1.add_artist(scalebar1)
# %%
scalebar2 = AnchoredSizeBar(transform=ax2.transData, **scalebar_kwargs)
scalebar2.txt_label._text.set_path_effects([patheffects.withStroke(linewidth=2, foreground='black', capstyle="round")])
ax2.add_artist(scalebar2)
# %% [markdown]
# ## Legg til annoteringer
# %%
ax0.annotate('a', xy=(0,0), xycoords='axes fraction', fontsize=50, color="red")
ax1.annotate('b', xy=(0,0), xycoords='axes fraction', fontsize=50, color="red")
ax2.annotate('c', xy=(0,0), xycoords='axes fraction', fontsize=50, color="red")
# %%
ax0.annotate('1', xy=(1,0), xycoords='axes fraction', fontsize=50, color="red")
ax1.annotate('2', xy=(1,0), xycoords='axes fraction', fontsize=50, color="red")
ax2.annotate('3', xy=(1,0), xycoords='axes fraction', fontsize=50, color="red")
# %%
ax0.set_xticks([])
ax0.set_yticks([])
ax1.set_xticks([])
ax1.set_xticks([])
ax2.set_yticks([])
ax2.set_yticks([])
# %%
fig.subplots_adjust()
fig.set_figwidth(20)
fig.set_figheight(20)

fig.get_figwidth()
fig.get_figheight()



# %%
fig.savefig("bilde.jpg",dpi=300)
fig

# %%
