from scipy import stats

for i in range(0, data.shape[0]):
    ttest = ttest_ind(tumor_data.iloc[i], normal_data.iloc[i], equal_var = False)
    pvalue.append(ttest[1])
pvalue = np.array(pvalue)


def ANOVA(dk1, dk2):
    pvalues = []
    for i in range(normadata.shape[0]):
        a = db1.iloc[i].values
        b = db2.iloc[i].values
        f, p=stats.f_oneway(
                   a[~np.isnan(a)], b[~np.isnan(b)])
        pvalues.append(p)
    pvalues = np.array(pvalues)
    return pvalues
    
def BHfdr(pvalues):
    pvalues = np.array(pvalues)
    rk = np.argsort(np.argsort(pvalues))
    qvalues0 = pvalues * len(pvalues) / (rk + 1)
    print(qvalues0)
    qvalues = np.zeros(len(pvalues))
    qvalues[np.argwhere(rk == 0)[0, 0]] = qvalues0[np.argwhere(rk == 0)[0, 0]]
    qvalues[np.argwhere(rk == (len(rk) - 1))[0, 0]] = qvalues0[np.argwhere(
        rk == (len(rk) - 1))[0, 0]]
    for j in range(len(pvalues) - 2, 0, -1):
        qvalues[np.argwhere(rk == j)] = min(qvalues0[np.argwhere(rk == j)][0, 0],
                             qvalues[np.argwhere(rk == (j + 1))][0, 0])
    return qvalues 
