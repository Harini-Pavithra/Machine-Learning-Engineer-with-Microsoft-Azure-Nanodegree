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

After authenticating,a new AutoML experiment is created which includes,importing the dataset,configuring the run and setting up the environmet for AutoML run.After the run is completed,the best model is identified and deployed with Azure Container Instance,then the application insights are enabled using script file(logs.py).The next step is creating swagger documentation which is helpful to check if the model can get POST request and respond back.It is done with the help of swagger.json file,downloaded via SWagger URI. Next step is to consume the model via endpoint.py and benchmarking is done via benchmark.sh files.Finally the pipeline is created,published and consumed.
.

## Steps Involved in Python SDK
![Python_SDK](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Architecture%20Diagram/Python_SDK.JPG)


### Explanation

In notebook section we first upload the python file(aml-pipelines-with-automated-machine-learning-step.py),once it is uploaded we create a cluster to execute the python file.After initializing the workspace, we create a new or use existing AutoML experiment followed by creating or attaching the existing cluster.Then we load the dataset(bankmarkerting_train.csv),once the dataset is loaded,the model is trained with different models and scaling methods,then the best model is retrived and deployed with Azure Container Instance and finally the model is consumed via the REST endpoint.

# Steps in Detail

## Step 1: Authentication

Authentication is crucial for the continuous flow of operations. Continuous Integration and Delivery system (CI/CD) rely on uninterrupted flows. When authentication is not set properly, it requires human interaction and thus, the flow is interrupted. An ideal scenario is that the system doesn't stop waiting for a user to input a password. So whenever possible, it's good to use authentication with automation.Authentication types 1. Key Based 2.Token based 3. Interactive

Udacity Classroom - "If you are using the lab Udacity provided to you, you can skip this step since you are not authorized to create a security principal".So, this step is skipped in Azure.

## Step 2:Automated ML Experiment

1. A new AutoML model is created.

2. Next the dataset is selceted which is already registered and uploaded Via URI(https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv)
![1.Selecting_Dataset](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%202%20Output/1.Selecting_Dataset.JPG)

3. Then we create a cluster,we use this cluster to run the autoML experiment.
![4.Creating_Cluster](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%202%20Output/4.Creating_Cluster.JPG)

4. The run is configured and task type is selected
![7.Selecting_Task_type](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%202%20Output/7.Selecting_Task_type.JPG)

5. After the AutoML experiment run completes, a summary of all the models and their metrics are shown, including explanations.
![10.AutoML_Run_Completed](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%202%20Output/10.AutoML_Run_Completed.JPG)


6. Next the best model is retrived.
![11.Best_Model](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%202%20Output/11.Best_Model.JPG)

## Step 3:Deploy the best model

Under the Experiments section,go to the "Model" tab and select the model with highest accuracy.Click on deploy option available and fill out the form with a meaningful name and description. For Compute Type select Azure Container Instance (ACI) and enable Authentication.Deployment takes a few seconds. After a successful deployment,  the "Deploy status" will show as succeed and condition will be changed to "Healthy" from "Transistion".

## Step 4:Enable logging

Application Insights is a very useful tool to detect anomalies, visualize performance. It can be enabled before or after a deployment. To enable Application Insights after a model is deployed, you can use the below command with the python SDK. In the next section, you will learn how to do it.The script file logs.py is modified and executed with the help of config.json file.

## Step 5:Swagger Documentation

Swagger is a tool that helps build, document, and consume RESTful web services like the ones you are deploying in Azure ML Studio. It further explains what types of HTTP requests that an API can consume, like POST and GET.Azure provides a swagger.json that is used to create a web site that documents the HTTP endpoint for a deployed model.The port of swagger.sh file is changed and execcuted when docker is running,similarly the se  .py file is executed and verified.

## Step 6:Consume model endpoints

You can consume a deployed service via an HTTP API. An HTTP API is a URL that is exposed over the network so that interaction with a trained model can happen via HTTP requests.
Users can initiate an input request, usually via an HTTP POST request. HTTP POST is a request method that is used to submit data. The HTTP GET is another commonly used request method. HTTP GET is used to retrieve information from a URL. The allowed requests methods and the different URLs exposed by Azure create a bi-directional flow of information.
The APIs exposed by Azure ML will use JSON (JavaScript Object Notation) to accept data and submit responses. It served as a bridge language among different environments.

The endpoint.py file is 
The benchmark.sh 


## Step 7:Create and publish a pipeline




# Future Improvements

# Screencast Video
