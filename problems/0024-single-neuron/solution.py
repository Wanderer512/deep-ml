import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> tuple[list[float], float]:
    """Computes neuron probabilities (sigmoid) and mean squared error."""
    probabilities = []
    
    for sample in features:
        # 1. Compute dot product and add bias
        linear_comb = sum(f * w for f, w in zip(sample, weights)) + bias
        
        # 2. Numerically stable sigmoid activation
        if linear_comb >= 0:
            prob = 1 / (1 + math.exp(-linear_comb))
        else:
            z = math.exp(linear_comb)
            prob = z / (1 + z)
            
        probabilities.append(prob)
    
    # 3. Compute Mean Squared Error (MSE)
    squared_errors = [(label - prob) ** 2 for label, prob in zip(labels, probabilities)]
    mse = sum(squared_errors) / len(labels) if labels else 0.0
    
    return probabilities, mse