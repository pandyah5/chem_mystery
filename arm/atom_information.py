import cv2
from atom_information_helper import preprocess_image, showImage

def iterate_contours(img):
    showImage("Original", image)
    dilation = preprocess_image(img)

    # Finding contours
    contours, hierarchy = cv2.findContours(dilation,
                                           cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)

    # Creating a copy of image
    im2 = img.copy()

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        custom_config = r'--oem 3 --psm 6'
        # element = pytesseract.image_to_string(img, config=custom_config)

        # print("The element is:", element)

        showImage("Added Boxes", rect)

    return

image = cv2.imread(r'C:\Users\Hetav Pandya\Downloads\chem_mystery\data\sample_co2.png')
iterate_contours(image)
