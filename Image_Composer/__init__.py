from .image_compose import napari_experimental_provide_dock_widget

#__version__ = "0.1.7"
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"


def get_module_version():
    return __version__


