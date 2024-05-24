import cv2
import config
from pyzbar import pyzbar

def decode_barcode(frame):
    barcodes = pyzbar.decode(frame)
    if(config.ESCANEAR_CODIGO_DE_BARRA == True):
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type
            #barcode_data, barcode_type retornar esses valores para o ROS2 

            print(barcode_data)
            text = f'{barcode_data} ({barcode_type})'
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame, barcodes

def main():
    cap = cv2.VideoCapture(config.CAMERA_PRINCIPAL)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame, barcodes = decode_barcode(frame)

        cv2.imshow('Barcode Scanner', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()