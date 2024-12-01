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

- **Data**: Datasets used for training and evaluation can be obtained via [this link](https://uniluxembourg-my.sharepoint.com/personal/salijona_dyrmishi_uni_lu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fsalijona%5Fdyrmishi%5Funi%5Flu%2FDocuments%2Frealistic%5Fadversarial%5Fhardening&ga=1).

The original repository for this project can be cloned using the command:
```bash
git clone https://github.com/serval-uni-lu/realistic_adversarial_hardening.git
```

## Getting started

1. **Install the necessary libraries** to run the different codes in the project.

2. **Several fixes have been made** in order to carry out the project properly:
   -  Change `fence.neris.attack_tf2_modified` to `fence.neris_attack_tf2` in `datagen.py` if you are working with the original repository.
   - You need to add `eq_min_max=eq_min_max` and `mask_idx=mask_idx` variables in `train.py` in method `pd`, add it in the `get_processing_data(config)` in the `helpers.py` file, and equally add it to each of the original config files (`neris.json`, `virut.json`, `rbot.json`) present in `../botnet/training/config` with their correspondence in the data file you downloaded.
   -  In our case, the ART library used(v1.18) had some issues, so we were supposed to change [this line](https://github.com/Trusted-AI/adversarial-robustness-toolbox/blob/970c74a849b9dde060a9ad33024476882c995d5f/art/attacks/evasion/projected_gradient_descent/projected_gradient_descent_tensorflow_v2.py#L154) to `targets = self._set_targets(x, y, False)` and add `target = np.expand_dims(target, axis=1)` after [this line](https://github.com/serval-uni-lu/realistic_adversarial_hardening/blob/2103877bb3a1e48b9953bc08f3abc319f7b8d695/botnet/attack/pgd/pgd_attack_art.py#L48) in the `pgd_attack_art.py` file.
