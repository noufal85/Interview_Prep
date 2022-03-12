from libcst import FlattenSentinel


def is_balanced(parents):

    stack = []
    openings = set('([{')
    matches = [('{','}'),('(',')'),('[',']')]
    for paren in parents:
        if paren in openings:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()

            if (last_open,paren) not in matches:
                return False

    return len(stack) == 0 



