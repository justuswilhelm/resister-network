#!/usr/bin/env python3
from argparse import ArgumentParser
import itertools


def combine(*lst):
    return 1 / sum(1 / i for i in lst)


def parse_given(val):
    return set(int(v) for v in val.split(','))


def print_combination(diff, value, combination):
    print("Deviation: {:+2.2f} Ohm, Candidate: {}, Resistance: {} Ohm".format(
        diff,
        " + ".join("{} Ohm".format(s) for s in combination),
        value,
    ))


def main(target, given, max_combinations=2, num=2):
    combinator = itertools.combinations_with_replacement
    products = sorted(
        (
            (
                target - combine(*lst),
                combine(*lst),
                lst,
            )
            for combination in range(1, max_combinations + 1)
            for lst in combinator(given, combination)
        ),
        key=lambda i: abs(i[0]),
    )

    for p in products[:num]:
        print_combination(*p)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-t', '--target', type=int, required=True)
    parser.add_argument('-c', '--max-combinations', type=int, default=2)
    parser.add_argument('-g', '--given', type=parse_given, default={
        1.5,
        4.7,
        10,
        47,
        100,
        220,
        330,
        470,
        680,
        1000,
        2200,
        3300,
        4700,
        10000,
        22000,
        47000,
    })
    args = parser.parse_args()
    main(args.target, args.given, args.max_combinations)
