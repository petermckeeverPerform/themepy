import matplotlib as mpl
from cycler import cycler
from .set_theme import set_params, list_themes



class Theme:

    def __init__(self, theme_name=None):
        self.theme_list = list_themes()
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
            self.dpi = 100

        else:
            set_params(self, theme_name)
                
    def __repr__(self):
        return self.theme_name + " is the active theme"
    def __str__(self):
        return self.theme_name + " is the active theme"

    def set_theme(self, theme_name=None):
        set_params(self, theme_name)

        return self

    def set_font(self, fontfamily=None):
        if fontfamily is None:
            self.fontfamily = mpl.rcParams['font.family']
        else:
            self.fontfamily = fontfamily
            mpl.rcParams['font.family'] = fontfamily
            self.title_font = {"fontfamily": fontfamily}
            self.body_font = {"fontfamily": fontfamily}
        
        return self

    def set_title_font(self, title_font=None):
        if title_font is None:
            self.title_font = {"fontfamily": mpl.rcParams['font.family']}
        else:
            self.title_font = {"fontfamily": title_font}

        return self

    def set_body_font(self, body_font=None):
        if body_font is None:
            self.body_font = {"fontfamily": mpl.rcParams['font.family']}
        else:
            self.body_font = {"fontfamily": body_font}

        return self

    def set_pips(self, state=True):
        if state in ["on", True]:    
            mpl.rcParams['xtick.bottom'] = True
            mpl.rcParams['ytick.left'] = True
        elif state in ["off", False]:
            mpl.rcParams['xtick.bottom'] = False
            mpl.rcParams['ytick.left'] = False

        else:
            raise NameError("unrecognised state. Must be one of True/False or 'on'/'off")

        return self

    def set_spines(self,state="on", which=["top", "right", "bottom", "left"]):
        
        if state == "on":
            switch = True
        else:
            switch = False
        
        for spine in which:
            mpl.rcParams['axes.spines.'+spine] = switch

        return self

    def set_ticklabel_size(self, size="medium", which="both"):

        if (type(size) is str) & (size not in ["small","medium","large"]):
            raise ValueError("""{} is not a value size arguement. size must either be a value or one of xx-small, x-small, small, medium, large, x-large, xx-large, smaller, larger""".format(size))   

        if which == "both":
            mpl.rcParams['xtick.labelsize'] = size
            mpl.rcParams['ytick.labelsize'] = size

        elif which == "x":
            mpl.rcParams['xtick.labelsize'] = size
        
        elif which == "y":
            mpl.rcParams['ytick.labelsize'] = size
        
        else:
            raise KeyError("{} is not a valid arg. Must be 'both' or one of 'x' or 'y'".format(which))

        return self
