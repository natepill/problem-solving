"""
Given a list of pairs of running times(int start, int end) for programs,
 return the maximum amount of programs that were running at one time.
"""


def max_programs_being_run(timeframes):
    """Return the maximum amount of programs that were running at one time."""

    current_time_frame = None
    max_number_programs_running = 0
    timeframe_counter = {}

    for timeframe in timeframes:

        for num in range(timeframe[0], timeframe[1]):
            if timeframe_counter[num] is not None:
                timeframe_counter[num] += 1

            else:
                timeframe_counter[num] = 1

    return timeframe_counter

input = [(1,3), (1,4), (2,6), (4,7), (5,8)]

print(max_programs_being_run(input))
# Answer: 3



# Have a variable tracking the numbers of programs that are currently being run
# Have a variable tracking the largest number of programs being run as we iterate
# Return the max variable
