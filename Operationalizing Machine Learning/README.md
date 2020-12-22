# Operationalizing Machine Learning with Microsoft Azure

In this project, we will work with the [Bank Marketing dataset](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/tree/main/Operationalizing%20Machine%20Learning/Dataset). we will use Azure to configure a cloud-based machine learning production model, deploy it, and consume it. we will also create, publish, and consume a pipeline.Both the Azure ML Studio and the Python SDK will be used in this project.

# Dataset
The Dataset used here is bankmarkerting_train.csv, it is a UCI Dataset, which contains data about direct marketing campaigns (phone calls) of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.we seek to predict if the client will subscribe a term deposit (variable y) or not. There are 21 features, 32.950 rows and target variable in total.Two Machine Learning models were built using this dataset.

# Steps Involved

1. Authentication
2. Automated ML Experiment
3. Deploy the best model
4. Enable logging
5. Swagger Documentation
6. Consume model endpoints
7.Create and publish a pipeline

# Architectural Diagram

## Steps Involved in Azure ML Studio
![Azure_ML_Studio](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Architecture%20Diagram/Azure_ML_Studio.JPG)

### Explanation

After authenticating,a new AutoML experiment is created which includes,importing the dataset,setting up the environmet for AutoML run.After the run is completed,the best model is identified and deployed with Azure Container Instance,then the application insights are enabled using script file(logs.py).The next step is creating swagger documentation which is helpful to check if the model can get POST request and respond back.It is done with the help of swagger.json file,downloaded via SWagger URI. Next step is to consume the model via endpoint.py and benchmarking is done via benchmark.sh files.Finally the pipeline is created,published and consumed.
.

## Steps Involved in Python SDK
![Python_SDK](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Architecture%20Diagram/Python_SDK.JPG)


### Explanation

In notebook section we first upload the python file(aml-pipelines-with-automated-machine-learning-step.py),once it is uploaded we create a cluster to execute the python file.After initializing the workspace, we create a new or use existing AutoML experiment followed by creating or attaching the existing cluster.Then we load the dataset(bankmarkerting_train.csv),once the dataset is loaded,the model is trained with different models and scaling methods,then the best model is retrived and deployed with Azure Container Instance and finally the model is consumed via the REST endpoint.

# Steps in Detail

## Step 1: Authentication

Udacity Classroom - "If you are using the lab Udacity provided to you, you can skip this step since you are not authorized to create a security principal".So, this step is skipped 

