def load_image_data(filename: str) -> list[list[list[int]]]:
    with open(filename, "r") as file:

        value_types = []

        while value_types < 4:
            file.readlines()

        if value_types[0] != "P3":
            print("Error: Invalid File Type")

            width = int(value_types[1])
            height = int(value_types[2])
            color = int(value_types[3])

        pixel_3d = []



    print("Enter name of PPM file for processing:", input())

    return 

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