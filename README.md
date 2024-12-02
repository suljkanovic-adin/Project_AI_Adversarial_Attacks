# Project_AI: On The Empirical Effectiveness of Unrealistic Adversarial Hardening Against Realistic Adversarial Attacks

This repository contains the data and code used in our project titled **"On The Empirical Effectiveness of Unrealistic Adversarial Hardening Against Realistic Adversarial Attacks."**

## Overview

In this study, we investigate a pivotal question in the field of machine learning security: **Can "cheap" unrealistic adversarial attacks effectively harden machine learning models against more sophisticated and computationally expensive realistic attacks?**

Our task delves into two distinct use cases:
- **Text Classification**: Assessing the resilience of natural language processing models.
- **Botnet Detection**: Evaluating the robustness of cybersecurity systems against adversarial manipulation.

For each use case, we employ one realistic attack and one unrealistic attack, providing a comprehensive analysis of the effectiveness of adversarial hardening techniques.

## Key Contributions

- **Empirical Analysis**: We present a thorough empirical evaluation of adversarial training methods using both unrealistic and realistic attacks.
- **Comparative Study**: Our findings highlight the differences in model performance when subjected to various attack types.
- **Practical Implications**: The results offer valuable insights for practitioners aiming to enhance model robustness in real-world applications.

## Repository Contents

- **Data**: Datasets used for training and evaluation can be obtained via [this link](https://uniluxembourg-my.sharepoint.com/personal/salijona_dyrmishi_uni_lu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fsalijona%5Fdyrmishi%5Funi%5Flu%2FDocuments%2Frealistic%5Fadversarial%5Fhardening&ga=1) and make sure the data downloaded is placed in the same directory as training,attack and out folders.

The original repository for this project can be cloned using the command:
```bash
git clone https://github.com/serval-uni-lu/realistic_adversarial_hardening.git
```

## Getting Started
## PART I:BOTNET
1. **Install the necessary libraries** to run the different codes in the project.

2. **Several fixes have been made** in order to carry out the project properly:
   -  Change `fence.neris.attack_tf2_modified` to `fence.neris_attack_tf2` in `datagen.py` if you are working with the original repository.
   -  You need to add `eq_min_max=eq_min_max` and `mask_idx=mask_idx` variables in `train.py` in method `pd`, add it in the `get_processing_data(config)` in the `helpers.py` file, and equally add it to each of the original config files (`neris.json`, `virut.json`, `rbot.json`) present in `../botnet/training/config` with their correspondence in the data file you downloaded.
   - In our case, the ART library used had some issues, so we were supposed to change [this line](https://github.com/Trusted-AI/adversarial-robustness-toolbox/blob/970c74a849b9dde060a9ad33024476882c995d5f/art/attacks/evasion/projected_gradient_descent/projected_gradient_descent_tensorflow_v2.py#L154) to `targets = self._set_targets(x, y, False)` and add `target = np.expand_dims(target, axis=1)` after [this line](https://github.com/serval-uni-lu/realistic_adversarial_hardening/blob/2103877bb3a1e48b9953bc08f3abc319f7b8d695/botnet/attack/pgd/pgd_attack_art.py#L48) in the `pgd_attack_art.py` file..
   - There were many other changes made, but these were the most essential ones.

3. **The repository was uploaded to HPC** to increase the speed of training the datasets, which demands a lot of resources.

4. **Connect to the HPC** and load the latest Python module with the command:
   ```bash
   module load lang/Python/3.8.6-GCCcore-10.2.0
   ```
5 **The resulting** model will be saved under the ../botnet/out directory, which is used as input in the attack.py file for the attack of the trained model

6 **With the different results** obtained across the three datasets, you can make your observations and conclusions.

## PART II: TEXT

# Unrealistic vs Realistic Adversarial Training in Text Classification

This project replicates the text classification portion of the paper "On The Empirical Effectiveness of Unrealistic Adversarial Hardening Against Realistic Adversarial Attacks" (Dyrmishi et al., 2023). The experiment investigates whether training with computationally cheaper unrealistic adversarial examples (DeepWordBug) can effectively protect models against realistic adversarial attacks (TextFooler and PWWS).

## Project Structure

The experiment is organized across multiple notebooks:

### Training Notebooks
- `adversarial_rotten_tomatoes.ipynb`: Training on Rotten Tomatoes dataset
- `adversarial_ag_news.ipynb`: Training on AG News dataset  
- `adversarial_tweet_offensive.ipynb`: Training on Tweet Offensive dataset

For each dataset, we trained three models:
- Baseline model: 5 clean epochs
- DeepWordBug hardened model: 1 clean epoch + 4 adversarial epochs
- TextFooler hardened model: 1 clean epoch + 4 adversarial epochs

### Evaluation Notebooks
- `models_clean_evaluation.ipynb`: Evaluates clean accuracy for all 9 trained models
- `models_robust_evaluation_TF.ipynb`: Evaluates robust accuracy against TextFooler attack
- `models_robust_evaluation_PWWS.ipynb`: Evaluates robust accuracy against PWWS attack

## Trained Models

Due to size limitations, trained models are hosted externally. You can access all trained models here: https://uniluxembourg-my.sharepoint.com/:u:/g/personal/0211413060_uni_lu/EctVdHweIqNFsG2jy6jxP1gBYbvJXFc6QLiaFbozqrZlJw?e=Y41DYX

## Dependencies

- Python 3.10
- textattack[tensorflow,optional]==0.2.15
- tensorflow==2.12
- PyTorch
- transformers
- nltk

## Setup and Usage

1. Install the required packages:

pip install textattack[tensorflow,optional]

pip install tensorflow==2.12

2. For Tweet Offensive dataset processing, you'll need additional NLTK data:

import nltk
nltk.download('averaged_perceptron_tagger_eng')

3. **Important:** If you encounter concatenation errors when evaluating the Tweet Offensive dataset, apply the following fix:
# Fix for textattack dataset_args.py concatenation issue
file_path = '/usr/local/lib/python3.10/dist-packages/textattack/dataset_args.py'
with open(file_path, 'r') as f:
    lines = f.readlines()

lines[278] = lines[278].replace('dataset_args[:2] + (args.dataset_split,)', 
                               'dataset_args[:2] + list((args.dataset_split,)) + dataset_args[3:]')

with open(file_path, 'w') as f:
    f.writelines(lines)
    
4.Run the training notebooks in the following order:
- `adversarial_rotten_tomatoes.ipynb`
- `adversarial_ag_news.ipynb` 
- `adversarial_tweet_offensive.ipynb`

5. After training, run the evaluation notebooks:
- `models_clean_evaluation.ipynb`
- `models_robust_evaluation_TF.ipynb`
- `models_robust_evaluation_PWWS.ipynb`

## Environment

All experiments were conducted using Google Colab.

## Results

Detailed results and analysis are available in the presentation. 

## Citation

If you use this code, please cite the original paper: 

On The Empirical Effectiveness of Unrealistic Adversarial Hardening Against Realistic Adversarial Attacks
