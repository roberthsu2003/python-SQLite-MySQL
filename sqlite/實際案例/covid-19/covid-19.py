import pygal.maps.world

worldMap = pygal.maps.world.World()
worldMap.title = "China in the Map"
worldMap.add('Chine',['cn'])
worldMap.render_to_file('out_1_17.svg')
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

drawing = svg2rlg('out_1_17.svg')
renderPM.drawToFile(drawing, "temp.png", fmt="PNG")