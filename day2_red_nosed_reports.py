def is_increasing(report):
    """Check if the report is increasing and each difference is between 1 and 3."""
    return all(0 < y - x <= 3 for x, y in zip(report, report[1:]))

def is_decreasing(report):
    """Check if the report is decreasing and each difference is between -3 and -1."""
    return all(-3 <= y - x < 0 for x, y in zip(report, report[1:]))

def evaluate_report(report):
    """Evaluate if the report is safe based on increasing or decreasing conditions."""
    report = [int(level) for level in report]  # Convert levels to integers
    
    if is_increasing(report):
        # print("This report is SAFE: Increasing trend.")
        return "SAFE"
    elif is_decreasing(report):
        # print("This report is SAFE: Decreasing trend.")
        return "SAFE"
    else:
        # print("This report is UNSAFE.")
        return "UNSAFE"



# Main execution
filename = "input_day2.txt"
with open(filename, "r") as file:
    data = [line.strip().split() for line in file.readlines()]
safe_count = 0


for report in data:
    evaluate_report(report)
    if evaluate_report(report) == "SAFE":
        safe_count +=1
print(safe_count, "reports are safe")
#686 reports are safe
