import matplotlib as mpl


def get_rcParams_containing(string="", return_values=True):
    """helper to search rcParams for keys containing a specific string, eg. "axes"

    Args:
        string (str): string that rcParam keys should contain. Defaults to "" returning all rcParams.
        return_values (bool, optional): whether to return the values in addition to the keys. Defaults to True.

    Returns:
        dict: rcParams with keys containing `string`
    """
    if return_values:
        return {key: val for key, val in dict(mpl.rcParams).items() if string in key}
    else:
        return [key for key in dict(mpl.rcParams).keys() if string in key]
