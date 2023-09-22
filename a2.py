from typing import List


def match(pattern: List[str], source: List[str]) -> List[str]:
    """Attempts to match the pattern to the source.

    % matches a sequence of zero or more words and _ matches any single word

    Args:
        pattern - a pattern using to % and/or _ to extract words from the source
        source - a phrase represented as a list of words (strings)

    Returns:
        None if the pattern and source do not "match" ELSE A list of matched words
        (words in the source corresponding to _'s or %'s, in the pattern, if any)
    """
    sind = 0  
    pind = 0  
    result: List[str] = [] 

    while pind < len(pattern) or sind < len(source):

        # 1) if we reached the end of the pattern but not source
        if pind == len(pattern) and sind < len(source):
            return None
        # 2) if the current thing in the pattern is a %
        elif pattern[pind] == "%":
            pind += 1
            if pind == len(pattern):
                result.append(" ".join(source[sind:]))
                return result
            else:
                current = sind
                while pattern[pind] != source[sind]:
                    sind += 1
                    if sind == len(source):
                        return None
                result.append(" ".join(source[current:sind]))
            
        # 3) if we reached the end of the source but not the pattern
        elif sind == len(source) and pind < len(pattern): 
            return None
        # 4) if the current thing in the pattern is an _
        elif pattern[pind] == "_":
            # result.append(source[sind])
            result += [source[sind]]
            pind += 1
            sind += 1
        # 5) if the current thing in the pattern is the same as the current thing in the source
        elif pattern[pind] == source[sind]:
            pind += 1
            sind += 1
        # 6) else : this will happen if none of the other conditions are met it
        else:
            return None

    return result


if __name__ == "__main__":
    print(match(["x", "y", "z"], ["x", "y", "z"]))
    assert match(["x", "y", "z"], ["x", "y", "z"]) == [], "test 1 failed"
    print(match(["x", "z", "z"], ["x", "y", "z"]))
    assert match(["x", "z", "z"], ["x", "y", "z"]) == None, "test 2 failed"
    print(match(["x", "y"], ["x", "y", "z"]))
    assert match(["x", "y"], ["x", "y", "z"]) == None, "test 3 failed"

    assert match(["x", "y", "z", "z"], ["x", "y", "z"]) == None, "test 4 failed"
    assert match(["x", "_", "z"], ["x", "y", "z"]) == ["y"], "test 5 failed"
    assert match(["x", "_", "_"], ["x", "y", "z"]) == ["y", "z"], "test 6 failed"
    assert match(["%"], ["x", "y", "z"]) == ["x y z"], "test 7 failed"
    print(match(["x", "%", "z"], ["x", "y","a", "b", "z"]))
    assert match(["x", "%", "z"], ["x", "y", "z"]) == ["y"], "test 8 failed"
    assert match(["%", "z"], ["x", "y", "z"]) == ["x y"], "test 9 failed"
    assert match(["x", "%", "y"], ["x", "y", "z"]) == None, "test 10 failed"
    assert match(["x", "%", "y", "z"], ["x", "y", "z"]) == [""], "test 11 failed"
    assert match(["x", "y", "z", "%"], ["x", "y", "z"]) == [""], "test 12 failed"
    assert match(["_", "%"], ["x", "y", "z"]) == ["x", "y z"], "test 13 failed"
    assert match(["_", "_", "_", "%"], ["x", "y", "z"]) == [
        "x",
        "y",
        "z",
        "",
    ], "test 14 failed"
    
    assert match(["x", "%", "z"], ["x", "y", "z", "z", "z"]) == None, "test 15 failed"
    assert match(["%", "z"], ["x", "y", "w"]) == None, "test 16 failed"

    print("All tests passed!")