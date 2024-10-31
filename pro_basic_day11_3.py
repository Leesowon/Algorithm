def solution(my_string, indices):
    indices.sort(reverse=True)

    for i in indices:
        for s in range(len(my_string)):
            if i == s:
                my_string = my_string[:i] + my_string[i + 1:]
    return my_string