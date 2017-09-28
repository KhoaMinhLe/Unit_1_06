# Created by: Khoa Le
# Created on September 28 2017
# Created for ICS3U
# This program shows the difference between global and local variables and how they work.

import ui

variableX = 25

def variable_button_touch_up_inside(sender):
	variableX = 10
	variableY = 30
	variableZ = variableX + variableY
	
	view['variable_answer_label'].text = str(variableZ)
	
def global_variable_button_touch_up_inside(sender):
	global variableX
	variableX = variableX + 1
	variableY = 30
	variableZ = variableX + variableY
	
	view['global_variable_answer_label'].text = str(variableZ)


view = ui.load_view()
view.present('sheet')
