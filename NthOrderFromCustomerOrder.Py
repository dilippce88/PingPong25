from collections import Counter

def nth_highest_order_count(orders, n):
    # Count orders per customer
    customer_counts = Counter(order['customer_id'] for order in orders)
    
    # Get unique counts sorted descending
    sorted_counts = sorted(set(customer_counts.values()), reverse=True)

    if n > len(sorted_counts):
        return None  # Not enough distinct values

    return sorted_counts[n - 1]

# Example usage
orders = [
    {'order_id': 1, 'customer_id': 'A'},
    {'order_id': 2, 'customer_id': 'B'},
    {'order_id': 3, 'customer_id': 'A'},
    {'order_id': 4, 'customer_id': 'C'},
    {'order_id': 5, 'customer_id': 'B'},
    {'order_id': 6, 'customer_id': 'A'},
    {'order_id': 7, 'customer_id': 'B'},
    {'order_id': 8, 'customer_id': 'D'},
]

nth = 2
result = nth_highest_order_count(orders, nth)
print(f"The {nth} highest number of orders by a single customer is: {result}")