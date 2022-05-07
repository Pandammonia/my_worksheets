from plotly import colors
for key in colors.PLOTLY_SCALES.keys():
    print(key)

If you print the PLOTLY_SCALES dictionary, you can see how colorscales are defined. 
Every scale has a beginning color and an end color, and some scales have one or more 
intermediate colors defined as well. Plotly interpolates shades between each of these 
defined colors