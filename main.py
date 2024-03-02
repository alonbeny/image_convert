import glob
import os.path

from PIL import Image


def case_insensitive_glob(pattern, path='.'):
    # Convert the pattern to a case-insensitive pattern
    def char_to_cases(c):
        return f'[{c.lower()}{c.upper()}]' if c.isalpha() else c

    ci_pattern = ''.join(char_to_cases(c) for c in pattern)

    # Use the modified pattern to glob files
    return glob.glob(os.path.join(path, ci_pattern))


def find_images(input_path:str, img_format:str) -> list:
    pattern = fr"*.{img_format}"
    image_files = case_insensitive_glob(pattern=pattern, path=input_path)
    return image_files


def convert_and_save(output_path: str, input_paths: list, img_format: str) -> None:
    for i, image_file in enumerate(input_paths):
        # Open the JFIF image
        img = Image.open(image_file)

        # Save the image as JPEG
        output_path_for_image = os.path.join(output_path, f"{i}.JPEG")
        img.save(output_path_for_image, img_format)
    pass


if __name__ == '__main__':
    images = find_images(input_path=r"C:\Users\alonb\PycharmProjects\image_convert\input_folder", img_format="jfif")
    convert_and_save(input_paths=images, output_path=r"C:\Users\alonb\PycharmProjects\image_convert\output_folder", img_format="JPEG")

