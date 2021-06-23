import statistics
s_mode = [54,24,36.09,55.37,92] 

print("MD\t", statistics.median(s_mode))
print("mode\t", statistics.fmean(s_mode))
print("Geometry\t", statistics.geometric_mean(s_mode))
print("Med\t", statistics.median_low(s_mode))
print("medH\t", statistics.median_high(s_mode))
print("mode\t", statistics.mode(s_mode))
print("Median\t", statistics.median(s_mode))
