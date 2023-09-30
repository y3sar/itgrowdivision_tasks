# MNIST CNN Training and Testing

This project trains a simple Convolutional Neural Network (CNN) model on the MNIST dataset using PyTorch. The trained model is then tested on the test set. The results and metrics are reported through [WandB](https://wandb.ai/).

## Installation

```bash
pip install poetry
```

After installing Poetry, you can proceed with the rest of the installation instructions in the README.

```bash
poetry install
poetry shell
```

## Training

To train the model, run:

```bash
python train.py
```

This script will train the CNN model on the MNIST training set.

## Testing

After training, you can evaluate the model on the test set:

```bash
python test.py
```

This script will test the trained model on the MNIST test set and report accuracy metrics.

## WandB Report

The results and detailed metrics can be found in the WandB report [here](https://wandb.ai/y3sar/mnist-cnn/reports/Simple-CNN-training-on-MNIST--Vmlldzo1NTUxNjIz?accessToken=8ogsl9x5mitsxyjtb92m82nekz2z0vyaclm63bugcvf841lslb12m5kqksleebq9).

Feel free to explore the WandB report for a comprehensive overview of the training process and evaluation results.

