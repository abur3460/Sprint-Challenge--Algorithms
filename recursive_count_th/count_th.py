'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    count = 0

    list_breakdown = list(word)

    # base case for 2 letters
    if(len(list_breakdown)) < 2:
        return 0

    elif list_breakdown[0] == "t" and list_breakdown[1] == "h":
        count += 1

    return count + count_th(list_breakdown[1:])
