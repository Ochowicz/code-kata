def partition(arr, classifier_method):
    true_list = []
    false_list = []
    for item in arr:
        if classifier_method(item):
            true_list.append(item)
        else:
            false_list.append(item)
    return true_list, false_list