## Marketing Campaign Prediction
This repository contains a machine learning project aimed at predicting the success of marketing campaigns. By analyzing past campaign data, we develop models that can forecast the effectiveness of future campaigns, helping businesses optimize their marketing strategies.

## Workflow to follow
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the config_entity.py
5. Update the configuration manager in src/config
6. Update the components
7. Update the pipeline
8. Update main.py


## Table of Contents
Project Overview
Dataset
Installation
Usage
Model Building
Evaluation
Contributing
License


## Project Overview
Marketing campaigns are essential for businesses to promote their products and engage customers. Predicting the success of these campaigns can save resources and improve targeting strategies. This project leverages machine learning techniques to predict the outcome of marketing campaigns based on historical data.


## Data Source
The dataset can be downloaded from [This Link](https://www.kaggle.com/datasets/sujithmandala/marketing-campaign-positive-response-prediction).




## Clone the Repository
```git clone https://github.com/gbiamgaurav/Marketing-Campaign-Project.git```


## Run the following commands to set up the env
```bash init_setup.sh```


## Run the file
```python main.py```


## Run the DVC Commands
```dvc init```


```dvc repro```


```dvc dag```


## Run the Applications

```streamlit run app.py```

```python test.py```

## Feature Engineering
We perform feature engineering to enhance the predictive power of our models:

* Encoding categorical variables
* Scaling numerical features




## Model Building
The project uses several machine learning algorithms to build predictive models, including:
* Logistic Regression
* Decision Trees
* Random Forest
* Gradient Boosting
* Support Vector Machines (SVM)



## Evaluation
The performance of the models is evaluated from the following metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC AUC




## Contributing
We welcome contributions to improve the project. Here are some ways you can contribute:

* Fix bugs and issues
* Add new features or models
* Improve documentation

To contribute, please fork the repository, create a new branch, and submit a pull request.


## License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize this README.md file as per your specific project requirements. This template should give you a solid starting point for documenting your marketing campaign prediction use case using machine learning.