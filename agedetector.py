import cv2

# Load face detection model
faceProto = "deploy.prototxt"
faceModel = "res10_300x300_ssd_iter_140000.caffemodel"

# Load age detection model
ageProto = "deploy_age.prototxt"
ageModel = "age_net.caffemodel"

faceNet = cv2.dnn.readNet(faceModel, faceProto)
ageNet = cv2.dnn.readNet(ageModel, ageProto)

AGE_BUCKETS = ['(0-2)','(4-6)','(8-12)','(15-20)','(25-32)','(38-43)','(48-53)','(60-100)']

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    blob = cv2.dnn.blobFromImage(frame,1.0,(300,300),(104.0,177.0,123.0))
    faceNet.setInput(blob)
    detections = faceNet.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0,0,i,2]

        if confidence > 0.5:
            box = detections[0,0,i,3:7] * [frame.shape[1],frame.shape[0],frame.shape[1],frame.shape[0]]
            (x1,y1,x2,y2) = box.astype("int")

            face = frame[y1:y2, x1:x2]

            blob = cv2.dnn.blobFromImage(face,1.0,(227,227),(78.4263377603,87.7689143744,114.895847746),swapRB=False)
            ageNet.setInput(blob)
            preds = ageNet.forward()
            age = AGE_BUCKETS[preds[0].argmax()]

            text = "Age: {}".format(age)

            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(frame,text,(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)

    cv2.imshow("Age Detector",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()