"""Scrivere una funzione che prende in input una lista L e restituisce una lista di |L|!
liste in cui ciascuna lista contiene una diversa permutazione degli elementi della lista input L"""


def permute1(seq):
    if not seq:  # Shuffle any sequence: list
        return [seq]  # Empty sequence
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]  # Delete current node
            for x in permute1(rest):  # Permute the others
                res.append(seq[i:i + 1] + x)  # Add node at front
    return res



print(permute1([1,2,3,4,5]))