import datetime
import test_times

def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    if start_time_s > end_time_s: 
        raise ValueError("The start time is after the end time.")
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]

# Ensure that your main code stops this. Modify time_range to produce an error (ValueError) with a meaningful message when a "backwards" time_range is passed to it - this is called input validation.
# Write a test that tries to generate a time range for a date going backwards.
# Use pytest.raises to check for that error in the test.
# Commit, push and link to this issue (including Answers UCL-COMP0233-24-25/RSE-Classwork#13).
# What other similar tests could we add?


def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            # print(f'This is the low {low}')
            high = min(end1, end2)
            # print(f'This is the high {high}')
            if low < high: # Added the if statement
                overlap_time.append((low, high))
    return overlap_time

if __name__ == "__main__":
    large = time_range("2010-01-12 10:00:00", "2010-01-12 9:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    # print(short)
    # print(compute_overlap_time(large, short))

    overlap1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    
    print(compute_overlap_time(large, short))
