from sklearn.tree import DecisionTreeRegressor, export_graphviz
from sklearn.model_selection import cross_val_score
import csv
import numpy as np


data = np.loadtxt("/Users/francois/Documents/Neuropoly/Atef/Data_all_53_SPSS_final.csv",delimiter=",", skiprows=1)

names = ["PWV1","FA_CC","RD_CC","FA_CI","RD_CI","FA_CR","RD_CR","FA_SLF","RD_SLF"]

X = data[:,1]

for i in range(2,len(names)+1):
    name = names[i-1]
    Y = data[:,i]
    tree = DecisionTreeRegressor(criterion='mse', splitter='best', max_depth=1, min_samples_split=2, min_samples_leaf=1, max_leaf_nodes=None, min_impurity_decrease=0.0, presort=False)
    # scores = cross_val_score(tree, X.reshape(-1,1), Y, cv=10, scoring="neg_mean_squared_error")
    tree.fit(X.reshape(-1,1),Y)
    print name
    export_graphviz(tree, out_file="./PWV1_{}_tree.dot".format(name), feature_names=[names[0]], label="all", precision=5)
    #print "cv scores", scores
    print
    print "------------------------------"
