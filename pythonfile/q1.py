class Question1:
    size = int(input())
    boxes = []
    for i in range(size):
        boxes.append(int(input()))
    for i in range(len(boxes)):
        x = int(boxes[i]/5)
        different = boxes[i]-(5*x)
        if(different <= 2):
            boxes[i] = x*5
        else:
            boxes[i] = (x+1)*5
    print(boxes)
