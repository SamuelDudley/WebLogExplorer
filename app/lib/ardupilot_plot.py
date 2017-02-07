import numpy as np

tmp = np.load('/home/uas/opencv/datasets/cland/cland_day3_flight1/flight1_cland1_C_straight/numpy_arrays/EKF1.npy')
tmp2 = np.load('/home/uas/opencv/datasets/cland/cland_day3_flight1/flight1_cland1_C_straight/numpy_arrays/MSG.npy')
print(tmp2.dtype.fields)
print(tmp['Roll'])
for m in tmp2['Message']:
    print m
from bokeh.models import TapTool, CustomJS, ColumnDataSource, LegendItem, Legend
from bokeh.models import LinearAxis, Range1d, BoxAnnotation, HoverTool, Span, Label
from bokeh.plotting import figure, show, curdoc



from bokeh.layouts import column
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc

# create a plot and style its properties
t = tmp['timestamp']


#msg_source = ColumnDataSource(data=dict(x=tmp2['timestamp'],y=[10],msg=tmp2['Message']))

msgs = []

for idx in range(len(tmp2['timestamp'])):
    msgs.append(Label(x=tmp2['timestamp'][idx], y=70, x_units='data', y_units='screen',
                 text=tmp2['Message'][idx], render_mode='canvas', visible=False)
                )

code = """


d0 = cb_obj.selected["0d"];
console.log(d0)


if (d0.glyph) {
    var color = d0.get_view().visuals.line.line_color.value();
    var data = source.data;
    data['text'] = ['Selected the ' + color + ' line'];
    source.trigger('change');
}
"""

# use a source to easily update the text of the text-glyph
#source = ColumnDataSource(data=dict(text=['no line selected']))



# cannot supply sizing_mode='scale_both' and responsive = True
TOOLS = ['box_zoom,pan,crosshair,reset,wheel_zoom,save,redo,undo']
p = figure(plot_width=700,plot_height = 600,tools=TOOLS, webgl=False, responsive=True)
b1 = BoxAnnotation(left=2.971907e10, fill_alpha=0.1, fill_color='red',render_mode='canvas')
p.add_layout(b1) #right = 




y = tmp['Roll']
y2 = tmp['Pitch']
y3 = tmp['Yaw']

p.y_range = Range1d(min(y), max(y))
p.extra_y_ranges['foo'] = Range1d(min(y2), max(y2))
p.extra_y_ranges['barr'] = Range1d(min(y3), max(y3))

l1 = p.line(t, y, color='red', line_width=1, legend="Record")
l2 = p.line(t, y2, color='green', line_width=1, y_range_name="foo")
l3 = p.line(t, y3, color='blue',  line_width=1, y_range_name="barr")

#p.scatter(t, y, marker='cross', size=15, line_color="navy", fill_color="orange", alpha=0.5)
#p.text(0, -100, source=source)

p.add_layout(LinearAxis(y_range_name="foo"), 'left')
p.add_layout(LinearAxis(y_range_name="barr"), 'left')

p.xaxis.axis_label = "Time"
p.yaxis.axis_label = " "

#support for mode colours

legend = Legend(items=[
    LegendItem(label="sin(x)", renderers=[]),
    LegendItem(label="2*sin(x)", renderers=[]),
    LegendItem(label="3*sin(x)", renderers=[])
])



source = ColumnDataSource({'x0': [2.961807e10]})

vline_code = """
var x_idx = cb_data.index['0d'].indices[0]
console.log(x_idx)
vline.location = cb_data.geometry.x
""" 

vline = Span(location=source.data['x0'][0], dimension='height', line_color='red', line_width=1,render_mode='css')
p.renderers.extend([vline])

callback1 = CustomJS(args={'vline': vline}, code=vline_code)
hover2 = HoverTool(callback=callback1)
hover2.tooltips = [
    ("x,y", "(@x, @y)")
#("color", "$color[swatch]")
]
hover2.point_policy='snap_to_data'
hover2.line_policy='nearest'#'prev'
hover2.mode = 'vline'

p.add_tools(hover2)
for msg in msgs:
    p.add_layout(msg)

# put the button and plot in a layout and add to the document
curdoc().add_root(column(p))
curdoc().add_root(column(p))