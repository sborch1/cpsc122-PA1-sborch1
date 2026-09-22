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
    Calls the correct image modification to modify the file
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
        return compute_pixel_gray_scale(data)

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

def compute_negative(val: int) -> int:
    """
    Calculates the negative of a given RGB value
    """
    return abs(255 - val)

def apply_negative(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Applies the negative of a given RGB value found from the above function to an image
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
    """

    if val <= 127:
        return 0
    else:
        return 255

def apply_high_contrast(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Applies high contrast calculated from the above function to the image
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
    Calcultes the gray scale for the image
    """

    avg = (pixel[0] + pixel[1] + pixel[2]) // 3

    return [avg, avg, avg]

def apply_pixel_gray_scale(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Applies the calculated gray sacle from the above function to the image
    """

    new_data = []
    
    for row in data:
        new_row = []
    
        for pixel in row:
            new_row.append(compute_pixel_gray_scale[pixel])
    
        new_data.append(new_row)
    
    return new_data    

def apply_horizontal_blur(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """
    Applies a horizontal blur to the image by using values of neighboring pixels
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

            new_pixel = [red_total // count, green_total // count, blue_total, count]

            new_row.append(new_pixel)

        new_data.append(new_row)

    return new_data

def main():
    file = input("Enter name of image file to modify: ")
    print(f"Processing {file}...")
    print()

    data = load_image_data(file)

    if file.endswith(".ppm"):
        base_file = file[:-4]
    else:
        base_file = file

    modifications = ["vertical_flip", "horizontal_flip", "remove_green", "negative",
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