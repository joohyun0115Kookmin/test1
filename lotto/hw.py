# The Best Time to Party
#
# Given a list of intervals when celebrities will be at the party.
# Output is the time that you want to go the party when the maximum number of
# celebrities are still there.

# Brute force algorithm here; assumes start/end times are non-negative ints.

small_sched = [(1, 3), (2, 4), (2, 3)]

sched = [(6, 8), (10, 11), (10, 12), (6, 12), (6, 7), (7, 8),
         (7, 10), (8, 9), (8, 10), (9, 12), (9, 10), (11, 12)]


def best_time_to_party(schedule):
    # Find party start time and end time
    party_start = schedule[0][0]
    party_end = schedule[0][1]
    for c in schedule:
        party_start = min(c[0], party_start)
        party_end = max(c[1], party_end)

    # Compute count of celebrities at each time
    count = celebrity_density(schedule, party_start, party_end)
    print('celebrity count =', count)

    # Range over times to find the time when the max number of celebrities are around.
    max_count = 0
    for i in range(party_start, party_end + 1):
        if count[i] > max_count:
            max_count = count[i]
            best_time = i

    # Output the best time to party.
    # Note that the \ means the statement continues on the next line.
    print('Best time to attend the party is at', best_time, \
          'o\'clock', ':', max_count, 'celebrities will be attending!')


def celebrity_density(sched, start, end):
    # Initialize a list of length end + 1 to all 0's
    count = [0] * (end + 1)
    # i ranges over different times
    for i in range(start, end + 1):
        count[i] = 0
        for c in sched:
            # Check if celebrity c is around at time i
            if c[0] <= i and c[1] > i:
                count[i] += 1

    return count


# best_time_to_party(small_sched)
best_time_to_party(sched)
