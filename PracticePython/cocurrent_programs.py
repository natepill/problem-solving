"""
Given a list of pairs of running times(int start, int end) for programs,
 return the maximum amount of programs that were running at one time.
"""


def max_programs_being_run(timeframes):
    """Return the maximum amount of programs that were running at one time."""

    current_time_frame = None
    num_of_programs_running = 0


    for timeframe in timeframes:

        if timeframe[0] >= current_time_frame:
            # end of current



input = [(1,3), (1,4), (2,6), (4,7), (5,8)]
# Answer: 3



# Have a variable tracking the numbers of programs that are currently being run
# Have a variable tracking the largest number of programs being run as we iterate
# Return the max variable
