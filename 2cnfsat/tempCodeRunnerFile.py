    if (index % 2 == 0):
        if (assignments[index] == -1 or assignments[index + 1] == 1):
            contradictions += 1
            return asList
        else:
            assignments[index] = 1
            assignments[index + 1] = -1
    else:
        if (assignments[index] == -1 or assignments[index - 1] == 1):
            contradictions += 1
            return asList
        else:
            assignments[index] = 1
            assignments[index - 1] = -1