import numpy as np

from utils import test_all_problems


avg_trial_hist = []
avg_before_prune_hist = []
avg_after_prune_hist = []

for _ in range(100):
    avg_trial, avg_before_prune, avg_after_prune = test_all_problems()
    avg_trial_hist.append(avg_trial)
    avg_before_prune_hist.append(avg_before_prune)
    avg_after_prune_hist.append(avg_after_prune)

print(avg_trial_hist)
print(avg_before_prune_hist)
print(avg_after_prune_hist)

print('Average trial times: {}±{}'.format(np.mean(avg_trial_hist), np.std(avg_trial_hist)))
print('Average solving step before prune: {}±{}'.format(np.mean(avg_before_prune_hist), np.std(avg_before_prune_hist)))
print('Average solving step after prune: {}±{}'.format(np.mean(avg_after_prune_hist), np.std(avg_after_prune_hist)))

