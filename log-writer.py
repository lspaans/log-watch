#!/usr/bin/env python

import os
import random
import sys
import time

FILE_NAME = './random-data.log'
FILE_SIZE = 1048576
MIN_SLEEP_SECONDS = 0
MAX_SLEEP_SECONDS = 5
MIN_WORDS = 5
MAX_WORDS = 10
MIN_WORD_LENGTH = 5
MAX_WORD_LENGTH = 10
PROGRAM = sys.argv[0]
SEVERITY_WEIGHTS = (
    ('ERROR', 1),
    ('WARNING', 5),
    ('CRITICAL', 1),
    ('NOTICE', 20),
    ('INFO', 20),
    ('EMERGENCY', 1)
)
TIME_MASK = '%Y-%m-%d %H:%M:%S'

if len(sys.argv) > 1:
    FILE_NAME = sys.argv[1]


def get_letter():
    return(random.choice(
        map(lambda n: chr(n), xrange(ord('A'), ord('Z')+1)) +
        map(lambda n: chr(n), xrange(ord('a'), ord('z')+1))
    ))


def get_log_line():
    return('{time} {program}[{pid}] {severity}: {message}\n'.format(
        time=get_time(),
        program=get_program(),
        pid=get_pid(),
        severity=get_severity(),
        message=get_message()
    ))


def get_message(min_words=MIN_WORDS, max_words=MAX_WORDS):
    return(' '.join(map(lambda n: get_word(), xrange(
        random.choice(xrange(min_words, max_words+1)))
    )))


def get_pid():
    return(os.getpid())


def get_program(program=PROGRAM):
    return(os.path.splitext(os.path.basename(program))[0])


def get_severity(weights=SEVERITY_WEIGHTS):
    return(random.choice(reduce(lambda a, b: a + b, map(
        lambda w: map(lambda n: w[0], xrange(w[1])), weights
    ))))


def get_sleep(min_seconds=MIN_SLEEP_SECONDS, max_seconds=MAX_SLEEP_SECONDS):
    return(random.choice(xrange(min_seconds, max_seconds+1)))


def get_time(mask=TIME_MASK):
    return(time.strftime(mask))


def get_word(
    min_length=MIN_WORD_LENGTH,
    max_length=MAX_WORD_LENGTH
):
    return(''.join(map(lambda n: get_letter(), xrange(
        random.choice(xrange(min_length, max_length+1)))
    )))


def write_log(file_name=FILE_NAME, file_size=FILE_SIZE):
    bytes_written = 0
    try:
        with open(file_name, 'a+') as f:
            while bytes_written < file_size:
                log_line = get_log_line()
                bytes_written += len(log_line)
                f.write(log_line)
                f.flush()
                time.sleep(get_sleep())
    except KeyboardInterrupt as e:
        pass


def main():
    write_log()


if __name__ == '__main__':
    main()
