__title__ = "Test 07/05/2022"
__author__ = "SAS FERMI"
__doc__ = "Ceci est un commentaire ! :)..."

# dependencies
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('IronPython.Wpf')

# find the path of ui.xaml
from pyrevit import UI
from pyrevit import script

xamlfile = script.get_bundle_file('ui.xaml')
# import WPF creator and base Window
import wpf
from System import Windows

class MyWindow(Windows.Window):
    def __init__(self):
        wpf.LoadComponent(self, xamlfile)



    def say_hello(self, sender, args):
        UI.TaskDialog.Show("Hello World", "Hello {}")

# let's show the window (modal)
MyWindow().ShowDialog()