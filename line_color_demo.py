import krpc
import time

# create a connection to KSP and the active vessel
conn = krpc.connect(name='Line Drawing Test')
vessel = conn.space_center.active_vessel

# define the reference frame we want to use
ref_frame = vessel.surface_reference_frame

# create the line objects in the flight view
x_axis = conn.drawing.add_line((1, 0, 0), (10, 0, 0), ref_frame)
y_axis = conn.drawing.add_line((0, 1, 0), (0, 10, 0), ref_frame)
z_axis = conn.drawing.add_line((0, 0, 1), (0, 0, 10), ref_frame)

# color them 
x_axis.color = (1., 0., 0.)
y_axis.color = (0., 1., 0.)
z_axis.color = (0., 0., 1.)

# turn the lines off temporarily
x_axis.visible = False
y_axis.visible = False
z_axis.visible = False

# wait 4 seconds
time.sleep(4)

print('turning on surface reference lines')
x_axis.visible = True
y_axis.visible = True
z_axis.visible = True
