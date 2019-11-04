"""
Very simple window to act as stand-in app
"""
#pylint: disable=invalid-name
import sys
import pyscreenshot as ImageGrab
from PySide2 import QtWidgets, QtCore
from pynput import mouse


class SnapShot(mouse.Listener, QtWidgets.QRubberBand):
    """
    Entirely self-contained widget for selecting a portion of the screen.

    :param QApplication parent: parent QApplication as per Qt methodology.
    """
    def __init__(self, parent):
        self.parent = parent
        self.origin = QtCore.QPoint()
        self.bbox = None
        mouse.Listener.__init__(self,
                                on_move=self.on_mouse_move,
                                on_click=self.on_mouse_click,
                                suppress=True)
        QtWidgets.QRubberBand.__init__(self, QtWidgets.QRubberBand.Rectangle)
        self.setWindowOpacity(0.25)
        self.start()

    def on_mouse_click(self, x, y, _, pressed):
        """
        If mouse is pressed, start drawing the rubber band based on where the mouse is.
        If mouse is released, print bounding box of the rubber band and exit the app cleanly

        :param int x: screen width position of click
        :param int y: screen height position of click
        :param button _: unused, but required by caller
        :param bool pressed: if the button was pressed (or released)
        """
        if pressed:
            self.origin = QtCore.QPoint(x, y)
            self.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
            self.show()
        else:
            geo = self.geometry()
            self.bbox = (geo.x(), geo.y(), geo.x()+geo.width(), geo.y()+geo.height())
            print("Position Width: %s" % geo.x())
            print("Position Height: %s" % geo.y())
            print("Size Width: %s" % geo.width())
            print("Size Height: %s" % geo.height())
            self.hide()
            im = ImageGrab.grab(bbox=S.bbox, backend='gnome-screenshot')
            im.save('here.png')
            self.fexit()

    def on_mouse_move(self, x, y):
        """
        Update the rubber band to the latest mouse position.

        :param int x: width position on screen
        :param int y: height position on screen
        """
        self.setGeometry(QtCore.QRect(self.origin, QtCore.QPoint(x, y)).normalized())

    def fexit(self):
        """
        Cleanly exit the app:
         - Hide the rubberband window
         - Stop the mouse listener
         - Exit the parent QApplication
        """
        self.stop()
        self.parent.exit()


APP = QtWidgets.QApplication(sys.argv)
S = SnapShot(APP)
APP.exec_()
