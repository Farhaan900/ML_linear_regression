## Linear regression from scratch


This script uses gradient descent to calculate weights for each attribute in the dataset.

Execution stops when the change in error is equal to or less than the threshold.

To run the code, give the following command
```{r, engine='python', count_lines}
linearregr.py --data <PathToData> --learningRate <LearningRate> --threshold <Threshold
```

Two data sets are given named random.csv and yacht.csv which can be used in this program

For example, the script can be run as follows 
```{r, engine='python', count_lines}
linearregr.py --data yacht.csv --learningRate 0.0001 --threshold 0.0001
```

Output will be stored in a csv file mentioned at the end of execution