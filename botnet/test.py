import pickle

# Path to your pickle file
metrics_path = '/home/users/nfondop/realistic_adversarial_hardening/botnet/out/virut/fence_10epochs/fence_model_metrics.pickle'

# Reading the pickle file
with open(metrics_path, 'rb') as file:
    metrics = pickle.load(file)

# Now you can use the loaded metrics
print(metrics)

