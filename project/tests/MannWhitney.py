from scipy.stats import mannwhitneyu


# Example data for two independent samples
sample1 = [85, 92, 78, 89, 91]
sample2 = [69, 74, 82, 68, 73]

# Perform Mann-Whitney U test
statistic, p_value = mannwhitneyu(sample1, sample2)
print ("I'm here")
# Output the results
print("Mann-Whitney U statistic:", statistic)
print("p-value:", p_value)

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the samples.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the samples.")
