def calculate_stats(*a):
    stats = {
        'count': len(a),
        'sum': sum(a),
        'average': sum(a) / len(a),
        'max': max(a),
        'min': min(a)
    }
    return stats


c = calculate_stats(1, 2, 3, 4, 5, 6)
print(c)
