import sys
import numpy as np
from attack.fence.neris_attack_tf2 import Neris_attack
from attack.pgd.pgd_attack_art import PgdRandomRestart
def generate_adversarial_batch_fence(model, total, samples, labels, distance, iterations, scaler, mins, maxs, model_path):
    while True:
        model.save(model_path)

        attack_generator = Neris_attack(model_path=model_path, iterations=iterations, distance=distance, scaler=scaler, mins=mins, maxs=maxs)

        # Initialize our perturbed data and labels
        perturbSamples = []
        perturbLabels = []
        idxs = np.random.choice(range(0, len(samples)), size=total, replace=False)
        for i in idxs:
            sample = samples[i]
            sample = np.expand_dims(sample, axis=0)
            label = labels[i]
            # Generate an adversarial sample
            adversary = attack_generator.run_attack(sample, label)
            perturbSamples.append(adversary)
            perturbLabels.append(label)

        perturbSamples = np.squeeze(np.array(perturbSamples))
        yield (np.array(perturbSamples), np.array(perturbLabels))


def generate_adversarial_batch_pgd(model, total, samples, labels, distance, iterations, scaler, mins, maxs, mask_idx, eq_min_max):
    # Ensure mins and maxs are valid before creating the attack generator
    if np.any(mins >= maxs):
        raise ValueError("Invalid `mins` and `maxs`: min must be less than max.")

    # Initialize the PGD attack generator with all required parameters
    attack_generator = PgdRandomRestart(
        model=model,
        eps=distance,
        alpha=1,
        num_iter=iterations,
        restarts=5,
        scaler=scaler,
        mins=mins,
        maxs=maxs,
        mask_idx=mask_idx,
        eq_min_max=eq_min_max
    )

    while True:
        idxs = np.random.choice(range(0, len(samples)), size=total, replace=False)
        batch_samples = samples[idxs]
        perturbLabels = labels[idxs]
        print(perturbLabels.shape)
        perturbLabels = np.expand_dims(perturbLabels, axis=1)
        print(perturbLabels.shape)

        print(batch_samples.shape)
        # Run the attack to generate adversarial samples
        perturbSamples = attack_generator.run_attack(batch_samples, perturbLabels)
        print("After  attack",perturbLabels.shape)

        yield (np.array(perturbSamples), np.array(perturbLabels))

# Debugging function to log clip values
# def log_clip_values(clip_min, clip_max):
#     print(f"Clip Min: {clip_min}")
#     print(f"Clip Max: {clip_max}")
