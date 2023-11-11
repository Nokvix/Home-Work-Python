from random import randint, choice


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrushError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def generate_random_exception():
    exceptions = [
        KillError(),
        DrunkError(),
        CarCrushError(),
        GluttonyError(),
        DepressionError()
    ]

    if randint(1, 10) == 10:
        raise choice(exceptions)


def one_day():
    generate_random_exception()
    return randint(1, 7)


def main():
    karma = 500
    cur_karma = 0
    with open('karma.log', 'w', encoding='utf-8') as karma_log_file:
        while cur_karma < karma:
            try:
                cur_karma += one_day()
            except (KillError, DrunkError, CarCrushError, GluttonyError, DepressionError) as exc:
                karma_log_file.write(f'{type(exc).__name__}\n')


if __name__ == '__main__':
    main()
