import inspect
import numpy as np
import scipy as scp
import pandas as pd
import seaborn as sbn
import csv
import matplotlib as mpt
import statsmodels
import statsmodels.formula.api as sm
from matplotlib import pyplot as plt
import reliability as rel
import lifelines


print('\\begin{tabular}{lrrrr}\n\\toprule\n & Log-likelihood & AICc & BIC & AD \\\\\n\\midrule\ncount & 15.00 & 15.00 & 15.00 & 15.00 \\\\\nmean & -126.56 & 259.12 & 261.96 & 4.36 \\\\\nstd & 7.95 & 14.78 & 14.51 & 1.12 \\\\\nmin & -147.79 & 247.71 & 250.99 & 3.44 \\\\\n25% & -126.35 & 252.05 & 255.70 & 3.62 \\\\\n50% & -125.30 & 255.04 & 257.39 & 4.00 \\\\\n75% & -121.90 & 257.14 & 259.50 & 4.53 \\\\\nmax & -118.04 & 300.02 & 302.38 & 6.90 \\\\\n\\bottomrule\n\\end{tabular}\n')



print('\\begin{tabular}{llllllllllllllrrrrl}\n\\toprule\n & Distribution & Alpha & Beta & Gamma & Alpha 1 & Beta 1 & Alpha 2 & Beta 2 & Proportion 1 & DS & Mu & Sigma & Lambda & Log-likelihood & AICc & BIC & AD & optimizer \\\\\n\\midrule\n0 & Gamma_3P & 270.72 & 0.50 & 4.00 &  &  &  &  &  &  &  &  &  & -120.39 & 247.71 & 250.99 & 3.78 & TNC \\\\\n0 & Weibull_3P & 106.13 & 0.61 & 4.00 &  &  &  &  &  &  &  &  &  & -120.93 & 248.79 & 252.07 & 3.66 & TNC \\\\\n0 & Weibull_Mixture &  &  &  & 56.57 & 1.10 & 389.96 & 116.37 & 0.76 &  &  &  &  & -118.04 & 248.57 & 253.08 & 3.59 & powell \\\\\n0 & Loglogistic_3P & 57.80 & 0.78 & 4.00 &  &  &  &  &  &  &  &  &  & -122.66 & 252.25 & 255.53 & 3.54 & TNC \\\\\n0 & Weibull_CR &  &  &  & 128.49 & 0.74 & 390.17 & 120.53 &  &  &  &  &  & -121.13 & 251.86 & 255.86 & 4.29 & TNC \\\\\n0 & Lognormal_2P &  &  &  &  &  &  &  &  &  & 4.13 & 1.39 &  & -124.59 & 253.62 & 255.98 & 3.60 & TNC \\\\\n0 & Exponential_1P &  &  &  &  &  &  &  &  &  &  &  & 0.01 & -126.91 & 255.97 & 257.23 & 4.76 & TNC \\\\\n0 & Loglogistic_2P & 60.37 & 1.19 &  &  &  &  &  &  &  &  &  &  & -125.30 & 255.04 & 257.39 & 3.63 & TNC \\\\\n0 & Lognormal_3P &  &  & 3.00 &  &  &  &  &  &  & 4.02 & 1.63 &  & -123.98 & 254.87 & 258.15 & 3.44 & TNC \\\\\n0 & Exponential_2P &  &  & 4.00 &  &  &  &  &  &  &  &  & 0.01 & -125.87 & 256.18 & 258.54 & 5.20 & TNC \\\\\n0 & Weibull_2P & 114.41 & 0.83 &  &  &  &  &  &  &  &  &  &  & -126.20 & 256.85 & 259.21 & 4.00 & TNC \\\\\n0 & Gamma_2P & 153.69 & 0.80 &  &  &  &  &  &  &  &  &  &  & -126.49 & 257.43 & 259.79 & 4.18 & TNC \\\\\n0 & Weibull_DS & 114.41 & 0.83 &  &  &  &  &  &  & 1.00 &  &  &  & -126.20 & 259.33 & 262.61 & 4.00 & TNC \\\\\n0 & Normal_2P &  &  &  &  &  &  &  &  &  & 112.97 & 119.09 &  & -141.89 & 288.23 & 290.58 & 6.81 & TNC \\\\\n0 & Gumbel_2P &  &  &  &  &  &  &  &  &  & 185.54 & 139.42 &  & -147.79 & 300.02 & 302.38 & 6.90 & TNC \\\\\n\\bottomrule\n\\end{tabular}\n')









