# CodeAI_EDA-and-ML-task
Repo for CodeAI task  

`dataset.csv`: this is the main dataset provided to us    

`primary-eda`: this file contains the fundamental EDA done on the dataset.    

`dataset02.csv` : this is the second dataset with which regression model is trained.    

`regression_model`: this is the file in which regression model is trained and compared  

# Models Used  

`LinearRegression` : With average cross validation score = 0.60023  

`RidgeRegression` : With average cross validation score = 0.61311  

`LassoRegression` : With average cross validation score = 0.60405   

> **NOTE:** Colums like `instant`, `dteday`, `registered`, `casaul` were dropped during training, as they were giving unusual cross validation scoress and R2 scores
