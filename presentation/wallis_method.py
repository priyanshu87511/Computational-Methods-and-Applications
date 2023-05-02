from matplotlib import pyplot as plt

def estimate_pi_wallis(n):
    # Initialize the product to 1
    product = 1

    # Multiply by the fractions in the series
    for i in range(1, n+1):
        numerator = (2*i) * (2*i)
        denominator = (2*i - 1) * (2*i + 1)
        product *= numerator / denominator

    # multiply by 2 to get value of PI
    return product*2

# Example usage: estimate pi using the first 10 fractions in the series
print(estimate_pi_wallis(100))