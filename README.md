<!--
-*- coding: utf-8 -*-

 Author: Jantine Broek <jantine@mysine.io>
 License: MIT
-->

# BioSignal-DL

## Table of Contents
1. [General Info](#general-info)
2. [Model and Data](#model-and-data)
3. [Build and Run](#build-and-run)
4. [License](#license)

<a name="general-info"></a>
## General Info

This repository contains analysis of biological time series data using deep learning approaches. The goal is to analyse and predict patterns in biological signals such as blood glucose levels and EEG measurements using LSTM (Long Short-Term Memory) networks and CNNs (Convolutional Neural Networks).

### Repository Structure

```
BioSignal-DL/
├── notebooks/                     # Jupyter notebooks
│   ├── exploratory/               # Initial data exploration
│   │   ├── glucose_exploration.ipynb   # Initial blood glucose data analysis
│   │   └── eeg_exploration.ipynb       # Initial EEG data analysis
│   └── analysis/                  # Final analysis notebooks
│       ├── glucose_lstm.ipynb     # LSTM models for glucose prediction
│       ├── eeg_cnn.ipynb          # CNN models for EEG classification
│       └── combined_models.ipynb  # Multi-modal approaches
├── models/                        # Saved model files
│   ├── lstm/                      # LSTM model checkpoints
│   └── cnn/                       # CNN model checkpoints
├── results/                       # Output from analysis
│   ├── figures/                   # Generated plots and visualisations
│   └── tables/                    # Generated data tables
├── configs/                       # Configuration files
│   ├── params.yaml                # Model parameters, etc.
│   └── data_paths.yaml            # Paths to data
├── scripts/                       # Command-line scripts
├── .pre-commit-config.yaml        # Pre-commit hooks configuration
├── requirements.txt               # Project dependencies
├── setup.py                       # Make the project installable
├── README.md                      # Project documentation
└── .gitignore                     # Include patterns to ignore large data files
```

<a name="model-and-data"></a>
## Model and Data

This repository includes implementations of:

1. **LSTM Networks** for predicting time series data such as:
   - Blood glucose level forecasting
   - Temporal patterns in biological signals

2. **Convolutional Neural Networks** for:
   - EEG signal classification
   - Feature extraction from biosignals

The data used in this repository typically consists of time series measurements from biological sources. These are accessed from external sources that should be configured in the `configs/data_paths.yaml` file.

<a name="build-and-run"></a>
## Build and Run

### How to Build

This repository uses Git Large File Storage (Git LFS) to handle the large `.pth` model files. To clone and use this repository:

1. Install Git LFS if you haven't already:
   ```bash
   # For Ubuntu/Debian
   apt-get install git-lfs

   # For macOS with Homebrew
   brew install git-lfs

   # For Windows with Chocolatey
   choco install git-lfs
   ```

2. Enable Git LFS:
   ```bash
   git lfs install
   ```

3. Ensure you have Python 3.8 or higher installed.
4. Clone the repository:
   ```bash
    git clone https://github.com/MYSINELTD/BioSignal-DL.git
    cd MYSINELTD/BioSignal-DL
   ```

5. Pull the LFS files:
   ```bash
   git lfs pull
   ```

6. Create a conda environment:

    ```bash
    conda create -n biosignal_dl python=3.11
    conda activate biosignal_dl
    ```

7. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Install the Packages

1. If you need to access related data repositories, clone them in the same parent directory:

   ```bash
   mkdir -p ~/Projects/MYSINELTD
   cd ~/Projects/MYSINELTD
   git clone https://github.com/MYSINELTD/BioSignal-DL.git
   # Clone any data repositories if needed
   ```

2. Configure data paths by adding this to your .bashrc or .zshrc file:

   ```bash
   export BIOSIGNAL_DATA_DIR=~/path/to/your/data
   ```

3. Install the package locally in your conda environment:

    ```bash
    pip install -e .
    ```

### How to Run

This repository uses Pre-Commit to maintain PEP8 standards. To use Pre-Commit:

1. Activate your conda environment:

    ```bash
    conda activate biosignal_dl
    ```

2. Install pre-commit hooks:

    ```bash
    pip install pre-commit
    pre-commit install
    ```

3. Test the Pre-Commit hooks:

    ```bash
    pre-commit run --all-files
    ```

4. Run the Jupyter notebooks:

    ```bash
    jupyter lab
    # or
    jupyter notebook
    ```

5. To train models from the command line, use the provided scripts:

    ```bash
    python scripts/train_lstm.py --config configs/params.yaml
    ```

## License

MIT