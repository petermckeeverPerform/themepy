import matplotlib as mpl
from cycler import cycler
import os
import ast
import os.path as path


def list_themes():
    """
    Displays list of current themes found in themes folder
    """

    theme_list = os.listdir(path.dirname(path.abspath(__file__))+'/themes/')
    # only list .txt files and  drop .txt extension from name
    theme_list = [x.split(".")[0] for x in theme_list if ".txt" in x in theme_list]
    
    return theme_list


def set_params(self, theme_name=None):
    """
    Passes values from our selected theme (or defaults)
    Input
    =====
    theme_name: str - name of theme to use

    Returns
    =======
    changed properties of instantiated class
    """

    self.theme_name = None

    if theme_name is None:
        mpl.rcParams.update(mpl.rcParamsDefault)
        self.theme_name = "Matplotlib"
        self.background = mpl.rcParams['figure.facecolor']
        self.primary_color = '#1f77b4'
        self.secondary_color = '#ff7f0e'
        self.tertiary_color = '#2ca02c'
        self.markings = "k"
        self.fontfamily = mpl.rcParams['font.family']
        self.title_font = {"fontfamily": mpl.rcParams['font.family']}
        self.body_font = {"fontfamily": mpl.rcParams['font.family']}

    elif theme_name.lower() in list_themes():
        theme_dict = (ast.literal_eval(
                        open(path.dirname(path.abspath(__file__))+"/themes/" +
                             theme_name +
                             ".txt", 'r').read()))

        self.theme_name = theme_name
        param_keys = theme_dict.keys()
        param_vals = theme_dict.values()
        for key, val in zip(param_keys, param_vals):
            if key == 'cycler-prop-cycles':
                pass
            else:
                mpl.rcParams[key] = val

        c_cycler = []
        i = 0
        for i in range(len(theme_dict['cycler-prop-cycles'])):
            c_cycler.append(theme_dict['cycler-prop-cycles'][i])


        self.background = mpl.rcParams['figure.facecolor']
        self.primary_color = c_cycler[0]
        self.secondary_color = c_cycler[1]
        self.tertiary_color = c_cycler[2]
        self.markings = "lightgrey"
        self.fontfamily = mpl.rcParams['font.family']
        self.title_font = {"fontfamily": mpl.rcParams['font.family']}
        self.body_font = {"fontfamily": mpl.rcParams['font.family']}

    else:
        raise NameError("This theme does not exist. Choose one of the existing themes - found by running themepy.list_themes()")

    return self
