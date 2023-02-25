def solution(a, b, c):
    # transfer to ascii code
    skip = sorted([ord(i) for i in b])
    result = [ord(i) for i in a]
    alphabet = [i for i in range(97, 123)]
    answer = []

    for i in skip:
        alphabet.remove(i)

    for i in result:
        while i not in alphabet:
            i += 1
        tmp = alphabet.index(i)+ c

        if tmp >= (26 - len(b)):
            tmp -= (26 - len(b))* (tmp // (26 - len(b)))

        answer.append(chr(alphabet[tmp]))

    return "".join(answer)
