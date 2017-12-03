from itertools import groupby
import sys


class Entry(object):
    __slots__ = ("when", "who", "what")

    def __init__(self, when, who, what):
        self.when = when
        self.who = who
        self.what = what

    def __repr__(self):
        return "when={self.when}, who={self.who}, what={self.what})".format(self=self)


class Item(object):
    __slots__ = ("duration", "who")

    def __init__(self, duration, who):
        self.duration = duration
        self.who = who

    def __repr__(self):
        return "when={self.duration}, who={self.who})".format(self=self)


def load():
    def make(line):
        parts = line.split(',')
        return Entry(int(parts[0].strip()), parts[1].strip(), parts[2].strip())

    with open(input_file, "r") as f:
        return [make(line) for line in f]


def save(items):
    with open(output_file, "w") as f:
        f.write("duration, who")
        for item in items:
            f.write("\n{0}, {1}".format(item.duration, item.who))


def work():
    entries = load()

    keys = []
    groups = []
    entries = sorted(entries, key=lambda x: x.who)
    for k, g in groupby(entries, key=lambda x: x.who):
        groups.append(list(g))
        keys.append(k)

    items = []

    for i in range(0, len(keys)):
        g = groups[i]
        ordered = list(sorted(g, key=lambda x: x.when))

        start = 0
        duration = 0

        for entry in ordered:
            if entry.what == "login":
                start = entry.when
            elif entry.what == "logout":
                duration += entry.when - start

        items.append(Item(duration, keys[i]))

    items = sorted(items, key=lambda x: x.duration, reverse=True)

    save(items)

input_file = sys.argv[1]
output_file = "out.txt"

if len(sys.argv) > 2:
    output_file = sys.argv[2]

work()
