

### What is Perceptron?
Perceptron is a single layer neural network.
![image](./resources/perceptron.png)
all the input $x$ are multiplied with their weights $w$, then add all the multiplied values, the result is called **Weighted Sum**, finally the sum is applied to the **Activation Function**(such as sigmoid function)
the solution to the $w$ is $w _ { i } \leftarrow w _ { i } + \Delta w _ { i }$, and $\Delta w _ { i }$ is $ \eta ( y - \hat { y } ) x _ { i }$
### Code from scratch
see `perceptron.py`

### Perceptron vs SVM
For linear seperable input:

 * perceptron algorithm will find more than one separating line, and the exact line obtained through a run of the the perceptron algorithm depends on the learing process and variables. and for svm, there is only one seperating-line.
 * perceptron is an online algorithm, it can process the data points one by one. On the other hand, SVM needs all the training data before the classifier building start.
 * SVM finds the largest margin, which will help you classify the test data better.
