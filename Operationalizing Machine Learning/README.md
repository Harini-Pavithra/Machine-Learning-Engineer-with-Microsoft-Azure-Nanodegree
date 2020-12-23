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

![New_AutoML](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%202%20Output/New_AutoML.JPG)

2. Next the dataset is selceted which is already registered and uploaded Via URI(https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv)

![1.Selecting_Dataset](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%202%20Output/1.Selecting_Dataset.JPG)

3. Then we create a cluster,we use this cluster to run the autoML experiment.

![4.Creating_Cluster](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%202%20Output/4.Creating_Cluster.JPG)

4. The run is configured and task type is selected

![7.Selecting_Task_type](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%202%20Output/7.Selecting_Task_type.JPG)

5. After the AutoML experiment run completes, a summary of all the models and their metrics are shown, including explanations.

![10.AutoML_Run_Completed](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%202%20Output/10.AutoML_Run_Completed.JPG)

![13.List_Of_Models](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%202%20Output/13.List_Of_Models.JPG)

6. Next the best model is retrived.

![11.Best_Model](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%202%20Output/11.Best_Model.JPG)

Registered Dataset:

![Dataset_1](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%202%20Output/Dataset_1.JPG)

All screenshots of Step 2 are available in [Step 2 Output](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/tree/main/Operationalizing%20Machine%20Learning/Step%202%20Output)

## Step 3:Deploy the best model

1.Under the Experiments section,go to the "Model" tab and select the model with highest accuracy.

![1.Deployment](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%203%20Outputs/1.Deployment.JPG)

2.Click on deploy option available and fill out the form with a meaningful name and description. For Compute Type select Azure Container Instance (ACI) and enable Authentication.

![3.Deployement_Success](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%203%20Outputs/3.Deployement_Success.JPG)

3.Deployment takes a few seconds. After a successful deployment, the "Deploy status" will show as succeed and condition will be changed to "Healthy" from "Transistion".

![4.Healthy_State](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%203%20Outputs/4.Healthy_State.JPG
)

All screenshots of Step 3 are available in [Step 3 Output](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/tree/main/Operationalizing%20Machine%20Learning/Step%203%20Outputs)

## Step 4:Enable logging

Application Insights is a very useful tool to detect anomalies, visualize performance. It can be enabled before or after a deployment. 

1.config.json file is downloaded and placed in the same directory.

![1.Config_file](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%204%20Outputs/1.Config_file.jpg)

2.To enable insights, the script file logs.py is modified and executed

![2.Enabling](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%204%20Outputs/2.Enabling.JPG)

![3.Script_Execution](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%204%20Outputs/3.Script_Execution.JPG)

3.After running it once again to enable insights. The Attributes page should show Insights is now enabled for the deployed model.

![5.Enabled](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%204%20Outputs/5.Enabled.JPG)

All screenshots of Step 4 are available in [Step 4 Output](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/tree/main/Operationalizing%20Machine%20Learning/Step%204%20Outputs)
## Step 5:Swagger Documentation

Swagger is a tool that helps build, document, and consume RESTful web services like the ones you are deploying in Azure ML Studio. It further explains what types of HTTP requests that an API can consume, like POST and GET.Azure provides a swagger.json that is used to create a web site that documents the HTTP endpoint for a deployed model.

1.swagger.json is placed in the same directory.

![1.Swagger_file](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%205%20Outputs/1.Swagger_file.jpg)

2.swagger.sh is executed when docker is running which will download the latest Swagger container, and it will run it on port 9000.

![2.Swagger_Execution](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%205%20Outputs/2.Swagger_Execution.JPG)

![4.Localhost_Run](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%205%20Outputs/4.Localhost_Run.JPG)

3.serve.py is executed and it will start a Python server on port 8000. This script needs to be right next to the downloaded swagger.json file

![5.Script_Execution](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%205%20Outputs/5.Script_Execution.JPG)

![6.Swager_output](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%205%20Outputs/6.Swager_output.JPG)

All screenshots of Step 5 are available in [Step 5 Outputs](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/tree/main/Operationalizing%20Machine%20Learning/Step%205%20Outputs)

## Step 6:Consume model endpoints

You can consume a deployed service via an HTTP API. An HTTP API is a URL that is exposed over the network so that interaction with a trained model can happen via HTTP requests.
Users can initiate an input request, usually via an HTTP POST request. HTTP POST is a request method that is used to submit data. The HTTP GET is another commonly used request method. HTTP GET is used to retrieve information from a URL. The allowed requests methods and the different URLs exposed by Azure create a bi-directional flow of information.
The APIs exposed by Azure ML will use JSON (JavaScript Object Notation) to accept data and submit responses. It served as a bridge language among different environments.

1.Using the provided endpoint.py replaced the scoring_uri and key to match the REST endpoint and primary key respectively. The script issues a POST request to the deployed model and gets a JSON response that gets printed to the terminal.

![Script_update](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%206%20Outputs/Script_update.JPG)

2.A data.json file will appear after we run endpoint.py

![Script_Output](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%206%20Outputs/Script_Output.JPG)

![data_json_file](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%206%20Outputs/data_json_file.JPG)

## Benchmark

A benchmark is used to create a baseline or acceptable performance measure. Benchmarking HTTP APIs is used to find the average response time for a deployed model.One of the most significant metrics is the response time since Azure will timeout if the response times are longer than sixty seconds.Apache Benchmark is an easy and popular tool for benchmarking HTTP services.

1. Benchmark file is executed and output is verified

![Benchmarch](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%206%20Outputs/Benchmark/Benchmarch.JPG)

![Benchmark_output](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%206%20Outputs/Benchmark/Benchmark_output.JPG)

All screenshots of Step 6 are available in [Step 6 Outputs](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/tree/main/Operationalizing%20Machine%20Learning/Step%206%20Outputs)

## Step 7:Create and publish a pipeline

1. Cluster is created and the file is uploaded.

![Cluster](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Compute%20Instance/Cluster.JPG)

2. The cells are executed one by one and AutoML run is completed.

![Run_Details](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%207%20Outputs/Run_Details.JPG)

![Run_Finished](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%207%20Outputs/Run_Finished.JPG)

![Graph_Completed](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%207%20Outputs/Graph_Completed.JPG)

![Pipeline_Completed_1](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%207%20Outputs/Pipeline_Completed_1.JPG)

![Pipelinerun_Graph](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%207%20Outputs/Pipelinerun_Graph.JPG)

![Pipeline_Run](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%207%20Outputs/Pipeline_Run.JPG)

![Pipeline_Endpoint](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%207%20Outputs/Pipeline_Endpoint.JPG)

3. Then we retrive the best model,next it is published and consumed.

![Publish_Details](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%207%20Outputs/Publish_Details.JPG)

![Pipeline_Published](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%207%20Outputs/Pipeline_Published.JPG)

![Pipeline_Active](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/blob/main/Operationalizing%20Machine%20Learning/Step%207%20Outputs/Pipeline_Active.JPG)

All screenshots of Step 7 are available in [Step 7 Outputs](https://github.com/Harini-Pavithra/Machine-Learning-Engineer-with-Microsoft-Azure-Nanodegree/tree/main/Operationalizing%20Machine%20Learning/Step%207%20Outputs)

# Future Improvements

1. The accuracy of the model can be improved by solving the class imbalance issue in dataset.
2. Increasing the number of cross validation can improve accuracy
3. Trying deep Learning algorithms which is not used by the  AutoML in the runs.

# Screencast Video
