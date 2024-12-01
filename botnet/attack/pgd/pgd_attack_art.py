import numpy as np
import tensorflow as tf
from art.attacks.evasion import ProjectedGradientDescent as PGD
from art.estimators.classification.tensorflow import TensorFlowV2Classifier as kc


class PgdRandomRestart():
    def __init__(self, model, eps, alpha, num_iter, restarts, scaler, mins, maxs, mask_idx, eq_min_max):
        """
        :param model: instance of tf.keras.Model that is used to generate adversarial examples
        :param eps: float number - maximum perturbation size for adversarial attack
        :param alpha: float number - step size in adversarial attack
        :param num_iter: integer - number of iterations of pgd during one restart iteration
        :param restarts: integer - number of restarts
        """
        self.name = "PGD With Random Restarts"
        self.specifics = "PGD With Random Restarts - " \
                         f"eps: {eps} - alpha: {alpha} - " \
                         f"num_iter: {num_iter} - restarts: {restarts}"
        self.alpha = alpha
        self.num_iter = num_iter
        self.restarts = restarts
        self.eps = eps
        self.model = model
        self.scaler = scaler
        self.clip_min = self.scaler.transform(np.array(mins).reshape(1, -1)).flatten()
        self.clip_max = self.scaler.transform(np.array(maxs).reshape(1, -1)).flatten()

        # Adjust clip values to ensure clip_min < clip_max
        if np.any(self.clip_min >= self.clip_max):
            raise ValueError("Invalid `clip_values`: min >= max.")

        # Adjust for equal minimum and maximum adjustments
        self.clip_max[eq_min_max.tolist()] += 1e-9  # Small adjustment to avoid min >= max
        self.mask_idx = mask_idx

    def run_attack(self, clean_samples, true_labels):
        n = clean_samples.shape[0]
        mask_feat = np.zeros((clean_samples.shape[1],))
        mask_feat[self.mask_idx] = 1

        # ----- Attack

        true_labels = np.squeeze(true_labels)
        target = 1 - true_labels
        target = np.expand_dims(target, axis=1)

        kc_classifier = kc(self.model, clip_values=(self.clip_min, self.clip_max), nb_classes=2, input_shape=(756),
                           loss_object=tf.keras.losses.BinaryCrossentropy())
        pgd = PGD(kc_classifier)
        pgd.set_params(eps=self.eps, verbose=False, max_iter=self.num_iter, num_random_init=self.restarts, norm=2,
                       eps_step=self.alpha, targeted=True)

        attacks = pgd.generate(x=clean_samples, y=target, mask=mask_feat)

        return attacks
