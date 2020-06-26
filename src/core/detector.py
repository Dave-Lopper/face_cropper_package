import dlib
from termcolor import colored


def detect(image: str, verbose: bool = False):
    """Detects faces on a given image using dlib and returns matches.

    :param image: Path to access the image to be searched
    :type image: [string]
    :param verbose: Wether or not command should output informations
    :type image: [bool], default to False

    :raises RuntimeError: When the provided image_path is invalid

    :return: The detected faces
    :rtype: [list of dlib.rectangle]
    """
    detector = dlib.get_frontal_face_detector()
    img = dlib.load_rgb_image(image)

    dets = detector(img, 1)
    verbose and print(
        colored(
            f"Number of faces detected: {len(dets)}\n",
            'yellow'
        )
    )
    detections = []

    # Avoiding circular imports
    from src.cli.output import colored_detection_output
    for index, detection in enumerate(dets):
        detections.append(detection)
        verbose and print(colored(f"Detection {index}:", 'green'))
        verbose and colored_detection_output(detection)
    return detections
