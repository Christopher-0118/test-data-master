import json
from pascal_voc_writer import Writer

source = './bdd.json'
with open(source, 'r') as source_json:
    imgs = json.load(source_json)
    for img in imgs:
        url = img['url']
        name = url[url.rfind("/") + 1:]
        writer = Writer('./' + name, 1000, 1000)
        for label in img['labels']:
            box2d = label['box2d']
            writer.addObject(
                label['category'],
                box2d['x1'], 
                box2d['y1'], 
                box2d['x2'],
                box2d['y2']
            )
        writer.save('./xml/' + name + '.xml')
