
#-----Exercise Description-------------------------------------------#
#
#  Hidden pictures
#
#  This exercise gives you more practice at working with lists and
#  also illustrates how visual data can be encoded in a non-obvious
#  way.
#
#  In this exercise you must write a Python function that uses
#  Turtle graphics to draw pictures by following a pre-defined script
#  of commands stored in a list.  (In effect, you will be writing your
#  own language interpreter!)
#
#  Each picture is encoded using the following eight commands.
#
#  COMMAND           MEANING
#  'lift pen'        Don't draw when the turtle (cursor) moves
#  'lower pen'       Draw when the turtle moves
#  'thin lines'      Draw with thin lines, 3 pixels wide
#  'thick lines'     Draw with thick lines, 6 pixels wide
#  'black pen'       Draw with black lines
#  'red pen'         Draw with red lines
#  ['go to', x, y]   Move the turtle to coordinates (x, y)
#  ['draw dot', s]   Draw a dot of size s pixels
#
#  In the test data below are lists containing "scripts" to draw
#  five pictures.  You must write a function called "draw" which
#  accepts one of these lists as its argument and draws the
#  corresponding picture.
#
#--------------------------------------------------------------------#



#-----Test Data------------------------------------------------------#
#
#  The five variables defined below, enigma, riddle, puzzle, mystery
#  and conundrum contain lists of drawing commands.  Given one
#  of these lists as its argument, your function should draw a
#  corresponding picture using Turtle graphics.
#

enigma = ['black pen',
'lift pen',
'thin lines',
['go to', -2, 6],
'lower pen',
['go to', -19, 1],
['go to', -25, -7],
['go to', -22, -21],
['go to', -13, -28],
['go to', 2, -28],
'lift pen',
['go to', 36, -4],
['draw dot', 20],
'lift pen',
['go to', -49, -4],
['draw dot', 20],
'lift pen',
['go to', -86, -44],
'lower pen',
['go to', -71, -57],
['go to', -54, -66],
['go to', -38, -72],
['go to', -21, -73],
['go to', -2, -73],
['go to', 16, -74],
['go to', 31, -71],
['go to', 45, -67],
['go to', 58, -60],
['go to', 67, -54],
'lift pen',
['go to', -15, 71],
'lower pen',
['go to', -23, 73],
['go to', -35, 71],
['go to', -48, 63],
['go to', -60, 54],
['go to', -67, 44],
['go to', -57, 32],
['go to', -43, 29],
['go to', -33, 27],
['go to', -22, 29],
['go to', -10, 37],
['go to', -10, 44],
['go to', -14, 51],
['go to', -22, 54],
['go to', -27, 48],
['go to', -19, 40],
['go to', -8, 33],
['go to', 4, 25],
['go to', 13, 26],
['go to', 21, 29],
['go to', 24, 35],
['go to', 21, 40],
['go to', 17, 36],
'lift pen',
'thick lines',
['go to', 134, -2],
'lower pen',
['go to', 146, -7],
['go to', 153, -21],
['go to', 153, -38],
['go to', 143, -47],
['go to', 129, -51],
['go to', 126, -71],
['go to', 111, -89],
['go to', 95, -105],
['go to', 76, -116],
['go to', 51, -129],
['go to', 33, -134],
['go to', 8, -137],
['go to', -22, -138],
['go to', -45, -133],
['go to', -71, -122],
['go to', -92, -109],
['go to', -107, -98],
['go to', -120, -86],
['go to', -132, -62],
['go to', -138, -42],
['go to', -139, -18],
['go to', -138, 4],
['go to', -131, 28],
['go to', -118, 54],
['go to', -102, 77],
['go to', -78, 97],
['go to', -42, 113],
['go to', -10, 118],
['go to', 24, 118],
['go to', 52, 114],
['go to', 76, 103],
['go to', 98, 88],
['go to', 114, 69],
['go to', 128, 47],
['go to', 132, 26],
['go to', 134, -2],
'lift pen',
['go to', -141, -6],
'lower pen',
['go to', -151, -15],
['go to', -151, -27],
['go to', -139, -41]
]

riddle = ['red pen',
'lift pen',
'thick lines',
['go to', -181, 155],
'lower pen',
['go to', 166, 156],
['go to', 261, 72],
['go to', -4, -219],
['go to', -273, 69],
['go to', -181, 155],
'lift pen',
'thin lines',
['go to', -167, 126],
'lower pen',
['go to', -228, 67],
['go to', -194, 30],
['go to', -192, 58],
['go to', -182, 75],
['go to', -171, 90],
['go to', -160, 101],
['go to', -144, 113],
['go to', -135, 122],
['go to', -132, 125],
['go to', -167, 126],
'lift pen',
['go to', 81, 127],
'lower pen',
['go to', 109, 127],
['go to', 99, 108],
['go to', 81, 127],
'lift pen',
['go to', -66, -107],
'lower pen',
['go to', -33, -116],
['go to', 4, -120],
['go to', 28, -117],
['go to', 49, -111],
['go to', -2, -170],
['go to', -66, -107],
'lift pen',
['go to', -153, -14],
'lower pen',
['go to', -97, -22],
['go to', -46, -28],
['go to', 1, -29],
['go to', 43, -31],
['go to', 65, -35],
['go to', 82, -40],
['go to', 97, -49],
['go to', 95, -58],
['go to', 85, -65],
['go to', 67, -72],
['go to', 49, -75],
['go to', -8, -76],
['go to', -17, -66],
['go to', -28, -53],
['go to', -46, -50],
['go to', -65, -48],
['go to', -80, -51],
['go to', -93, -53],
['go to', -107, -60],
['go to', -153, -14],
'lift pen',
['go to', 169, 111],
'lower pen',
['go to', 217, 68],
['go to', 159, 4],
['go to', 139, 21],
['go to', 118, 35],
['go to', 96, 44],
['go to', 76, 46],
['go to', 18, 47],
['go to', -45, 47],
['go to', -61, 51],
['go to', -77, 56],
['go to', -91, 61],
['go to', -105, 70],
['go to', -111, 81],
['go to', -103, 96],
['go to', -87, 109],
['go to', -68, 119],
['go to', -46, 123],
['go to', -22, 127],
['go to', 3, 123],
['go to', 28, 116],
['go to', 53, 104],
['go to', 71, 88],
['go to', 81, 69],
['go to', 81, 62],
['go to', 168, 63],
['go to', 169, 111]
]

puzzle = ['black pen',
'lift pen',
['go to', -228, 224],
'thick lines',
'lower pen',
['go to', 217, 223],
['go to', 217, -218],
['go to', -228, -218],
['go to', -228, 224],
'lift pen',
'thin lines',
'red pen',
['go to', -33, 182],
'lower pen',
['go to', 8, 181],
['go to', 9, 64],
['go to', 20, 55],
['go to', 33, 54],
['go to', 43, 56],
['go to', 51, 63],
['go to', 51, 173],
['go to', 92, 130],
['go to', 92, 57],
['go to', 85, 40],
['go to', 75, 28],
['go to', 65, 22],
['go to', 54, 18],
['go to', 43, 16],
['go to', 33, 15],
['go to', 18, 15],
['go to', 6, 18],
['go to', -4, 23],
['go to', -15, 30],
['go to', -21, 36],
['go to', -27, 44],
['go to', -31, 52],
['go to', -33, 58],
['go to', -33, 181],
'lift pen',
['go to', 58, 181],
'lower pen',
['go to', 94, 142],
['go to', 123, 141],
['go to', 123, 18],
['go to', 165, 18],
['go to', 165, 141],
['go to', 198, 140],
['go to', 197, 181],
['go to', 58, 181],
'lift pen',
['go to', -20, 17],
'lower pen',
['go to', -54, 53],
['go to', -45, 69],
['go to', -40, 85],
['go to', -41, 108],
['go to', -48, 132],
['go to', -60, 151],
['go to', -77, 168],
['go to', -96, 177],
['go to', -114, 182],
['go to', -137, 182],
['go to', -158, 177],
['go to', -179, 164],
['go to', -194, 148],
['go to', -205, 126],
['go to', -210, 105],
['go to', -208, 77],
['go to', -195, 53],
['go to', -177, 32],
['go to', -157, 20],
['go to', -134, 14],
['go to', -112, 15],
['go to', -99, 17],
['go to', -87, 23],
['go to', -119, 57],
['go to', -132, 57],
['go to', -149, 63],
['go to', -161, 72],
['go to', -169, 86],
['go to', -171, 98],
['go to', -169, 112],
['go to', -160, 128],
['go to', -145, 140],
['go to', -129, 144],
['go to', -109, 139],
['go to', -91, 125],
['go to', -83, 105],
['go to', -86, 86],
['go to', -98, 97],
['go to', -143, 96],
['go to', -68, 17],
['go to', -20, 17]
]

mystery = ['black pen',
'lift pen',
'thick lines',
['go to', -37, 70],
'lower pen',
['go to', -71, 66],
['go to', -105, 63],
['go to', -134, 56],
['go to', -143, 51],
['go to', -213, -1],
['go to', -214, -10],
['go to', -202, -22],
['go to', -185, -26],
['go to', -167, -32],
['go to', -142, -41],
['go to', -116, -49],
['go to', -87, -53],
['go to', -61, -58],
['go to', -34, -58],
['go to', -9, -58],
['go to', 19, -57],
['go to', 45, -57],
['go to', 76, -54],
['go to', 108, -49],
['go to', 149, -36],
['go to', 177, -29],
['go to', 194, -19],
['go to', 197, -11],
['go to', 125, 47],
['go to', 106, 53],
['go to', 75, 59],
['go to', 49, 63],
['go to', 13, 69],
'lift pen',
'thin lines',
['go to', 123, 46],
'lower pen',
['go to', 111, 42],
['go to', 92, 39],
['go to', 73, 39],
['go to', 51, 37],
['go to', 31, 36],
['go to', 12, 36],
['go to', -14, 36],
['go to', -45, 36],
['go to', -63, 37],
['go to', -85, 39],
['go to', -105, 43],
['go to', -117, 45],
['go to', -129, 48],
['go to', -134, 51],
'lift pen',
['go to', -171, -31],
'lower pen',
['go to', -143, -36],
['go to', -103, -41],
['go to', -71, -44],
['go to', -34, -45],
['go to', 6, -45],
['go to', 41, -45],
['go to', 65, -44],
['go to', 94, -42],
['go to', 116, -41],
['go to', 139, -40],
'lift pen',
['go to', -64, 28],
'lower pen',
['go to', -13, 25],
['go to', -13, -32],
['go to', -86, -29],
['go to', -64, 26],
'lift pen',
['go to', 78, 33],
'lower pen',
['go to', 105, -3],
['go to', 128, -3],
['go to', 145, 2],
['go to', 161, 8],
['go to', 121, 41],
['go to', 110, 37],
['go to', 97, 36],
['go to', 78, 33],
'lift pen',
['go to', 100, 35],
'lower pen',
['go to', 129, -3],
'lift pen',
['go to', 114, 37],
'lower pen',
['go to', 147, 3],
'lift pen',
'red pen',
['go to', 9, 69],
'lower pen',
['go to', -1, 66],
['go to', -13, 66],
['go to', -23, 66],
['go to', -34, 68],
['go to', -34, 76],
['go to', -31, 84],
['go to', -24, 88],
['go to', -15, 90],
['go to', -6, 88],
['go to', 1, 84],
['go to', 5, 82],
['go to', 8, 68],
'lift pen',
['go to', -55, -60],
'lower pen',
['go to', -47, -69],
['go to', -31, -71],
['go to', -14, -71],
['go to', 4, -70],
['go to', 20, -70],
['go to', 30, -69],
['go to', 37, -60],
'lift pen',
['go to', 19, -70],
'lower pen',
['go to', 21, -62],
'lift pen',
['go to', 7, -70],
'lower pen',
['go to', 8, -60],
'lift pen',
['go to', -8, -70],
'lower pen',
['go to', -6, -62],
'lift pen',
['go to', -21, -70],
'lower pen',
['go to', -24, -61],
'lift pen',
['go to', -38, -70],
'lower pen',
['go to', -38, -61],
'lift pen',
['go to', 16, 11],
'black pen',
['draw dot', 20],
'lift pen',
['go to', -195, 85],
'red pen',
['draw dot', 10],
'lift pen',
['go to', -220, -77],
['draw dot', 5],
'lift pen',
['go to', -90, -104],
['draw dot', 6],
'lift pen',
['go to', 90, -87],
['draw dot', 14],
'lift pen',
['go to', 179, 77],
['draw dot', 9],
'lift pen',
['go to', 172, -89],
['draw dot', 3],
'lift pen',
['go to', -79, 103],
['draw dot', 8],
'lift pen',
['go to', -219, 27],
['draw dot', 10],
'lift pen',
['go to', -143, -68],
['draw dot', 13],
'lift pen',
['go to', 20, -114],
['draw dot', 16],
'lift pen',
['go to', 136, 74],
['draw dot', 6],
'lift pen',
['go to', 108, 122],
['draw dot', 8],
'lift pen',
['go to', -165, -107],
['draw dot', 9]
]

conundrum = ['black pen',
'lift pen',
['go to', -98, 132],
['draw dot', 10],
'lift pen',
['go to', -120, 137],
['draw dot', 10],
'lift pen',
'thick lines',
['go to', -55, 80],
'lower pen',
['go to', -35, 84],
['go to', -7, 86],
['go to', 15, 84],
['go to', 38, 77],
['go to', 61, 63],
['go to', 77, 51],
['go to', 91, 28],
['go to', 97, 0],
['go to', 92, -25],
['go to', 80, -47],
['go to', 64, -63],
['go to', 44, -78],
['go to', 26, -84],
['go to', -4, -91],
['go to', -31, -92],
['go to', -59, -90],
['go to', -78, -82],
['go to', -101, -69],
['go to', -118, -52],
['go to', -131, -29],
['go to', -135, -8],
['go to', -133, 10],
['go to', -128, 29],
['go to', -120, 37],
'thin lines',
['go to', -120, 25],
['go to', -112, 21],
['go to', -99, 30],
['go to', -99, 18],
['go to', -93, 15],
['go to', -82, 18],
['go to', -77, 26],
['go to', -69, 20],
['go to', -54, 30],
['go to', -56, 36],
['go to', -42, 38],
['go to', -34, 45],
['go to', -36, 52],
['go to', -20, 53],
['go to', -19, 60],
['go to', -23, 67],
['go to', -35, 72],
['go to', -46, 74],
['go to', -57, 79],
['go to', -61, 90],
['go to', -64, 103],
['go to', -64, 111],
['go to', -61, 123],
['go to', -60, 133],
['go to', -64, 140],
['go to', -70, 147],
['go to', -76, 153],
['go to', -81, 156],
['go to', -92, 158],
['go to', -105, 157],
['go to', -115, 154],
['go to', -120, 149],
['go to', -126, 143],
['go to', -133, 132],
'lift pen',
['go to', -117, 111],
'lower pen',
['go to', -138, 99],
['go to', -142, 100],
['go to', -145, 107],
['go to', -144, 113],
['go to', -134, 126],
['go to', -128, 125],
['go to', -118, 116],
['go to', -115, 113],
'lift pen',
'red pen',
['go to', -139, 121],
'lower pen',
['go to', -142, 122],
['go to', -140, 126],
['go to', -133, 129],
['go to', -125, 129],
['go to', -111, 130],
['go to', -105, 126],
['go to', -97, 113],
['go to', -101, 99],
['go to', -110, 91],
['go to', -115, 74],
['go to', -109, 59],
['go to', -103, 53],
['go to', -104, 43],
['go to', -111, 39],
['go to', -123, 41],
['go to', -136, 47],
['go to', -137, 49],
['go to', -129, 62],
['go to', -130, 65],
['go to', -136, 66],
['go to', -139, 70],
['go to', -131, 81],
['go to', -133, 86],
['go to', -129, 95],
['go to', -116, 112],
'lift pen',
['go to', -8, 44],
'lower pen',
['go to', -15, 43],
['go to', -30, 35],
['go to', -40, 28],
['go to', -51, 17],
['go to', -64, 0],
['go to', -62, -18],
['go to', -51, -31],
['go to', -30, -43],
['go to', -10, -41],
['go to', 2, -38],
['go to', 8, -42],
['go to', 19, -56],
['go to', 25, -52],
['go to', 33, -44],
['go to', 34, -38],
['go to', 26, -21],
['go to', 33, -29],
['go to', 43, -29],
['go to', 55, -27],
['go to', 62, -21],
['go to', 60, -14],
['go to', 54, -7],
['go to', 53, -4],
['go to', 56, 0],
['go to', 80, 7],
['go to', 84, 12],
['go to', 83, 23],
['go to', 79, 34],
['go to', 73, 39],
['go to', 60, 41],
['go to', 43, 40],
['go to', 27, 37],
['go to', 13, 37],
['go to', 7, 39],
['go to', -7, 43],
'lift pen',
['go to', -53, 81],
'lower pen',
['go to', -54, 96],
['go to', -52, 114],
['go to', -44, 130],
['go to', -35, 145],
['go to', -26, 154],
['go to', -14, 158],
['go to', -3, 157],
['go to', 8, 148],
['go to', 16, 133],
['go to', 20, 114],
'black pen',
'lift pen',
['go to', 1, 85],
'lower pen',
['go to', 10, 101],
['go to', 22, 114],
['go to', 37, 128],
['go to', 55, 136],
['go to', 68, 139],
['go to', 80, 132],
['go to', 87, 110],
['go to', 83, 94],
['go to', 75, 79],
['go to', 65, 62],
'lift pen',
'red pen',
['go to', 83, 90],
'lower pen',
['go to', 99, 94],
['go to', 116, 93],
['go to', 130, 84],
['go to', 132, 60],
['go to', 121, 46],
['go to', 111, 35],
['go to', 94, 26],
'lift pen',
'black pen',
['go to', 114, 35],
'lower pen',
['go to', 131, 31],
['go to', 143, 22],
['go to', 147, 4],
['go to', 140, -9],
['go to', 128, -16],
['go to', 118, -22],
['go to', 107, -26],
['go to', 93, -28],
'lift pen',
'red pen',
['go to', 118, -25],
'lower pen',
['go to', 130, -33],
['go to', 138, -46],
['go to', 137, -61],
['go to', 129, -70],
['go to', 118, -77],
['go to', 109, -81],
['go to', 98, -83],
['go to', 83, -84],
['go to', 71, -84],
['go to', 62, -83],
['go to', 49, -79],
]

#
#--------------------------------------------------------------------#



#-----Solution-------------------------------------------------------#
#
#  This is where you will define your "draw" function.  The solution
#  strategy is as follows.
# 
#  1. Create a drawing window
#  2. For each command in the given list:
#     a. If the command is 'lift pen' then lift the pen; or
#     b. If the command is 'black pen' then make the pen black; or
#     c. ... and so on for all eight commands.
#  3. Close the drawing window.
#

from turtle import *

###### DEFINE YOUR draw FUNCTION HERE


#
#--------------------------------------------------------------------#



#-----Testing--------------------------------------------------------#
#
#  This main program calls your "draw" function to produce a picture.
#  Uncomment one of the function calls at a time.

draw(puzzle)
# draw(riddle)
# draw(enigma)
# draw(mystery)
# draw(conundrum)

#
#--------------------------------------------------------------------#
