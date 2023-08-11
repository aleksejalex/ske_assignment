import matplotlib.pyplot as plt
from sksurv.datasets import load_breast_cancer
from sksurv.preprocessing import OneHotEncoder
from sksurv.linear_model import CoxnetSurvivalAnalysis

X, y = load_breast_cancer()
X = OneHotEncoder().fit_transform(X)

estimator = CoxnetSurvivalAnalysis(l1_ratio=0.99, fit_baseline_model=True)
estimator.fit(X, y)

chf_funcs = {}
for alpha in estimator.alphas_[:5]:
    chf_funcs[alpha] = estimator.predict_cumulative_hazard_function(
        X.iloc[:1], alpha=alpha)


for alpha, chf_alpha in chf_funcs.items():
    for fn in chf_alpha:
        plt.step(fn.x, fn(fn.x), where="post",
                 label=f"alpha = {alpha:.3f}")

plt.ylim(0, 1)
plt.legend()
plt.show()