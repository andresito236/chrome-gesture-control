import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import pygetwindow as gw
import re
import pyautogui as gui
import time
import sys

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

offset = 20
imgSize = 300

counter = 0

labels = ["acercate", "asi-beh", "boca-cerrada", "cinco-dedos", "cinco-lado", "cuatro-dedos", "cuatro-lado", "dame", "dos-dedos", "golpear-con-anular", "grande-vertical", "iglu", "indice-arriba", "L-con-medio", "letra-L", "okay", "pistolita", "poquito", "promesa-L", "pulgar-abajo", "pulgar-arriba", "puno-cerrado", "rock", "rock-lado", "rock-sin-pulgar", "telefono", "telefono-frontal", "tijera", "tres-dedos", "tres-lado"]
validLabels = ["acercate", "cinco-lado", "cuatro-lado", "dame", "dos-dedos", "grande-vertical", "iglu", "indice-arriba", "pistolita", "poquito", "promesa-L", "pulgar-abajo", "pulgar-arriba", "puno-cerrado", "rock", "rock-lado", "rock-sin-pulgar", "telefono", "tijera"]
patron = r"^.*Google Chrome$"

def obtener_ventana_chrome():
    for window in gw.getAllWindows():
        if re.match(patron, window.title):
            return window
    return None


def restaurar_chrome():
    chromeWindow = obtener_ventana_chrome()
    if chromeWindow is not None:
        chromeWindow.restore()
        chromeWindow.activate()
    else:
        chromeCoords = gui.locateCenterOnScreen("imgs/chrome-logo.png")
        gui.moveTo(chromeCoords)
        gui.click()
        time.sleep(2)


restaurar_chrome()

cerrado = False
primeraVezIglu = True
while not cerrado:
    try:
        success, img = cap.read()
        imgOutput = img.copy()
        hands, img = detector.findHands(img)
        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']

            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

            imgCropShape = imgCrop.shape

            aspectRatio = h / w

            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize


            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize

            prediction, index = classifier.getPrediction(imgWhite, draw=False)

            cv2.rectangle(imgOutput, (x - offset, y - offset - 50),
                          (x - offset + 90, y - offset - 50 + 50), (255, 0, 255), cv2.FILLED)
            cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
            cv2.rectangle(imgOutput, (x - offset, y - offset),
                          (x + w + offset, y + h + offset), (255, 0, 255), 4)

            titulo = gw.getActiveWindow().title

            if (not re.match(patron, titulo)):
                if (labels[index] == "pistolita" or labels[index] == "iglu") and obtener_ventana_chrome() is None:
                    raise SystemExit("El programa ha sido cerrado.")
                restaurar_chrome()
            else:
                if labels[index] in validLabels and prediction[index] > 0.99:
                    toSleep = 1.5
                    if labels[index] == "telefono":
                        gui.hotkey("ctrl", "t")
                    elif labels[index] == "pistolita":
                        gui.hotkey("ctrl", "w")
                        toSleep += 0.75
                    elif labels[index] == "cuatro-lado": # este va a la pestaña de la izquierda
                        gui.hotkey("ctrl", "pageup")
                    elif labels[index] == "cinco-lado": # este va a la pestaña de la derecha
                        gui.hotkey("ctrl", "pagedown")
                    elif labels[index] == "pulgar-arriba":
                        gui.hotkey("pageup")
                    elif labels[index] == "pulgar-abajo":
                        gui.hotkey("pagedown")
                    elif labels[index] == "indice-arriba":
                        gui.hotkey("up")
                        toSleep = 0.75
                    elif labels[index] == "puno-cerrado":
                        gui.hotkey("down")
                        toSleep = 0.75
                    elif labels[index] == "grande-vertical":
                        gui.hotkey("left")
                    elif labels[index] == "promesa-L":
                        gui.hotkey("right")
                    elif labels[index] == "rock-sin-pulgar":
                        gui.hotkey("tab")
                        toSleep = 0.75
                    elif labels[index] == "rock":
                        gui.hotkey("shift", "tab")
                        toSleep = 0.75
                    elif labels[index] == "rock-lado":
                        gui.hotkey("enter")
                    elif labels[index] == "acercate":
                        gui.hotkey("ctrl", "r")
                    elif labels[index] == "poquito":
                        gui.hotkey("alt", "left")
                    elif labels[index] == "dame":
                        gui.hotkey("alt", "right")
                    elif labels[index] == "dos-dedos":
                        gui.hotkey("esc")
                    elif labels[index] == "tijera":
                        gui.hotkey("alt")
                    elif labels[index] == "iglu":
                        if primeraVezIglu:
                            primeraVezIglu = False
                        else:
                            gui.hotkey("alt", "f4")
                            primeraVezIglu = True

                    time.sleep(toSleep)


        cv2.imshow("Captura de gestos", imgOutput)
        cv2.waitKey(1)
        if cv2.getWindowProperty("Captura de gestos", cv2.WND_PROP_VISIBLE) < 1:
            cerrado = True

    except SystemExit:
        sys.exit(0)
    except:
        continue

cv2.destroyAllWindows()