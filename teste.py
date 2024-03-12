import cv2
from deepface import DeepFace

#Inicializa o detector de faces do OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#Mapeamento de emoções em inglês para português
emotion_translation = {

'happy': 'feliz',
'sad': 'triste' 

}

#inicia a câmera (pode ser necessário ajustar o número do dispositivo)
cap = cv2.VideoCapture(2)
print(cap) 