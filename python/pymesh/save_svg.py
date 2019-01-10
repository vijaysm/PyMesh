from .version import __version__
import logging

def save_svg(filename, mesh):
    if mesh.dim != 2:
        logger = logging.getLogger(__name__);
        logger.warning("Mesh dim is not 2, only saving X and Y coordinates in svg file.");

    template = """<?xml version="1.0" encoding="utf-8"?>
<!-- Generated by PyMesh v{version}.)  -->
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="{bbox_min[0]} {bbox_min[1]} {bbox_max[0]} {bbox_max[1]}"
         style="enable-background:new {bbox_min[0]} {bbox_min[1]} {bbox_max[0]} {bbox_max[1]};" xml:space="preserve">
<style type="text/css">
	.st0{{fill:#F8F4EC;stroke:#484846;}}
</style>
{data}
</svg>
"""

    bbox_min, bbox_max = mesh.bbox;
    data = [];
    vertices = mesh.vertices;
    faces = mesh.faces;
    for f in faces:
        coordinates = ["{v[0]},{v[1]}".format(v=v) for v in vertices[f, :]];
        poly = "<polygon class=\"st0\" points=\"{}\"/>".format(" ".join(coordinates));
        data.append(poly);
    data = "\n".join(data);

    svg_ascii = template.format(
            version=__version__,
            bbox_min = bbox_min,
            bbox_max = bbox_max,
            data = data);

    with open(filename, 'w') as fout:
        fout.write(svg_ascii);

