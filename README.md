# CodeAI_EDA-and-ML-task
Repo for CodeAI task  

`dataset.csv`: this is the main dataset provided to us    

`primary-eda`: this file contains the fundamental EDA done on the dataset.    

`dataset02.csv` : this is the second dataset with which regression model is trained.    

`regression_model`: this is the file in which regression model is trained and compared  

# Models Used  

`LinearRegression` : R2 Score: 0.8565676064919518 (while predicting directly `cnt`)

`RidgeRegression` : R2 Score:  0.8565611384382965 (while predicting directly `cnt`)

`LassoRegression` : R2 score:  0.8564998234510169 (while predicting directly `cnt`)

> **NOTE:** Colums like `instant`, `dteday`, `registered`, `casaul` were dropped during training, as they were giving unusual cross validation scoress and R2 scores


# Reason For model choice  
For the task. Linear Regression was used and then it was regularised using Ridge Regression, the reason behind Ridge regression is:-  
1. Ridge regression minimizes the cost function MSE(theta) by adding a regularization term
2. It reduces the coefficients for least related column with the target value
3. Before using Ridge Regression, the dataset were scaled as, these regularized models are sensitive to scale of input features
4. Also, the dataset is comparitively smaller with 731 rows and 16 columns, so using other regressors like RandomForest or GradientBoosting would increase the chances of model being overfit (though this can be avoided by fine tuning the hyperparameters)
5. Ridge Regression is chosen because it is better for small dataset like this and easy to implement.
6. Despite the R2 score of Linear Regression being more than RidgeRegression while directly predicting the `cnt`, Still RidgeRegression was chosen because it has Cross Validation score of 0.61311 where as Linear Regression has 0.60023

# Tuning Performed on Hyperparameters like alpha in case of RidgeRegression  
It is important to select perfect value of alpha so that the model performs well, so for that RidgeCV was performed on a list of alpha values ranging from 2.1 to 4.0.  

# Brownie Points  
1. Initially, the Ridge Regression model predict directly the `cnt` values with R2 score of 0.85656114 with `alpha = 2.7` and using `solver = cholesky`.
2. Then, two seperate Ridge models were created to predict the `casual ` rents and `registered` rents, the casual model gave R2 of 0.78936634 and the registered model gave R2 of 0.97004162.
3. Then using the predictions from both these models, `cnt_predictions` series was created by adding `reg_predictions` and `cas_predictions`.
4. Then when R2 was evaluated using `cnt_r2 = r2_score(y_test_cnt, cnt_predictions)` it was 0.9999998, this is because, in the dataset `cnt` is just the mathematical sum of `registered` and `casual` counts.
> **NOTE**: `alpha` for predicting casual counts and registered counts were different `4.0 and 3.8` respectively only to keep R2 < 1 for final count predictions after summing up. 
