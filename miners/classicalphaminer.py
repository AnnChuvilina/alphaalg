import itertools
from snakes.nets import *


def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(1, len(s) + 1))


def alphaminer(log):
    net = PetriNet(log.name)
    transitions = list()
    for activity in log.activities():
        transition = Transition(activity)
        transitions.append(transition)
        net.add_transition(transition)

    footprint = dict()
    greater = set([(t[i-1], t[i]) for t in log.traces() for i in range(1, len(t)) if len(t) > 1])
    for a1 in log.activities():
        for a2 in log.activities():
            rel = '#'
            if (a1, a2) in greater and not (a2, a1) in greater:
                rel = '->'
            elif (a1, a2) in greater and (a2, a1) in greater:
                rel = '||'
            if rel != '#':
                footprint[(a1, a2)] = rel

    powerA = list(powerset(log.activities()))
    powerB = list(powerA)
    placeset = list()
    for A in powerA:
        for B in powerB:
            items = list(A)+list(B)
            fail = False
            for r in range(len(items)):
                for c in range(len(items)):
                    if r < len(A) and c < len(A) and footprint.get((items[r], items[c]), '#') == '#':
                        continue
                    elif r < len(A) and c >= len(A) and footprint.get((items[r], items[c]), '#') == '->':
                        continue
                    elif r >= len(A) and c < len(A) and footprint.get((items[c], items[r]), '#') == '->':
                        continue
                    elif r >= len(A) and c >= len(A) and footprint.get((items[r], items[c]), '#') == '#':
                        continue
                    else:
                        fail = True
                        break
                if fail:
                    break
            if not fail:
                placeset.append([set(A), set(B)])
    for p in placeset:
        supersets = [s for s in placeset if s != p and s[0] >= p[0] and s[1] >= p[1]]
        if not supersets:
            placename = ''.join(list(sorted([str(a) for a in p[0]])))+'->'+''.join(list(sorted([str(a) for a in p[1]])))
            place = Place(placename)
            net.add_place(place)
            for t in transitions:
                if t.name in p[1]:
                    net.add_input(placename, t.name, Variable('x'))
                elif t.name in p[0]:
                    net.add_output(placename, t.name, Variable('x'))
    startplace = Place('start', [0])
    endplace = Place('end')
    net.add_place(startplace)
    net.add_place(endplace)
    ti = set([t[0] for t in log.traces()])
    to = set([t[-1] for t in log.traces()])
    for i in ti:
        for t in transitions:
            if t.name == i:
                net.add_input('start', t.name, Variable('x'))
    for o in to:
        for t in transitions:
            if t.name == o:
                net.add_output('end', t.name, Variable('x'))

    return net
