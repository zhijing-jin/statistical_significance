
Scientific publications require [statistical significance tests](https://en.wikipedia.org/wiki/Statistical_significance) when reporting experiment results. However, the exact way to calculate it is usually very confusing for many people. 

This repo will introduce how to **calculate statistical significance for deep learning experiments**, although the key ideas are also applicable to other scenarios.

### Calculation of Statistical Significance
Suppose we have 
- a baseline (i.e., model 1), 
- our proposed model (i.e., model 2), and
- a test set of N instances.

#### Step 1: Record the correctness of each model's prediction on each test instance.

- Correctness of model 1: `result1 = [True, False, True, False, False, False ]`

    In this case, test set has N=7 instances, model 1 is correct on the 1st and 3rd instance, and wrong on all others.
- Correctness of model 2: `result2 = [True, True, True, False, False, False ]` 

    On the same test set, model 2 is correct on 1st, 2nd, and 3rd instances, and wrong on all others.

#### Step 2: Use Scipy to calculate statistical significance
We set the threshold p-value `P_VALUE_THRES=0.05`. Reasonable p-values include `0.01`, `0.05`, `0.1`. 

```python
from scipy import stats
import numpy as np

result1 = [True, False, True, False, False, False ]
result2 = [True, True, True, False, False, False ]

P_VALUE_THRES=0.05

score, p_value = stats.ttest_ind(result1, np.array(result2), equal_var=False)
if_significantly_different = p_value <= P_VALUE_THRES
```

#### Step 3: Report Statistical Significance
If `if_significantly_different` is True, then you can report "our proposed model shows a **significant** improvement over the baseline model."

Or in your results table, you can put an asteriod near your reported result, for example, 86.7*. 

### Use of the code
```
from stat_sign import if_significantly_different

# result1, result2 are two lists, or 1-dimensional arrays

if_sign = if_significantly_different(result1, result2)

# if_sign is a True-or-False value
```
### References
Scipy's doc on the [independent T-Test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html): 





