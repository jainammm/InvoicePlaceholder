def getMaxConfidence(model_output, class_name):
    outputs = []

    for item in model_output:
        if item['class_name'] == class_name:
            outputs.append(item)

    confidence = 0
    final_output = ''
    final_id = -1

    for item in outputs:
        if confidence < item['confidence']:
            final_output = item['text']
            final_id = item['id']
            confidence = item['confidence']

    print(final_id, final_output, confidence)

    return final_id, final_output

def getAddress(model_output, class_name):
    outputs = []

    for item in model_output:
        if item['class_name'] == class_name:
            outputs.append(item)
        
    confidence = 0
    bounding_box = []

    for item in outputs:
        if confidence < item['confidence']:
            bounding_box = item['bounding_box']
            confidence = item['confidence']

    word_size = bounding_box[3] - bounding_box[1]

    valid_box_ymin = bounding_box[1] - int(2.5*word_size)
    valid_box_ymax = bounding_box[3] + int(2.5*word_size)

    final_address = ''

    for item in outputs:
        bbox_item = item['bounding_box']
        ymin = bbox_item[1]
        ymax = bbox_item[3]
        if ymin < valid_box_ymax and ymax > valid_box_ymin:
            final_address += ' ' + item['text'] 

    return final_address
