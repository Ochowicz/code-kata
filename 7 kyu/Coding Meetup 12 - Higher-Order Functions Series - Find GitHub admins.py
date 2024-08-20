def find_admin(lst, lang):
    return [x for x in lst if x['language'] == lang and x['githubAdmin'] == 'yes']