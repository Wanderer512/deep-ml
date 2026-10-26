import numpy as np

def mmlu_log_prob_score(log_probs: list, correct_answers: list) -> dict:
    """
    Compute MMLU-style log-probability scoring metrics.
    
    Args:
        log_probs: List of lists, where each inner list contains 
                   log-probabilities for each answer choice
        correct_answers: List of correct answer indices (0-indexed)
    
    Returns:
        Dictionary with 'accuracy', 'predictions', and 'avg_correct_prob'
    """
    log_probs = np.array(log_probs, dtype=float)
    correct_answers = np.array(correct_answers)
    
    # 1. Determine predicted answers (choice with highest log-probability)
    predictions = np.argmax(log_probs, axis=1)
    
    accuracy = float(np.mean(predictions == correct_answers))
    
    # 3. Convert log-probabilities to probabilities with numerical stability (stable softmax)
    shifted_log_probs = log_probs - np.max(log_probs, axis=1, keepdims=True)
    probs = np.exp(shifted_log_probs)
    probs /= np.sum(probs, axis=1, keepdims=True)
    
    # Compute average probability assigned to the correct answer across all questions
    correct_probs = probs[np.arange(len(correct_answers)), correct_answers]
    avg_correct_prob = float(np.mean(correct_probs))
    
    return {
        'accuracy': accuracy,
        'predictions': predictions.tolist(),
        'avg_correct_prob': avg_correct_prob
    }