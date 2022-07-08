## MLOps Notes

MLOps is set of practices to build Machine Learning models in a systematic way, putting models into 
production, monitoring the data and models and automating this process, so MLOps covers majority of
the Machine Learning Life Cycle. 

One of the core steps of this cycle is modelling. In modelling step, different approaches, parameters 
are experimented and it creates a need to track experiments. To compare different experiments and 
to prevent manual maintenance of models and results we should log parameters, metrics, plots and other 
useful artifacts to tools and we should automate this process to decrease errors. Another need in 
modelling step is reproducing results and converting experiments which is mostly done in notebooks
in ad hoc manner to production grade scripts. Model pipelines comes into play to fulfill this need. 
It allows us to reproduce results, put training/validation steps in a meaningful order and easy
execution.

After we have a model we should deploy it. Deployment depends on the use case of the model. If it
will be used for batch prediction in specific intervals then we can automate this process by using
workflow orchestrators. If our use case is online prediction. Then we can create a web service to 
make prediction as new data comes. If online prediction will be made when a specific event occurs,
then we can use tools like Kafka to subcribe our model to a event stream and publish predictions
on another stream.

We should monitor our deployments. To ensure that our model is working as expected and there is no
issues such as data shift, concept shift, platform or network related issues. To prevent our model
to be stale we should monitor its performance based on pre-determined metrics and we should re-run
our pipeline with new data or we should take other measures to adapt our model to changes. We also
should monitor platform related metrics such as resource usage and network usage, requests per second
to provide an available platform and to act accordingly when there is a problem.

Other than using MLOps we should follow best practices and processes.


Designing Machine Learning systems are an iterative process. One step in the process might require
updating previous steps. Steps according to Chip Huyen: Project setup, data pipeline, modelling &
training, serving.

###Project Setup
First we should find out as much detail about the problem as possible.
    - We should analyze the problem and determine the goals
    - We should clarify how the end users will consume predictions
    - We should determine performance constraints/objectives
    - We should determine how to evaluate the performance of the system
    
Second step is data pipeline. Machine Learning is more driven by data than algorithms. After analyzing
the problem at hand and determining objectives we should think about data. What type of data we need,
inputs and outputs of our system, cost of data collection and if required cost of labelling, in where
to store data, data volume/velocity, data preprocessing, class imbalance, feature engineering, data
regulation, anonymization, bias etc...

Third step is modelling and training. We can frame the problem in different ways and it might require 
changes in previous steps as well. We can outline some important sub steps in modelling. We should 
start with simple solutions to form baseline. We can add more complexity for improving the model and 
it provides easier debugging because complexity is added incrementally. Overfitting the model into a 
small data also gives an initial idea. If even it is not possible then it indicates to a problem with
implementation. To reproduce errors/results and also to compare results across experiments we should
use random seeds.   

Last step is serving. In serving process it might be required to consider these points:
    - Whether the model satisfies the constraints/objectives determined in problem setup step earlier
    - Whether model we'll continuously improve itself by retraining with new samples  
    - Customer feedback, how to understand whether model works good, users will be allowed to suggest
    better predictions
    - How often model should be updated
    - What to do with the cases in which model confidence is low
    - In where inference should be run, in cloud, on-prem or on user device
    - Regulations
    - Explainability
    - Ethical issues

