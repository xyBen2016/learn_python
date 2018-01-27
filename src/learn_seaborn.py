# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
#
#
# data = pd.read_csv("C:/Users/Administrator/Desktop/b.csv")
# sns.set(style="darkgrid")
#
# g = sns.factorplot(x="severity", data=data, kind="count",
#                    palette="BuPu", size=6, aspect=1.5)
# sns.plt.show()


# """Facetting histograms by subsets of data"""
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set(style="darkgrid")
#
# tips = sns.load_dataset("tips")
# g = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)
# bins = np.linspace(0, 60, 13)
# g.map(plt.hist, "total_bill", color="steelblue", bins=bins, lw=0)
# sns.plt.show()

"""Barplot timeseries"""
# import numpy as np
# import seaborn as sns
# sns.set(style="white")
#
# # Load the example planets dataset
# planets = sns.load_dataset("planets")
#
# # Make a range of years to show categories with no observations
# years = np.arange(1996, 2015)
#
# # Draw a count plot to show the number of planets discovered each year
# g = sns.factorplot(x="year", data=planets, kind="count",
#                    palette="BuPu", size=6, aspect=1.5, order=years)
# g.set_xticklabels(step=2)
# sns.plt.show()

"""Color palette choices"""
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set(style="white", context="talk")
# rs = np.random.RandomState(7)
#
#
# # Set up the matplotlib figure
# f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6), sharex=True)
#
# # Generate some sequential data
# x = np.array(list("ABCDEFGHI"))
# y1 = np.arange(1, 10)
# sns.barplot(x, y1, palette="BuGn_d", ax=ax1)
# ax1.set_ylabel("Sequential")
#
# # Center the data to make it diverging
# y2 = y1 - 5
# sns.barplot(x, y2, palette="RdBu_r", ax=ax2)
# ax2.set_ylabel("Diverging")
#
# # Randomly reorder the data to make it qualitative
# y3 = rs.choice(y1, 9, replace=False)
# sns.barplot(x, y3, palette="Set3", ax=ax3)
# ax3.set_ylabel("Qualitative")
#
# # Finalize the plot
# sns.despine(bottom=True)
# plt.setp(f.axes, yticks=[])
# plt.tight_layout(h_pad=3)
#
# sns.plt.show()


"""Anscombe’s quartet"""
# import seaborn as sns
#
# sns.set(style="ticks")
#
# # Load the example dataset for Anscombe's quartet
# df = sns.load_dataset("anscombe")
#
# # Show the results of a linear regression within each dataset
# sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
#            col_wrap=2, ci=None, palette="muted", size=4,
#            scatter_kws={"s": 50, "alpha": 1})
#
# sns.plt.show()

""""""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats, integrate

# data = np.random.rand(75)
# plt.hist(data)
# sns.plt.show()


# sns.set(style="whitegrid")
#
# # Initialize the matplotlib figure
# f, ax = plt.subplots(figsize=(6, 15))
#
# # Load the example car crash dataset
# crashes = sns.load_dataset("E:/xy/test/pythom_install/seaborn-data-master/car_crashes") \
#     .sort_values("total", ascending=False)

# Plot the total crashes
# sns.set_color_codes("pastel")
# sns.barplot(x="total", y="abbrev", data=crashes,
#             label="Total", color="b")

# Plot the crashes where alcohol was involved
# sns.set_color_codes("muted")
# sns.barplot(x="alcohol", y="abbrev", data=crashes,
#             label="Alcohol-involved", color="b")

# sns.set_color_codes("colorblind")
# sns.barplot(x="speeding", y="abbrev", data=crashes,
#             label="speeding-involved", color="b")
#
# sns.set_color_codes("colorblind")
# sns.barplot(x="not_distracted", y="abbrev", data=crashes,
#             label="not_distracted", color="b")
#
# sns.set_color_codes("colorblind")
# sns.barplot(x="no_previous", y="abbrev", data=crashes,
#             label="no_previous", color="b")
#
# sns.set_color_codes("colorblind")
# sns.barplot(x="not_distracted", y="abbrev", data=crashes,
#             label="not_distracted", color="b")
#
# sns.set_color_codes("colorblind")
# sns.barplot(x="ins_losses", y="abbrev", data=crashes,
#             label="ins_losses", color="b")


# Add a legend and informative axis label
# ax.legend(ncol=2, loc="lower right", frameon=True)
# ax.set(xlim=(0, 24), ylabel="",
#        xlabel="Automobile collisions per billion miles")
# sns.despine(left=True, bottom=True)
# sns.plt.show()

# a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# x = [int(s) for s in a]
# x = [11, 11, 11, 11, 11, 11, 11, 11, 26, 25, 34, 98, 98, 98, 98, 98, 98]
# print(x)
# sns.distplot(x)
# http://192.168.1.101:8888/login
# 92356f7818d6c69e688e58f987d460d768b4a0c6be3432c1

# x = [-2.04713616, -1.64185099, -1.23656582, -0.83128065, -0.42599548,
#         -0.02071031,  0.38457486,  0.78986003,  1.1951452 ,  1.60043037,
#          2.00571554]
# sns.distplot(x)
# sns.plt.show()

# sns.set(rc={"figure.figsize": (6, 6)})
# np.random.seed(sum(map(ord, "palettes")))

# np.random.seed(sum(map(ord, "aesthetics")))
# def sinplot(flip=1):
#     x = np.linspace(0, 14, 100)  #0开始，14结束，100数量
#     for i in range(1, 7):  # 6根正弦线
#         plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

"""Visualizing the distribution of a dataset"""

# sns.set(color_codes=True)
# np.random.seed(sum(map(ord, "distributions")))
# x = np.random.normal(size=100)

"""Kernel density estimaton"""
# sns.distplot(x, hist=False, rug=True);


""""""
# sns.distplot(x, bins=20, kde=False, rug=True);

"""Histograms"""
# sns.distplot(x, kde=False, rug=True);

"""Plotting univariate distributions"""

# sns.distplot(x);
# sns.plt.show()


"""Choosing color palettes"""
"""Building color palettes with color_palette()"""
# current_palette = sns.color_palette()
# sns.palplot(current_palette)
# sns.palplot(sns.color_palette("hls", 8))
# sns.palplot(sns.hls_palette(8, l=.3, s=.8))
# sns.palplot(sns.color_palette("husl", 8))
# sns.palplot(sns.color_palette("Paired"))
# sns.palplot(sns.color_palette("Set2", 10))
# flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
# sns.palplot(sns.color_palette(flatui))
# plt.plot([0, 1], [0, 1], sns.xkcd_rgb["pale red"], lw=3)
# plt.plot([0, 1], [0, 2], sns.xkcd_rgb["medium green"], lw=3)
# plt.plot([0, 1], [0, 3], sns.xkcd_rgb["denim blue"], lw=3);
# colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
# sns.palplot(sns.xkcd_palette(colors))
# sns.palplot(sns.color_palette("Blues"))
# sns.palplot(sns.color_palette("BuGn_r"))
# sns.palplot(sns.color_palette("GnBu_d"))
# sns.palplot(sns.color_palette("cubehelix", 8))
# sns.palplot(sns.cubehelix_palette(8))
# sns.palplot(sns.cubehelix_palette(8, start=.5, rot=-.75))
# sns.palplot(sns.cubehelix_palette(8, start=2, rot=0, dark=0, light=.95, reverse=True))
# x, y = np.random.multivariate_normal([0, 0], [[1, -.5], [-.5, 1]], size=300).T
# cmap = sns.cubehelix_palette(light=1, as_cmap=True)
# sns.kdeplot(x, y, cmap=cmap, shade=True);
# sns.palplot(sns.light_palette("green"))
# sns.palplot(sns.dark_palette("purple"))
# sns.palplot(sns.light_palette("navy", reverse=True))
# pal = sns.dark_palette("palegreen", as_cmap=True)
# sns.kdeplot(x, y, cmap=pal);
# sns.palplot(sns.light_palette((210, 90, 60), input="husl"))
# sns.palplot(sns.dark_palette("muted purple", input="xkcd"))
# sns.palplot(sns.color_palette("BrBG", 7))
# sns.palplot(sns.color_palette("RdBu_r", 7))
# sns.palplot(sns.color_palette("coolwarm", 7))
# sns.palplot(sns.diverging_palette(220, 20, n=7))
# sns.palplot(sns.diverging_palette(145, 280, s=85, l=25, n=7))
# sns.palplot(sns.diverging_palette(10, 220, sep=80, n=7))


"""Scaling plot elements with plotting_context() and set_context()"""
# sns.set()  # reset the default parameters
# # sns.set_context("paper")
# # sns.set_context("talk")
# sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
# # plt.figure(figsize=(8, 6))
# sinplot()
# sns.plt.show()


"""Styling figures with axes_style() and set_style()"""
# sns.set_style("darkgrid", {"axes.facecolor": ".9"})
# sinplot()
# sns.plt.show()
# {'axes.axisbelow': True,
#  'axes.edgecolor': '.8',
#  'axes.facecolor': 'white',
#  'axes.grid': True,
#  'axes.labelcolor': '.15',
#  'axes.linewidth': 1.0,
#  'figure.facecolor': 'white',
#  'font.family': [u'sans-serif'],
#  'font.sans-serif': [u'Arial',
#   u'Liberation Sans',
#   u'Bitstream Vera Sans',
#   u'sans-serif'],
#  'grid.color': '.8',
#  'grid.linestyle': u'-',
#  'image.cmap': u'Greys',
#  'legend.frameon': False,
#  'legend.numpoints': 1,
#  'legend.scatterpoints': 1,
#  'lines.solid_capstyle': u'round',
#  'text.color': '.15',
#  'xtick.color': '.15',
#  'xtick.direction': u'out',
#  'xtick.major.size': 0.0,
#  'xtick.minor.size': 0.0,
#  'ytick.color': '.15',
#  'ytick.direction': u'out',
#  'ytick.major.size': 0.0,
#  'ytick.minor.size': 0.0}

""""""
# with sns.axes_style("darkgrid"):
#     plt.subplot(211)
#     sinplot()
# plt.subplot(212)
# sinplot(-1)

"""去除边框"""
# data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
# sns.set_style("whitegrid")
# sns.boxplot(data=data, palette="deep")
# sns.despine(left=True)
# sns.plt.show()

"""去除边框指针"""
# sns.despine()

"""seaborn有五个主题：darkgrid（默认）, whitegrid, dark, white, ticks."""
# sns.set_style("ticks")  # 白色网格背景
# # sns.set_style("whitegrid")  # 白色网格背景
# # sns.set_style("dark")  # 灰暗色背景
# data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
# sns.boxplot(data=data)
# sns.plt.show()

"""正弦，seaborn图和matplotlib图的区别"""
# sinplot()
# sns.plt.show()  # 使用seaborn展示sin图
# plt.show()  # 使用matplotlib展示sin图
