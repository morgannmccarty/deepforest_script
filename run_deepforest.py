import argparse
from deepforest import main as deepforest_main
import PIL.Image as Image

def main(input: str, output: str) -> None:
    """
    Open input image, process it through DeepForest, then output to file.

    :param input:
    :param output:
    :return:
    """
    model = deepforest_main.deepforest()
    model.use_release()

    img = model.predict_image(path = input, return_plot = True)

    img = Image.fromarray(img)

    img.save(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data visualization")
    parser.add_argument("--input", "-i", type=str, help="The input image file")
    parser.add_argument("--output", "-o", type=str, help="The output file path to save")

    args = parser.parse_args()
    main(**vars(args))