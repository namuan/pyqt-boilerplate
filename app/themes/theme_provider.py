import darkdetect
from PyQt5.QtGui import QFont, QIcon, QFontDatabase

from app.themes.theme_loader import ThemeLoader, styles_from_file

__pyg_styles = None


def is_dark():
    return darkdetect.isDark()


def configure_theme(app):
    app.setWindowIcon(QIcon(":/icons/app.svg"))

    app.setStyle(ThemeLoader())
    theme_mode = "dark" if is_dark() else "light"
    app.style().load_stylesheet(theme_mode)

    font_db = QFontDatabase()
    font_db.addApplicationFont(":/fonts/JetBrainsMono-Regular.ttf")

    current_font: QFont = QFont("JetBrains Mono")
    current_font.setPointSize(14)
    app.setFont(current_font)


def pyg_styles():
    if __pyg_styles:
        return __pyg_styles
    else:
        pyg_theme = "dark" if is_dark() else "light"
        return styles_from_file(":/themes/pyg-{}.css".format(pyg_theme))
