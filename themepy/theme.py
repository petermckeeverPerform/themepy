import matplotlib as mpl
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
        """
        Passes values from our selected theme (or defaults)

        Input
        =====
        theme_name: str - name of theme to use

        Returns
        =======
        changed properties of instantiated class
        """
        set_params(self, theme_name)

        return self

    def set_font(self, fontfamily=None):
        """
        Sets the font that will be used for plotting.

        Input
        =====
        font_name: str - name of font that is
                  currently availble in matplotlib

        Returns
        =======
        updated self.fontfamily
                self.title_font
                self.body_font

        """
        if fontfamily is None:
            self.fontfamily = mpl.rcParams['font.family']
        else:
            self.fontfamily = fontfamily
            mpl.rcParams['font.family'] = fontfamily
            self.title_font = {"fontfamily": fontfamily}
            self.body_font = {"fontfamily": fontfamily}

        return self

    def set_title_font(self, title_font=None):
        """
        Allows us to use a different font with **kwarg.
        This does not automatically change the title font.
        e.g:
        theme = themepy.Theme()
        theme.set_title_font("Arial")

        fig, ax = plt.subplots(figsize=(8,8))

        ax.set_title("This is a title", **theme.title_font)

        plt.show()

        Input
        =====
        title_font: str - name of font that is
                    currently availble in matplotlib

        Returns
        =======
        updated self.title_font

        """
        if title_font is None:
            self.title_font = {"fontfamily": mpl.rcParams['font.family']}
        else:
            self.title_font = {"fontfamily": title_font}

        return self

    def set_body_font(self, body_font=None):
        """
        Allows us to use a different font with **kwarg.
        This does not automatically change the body font.

        e.g:
        theme = themepy.Theme()
        theme.set_title_font("Arial")

        fig, ax = plt.subplots(figsize=(8,8))

        ax.text(0.5, 0.5,
                "This is a some text", **theme.body_font)

        plt.show()

        Input
        =====
        body_font: str - name of font that is
                   currently availble in matplotlib

        Returns
        =======
        updated self.body_font
        """
        if body_font is None:
            self.body_font = {"fontfamily": mpl.rcParams['font.family']}
        else:
            self.body_font = {"fontfamily": body_font}

        return self

    def set_pips(self, state=True):
        """
        Show or hide tick lines on plots.

        Input
        =====
        state: bool - True of False

        Returns
        =======
        updated mpl.rcParams with ticks toggled on or off
        """
        if state in ["on", True]:
            mpl.rcParams['xtick.bottom'] = True
            mpl.rcParams['ytick.left'] = True
        elif state in ["off", False]:
            mpl.rcParams['xtick.bottom'] = False
            mpl.rcParams['ytick.left'] = False

        else:
            raise NameError("unrecognised state. Must be one of True/False or 'on'/'off")

        return self

    def set_spines(self, state="on", which=["top", "right", "bottom", "left"]):
        """
        Sets the spines on or off. A method in matplotlib
        to turn spines off might be:

        Input
        =====
        state: str - "on" or "off"
        which: list - spines to be turned on or off.

        Returns
        =======
        updated mpl.rcParams for spine visibility
        """
        if state == "on":
            switch = True
        else:
            switch = False

        for spine in which:
            mpl.rcParams['axes.spines.'+spine] = switch

        return self

    def set_ticklabel_size(self, size="medium", which="both"):
        """
        Sets the size of x, y, or both ticklabels.

        Input
        =====
        size: str or int
        which: str - 'both', 'x', or 'y'

        Returns
        =======
        updated mpl.rcParams for x and/or y tick labelsize
        """
        if (type(size) is str) & (size not in ["small", "medium", "large"]):
            raise ValueError("""{} is not a value size arguement. Size must either be a value or one of xx-small, x-small, small, medium, large, x-large, xx-large, smaller, larger""".format(size))

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
