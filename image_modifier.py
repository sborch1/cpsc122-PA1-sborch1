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
    """
    Calls the correct modification to modify the file
    """

    if mod == "vertical_flip":
        return apply_vertical_flip(data)

    elif mod == "horizontal_flip":
        return apply_horizontal_flip(data)

    elif mod == "horizontal_blur":
        return apply_horizontal_blur(data)

    elif mod == "remove_red":
        return remove_color(data, 0)

    elif mod == "remove_green":
        return remove_color(data, 1)

    elif mod == "remove_blue":
        return remove_color(data, 2)

    elif mod == "negative":
        return compute_negative(data)

    elif mod == "high_contrast":
        return compute_high_contrast(data)

    elif mod == "random_noise":
        return compute_random_noise(data)

    elif mod == "gray_scale":
        return compute_gray_scale(data)

    return None

def write_image_data(data: list[list[list[int]]], filename: str) -> None:
    """
    writes new data into an image file
    """

    height = len(data)
    width = len(data[0])

    with open(filename, "w") as file:
        file.write("P3\n")
        file.write(f"{width} {height}\n")
        file.write("255\n")

        for row in data:
            for pixel in row:
                file.write(f"{pixel[0]} {pixel[1]} {pixel[2]}")
            file.write("\n")


def apply_vertical_flip(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Vertically flips the image
    """

    new_data = []

    for row in data:
        new_data.insert(0, [pixel[:] for pixel in row])

    return new_data

def apply_horizontal_flip(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Horizontally flips the image
    """

    new_data = []

    for row in data:
        new_row = []

        for pixel in row:
            new_row.insert(0, pixel[:])

        new_data.append(new_row)

    return new_data

def remove_color(data: list[list[list[int]]], color_index: int) -> list[list[list[int]]]:
    """
    Gets rid of one RGB color from every pixel
    """

    new_data = []

    for row in data:
        new_row = []

        for pixel in row:
            new_pixel = pixel[:]
            new_pixel[color_index] = 0
            new_row.append(new_pixel)

        new_data.append(new_row)

    return new_data

def apply_horizontal_blur(data: list[list[list[int]]]) -> list[list[list[int]]]:
    pass


def compute_negative(val: int) -> int:
    pass

def compute_high_contrast(val: int) -> int:
    pass

def compute_random_noise(val: int) -> int:
    pass

def compute_gray_scale(pixel: list[int]) -> list[int]:
    pass



def main():
    load_image_data(input())

main()