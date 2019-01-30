
Las Vegas Wrapper is one kind of wrapper methods which measure the "usefulness" of features based on the classifier performance. Las Vegas Wrapper searches for the best feature subsets using the Las Vegas method as its tool and error of the classifier as its measurement.

It goes like other wrapper methods:
```python
 set of all features.
repeat:
    randomly generete a subset
    use the subset to train a model
    evaluate the precision of the model
find the best subset
```


### Difference between Filter and Wrapper methods
 * Filter method measure the relevance of features while wrapper measure the usefulness of a feature subset
 * Filter method use statistical methods to evaluate while wrapper use cross validation
 * Filter are much faster.
 * Filter might fail, but wrapper can always win
 * Wrapper-best subset make the model more prone to overfitting.

### Ref
https://www.analyticsvidhya.com/blog/2016/12/introduction-to-feature-selection-methods-with-an-example-or-how-to-select-the-right-variables/