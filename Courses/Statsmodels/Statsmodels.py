#!/usr/bin/env python
# coding: utf-8

# # Linear models: statsmodels, sklearn and sympy
# 
# ***
# > __Auteur__: Joseph Salmon
# > <joseph.salmon@umontpellier.fr>

# # Statsmodels and least-squares
# Beware: to usethe "R" syntax in statsmodel, install patsy, version > '0.5.1'

# %%
import patsy
patsy.__version__


# %%

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import t
from sklearn import linear_model
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from download import download

# %%


url = "http://josephsalmon.eu/enseignement/datasets/arbres.txt"
path_target = "./arbres.txt"
download(url, path_target, replace=False)


# %%


df_arbres = pd.read_csv("arbres.txt", sep=' ')
df_arbres.columns


# Aide disponible ici pour le package statsmodels (avec la syntaxe de R):
# http://www.statsmodels.org/devel/example_formulas.html

# %%


results = smf.ols('vol ~ aire', data=df_arbres).fit()
results.summary()


# %%


results.params


# %%


xlim = [0, 900]
ylim = [0, 0.5]
df_out = pd.DataFrame(columns=["aire"],
                       data=np.arange(0.9 * df_arbres['aire'].min(),
                       1.1 * df_arbres['aire'].max(), step=10))


# %%

plt.figure()
plt.scatter(df_arbres['aire'], df_arbres['vol'], label='Données')
plt.xlabel('Aire')
plt.ylabel('Volume')
plt.plot(df_out, results.prdf_outedict(df_out), '--', label='OLS')
plt.xlim(xlim)
plt.ylim(ylim)

plt.legend();
plt.show()


# %%


predictions = results.get_prediction(df_out)
predictions.summary_frame(alpha=0.05)


# %%


alpha=0.05
df_predictions = predictions.summary_frame(alpha=alpha)


# %%


# Computing prediction interval by hand:
n_samples, _ = df_arbres.shape
t_alpha = t.ppf(1 - alpha / 2, n_samples - 2)
sigmahat = np.sqrt(np.sum(results.resid ** 2) / (n_samples - 2))
meanX = (np.array(df_arbres['aire'].mean(axis=0), dtype=pd.Series))
varX = (np.array(df_arbres['aire'].var(axis=0), dtype=pd.Series))
sigmapred_hat = (sigmahat**2 * (varX +
                                (df_out['aire'] - meanX)**2) / (varX * n_samples))
sigmapred_hat = sigmapred_hat ** 0.5
IC_down = results.predict(df_out['aire']) - t_alpha * sigmapred_hat
IC_up = results.predict(df_out['aire']) + t_alpha * sigmapred_hat


# %%


plt.figure()
plt.scatter(df_arbres['aire'], df_arbres['vol'], label='Données')
plt.xlabel('Aire')
plt.ylabel('Volume')
plt.plot(df_out, results.predict(df_out), '--', label='OLS')

plt.plot(df_out, IC_down,'--',color='k',  linewidth=1,
        label="IC($1-\\alpha$), $\\alpha={}$".format(alpha))
plt.plot(df_out, IC_up,'--',color='k', linewidth=1, label='')

ax = plt.gca()

# Computing prediction interval using statmodels:

ax.fill_between(df_out.squeeze(),
                df_predictions['mean_ci_upper'].astype(float),
                df_predictions['mean_ci_lower'].astype(float), facecolor='blue', alpha=.2)


plt.xlim(xlim)
plt.ylim(ylim)

plt.legend();


# # `sklearn`: another least-squares syntax 

# %%


skl_linmod = linear_model.LinearRegression(fit_intercept=True)
# ATTENTION: sklearn a besoin d'une matrice de taille n x p (p ne peut pas être 0)
skl_linmod.fit(df_arbres[['aire']], df_arbres['vol'])


# %%


plt.figure(figsize=(8, 6))
plt.scatter(df_arbres['aire'], df_arbres['vol'], label='Données')
plt.xlabel('Aire')
plt.ylabel('Volume')
plt.xlim([0, 900])
plt.ylim([0, 0.5])
plt.plot(df_out, skl_linmod.predict(df_out), '--', label='OLS')
plt.legend();


# # Anova et calcul symbolique: forme de la matrice $(X^\top X)^{-1}$

# %%


import sympy as sym


# %%


sym.init_printing()

nF, nM, n = sym.symbols('n_F n_M n')
matrix = sym.Matrix([[n, nF],
                     [nF, nF]])
matrix


# %%


sol = matrix.inv()
sol


# %%


sol=sym.simplify(sol)
sol


# %%


new_sol = sol.subs(n - nF, nM)
new_sol


# %%


new_sol = sol.subs(n, nM + nF)
XTXinv = new_sol.expand()
XTXinv


# # Cas muli-modalités de l'anova:

# %%


n0, n1, n2, n3, n4, n = sym.symbols('n0 n1 n2 n3 n4 n')
matrix4 = sym.Matrix([[n, n1, n2, n3, n4],
                      [n1, n1, 0, 0, 0],
                      [n2, 0, n2, 0, 0],
                      [n3, 0, 0, n3, 0],
                      [n4, 0, 0, 0, n4]]
                     )
matrix4


# %%


sol4 = sym.simplify(matrix4.inv())
sol4


# %%


new_sol4 = sol4.subs(n, n0 + n1 + n2 + n3 + n4)
new_sol4.expand()


# %%


# %%

# %%
