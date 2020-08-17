import matplotlib as mpl
from cycler import cycler
import os
import ast
import os.path as path

def list_themes():

    theme_list = os.listdir(path.dirname(path.abspath(__file__))+'/themes/')
    theme_list = [x.split(".")[0] for x in theme_list if "__" not in x in theme_list][1:]

    return theme_list



def set_params(self, theme_name=None):
    """
    use as:

    set_theme("opta") #standard Opta theme
    set_theme("OptaPro") #OptaPro theme. accepts upper or lowercase
    set_theme("opta-dark") #Opta with dark colours
    set_theme("statsperform") #Statsperform vanilla theme
    set_theme() # revert to default theme.

    requires matplotlib to run

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
                            ".txt", 'r').read())
                        )

        self.theme_name = theme_name
        mpl.rcParams['xtick.color'] = theme_dict['xtick.color']
        mpl.rcParams['ytick.color'] = theme_dict['ytick.color']
        mpl.rcParams['font.family'] = theme_dict['font.family']
        mpl.rcParams['text.color'] = theme_dict['text.color']
        mpl.rcParams['figure.facecolor'] = theme_dict['figure.facecolor']
        mpl.rcParams['figure.edgecolor'] = theme_dict['figure.edgecolor']
        mpl.rcParams['axes.facecolor'] = theme_dict['axes.facecolor']
        mpl.rcParams['axes.edgecolor'] = theme_dict['axes.edgecolor']
        mpl.rcParams['savefig.edgecolor'] = theme_dict['savefig.edgecolor']
        mpl.rcParams['savefig.facecolor'] = theme_dict['savefig.facecolor']
        mpl.rcParams['grid.color'] = theme_dict['grid.color']

        c_cycler = []
        i = 0
        for i in range(len(theme_dict['cycler-prop-cycles'])):
            c_cycler.append(theme_dict['cycler-prop-cycles'][i])
        mpl.rcParams['axes.prop_cycle'] = (cycler
                                            (color=c_cycler))
        mpl.rcParams['axes.titlesize'] = 20
        mpl.rcParams['axes.titleweight'] = "regular"

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
