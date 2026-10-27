import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	mx = np.max(scores, axis=0)
	denominator = np.sum(np.exp(scores - mx), axis=0)
	softmax = np.exp(scores - mx)/denominator
	log_softmax = np.log(softmax)
	return log_softmax
	