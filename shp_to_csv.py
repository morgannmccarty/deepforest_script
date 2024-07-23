import argparse

from deepforest.utilities import shapefile_to_annotations


def main(input: str, image_path: str, output: str) -> None:
    df = shapefile_to_annotations(
        shapefile=input,
        rgb=image_path, )
    df.to_csv(output, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data visualization")
    parser.add_argument("--input", "-i", type=str, help="The input shape file")
    parser.add_argument("--image_path", "-ip", type=str, help="The input image file")
    parser.add_argument("--output", "-o", type=str, help="The output file path to save")

    args = parser.parse_args()
    main(**vars(args))