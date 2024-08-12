def largest(n, xs):
    return (sorted(xs, reverse=True)[0:n])[::-1]