
# Optimizing an ML Pipeline in Azure

# Overview

This project is part of the Udacity Azure ML Nanodegree.In this project, we build and optimize an Azure ML pipeline using the Python SDK and a provided Scikit-learn model.This model is then compared to an Azure AutoML run.

# Summary

## Problem Statement:

The dataset (bankmarketing_train.csv) is a UCI Dataset, which contains data about direct marketing campaigns (phone calls) of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.we seek to predict if the client will subscribe a term deposit (variable y) or not. There are 21 features, 32.950 rows and target variable in total.Two Machine Learning models were built using this dataset.

The first model we built is trained with Logistic regression and HyperDrive parameters which are tuned with the help of Azure ML python SDK and HyperDrive tools(Azure HyperDrive functionalities).The best accuracy obtained from this model is 91.10%

The Second model we built is with the help of Azure AutoML for training many types of models such as LightGBM, XGBoostClassifier, RandomForest, VotingEnsemble, StackEnsemble etc.The best accuracy obtained from this model is 91.74%

## Best Model:

Therefore, the best performing model is Voting Ensemble of Xgboost classifier using standard scaler wrapper with accuracy 91.74%

# Scikit-learn Pipeline

## Pipeline Architecture:

Initially in the training script (train.py),the dataset (bankmarkerting_train.csv) is retrieved from the URL (https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv) provided using TabularDatasetFactory Class (Contains methods to create a tabular dataset for Azure Machine Learning). The data is then pre-processed and cleaned with the help of clean_data() function by converting the categorical data to one hot encoding(One hot encoding is a process by which categorical variables are converted into a form that could be provided to ML algorithms to do a better job in prediction).Then the data is being split as train and test with the ratio of 70:30.

## Classification Algorithm:

The classification algorithm used here is Logistic Regression (Logistic regression is a well-known method in statistics that is used to predict the probability of an outcome, and is especially popular for classification tasks. The algorithm predicts the probability of occurrence of an event by fitting data to a logistic function). Then the training(train.py) script is passed to estimator and HyperDrive configurations to predict the best model and accuracy.

The HyperDrive run is executed successfully with the help of parameter sampler, policy, estimator and HyperDrive Config, before that Azure workspace and experiment is created successfully. Then Compute cluster is created with "Standard_DV_V2" as virtual machine size and 4 as the maximum number of nodes as per the instructions. 

## HyperParameter Tuning:

The Hyperparameters are then tuned (Hyperparameters are adjustable parameters that let you control the model training process and Hyperparameter tuning is the process of finding the configuration of hyperparameters that results in the best performance) with the help of parameter sampler.Parameter sampling method is to use over the hyperparameter space(hyperparameter space is tuning hyperparameters by exploring the range of values defined for each hyperparameter).

## Benefits Of The Parameter Sampler:

Random Sampling is used here. In random sampling, hyperparameter values are randomly selected from the defined search space. It supports discrete and continuous hyperparameters.  It also supports early termination of low-performance runs. Random Sampling is used on ‘--C’
( Inverse of regularization parameter ) which is a control variable that retains strength modification of Regularization by being inversely positioned to the Lambda regulator and ‘--max_iter’  (Maximum number of iterations to converge) which defines the number of times we want the learning to happen and this helps in solving high complex problems with large training hours as per the instructions. 

For ‘--C’, the parameter is set as (0.1,1) and for ‘—max_iter’ the parameter is set as (50,100,150,200) which returns a value uniformly distributed between low and high.


## Benefits Of The Early Stopping Policy:

Then the policy is defined, early stopping policy is defined to automatically terminate poorly performing runs with an early termination policy.It also improves computational efficiency. Bandit policy is used here with slack_factor=0.1,evaluation_internal=1, delay_evaluation=5.Bandit terminates runs where the primary metric is not within the specified slack factor/slack amount compared to the best performing run.

The SKLearn estimator is created with the training script(train.py), directory path and cluster name, then the configurations for runs is created using HyperDriveConfig with estimator(created using SKLearn),hyperparameter sampling(Random Sampling), policy(Bandit policy) and also included primary metric(Accuracy),it’s goal (Maximize) , maximum total runs(10) and maximum concurrent runs(4).

Finally the experiment is being submitted and using the Notebook widget(RunDetails(hyperdrive_run).show()), it is visualized. Once the run is successfully completed or executed, the best model is retrieved and  saved in outputs folder in source directory.

Screenshots of outputs are available in HyperDrive folder.

# AutoML

AutoML also referred as Automated machine learning or automated ML, is the process of automating the time consuming, iterative tasks of machine learning model development. Automated ML is applied when you want Azure Machine Learning to train and tune a model for you using the target metric you specify.

Initially the dataset(bankmarketing_train.csv) is retrieved from the URL
(https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv) provided using TabularDatasetFactory Class(Contains methods to create a tabular dataset for Azure Machine Learning). The data is then pre-processed and cleaned with the help of clean_data() function and it is then split as train and test with the ratio of 70:30.

AutoMLConfig is then defined for successfully executing the AutoML run with experiment timeout as ‘30’ minutes as per instructions,task type as ‘Clssification’(Classification is a type of supervised learning in which models learn using training data, and apply those learnings to new data. Classification models is to predict which categories new data will fall into based on learnings from its training data) primary metric as ‘accuracy’, label column as ‘Y’ and n cross validations as ‘5’. The models used here are LightGBM, XGBoostClassifier, RandomForest, VotingEnsemble, StackEnsemble etc as already mentioned and It also uses different pre- processing techniques like Standard Scaling, Min Max Scaling, Sparse Normalizer, MaxAbsScaler.


Finally the experiment is being submitted and using the Notebook widget(RunDetails(automl_run).show()), it is visualized. Once the run is successfully completed or executed, the best model is retrieved and  saved in outputs folder in source directory.

Screenshots of outputs are available in AutoML folder.

## Pipeline comparison

HyperDrive’s best run accuracy = 91.10%

AutoML’s best run accuracy = 91.74%

Thus,there is only a very small difference between AutoML’s model and HyperDrive’s model. AutoML’s model is better then HyperDrive’s model.

AutoML run tried creating different models and also used Voting Ensemble which combines the predictions from multiple other models. It is a technique that may be used to improve model performance, ideally achieving better performance than any single model used in the ensemble. But in HyperDrive run,Logistic Regression is used so,multiple models can’t be created  for the pipeline.


## Future work

1. Different algorithms can be used for HyperDrive run so that we can find out best Hyperparameters.
2. Increasing the estimate timeout for autoML to find out best model with high accuaracy.
3. The dataset has Class Imbalance,which can reflect in model’s accuracy,that has to be treated.
4. Instead of Random Sampling can try out Grid and Bayesian Sampling for tuning Hyperparameters.

