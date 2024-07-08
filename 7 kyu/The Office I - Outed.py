def outed(meet, boss):
    sums = sum(i for i in meet.values()) + meet[boss]
    av = sums / len(meet)
    return 'Nice Work Champ!' if av > 5 else 'Get Out Now!'