# Wilcoxon Signed Rank Test

Implementation of Wilcoxon signed rank test in python.

## Implementation

* In wilcoxon module wilcoxon_test function is implemented which calculated correlation rank
* In main module input file is read and best match is calculated as per requirement

## Execution

* To execute, use command 'python main.py'.
* Below message appears where you are asked to enter filename, enter csv filename which contains input data. I have added few files with different number of columns. 
![step_1.JPG](https://github.com/kulkarnisuraj92/wilcoxon-signed-rank-test/blob/master/images/step_1.JPG)
* After entering filename, details are shown such as header, key and non-key columns. 
![step_2.JPG](https://github.com/kulkarnisuraj92/wilcoxon-signed-rank-test/blob/master/images/step_2.JPG)
* Then best matching non-key product is determined based upon correlation rank of all pairs.
![step_3.JPG](https://github.com/kulkarnisuraj92/wilcoxon-signed-rank-test/blob/master/images/step_3.JPG)
* All possible combinations between non-key products are determined and displayed. Correlation rank with respect to key product is calculated for all these combinations and best combination is determined.
![step_4.JPG](https://github.com/kulkarnisuraj92/wilcoxon-signed-rank-test/blob/master/images/step_4.JPG)