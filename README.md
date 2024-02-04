# Lung-Colon-Cancer-Histopathological-Images-Classification-Project



## Lung and Colon Histopathology Web App

Welcome to the Lung and Colon Histopathology Web App repository! This web application is designed to classify histopathological images for cancer in the lung and colon using deep learning techniques. It leverages TensorFlow, Keras, Django, and various other tools to provide an interactive and informative platform for cancer diagnosis.

# Features

# Image Classification: 

The web app allows users to upload histopathological images of lung and colon tissues for cancer classification.

# Deep Learning Model: 

It utilizes state-of-the-art deep learning models trained on large datasets to achieve accurate classification results.

# Visualization:

Users can visualize the classification results along with confidence scores and other diagnostic information.
# User Authentication: 

Secure user authentication system ensures data privacy and control over user access.
# Integration with ML Platforms: 

The application seamlessly integrates with ML platforms like DVC, MLflow, and Dagshub for model versioning, experiment tracking, and collaboration.
## Technologies Used

# Python: 
Core programming language for backend development and machine learning tasks.

# TensorFlow & Keras: 
Deep learning frameworks used for model development and training.

# Django: 

Web framework for building the frontend and backend of the web application.

# VSCode: 

Integrated Development Environment (IDE) for coding and project management.

# DVC: 
Data Version Control for managing and versioning datasets and models.

# MLflow: 
Open-source platform for managing the end-to-end machine learning lifecycle.

# Dagshub: 

Collaboration platform for machine learning projects.

# Azure: 

Cloud platform for hosting the web application and managing resources.

# Kaggle: 

Platform for accessing datasets and participating in machine learning competitions.

### Getting Started
To run the Lung and Colon Histopathology Web App locally, follow these steps:

# Clone the repository:


```

git clone https://github.com/Towet-Tum/Lung-Colon-Cancer-Histopathological-Images-Classification-Project.git
```
# Install the dependencies:

```
pip install -r requirements.txt
```




# Model Experiment and Evaluation

Connect the github

Run this commands in the terminal

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/Towet-TumLung-Colon-Cancer-Histopathological-Images-Classification-Project.mlflow 

export MLFLOW_TRACKING_USERNAME=Towet-Tum

export MLFLOW_TRACKING_PASSWORD=39c66009c3d7d6d659cbc691e65a93c46873d3c4

```

3 Set up the database and perform migrations:

python manage.py makemigrations
python manage.py migrate
```
# Start the Django development server:

```
python manage.py runserver
```
Access the web app at http://localhost:8000 in your browser.

# Contributing

Contributions to the Lung and Colon Histopathology Web App are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request. Make sure to follow the code of conduct.

# License
This project is licensed under the MIT License. See the LICENSE file for details.


## Azure CI-CD Deployment 

docker build -t lungcolon.azurecr.io/lungcolon:latest .
docker login lungcolon.azurecr.io
docker push lungcolon.azurecr.io/lungcolon

#Save Password

MBnVS1hXYDuBB9WdKdRYezKlX4iZ3nWGfBTDmEkaj6+ACRDkD2vU