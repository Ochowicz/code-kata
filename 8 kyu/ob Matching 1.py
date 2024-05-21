def job_matching(candidate, job):
    if 'min_salary' not in candidate or 'max_salary' not in job:
        raise ValueError
    min_salary = candidate['min_salary']
    max_salary = job['max_salary']
    min_salary_with_wiggle_room = 0.9 * min_salary
    return min_salary_with_wiggle_room <= max_salary