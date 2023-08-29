from PIL import Image

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the skull using a 2D array of 0s (no pixel) and 1s (pixel)
# This is a small grid for illustration. You can expand it for more detail.
SKULL = [
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0]
]

# Define the size of each pixel (you can adjust this for your desired granularity)
PIXEL_SIZE = 10

# Create a blank white image
image_width = len(SKULL[0]) * PIXEL_SIZE
image_height = len(SKULL) * PIXEL_SIZE
img = Image.new('RGB', (image_width, image_height), WHITE)
pixels = img.load()

# Draw the skull on the image
for i in range(len(SKULL)):
    for j in range(len(SKULL[i])):
        if SKULL[i][j]:
            for x in range(PIXEL_SIZE):
                for y in range(PIXEL_SIZE):
                    pixels[j * PIXEL_SIZE + x, i * PIXEL_SIZE + y] = BLACK

# Save the image
img.save('pixel_skull.png')
img.show()
