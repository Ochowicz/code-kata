def who_is_online(friends):
    status_dict = {'online': [], 'offline': [], 'away': []}

    for friend in friends:
        username = friend['username']
        status = friend['status']
        last_activity = friend['last_activity']

        if status == 'offline':
            status_dict['offline'].append(username)
        elif status == 'online':
            if last_activity > 10:
                status_dict['away'].append(username)
            else:
                status_dict['online'].append(username)

    result = {key: value for key, value in status_dict.items() if value}

    return result