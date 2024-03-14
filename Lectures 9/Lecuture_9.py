"""
Week 9: Greedy algorithm.
"""

def paytoken(remaining:int) -> list:
    """_summary_
        Simple implementing Greedy algorithm with token payment.
    Args:
        remaining (float): Remaining token.

    Returns:
        paid (list): Sequence of paid token.
    """
    paid, token_list = [], [20, 10, 5, 1]
    for token in token_list:
        while remaining >= token:
            paid.append(token)
            remaining -= token
    return paid

if __name__ == "__main__":
    print("Start...")
    
    remaining = 128
    
    print(paytoken(remaining))
    
    print("End...")
