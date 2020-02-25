# multiple-linear-regression 

## Assumption of a linear Regression 
1. Linearity 
2. Homoscedasticity 
3. Multivariate normality 
4. Independence of errors 
5. Lack of multicollinearity 

## What is a P value 
- P values are used to determine whether the results of their experiement are within the normal range of values for the event being observed. 
- If p-value of a data set is below a pre-determined amount (significance level), "null hypothesis" will be rejected. For instance, you won't belive the prediction if it is lower than the pre-determined amount. 

## Bulding a model 
- Why can't we have all variables in our model? 

`We need to clean out the model that is reliable & we need to be able to explain the variables are how is certain variables predict the behavior(dependent variable)`

- Stepwise Regression 

`Backward Elimination , Forward Selection, and Bidirectional Elimination. Bidirectional Elimination is the most general approach of Stepwise regression`

### 1. All-in 
- Throw in all variable if you have "prior knowledge"
- All-in is used to prepare for backward elimination 

### 2. Backward Elimination 
- This is the fastest out of all methods 
- Step 1: Select significance level to stay in the model (e.g. 0.05)
- Step 2: Fit the full model with all possible predictors (all variables)
- Step 3: Consider the predictor with the **highest** P-value. If P > SL, go to STEP 4. otherwisde go to finish 
- Step 4: Remove the predictor 
- Step 5: Fit model without this variable 
- Once a variable is removed, we need to rebuild the lienar regression because the value is changed. 
- Step 3 - 5 is repeated til P is less than SL.

### 3. Forward Selection
-  This is a large procedure 
- Step 1: Select a significance level to enter the model (e.g. 0.05)
- Step 2: Fit all simple regression models y ~ Xn. Select the one with the lowest P-value
- Step 3: Keep this variable and fit all possible models with one extra predictor added to the one(s) you already have 
- Step 4: Consider the predictor with the **lowest** P-value. P < SL, go to STEP 3, otherside go to finish. 

### 4. Bidirectional Elimination 
- Conbination of Backward Elimination and forward Selection 
- Most tedious methods because we are repeating doing Backward and Forward
- Step 1: Select a significance level to enter and to stay in the model (s.g. SLENTER = 0.005 SLSTAY=0.05)
- Step 2: Preform the next step of Forward Selection (new variables must be P < SLENTER to enter)
- Step 3: Perform ALL teps of Backward Elimination (old variables must have P < SLSTAY to stay)
- Repeat step 2 and 3 
- Step 4: No new variables can enter and no old variables can exit

### Score Comaprison (All possible models )
- Step 1: Select a criterion of goodness of fit (e.g. Akaike criterion)
- Step 2: Contruct All Possible Regression Models: 2^n - 1 of total combinations
- Step 3: Select the one with best criterion 
- If we have 10 columns it is equivalent to 1023 models 



### Credit: https://www.superdatascience.com/pages/machine-learning