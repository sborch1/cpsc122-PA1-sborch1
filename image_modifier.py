def load_image_data(filename: str) -> list[list[list[int]]]:
    """
    Opens an image and a 3D list of RGB values
    """
    with open(filename, "r") as file:

        value_types = []

        # Reads the file and ignores comments and blank lines
        while len(value_types) < 3:
            file.readlines().strip()

        if value_types[0] != "P3":
            print("Error: Invalid File Type")
            return []

        # Grabs value types from second line in header
        dimensions = value_types[1].split()
        width = int(dimensions[1])
        height = int(dimensions[2])

        # Grabs maximum RGB value
        color = int(value_types[2])

        pixel_3d = []

        values_RGB = []

        # Convert rest of values to 3D list
        index = 0

        for row in range(height):
            row_pixel = []

            for column in range(width):
                red = values_RGB[index]
                blue = values_RGB[index + 1]
                green = values_RGB[index + 2]

                pixel = [red, green, blue]
                row_pixel.append(pixel)

                index += 3

            pixel_3d.append(row_pixel)

    return pixel_3d


def apply_modification(data: list[list[list[int]]], mod: str) -> list[list[list[int]]] | None:
    pass

def write_image_data(data: list[list[list[int]]], filename: str) -> None:
    pass


def apply_vertical_flip(data: list[list[list[int]]]) -> list[list[list[int]]]:
    pass

def apply_horizontal_flip(data: list[list[list[int]]]) -> list[list[list[int]]]:
    pass

def apply_horizontal_blur(data: list[list[list[int]]]) -> list[list[list[int]]]:
    pass


def compute_negative(val: int) -> int:
    pass

def compute_high_contrast(val: int) -> int:
    pass

def compute_random_noise(val: int) -> int:
    pass

def compute_pixel_gray_scale(pixel: list[int]) -> list[int]:
    pass



def main():
    load_image_data(input())

main()