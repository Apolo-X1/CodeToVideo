from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
from pygments.styles import get_style_by_name

import moviepy.editor as mp

with open('pr.py', 'r') as f:
    code = f.read()

def center_on_canvas(image_path, canvas_size=(1080, 1920)):
    img_clip = mp.ImageClip(image_path)
    margin = 60
    max_width = canvas_size[0] - 2 * margin
    max_height = canvas_size[1] - 2 * margin

    if img_clip.size[0] > max_width:
        img_clip = img_clip.resize(newsize=(max_width, img_clip.size[1]))

    if img_clip.size[1] > max_height:
        img_clip = img_clip.resize(newsize=(img_clip.size[0], max_height))

    x_center = (canvas_size[0] - img_clip.size[0]) // 2
    y_center = (canvas_size[1] - img_clip.size[1]) // 2
    position = (x_center, y_center)

    canvas = mp.ColorClip(size=canvas_size, color=(255, 255, 255))
    centered_clip = mp.CompositeVideoClip([canvas, img_clip.set_position(position)])
    centered_clip.save_frame(image_path)
    return image_path

formatter_options = {
    "style": get_style_by_name("monokai"),
    "font_size": 30
}

filenames = [f"datos/{i}.png" for i in range(len(code) + 1)]
filenames_cleaned = []

for idx, filename in enumerate(filenames):
    if code[idx - 1].isspace():
        continue
    with open(filename, "wb") as image_file:
        highlight(code[:idx], PythonLexer(), ImageFormatter(**formatter_options), image_file)
        center_on_canvas(filename)
        filenames_cleaned.append(filename)

print("Generating clip!")
clips = [mp.ImageClip(filename).set_duration(0.2) for filename in filenames_cleaned]
clips[-1] = clips[-1].set_duration(10)
print("Concatenating clips!")
final_clip = mp.concatenate_videoclips(clips, method="compose")
final_clip.write_videofile("code.mp4", fps=24, codec="libx264")
