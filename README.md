# IT Grow Division Ltd Project

## Overview

This project consists of three distinct components, each residing in its respective folder. Before running any part of the project, ensure that you have Poetry installed. If you haven't installed Poetry yet, you can do so by running:

```bash
pip install poetry
```

After installing Poetry, navigate to the project root directory and install the virtual environment by running:

```bash
poetry install
```

Activate the Poetry shell before running any component:

```bash
poetry shell
```

### 1. mnist_nn

This folder contains a Convolutional Neural Network (CNN) model for training and testing on the MNIST dataset.

#### Instructions:

- Navigate to the `mnist_nn` folder.
- Activate Poetry shell: `poetry shell`
- Train the CNN model: `python train.py`
- Test the trained model: `python test.py`

### 2. google_translate_cli

In this folder, you'll find a simple command-line interface (CLI) app that translates Bangla sentences to French using the Google Translate API.

#### Instructions:

- Navigate to the `google_translate_cli` folder.
- Activate Poetry shell: `poetry shell`
- Run the translation CLI: `python translate.py "পাইথন একটি দুর্দান্ত প্রোগ্রামিং ভাষা"`

### 3. social_network_crud_sql

Demonstrates CRUD operations on a social network user using a SQLite3 database.

#### Instructions:

- Navigate to the `social_network_crud_sql` folder.
- Activate Poetry shell: `poetry shell`
- Run CRUD operations test: `python test.py`

## Prerequisites

- Poetry: Ensure that Poetry is installed on your system.

## Additional Notes

- Each subfolder has its own Poetry dependencies. Activate Poetry shell in the respective folder before running the components.
- The project is structured to be modular, allowing you to work on and test each component independently.

Feel free to explore and modify the code to suit your needs!