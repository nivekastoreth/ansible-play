
def format_one(value, fmt):
    return fmt.format(value)


def as_minutes(value_spec):
    """
    Utility method for converting strings like '6m' and '8h' into minute values
    :param value_spec:
    :return:
    """
    def from_spec(spec, value):
        if spec == 's':
            return value / 60
        elif spec == 'm':
            return value
        elif spec == 'h':
            return value * 60
        elif spec == 'd':
            return value * 60 * 60
        else:
            raise Exception("Unknown duration format: %s. Supported format is <float>[smhd]: 0.5d" % (value_spec))
    return int(from_spec(
        value_spec[-1:],
        float(value_spec[:-1])
    ))


class FilterModule(object):
    @staticmethod
    def filters():
        return {
            'format_one': format_one,
            'as_minutes': as_minutes
        }


if __name__ == '__main__':
    as_minutes('bob')
