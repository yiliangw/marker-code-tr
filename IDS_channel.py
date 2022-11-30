import random
import symbols as sym


def __gen_noisy_sample(gold, sub_p, del_p, ins_p):
    symbols = sym.all()
    res = []
    for w in gold:
        r = random.random()
        if r < sub_p:
            res.append(random.choice(symbols))
        elif r < sub_p + ins_p:
            res.append(random.choice(symbols))
            res.append(w)
        elif r > sub_p+ins_p+del_p:
            res.append(w)
    return ''.join(res)

def generate_noisy_samples(gold, n, sub_p, del_p, ins_p):
    res = []
    for i in range(n):
        res.append(__gen_noisy_sample(gold, sub_p, del_p, ins_p))
    return res

