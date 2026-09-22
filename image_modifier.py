# Programmer: Stephen Borch
# Class: CPSC 122, Fall 2026
# Programming Assignment #1
# 9/21/26
# I attempted the bonus
# Description: This program accepts an input image file and then modifies that 
# image file using the modification functions: Flip the image vertically, Flip 
# the image horizontally, Remove a primary color (red, green, blue), Negate 
# the colors, Apply a high contrast, Add random noise, Apply a gray scale
# Apply a horizontal blur or custom modification. The program also produces 
# status updates to the console then produces an output file for every desired 
# modification.


import random

def load_image_data(filename: str) -> list[list[list[int]]]:
    """
    Opens an image and a 3D list of RGB values

    Args: 
        filename (str): the input file to be modified

    Returns:
        list[list[list[int]]]: the 3d list that has each pixel's RGB values in the image
    """
    with open(filename, "r") as file:

        value_types = []

        # Reads the file
        while len(value_types) < 3:
            line = file.readline().strip()

            if line != "" and not line.startswith("#"):
                value_types.append(line)

        if value_types[0] != "P3":
            print("Error: Invalid File Type")
            return []

        # Grabs value types from second line in header
        dimensions = value_types[1].split()
        width = int(dimensions[0])
        height = int(dimensions[1])

        # Grabs maximum RGB value
        color = int(value_types[2])

        pixel_3d = []

        values_RGB = []

        # Reads rest of file for rest of values
        for line in file:
            if not line.strip().startswith("#"):
                values = line.split()

                for value in values:
                    values_RGB.append(int(value))

        # Convert rest of values to 3D list
        index = 0

        for row in range(height):
            row_pixel = []

            for column in range(width):
                red = values_RGB[index]
                green = values_RGB[index + 1]
                blue = values_RGB[index + 2]

                pixel = [red, green, blue]
                row_pixel.append(pixel)

                index += 3

            pixel_3d.append(row_pixel)

    return pixel_3d


def apply_modification(data: list[list[list[int]]], mod: str) -> list[list[list[int]]] | None:
    """
    Calls the correct image modification to modify the file

    Args:
        data (list[list[list[int]]]): the 3d list that has each pixel's RGB values 
        in the image
        mod (str): the name of the modification to add to the image as a string
    Returns:
        list[list[list[int]]] | None: the 3d list that has new modified image data,
        or returns none if the modification is invalid or not supported
    """

    if mod == "vertical_flip":
        return apply_vertical_flip(data)

    elif mod == "horizontal_flip":
        return apply_horizontal_flip(data)

    elif mod == "horizontal_blur":
        return apply_horizontal_blur(data)

    elif mod == "remove_blue":
        return remove_color(data, 2)

    elif mod == "negative":
        return apply_negative(data)

    elif mod == "high_contrast":
        return apply_high_contrast(data)

    elif mod == "random_noise":
        return apply_random_noise(data)

    elif mod == "gray_scale":
        return apply_pixel_gray_scale(data)

    return None

def write_image_data(data: list[list[list[int]]], filename: str) -> None:
    """
    writes new data into an image file

    Args: 
        data (list[list[list[int]]]): the 3d list that has each pixel's RGB values 
        in the image
        filename (str): the name of the file to create or write over as a string

    Returns:
        None: does not return a value

    """

    height = len(data)
    width = len(data[0])

    with open(filename, "w") as file:
        file.write("P3\n")
        file.write(f"{width} {height}\n")
        file.write("255\n")

        for row in data:
            for pixel in row:
                file.write(f"{pixel[0]} {pixel[1]} {pixel[2]} ")
            file.write("\n")


def apply_vertical_flip(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Vertically flips the image

    Args:
        data (list[list[list[int]]]): the 3d list that has each pixel's RGB values 
        in the image

    Returns:
        list[list[list[int]]]: the 3d list that has the vertically flipped image
    """

    new_data = []

    for row in data:
        new_data.insert(0, [pixel[:] for pixel in row])

    return new_data

def apply_horizontal_flip(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Horizontally flips the image

    Args:
        data (list[list[list[int]]]): the 3d list that has each pixel's RGB values 
        in the image
        
    Returns:
        list[list[list[int]]]: the 3d list that has the horizontally flipped image
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

    Args:
        data (list[list[list[int]]]): the 3d list that has each pixel's RGB values 
        in the image
        color_index (int): the RGB color index to remove, 0 is red, 1 is green, 2 is blue
    
    Returns:
        list[list[list[int]]]: the 3d list that has the chosen color set to zero
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

def compute_negative(val: int) -> int:
    """
    Calculates the negative of a given RGB value

    Args:
        val (int): RGB color value between 0 and 255

    Returns:
        int: the negative value that was calculated from subtracting the original 
        value from 255
    """
    return abs(255 - val)

def apply_negative(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Applies the negative of a given RGB value found from the above function to an image

    Args:
        data (list[list[list[int]]]): the 3d list that has each pixel's RGB values 
        in the image

    Returns:
        list[list[list[int]]]: the 3d list that has the negative version of the image
    """
    new_data = []

    for row in data:
        new_row = []

        for pixel in row:
            new_pixel = [compute_negative(pixel[0]), compute_negative(pixel[1]), 
            compute_negative(pixel[2])]

            new_row.append(new_pixel)

        new_data.append(new_row)

    return new_data


def compute_high_contrast(val: int) -> int:
    """
    Calculates the maximum or minimum value for a RGB value (0 or 255)

    Args:
        val (int): RGB color value between 0 and 255

    Returns:
        int: 0 if val is less than or equal to 127 and returns 255 if val is greater 
        than 127
    """

    if val <= 127:
        return 0
    else:
        return 255

def apply_high_contrast(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Applies high contrast calculated from the above function to the image

    Args:
        data (list[list[list[int]]]): the 3d list that has each pixel's RGB values 
        in the image

    Returns:
        list[list[list[int]]]: the 3d list that has the high contrast version of 
        the image
    """

    new_data = []
    
    for row in data:
        new_row = []
    
        for pixel in row:
            new_pixel = [compute_high_contrast(pixel[0]), compute_high_contrast(pixel[1]), 
            compute_high_contrast(pixel[2])]
    
            new_row.append(new_pixel)
    
        new_data.append(new_row)
    
    return new_data

def compute_random_noise(val: int) -> int:
    """
    Inputs random noise into the image between RGB values -50 and 50

    Args:
        val (int): RGB color value between 0 and 255

    Returns:
        int: Modified RGB value after adding a random value between -50 and 50,
        but limited to the range of 0 to 255
    """

    new_value = val + random.randint(-50, 50)

    if new_value < 0:
        new_value = 0
    elif new_value > 255:
        new_value = 255

    return new_value

def apply_random_noise(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Applies a random amount of noise to the image

    Args:
        data (list[list[list[int]]]): the 3d list that has each pixel's RGB values 
        in the image

    Returns:
        list[list[list[int]]]: the 3d list that has random noise added to each 
        RGB value of the image
    """

    new_data = []
    
    for row in data:
        new_row = []
    
        for pixel in row:
            new_pixel = [compute_random_noise(pixel[0]), compute_random_noise(pixel[1]), 
            compute_random_noise(pixel[2])]
    
            new_row.append(new_pixel)
    
        new_data.append(new_row)
    
    return new_data    

def compute_pixel_gray_scale(pixel: list[int]) -> list[int]:
    """
    Calculates the gray scale for the image

    Args:
        pixel (list[int]): A list that has the RGB values of a single pixel.

    Returns:
        list[int]: A new pixel that has the average RGB value in all three indices.
    """

    avg = (pixel[0] + pixel[1] + pixel[2]) // 3

    return [avg, avg, avg]

def apply_pixel_gray_scale(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Applies the calculated gray sacle from the above function to the image

    Args:
        data (list[list[list[int]]]): the 3d list that has each pixel's RGB 
        values in the image

    Returns:
        list[list[list[int]]]: the 3d list that has the gray scale version of 
        the image
    """

    new_data = []
    
    for row in data:
        new_row = []
    
        for pixel in row:
            new_row.append(compute_pixel_gray_scale(pixel))
    
        new_data.append(new_row)
    
    return new_data    

def apply_horizontal_blur(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Applies a horizontal blur to the image by using values of neighboring pixels

    Args:
        data (list[list[list[int]]]): the 3d list that has each pixel's RGB 
        values in the image

    Returns:
        list[list[list[int]]]: the 3d list that has the horizontally blurred 
        version of the image   
    """

    height = len(data)
    width = len(data[0])

    new_data = []

    for row in range(height):
        new_row = []

        for col in range(width):
            start = max(0, col - 2)
            end = min(width, col + 3)

            count = end - start

            red_total = 0
            green_total = 0
            blue_total = 0

            for current_col in range(start, end):
                red_total += data[row][current_col][0]
                green_total += data[row][current_col][1]
                blue_total += data[row][current_col][2]

            new_pixel = [red_total // count, green_total // count, blue_total // count]

            new_row.append(new_pixel)

        new_data.append(new_row)

    return new_data

def main() -> None:
    """
    Runs the image modifier program

    The function asks the user for the name of an image file, loads the image 
    from that name, applies each specified modification, and writes each 
    modified image to a separate PPM file.
    
    Args:
        None: this function does not accept arguments

    Returns:
        None: this function does not return a value
    """
    file = input("Enter name of image file to modify: ")
    print(f"Processing {file}...")
    print()

    data = load_image_data(file)

    if file.endswith(".ppm"):
        base_file = file[:-4]
    else:
        base_file = file

    modifications = ["vertical_flip", "horizontal_flip", "remove_blue", "negative",
        "high_contrast", "random_noise", "gray_scale", "horizontal_blur"]

    for mod in modifications:
        print(f"Applying {mod}...")

        modified_data = apply_modification(data, mod)

        output_file = base_file + "_" + mod + ".ppm"

        print(f"Writing modified image data to {output_file}...")

        write_image_data(modified_data, output_file)

    print()
    print("Exiting program...")

if __name__ == "__main__":
    main()