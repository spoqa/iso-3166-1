import enum
import os


__all__ = 'Country', 'codes',


def read_from_csv(filename, sep='|'):
    table = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            codes = line.split(sep)
            table[codes[1]] = {
                'english_short_name': codes[0],
                'alpha2': codes[1],
                'alhpha3': codes[2],
                'numeric': codes[3],
            }
    return table


codes = read_from_csv(os.path.join(os.path.dirname(__file__),
                                   'table.csv'))


def update_enum_dict(locals_, table):
    for code in table.keys():
        locals_[code.lower()] = code


class Country(enum.Enum):

    update_enum_dict(locals(), codes)

    @property
    def alpha2(self):
        return codes[self.value]['alpha2']

    @property
    def alpha3(self):
        return codes[self.value]['alpha3']

    @property
    def numeric(self):
        return codes[self.value]['numeric']

    @property
    def english_short_name(self):
        return codes[self.value]['english_short_name']
