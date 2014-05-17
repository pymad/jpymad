import collections

from .types import Range, Constraint


try:
    unicode
except NameError:   # python3
    basestring = unicode = str


def is_word(value):
    """Check if value is a MAD-X identifier."""
    return value.isalnum() and value[0].isalpha()


def mad_quote(value):
    """Add quotes to a string value."""
    if is_word(value):
        return value
    quoted = repr(value)
    return quoted[1:] if quoted[0] == 'u' else quoted


def mad_parameter(key, value):
    """
    Format a single MAD-X command parameter.
    """
    key = str(key).lower()
    # the empty string was used in earlier versions in place of None:
    if value is None or value == '':
        return ''
    if isinstance(value, Range):
        return key + '=' + value.first + '/' + value.last
    elif isinstance(value, Constraint):
        constr = []
        if value.min is not None:
            constr.append(key + '>' + value.min)
        if value.max is not None:
            constr.append(key + '<' + value.max)
        if constr:
            return ', '.join(constr)
        else:
            return key + '=' + value.value
    elif isinstance(value, bool):
        return ('' if value else '-') + key
    elif key == 'range':
        if isinstance(value, basestring):
            return key + '=' + value
        else:
            return key + '=' + str(value[0]) + '/' + str(value[1])
    elif isinstance(value, basestring):
        return key + '=' + mad_quote(value)
    elif isinstance(value, collections.Sequence):
        if key == 'column':
            return key + '=' + ','.join(value)
        elif value and all(isinstance(v, basestring) for v in value):
            return key + '=' + ','.join(value)
        else:
            return key + '={' + ','.join(map(str, value)) + '}'
    else:
        return key + '=' + str(value)


def mad_command(*args, **kwargs):
    """
    Create a MAD-X command from its name and parameter list.

    :param args: initial bareword command arguments (including command name!)
    :param kwargs: following named command arguments
    :returns: command string
    :rtype: str

    Examples:

    >>> mad_command('twiss', sequence='lhc')
    'twiss, sequence=lhc;'

    >>> mad_command('option', echo=True)
    'option, echo;'

    >>> mad_command('constraint', betx=Constraint(max=3.13))
    'constraint, betx<3.13;'
    """
    _args = list(args)
    _args += [mad_parameter(k, v) for k,v in kwargs.items()]
    return ', '.join(filter(None, _args)) + ';'
