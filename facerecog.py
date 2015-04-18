
import cv2
import config
import face
import time


video_capture = cv2.VideoCapture(0)
if __name__ == '__main__':
	
	camera = config.get_camera()
	
	i=1;
	while i:
    # Capture frame-by-frame
		ret, frame = video_capture.read()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('Video', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			result =face.detect_single(gray)
			
			if result is None:
				print 'Error.Try again!'
			if result is not None:
				x, y, w, h = result
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
				crop = face.resize(face.crop(gray, x, y, w, h))
				
				facecrop = gray[y:y + h, x:x + w]
				print 'Image captured successfully!'
				
				break

	if result is None:
		print 'Could not detect single face!'
		
	else: 
		
		print 'Analysing image....'
		model = cv2.createEigenFaceRecognizer()
		model.load(config.TRAINING_FILE)
		
		
		label, confidence = model.predict(crop)
		print 'Predicted {0} face with confidence {1} (lower is more confident).'.format(
		   'POSITIVE' if label == config.POSITIVE_LABEL else 'NEGATIVE', 
		   confidence)
		if label == config.POSITIVE_LABEL and confidence < config.POSITIVE_THRESHOLD:
		   
			print 'Hello Girish'
		  
		else:
			print 'Bye intruder!'
