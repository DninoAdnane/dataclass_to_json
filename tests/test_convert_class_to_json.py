def _compare_two_jsons_structure(json1, json2):
    """used to compare two json if they have the same structure (same keys)

    Args:
        json1 (dict): the first json
        json2 (dict): the second json

    Returns:
        Boolean: return_description_ True if they have the same structure,
        False otherwise
    """
    for key in json1.keys():
        if isinstance(json1[key], dict):
            _compare_two_jsons_structure(json1[key], json2[key])
        if isinstance(json1[key], list):
            if len(json1[key]) and isinstance(
                json1[key][0], dict
            ):  # sometimes, we have an output where the list is empty!!!
                _compare_two_jsons_structure(json1[key][0], json2[key][0])
        if key not in json2:
            return False
