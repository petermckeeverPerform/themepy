import matplotlib as mpl
from .set_theme import set_params, list_themes
import os.path as path


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

    def set_background(self, facecolor, figure=True, ax=True):
        """[summary]

        Args:
            facecolor (string): color to set as background
            figure (bool, optional): Apply to matplotlib figure Defaults to True.
            ax (bool, optional): Apply to matplotlib ax background. Defaults to True.
        """
        if figure:
            mpl.rcParams['figure.facecolor'] = facecolor
            mpl.rcParams['savefig.facecolor'] = facecolor
        if ax:
            mpl.rcParams['axes.facecolor'] = facecolor

        self.background = facecolor

        return self

    def set_plot_colors(self, primary_color=None, secondary_color=None,
                        tertiary_color=None, fourth_color=None,
                        fifth_color=None, sixth_color=None):
        """[summary]

        Args:
            primary_color ([type], optional): [description]. Defaults to None.
            secondary_color ([type], optional): [description]. Defaults to None.
            tertiary_color ([type], optional): [description]. Defaults to None.
            fourth_color ([type], optional): [description]. Defaults to None.
            fifth_color ([type], optional): [description]. Defaults to None.
            sixth_color ([type], optional): [description]. Defaults to None.
        """

        current_cycler = [x['color'] for x in list(mpl.rcParams['axes.prop_cycle'])]
        set_colors = [primary_color, secondary_color,
                      tertiary_color, fourth_color,
                      fifth_color, sixth_color]
        i = 0
        for color in set_colors:
            if color is not None:
                current_cycler[i] = color
            i += 1

        mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=current_cycler)
        self.primary_color = current_cycler[0]
        self.secondary_color = current_cycler[1]
        self.tertiary_color = current_cycler[2]
        self.fourth_color = current_cycler[3]

        return self

    def set_font(self, fontfamily=None, color=None):
        """Sets the font that will be used for plotting.

        Args:
            fontfamily (str, optional): name of font that is
                  currently availble in matplotlib. Defaults to None.
            color (string, optional): color as name, hexcode, or RGB. Defaults to None.

        Returns:
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

        if color is None:
            self.fontcolor = mpl.rcParams['axes.labelcolor']
        else:
            self.fontcolor = color
            mpl.rcParams['text.color'] = color
            mpl.rcParams['axes.labelcolor'] = color
            mpl.rcParams['xtick.color'] = color
            mpl.rcParams['ytick.color'] = color
            self.title_font.update({"color": color})
            self.body_font.update({"color": color})

        return self

    def set_title_font(self, title_font=None, color=None):
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

        if color is not None:
            self.title_font.update({"color": color})

        return self

    def set_body_font(self, body_font=None, color=None):
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

        if color is not None:
            self.body_font.update({"color": color})

        return self

    def set_pips(self, state=True, color=None):
        """
        Show or hide tick lines on plots.

        Input
        =====
        state: bool - True or False
        color: str

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

        if color is not None:
            mpl.rcParams['xtick.color'] = color
            mpl.rcParams['ytick.color'] = color

        return self

    def set_spines(self, state="on",
                   which=["top", "right", "bottom", "left"],
                   color=None,
                   linewidth=None):
        """
        Sets the spines on or off. A method in matplotlib
        to turn spines off might be:

        Input
        =====
        state: str - "on" or "off"
        which: list - spines to be turned on or off.
        color: (optional) str - option to change color of spine

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

        if color is not None:
            mpl.rcParams['axes.edgecolor'] = color

        if linewidth is not None:
            mpl.rcParams['axes.linewidth'] = linewidth

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

    def set_grid(self, state="on", which=None, axis=None, color=None,
                 alpha=None, linestyle=None, linewidth=None):
        """
        Sets the grid on or off.

        Input
        =====
        state: str - "on" or "off"
        which: (optional) str - {'major', 'minor', 'both'}
        axis: (optional) str - {"both", "x", "y"}
        color: (optional) str - grid color
        alpha: (optional) str - grid alpha
        linestyle: (optional) str - grid linestyle
        linewidth: (optional) str - grid linewidth

        Returns
        =======
        updated mpl.rcParams for the axes grid

        """
        if state == "on":
            switch = True
        else:
            switch = False

        mpl.rcParams['axes.grid'] = switch
        mpl.rcParams['polaraxes.grid'] = switch
        mpl.rcParams['axes3d.grid'] = switch

        if which is not None:
            mpl.rcParams['axes.grid.which'] = which

        if color is not None:
            mpl.rcParams['grid.color'] = color

        if axis is not None:
            mpl.rcParams['axes.grid.axis'] = axis

        if alpha is not None:
            mpl.rcParams['grid.alpha'] = alpha

        if linestyle is not None:
            mpl.rcParams['grid.linestyle'] = linestyle

        if linewidth is not None:
            mpl.rcParams['grid.linewidth'] = linewidth

        return self

    def set_updated_rcparams(self):
        """
        sets the non-default rcParams to updated_params
        """
        self.updated_params = {}

        for key, val in mpl.pyplot.rcParams.items():
            default = mpl.rcParamsDefault[key]
            if default != val:
                self.updated_params[key] = val

        if 'axes.prop_cycle' in self.updated_params:
            cycler_ = self.updated_params.pop('axes.prop_cycle')
            cycler_colors = cycler_.by_key()['color']
            self.updated_params['cycler-prop-cycles'] = cycler_colors

    def add_theme(self, theme_name):
        """
        saves the non-default params of the theme locally to /themes/[theme_name].txt

        Input
        =====
            theme_name (string): the name of the theme
        """
        if theme_name in list_themes():
            choice = input(f"A theme named {theme_name} already exists, would you like to overwrite? [y/n]")
            if "y" in choice.lower():
                self.set_updated_rcparams()
                with open(path.dirname(path.abspath(__file__))+'/themes/'+theme_name+'.txt', 'w') as file:
                    print(str(self.updated_params).replace(', ', ',\n'), file=file)

                print(f"Theme {theme_name} successfully overwritten")
            else:
                print("please use a different theme name")

        else:
            self.set_updated_rcparams()
            with open(path.dirname(path.abspath(__file__))+'/themes/'+theme_name+'.txt', 'w') as file:
                print(str(self.updated_params).replace(', ', ',\n'), file=file)

            print(f"Theme {theme_name} successfully added locally")
