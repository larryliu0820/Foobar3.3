import itertools


def get_combos(occurrences, word_len):
    if len(occurrences) < 2:
        return [occurrences]
    elif len(occurrences) == 2:
        combos = [occurrences]
    else:
        combos = itertools.combinations(occurrences, 2)
    result = []
    for combo in combos:
        if abs(combo[1] - combo[0]) >= word_len:
            result.append(combo)
    return result


def answer(chunk, word):
    # your code here
    if word not in chunk:
        return [chunk]
    occurrences = [i for i in range(len(chunk)) if chunk[i:i+len(word)] == word]
    combos = get_combos(occurrences, len(word))
    results = []
    for combo in combos:
        print combo
        result = chunk[:]
        i = 0
        for i in range(len(combo)):
            ind = combo[i] - i * len(word)
            result = result[0:ind] + result[ind+len(word):]
        print result
        if result not in results:
            results.append(result)
    print results
    final_results = []
    for result in results:
        final_results = final_results + answer(result, word)
    return final_results