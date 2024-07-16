# Image Puzzle Assembly with OpenCV

This project demonstrates how to assemble a puzzle by placing multiple sub-images onto a single background image using OpenCV. Each sub-image is manipulated through resizing, rotation, and flipping to fit into the final composition.

## Features

- **Background Setup**: A white background of size 1200x600 is created.
- **Image Manipulation**: Sub-images are resized, rotated, and flipped as needed to fit into the puzzle.
- **Image Placement**: The manipulated sub-images are placed on specific locations on the background.

## Prerequisites

- Python 3.x
- OpenCV
- NumPy

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/image-puzzle-assembly.git
    ```
2. Navigate to the project directory:
    ```sh
    cd image-puzzle-assembly
    ```
3. Ensure the sub-images are placed in the `./puzzle/` directory with filenames `img1.png`, `img2.png`, ..., `img18.png`.
4. Run the script:
    ```sh
    python assemble_puzzle.py
    ```

## Code Explanation

- **Background Creation**: A white background is initialized using NumPy:
    ```python
    background = np.ones((600, 1200, 3), np.uint8) * 255
    ```

- **Sub-Image Loading**: Sub-images are loaded using OpenCV:
    ```python
    sub_image1 = cv2.imread("./puzzle/img1.png")
    # ... load other images similarly
    ```

- **Image Manipulation Functions**: Functions for resizing, rotating, and flipping images:
    ```python
    def resize(sub_image):
        img = cv2.resize(sub_image, (200, 200))
        img = cv2.addWeighted(img, 1.5, np.zeros(img.shape, img.dtype), 0, 0)
        return img

    def rotate_image(image, angle):
        image_center = tuple(np.array(image.shape[1::-1]) / 2)
        rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
        result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
        return result

    def flip(sub_image):
        return cv2.flip(sub_image, 1)
    ```

- **Image Placement**: The `place` function places the sub-images at specified positions:
    ```python
    def place(row, col, sub_image):
        x1 = (col - 1) * sub_image.shape[1]
        x2 = x1 + sub_image.shape[1]
        y1 = (row - 1) * sub_image.shape[0]
        y2 = y1 + sub_image.shape[0]
        background[y1:y2, x1:x2] = sub_image
    ```

- **Image Manipulation and Placement Execution**:
    ```python
    sub_image1 = resize(sub_image1)
    sub_image2 = resize(sub_image2)
    # ... manipulate other images similarly

    place(1, 1, sub_image1)
    place(3, 4, sub_image2)
    # ... place other images similarly
    ```

- **Final Image Save**: The final assembled image is saved:
    ```python
    cv2.imwrite("complete_image.jpg", background)
    ```

## Result

The final output image `complete_image.jpg` will be saved in the project directory, showcasing the assembled puzzle with all sub-images placed in their respective positions.
