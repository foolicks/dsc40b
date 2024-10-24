def histogram(points, bins):
    # Initialize counts for each bin
    counts = [0] * len(bins)
    # Get total number of points
    n = len(points)
    
    # Current bin index we're looking at
    current_bin = 0
    
    # Go through each point once
    for point in points:
        # If the point is past current bin, move to next bin(s)
        while current_bin < len(bins) and point >= bins[current_bin][1]:
            current_bin += 1
            
        # If we've gone through all bins, we're done
        if current_bin >= len(bins):
            break
            
        # If point falls in current bin, increment count
        if bins[current_bin][0] <= point < bins[current_bin][1]:
            counts[current_bin] += 1
    
    # Calculate densities
    densities = []
    for i in range(len(bins)):
        bin_width = bins[i][1] - bins[i][0]
        density = counts[i] / (n * bin_width)
        densities.append(density)
    
    return densities