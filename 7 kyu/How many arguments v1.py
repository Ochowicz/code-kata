def args_count(*args, **kwargs):
    count_positional = len(args)
    count_keyword = len(kwargs)
    total_count = count_positional + count_keyword
    return total_count