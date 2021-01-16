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

AutoML also referred as Automated machine learning or automated ML, is the process of automating the time consuming, iterative tasks of machine learning model development. Automated ML is applied when you want Azure Machine Learning to train and tune a model for you using the target metric you specify.

Initially the dataset(Heart_Failure_Clinical_Records_Dataset.csv) is registered with the help of "from local files" option and loaded from Azure workspace.It is then converted to pandas dataframe,before that the Workspace,experiment and the cluster are created.

AutoMLConfig is then defined for successfully executing the AutoML run with automl_settings and compute target , the automl_settings is defined with experiment timeout as ‘30’ minutes,task type as ‘Classification’(Classification is a type of supervised learning in which models learn using training data, and apply those learnings to new data. Classification models is to predict which categories new data will fall into based on learnings from its training data) primary metric as ‘accuracy’, label column as ‘DEATH_EVENT’ ,n cross validations as ‘5’,training_dataset to “registered dataset”,max concurrent iterations as “4” and featurization as “auto”.

The models used here are LightGBM,SVM, XGBoostClassifier, RandomForest, VotingEnsemble, StackEnsemble etc and It also uses different pre-processing techniques like Standard Scaling, Min Max Scaling, Sparse Normalizer, MaxAbsScaler,MinAbsScaler etc.

Finally the experiment is being submitted and using the Notebook widget(RunDetails(remote_run).show()), it is visualized. Once the run is successfully completed or executed, the best model is retrieved and saved in output folder in source directory.

### Results

The first model we built is with the help of Azure AutoML for training many types of models such as LightGBM, XGBoostClassifier, RandomForest, VotingEnsemble, StackEnsemble etc.The best accuracy obtained from this model is 86.62%

The model can be futher improved by 2 increasing the estimate timeout for autoML to find best model.Thus a longer timeout will have greater number of models to run and thus higher the performance rate too.

## Hyperparameter Tuning

Initially in the training script (train.py),the dataset (Heart_Failure_Clinical_Records_Dataset.csv) is retrieved from the URL (https://raw.githubusercontent.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/main/Capstone%20Project/Dataset/Heart_Failure_Clinical_Records_Dataset.csv) provided using TabularDatasetFactory Class (Contains methods to create a tabular dataset for Azure Machine Learning).Then the data is being split as train and test with the ratio of 70:30.

The classification algorithm used here is Logistic Regression.Logistic regression is a well-known method in statistics that is used to predict the probability of an outcome, and is especially popular for classification tasks. The algorithm predicts the probability of occurrence of an event by fitting data to a logistic function. Then the training(train.py) script is passed to estimator and HyperDrive configurations to predict the best model and accuracy.The HyperDrive run is executed successfully with the help of parameter sampler, policy, estimator and HyperDrive Config, before that Azure workspace,experiment and cluster is created successfully.

The policy is defined.Bandit policy is used here with slack_factor=0.1,evaluation_internal=1, delay_evaluation=5.Bandit terminates runs where the primary metric is not within the specified slack factor/slack amount compared to the best performing run.Then,the Hyperparameters are then tuned (Hyperparameters are adjustable parameters that let you control the model training process and Hyperparameter tuning is the process of finding the configuration of hyperparameters that results in the best performance) with the help of parameter sampler.Random Sampling is used here.It is used on ‘--C’ ( Inverse of regularization parameter ) which is a control variable that retains strength modification of Regularization by being inversely positioned to the Lambda regulator and ‘--max_iter’ (Maximum number of iterations to converge) which defines the number of times we want the learning to happen and this helps in solving high complex problems with large training hours as per the instructions.For ‘--C’, the parameter is set as (0.1,1) and for ‘—max_iter’ the parameter is set as (50,100,150,200) which returns a value uniformly distributed between low and high.

The SKLearn estimator is created with the training script(train.py), directory path and cluster name, then the configurations for runs is created using hyperdrive_run_config with estimator(created using SKLearn),hyperparameter sampling(Random Sampling), policy(Bandit policy) and also included primary metric(Accuracy),it’s goal (Maximize) , maximum total runs(10) and maximum concurrent runs(4).

Finally the experiment is being submitted and using the Notebook widget(RunDetails(hyperdrive_run).show()), it is visualized. Once the run is successfully completed or executed, the best model is retrieved and saved in output folder in source directory.


### Results

The second model we built is trained with Logistic regression and HyperDrive parameters which are tuned with the help of Azure ML python SDK and HyperDrive tools(Azure HyperDrive functionalities).The best accuracy obtained from this model is 75.75%

The model can be futher improved with the help of tuning other parameters such as the criterion used to define the optimal split and the min/max samples leaf number of samples in the leaf node of each tree.


## Model Deployment

HyperDrive’s best run accuracy = 75.75%
AutoML’s best run accuracy = 86.62%
Thus,Automl's model has the highest accuracy.The model with the best accuracy is deployped as per the instructions,so the AutoML's best model is deployed.

Initially, the best model is registered and it's necessary files are downloaded.Then the Environment and inference is created with the help of required conda dependencies and score.py script file which has the intialization and exit function defined for the best model and the model is deployed with ACI(Azure Container Instance) and configurations such as cpu_cores=1, memory_gb=1.Once the deployment is sucessful, applications insights is enabled and the state of the service is verified.Then the behaviour of the endpoint is analyzed and the service is deleted

## Proof of cluster clean up

The cluster is selected and then deleted with the help of option avaliable in Compute tab. 


## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
