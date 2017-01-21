__all__ = ["MyoptError","myopt"]

try:
    from gettext import gettext as _
except ImportError:
    # Bootstrapping Python: gettext's dependencies not built yet
    def _(s): return s


class MyoptError(Exception):
    opt = ''
    msg = ''

    def __init__(self, msg, opt=''):
        self.msg = msg
        self.opt = opt
        Exception.__init__(self, msg, opt)

    def __str__(self):
        return self.msg


def myopt(args, shortopts, longopts = []):
    """getopt(args, options[, long_options]) -> opts, args

    >>> shortopts = 'y:'
    >>> args = '-y 2017'
    >>> myopt(args.split(), shortopts)
    ([('-y', '2017')], [])

    >>> longopts = ['year=']
    >>> args = '--year 2017'
    >>> myopt(args.split(), shortopts=shortopts, longopts=longopts)
    ([('--year', '2017')], [])

    """

    opts = []
    if type(longopts) == type(""):
        longopts = [longopts]
    else:
        longopts = list(longopts)
    while args and args[0].startswith('-') and args[0] != '-':
        if args[0] == '--':
            args = args[1:]
            break
        if args[0].startswith('--'):
            # print('in long')
            opts, args = do_longs(opts, args[0][2:], longopts, args[1:])
        else:
            # print('in short', args, shortopts)
            opts, args = do_shorts(opts, args[0][1:], shortopts, args[1:])

    return opts, args


def do_longs(opts, opt, longopts, args):
    try:
        i = opt.index('=')
    except ValueError:
        optarg = None
    else:
        opt, optarg = opt[:i], opt[i+1:]

    has_arg, opt = long_has_args(opt, longopts)
    if has_arg:
        if optarg is None:
            if not args:
                raise MyoptError(_('option --%s requires argument') % opt, opt)
            optarg, args = args[0], args[1:]
    elif optarg is not None:
        raise MyoptError(_('option --%s must not have an argument') % opt, opt)
    opts.append(('--' + opt, optarg or ''))
    return opts, args


def long_has_args(opt, longopts):
    # print(opt, longopts)
    possibilities = [o for o in longopts if o.startswith(opt)]
    if not possibilities:
        raise MyoptError(_('option --%s not recognized') % opt, opt)
    # Is there an exact match?
    if opt in possibilities:
        return False, opt
    elif opt + '=' in possibilities:
        return True, opt
    # No exact match, so better be unique.
    if len(possibilities) > 1:
        # XXX since possibilities contains all valid continuations, might be
        # nice to work them into the error msg
        raise MyoptError(_('option --%s not a unique prefix') % opt, opt)
    assert len(possibilities) == 1
    unique_match = possibilities[0]
    has_arg = unique_match.endswith('=')
    if has_arg:
        unique_match = unique_match[:-1]
    return has_arg, unique_match


def do_shorts(opts, optstring, shortopts, args):
    while optstring != '':
        opt, optstring = optstring[0], optstring[1:]
        if short_has_arg(opt, shortopts):
            if optstring == '':
                if not args:
                    raise MyoptError(_('option -%s requires argument') % opt,
                                      opt)
                optstring, args = args[0], args[1:]
            optarg, optstring = optstring, ''
        else:
            optarg = ''
        opts.append(('-' + opt, optarg))
    return opts, args


def short_has_arg(opt, shortopts):
    for i in range(len(shortopts)):
        if opt == shortopts[i] != ':':
            return shortopts.startswith(':', i+1)
    raise MyoptError(_('option -%s not recognized') % opt, opt)


if __name__ == '__main__':
    import sys
    import doctest
    doctest.testmod()
    # print(myopt(sys.argv[1:], "a:b", ["alpha=", "beta"]))
