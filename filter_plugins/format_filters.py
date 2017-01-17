

def format_one(input, format):
    return format.format(input)


class FilterModule(object):
    def filters(self):
        return {'format_one': format_one}