def if_significantly_different(result1: list, result2: list, P_VALUE_THRES=0.05):
    from scipy import stats
    import numpy as np

    score, p_value = stats.ttest_ind(result1, np.array(result2), equal_var=False)
    if_sign = p_value <= P_VALUE_THRES
    return if_sign
