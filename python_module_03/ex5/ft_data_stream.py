#!/usr/bin/env python3

import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:

    names: list[str] = ['alice', 'bob', 'charlie', 'dylan']
    actions: list[str] = ["run", "eat", "sleep", "grab", "move", "climb",
                          "swim", "release", "use"]

    while True:
        event: tuple[str, str] = [random.choice(names), random.choice(actions)]
        yield event


def consume_event(events: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        event = events[index]
        print("Got event from list:", event)
        del events[index]
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    event_list = []
    for i in range(10):
        event_list.append(next(gen))
    print(f"Built list of 10 events: {event_list}")
    for i in consume_event(event_list):
        print("Remains in list:", event_list)


if __name__ == "__main__":
    main()
