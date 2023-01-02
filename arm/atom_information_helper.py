import cv2

def showImage(name, img):
    cv2.imshow(name, img)
    while(cv2.waitKey(30) & 0xFF != ord('q')):
        pass

def preprocess_image(img):
    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray,
                                 0,
                                 255,
                                 cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    # Applying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

    return dilation

def get_atom_bounding_box(element):
    return


def get_atom_center_coordinates(element):
    return
