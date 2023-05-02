import random
import colorsys
from PIL import Image, ImageDraw, ImageChops

scale_factor = 2
target_size = 480
padding = 8 * scale_factor
background_color = (0, 0, 0)
image_size = target_size * scale_factor


def random_color(): 
    h = random.random()
    s = 1
    v = 1
    
    float_rgb = colorsys.hsv_to_rgb(h, s, v)
    rgb = [int(x * 255) for x in float_rgb]
    
    return tuple(rgb)
    
start_color = random_color()
end_color = random_color()

image = Image.new('RGB', size=(image_size, image_size), color=background_color)

draw = ImageDraw.Draw(image)

points = []

# Generate the points
for i in range(12): 
    random_point = (
        random.randint(padding, image_size - padding),
        random.randint(padding, image_size - padding)
    )
    points.append(random_point)
    
    max_x = max([p[0] for p in points])
    min_x = min([p[0] for p in points])

    max_y = max([p[1] for p in points])
    min_y = min([p[1] for p in points])
    
    delta_x = min_x - (image_size - max_x)
    delta_y = min_y - (image_size - max_y)
    
    for i, point in enumerate(points): 
        points[i] = (point[0] - delta_x // 2, point[1] - delta_y // 2)
    
    
def interpolate(start_color, end_color, factor: float): 
    reciprocal = 1 - factor
    return (
        int(start_color[0] * reciprocal + end_color[0] * factor), 
        int(start_color[1] * reciprocal + end_color[1] * factor), 
        int(start_color[2] * reciprocal + end_color[2] * factor)
    )

# Draw the points
thickness = 1
pointCount = len(points) - 1
for i, point in enumerate(points): 
    overlay = Image.new('RGB', size=(image_size, image_size), color=background_color)
    overlay_draw = ImageDraw.Draw(overlay)
    
    p1 = point
    if i == pointCount: 
        p2 = points[0]
    else: 
        p2 = points[i + 1]
    
    line = (p1, p2)
    color_factor = i / pointCount
    line_color = interpolate(start_color, end_color, color_factor)
    
    if i % 2 == 0: 
        thickness += scale_factor
        
    overlay_draw.line(line, fill=line_color, width=thickness)
    image = ImageChops.add(image, overlay)

image.save('vector-art.jpg')