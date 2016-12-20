# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.utils
import ga_example_tool.ga_tracking_window


def initialize_plugin():
    cmds.setParent('MayaWindow')
    cmds.menu(label=u'GA_Tools', tearOff=True)
    cmds.menuItem(subMenu=True, label='Test', tearOff=True)
    cmds.menuItem(label='GATrackingWindow',
                  command=open_ga_tracking_window)


def open_ga_tracking_window(*args, **kwargs):
    reload(ga_example_tool.ga_tracking_window)
    ga_example_tool.ga_tracking_window.GATrackingWindow.main()


maya.utils.executeDeferred(initialize_plugin)
