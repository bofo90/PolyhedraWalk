import glob

from PIL import Image

i, j = 17, 0


def make_gif(frame_folder):
    files = glob.glob(f"{frame_folder}/*.png")
    sorted_files = sorted(files)
    frames = [Image.open(image) for image in sorted_files[:-20]+files+sorted_files[-20::-1]]
    frame_one = frames[0]
    frame_one.save(
        f"Polyinsects/alpha_{i}_{j}.gif",
        format="GIF",
        append_images=frames[1:],
        save_all=True,
        optimize=False,
        # duration=100,
    )


if __name__ == "__main__":
    make_gif(f"/home/agustin/Programming/CoverPhDThesis/Polyinsects/alpha_{i}_{j}")
