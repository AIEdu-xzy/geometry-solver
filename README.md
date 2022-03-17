# geometry_solver

geometry_solver is a deep reinforcement learning agent for geometry reasoning.

## environment setup

First, you need to install python>=3.6. Then install dependancy using following comand:

```
pip install -r requirements.txt
```


## Training

To train the DRL agnet, you can simply enter: 

```
python rl_trainer.py
```

There are several options can be specified:
```
--algorithm: reinforcement algorithm.
--training_episode: Total training epoches.
--learning_rate
--gamma
--sample_num: number of samples taken by agent.
--test_num
--device: cpu or cuda
--show_process_bar
--log_interval
--epsilon
--target_replace_iter
--memory_capacity
--curriculum_learning: using curriculum learning
```

## Evaluate

```
python run_test.py -- num 100
```

