# -*- coding: utf-8 -*-
import maya.cmds as cmds
import platform
import random
from functools import partial
from tracker import before_tracking, after_tracking, send

_VERSION = "0.0.1"
_WINDOW_NAME = "GATrackingWindow"
GA_BASE_PARAMS = {'ul': str(cmds.about(uil=True)),
                  'an': 'ga_plugin_example',
                  'aid': 'ga_plugin_example_id',
                  'av': _VERSION,
                  'aiid': str(cmds.about(iv=True)),
                  'cd': _WINDOW_NAME,
                  'cd1': str(platform.platform())}


class GATrackingWindow(object):
    def __init__(self):
        self.windowName = _WINDOW_NAME
        self.windowTitle = self.windowName + "(v{0})".format(_VERSION)

    @classmethod
    def main(cls, *args):
        cls().create_gui()

    @before_tracking("screenview", GA_BASE_PARAMS)
    def create_gui(self):

        if cmds.window(self.windowName, exists=True):
            cmds.deleteUI(self.windowName)

        self.window = cmds.window(self.windowName,
                                  title=self.windowTitle,
                                  topLeftCorner=[200, 200],
                                  width=280, sizeable=True,
                                  maximizeButton=False, minimizeButton=False)

        cmds.frameLayout(label=u"GA Tracking",
                         marginWidth=6,
                         marginHeight=6,
                         borderStyle="etchedIn")

        cmds.button(label=u"Button1",
                    c=partial(self.button_command1, "button1"))
        cmds.button(label=u"Button2",
                    c=partial(self.button_command2, "button2"))

        cmds.setParent('..')

        cmds.showWindow(self.window)

    @after_tracking("event", GA_BASE_PARAMS, {'ec': "ToolAction",
                                              'ea': "ButtonPressed",
                                              'el': "button1"})
    def button_command1(self, arg, *args, **kwargs):
        print("pressed.", arg)

    @after_tracking("event", GA_BASE_PARAMS, {'ec': "ToolAction",
                                              'ea': "ButtonPressed",
                                              'el': "button2"})
    def button_command2(self, arg, *args, **kwargs):
        num = random.randint(0, 1)
        if num == 0:
            raise Exception("dancing with hard luck.")
            return
        print("pressed.", arg)
