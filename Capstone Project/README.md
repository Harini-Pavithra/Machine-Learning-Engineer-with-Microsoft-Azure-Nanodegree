# Heart Failure Predictions Using Microsoft Azure

This project is part of the Udacity Azure ML Nanodegree.In this project, we will work with the Heart Failure Clinical Records Dataset. we will use Azure to configure a cloud-based machine learning production model and deploy it. we use Hyper Drive and Auto ML methods to develop the model.Then the model with higest accuary is retrieved(voting ensemble in this case) and deployed in cloud with Azure Container Instances(ACI),also by enabling the authentication.

## Dataset

### Overview

This Dataset is available publicy in [Kaggle](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data)

Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worlwide.
Heart failure is a common event caused by CVDs and this dataset contains 12 features that can be used to predict mortality by heart failure.

Most cardiovascular diseases can be prevented by addressing behavioural risk factors such as tobacco use, unhealthy diet and obesity, physical inactivity and harmful use of alcohol using population-wide strategies.

People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.

### Task

In this project,we train a model to predict whether the person with Cardiovascular disease will survive or not.

### Access

In order to access the dataset, I used 2 different methods for 2 different models.

### HyperDrive

For the moodel,trained with HyperDrive functionalities,the dataset is saved in one of the public respositories and loaded with the help of TabularDataset.

### AutoML

For the model trained with AutoML functionalities, the dataset is registered with the help of "from local files" option and loaded from Azure workspace. 

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
