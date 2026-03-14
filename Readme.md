# MLOps MLflow Project – End-to-End Machine Learning Pipeline

This project is a **learning-focused MLOps pipeline** . The system implements a complete **ML lifecycle pipeline**, including data ingestion, transformation, model training, experiment tracking with MLflow, and experiment logging to DagsHub.

The project focuses on **reproducibility, modular architecture, and experiment management**, making it useful for understanding real-world ML workflows and MLOps best practices.

DagsHub Experiment Tracking:
https://dagshub.com/Shubham-rawat0/mlops.mlflow

---

## Features

### ⚙️ Modular ML Pipeline

* Fully modular machine learning pipeline
* Clear separation of components for maintainability
* Each stage implemented as an independent module

Pipeline stages include:

* Data Ingestion
* Data Transformation
* Model Training
* Model Evaluation

---

### 📊 Experiment Tracking with MLflow

* Track hyperparameters and training runs
* Log evaluation metrics such as R² score
* Store trained models as artifacts
* Compare model performance across runs
* Visualize experiments in the MLflow dashboard

---

### ☁️ Remote Tracking with DagsHub

* MLflow tracking integrated with DagsHub
* Centralized experiment tracking
* Version-controlled experiment logs
* Enables collaboration and experiment reproducibility

---

### 🧠 Multiple Model Training

The training pipeline evaluates multiple machine learning models automatically.

Examples include:

* Linear Regression
* Decision Tree
* Random Forest
* Gradient Boosting

Each model is evaluated and the **best-performing model is selected automatically**.

---

### 🔍 Hyperparameter Tuning

* Uses **GridSearchCV** for automated hyperparameter optimization
* Cross-validation ensures robust evaluation
* Best parameters are selected based on model performance

---

### 📦 Artifact & Model Management

The pipeline saves:

* trained models
* preprocessing pipelines
* experiment metadata
* training artifacts

Artifacts are logged to MLflow and can be retrieved for deployment or further experimentation.

---

## Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Experiment Tracking

* MLflow

### Experiment Hosting

* DagsHub

### Development Environment

* VS Code
* Virtual Environment (venv)

---

## Project Architecture

The project follows a **modular MLOps architecture**.

```
mlops/
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│
├── src/
│   └── mlops/
│       ├── components/
│       │   ├── data_ingestion.py
│       │   ├── data_transformation.py
│       │   └── model_trainer.py
│       │
│       ├── pipeline/
│       │   └── training_pipeline.py
│       │
│       ├── utils.py
│       ├── logger.py
│       └── exception.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Pipeline Workflow

The system executes the following pipeline:

```
Raw Dataset
     ↓
Data Ingestion
     ↓
Train/Test Split
     ↓
Data Transformation
     ↓
Feature Engineering & Preprocessing
     ↓
Model Training
     ↓
Hyperparameter Tuning
     ↓
Model Evaluation
     ↓
MLflow Experiment Logging
     ↓
Best Model Selection
```

---

## Data Ingestion

The ingestion module:

* Reads the dataset
* Splits it into training and testing sets
* Saves intermediate datasets as artifacts

Outputs:

* `train.csv`
* `test.csv`

---

## Data Transformation

The transformation stage prepares the dataset for training.

Operations include:

* Feature scaling
* Data preprocessing pipelines
* Target column separation
* Preprocessor object serialization

Artifacts produced:

```
preprocessor.pkl
train_array
test_array
```

---

## Model Training

The model trainer performs:

1. Training multiple models
2. Hyperparameter tuning using GridSearchCV
3. Model performance evaluation
4. Best model selection

Evaluation metric used:

* **R² Score**

The model with the highest test score is selected as the final model.

---

## MLflow Experiment Tracking

Each training run logs:

* model parameters
* evaluation metrics
* trained model artifacts
* experiment metadata

Example logged information:

```
parameters:
  n_estimators
  max_depth

metrics:
  r2_score

artifacts:
  trained_model.pkl
```

---

## DagsHub Integration

Experiments are tracked remotely via DagsHub.

This enables:

* centralized experiment dashboards
* experiment comparison
* artifact storage
* version control integration

Project page:

https://dagshub.com/Shubham-rawat0/mlops.mlflow

---

## Run Locally

### Prerequisites

* Python 3.9+
* Git
* Virtual Environment

---

### Clone Repository

```bash
git clone https://github.com/Shubham-rawat0/mlops
cd mlops
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Training Pipeline

```bash
python app.py
```





DagsHub Project:
https://dagshub.com/Shubham-rawat0/mlops.mlflow
