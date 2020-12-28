from plugins.apps import Apps
from plugins.calculator import Calculator
from plugins.files import Files
from plugins.search import GoogleSearch, YoutubeSearch

DEFAULT_CALCULATOR = Calculator

DEFAULT_PLUGIN = Apps

PLUGINS = {
    'g': GoogleSearch,
    'y': YoutubeSearch,
    'f': Files,
}
