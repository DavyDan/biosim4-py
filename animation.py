import pygame
import numpy as np
from PIL import Image  # For creating GIFs

class Animation:
    def __init__(self, arenasize, screen_size=800, cell_size=40):
        # Initialize animation parameters
        self.arenasize = arenasize
        self.screen_size = screen_size
        self.cell_size = cell_size
        self.frames = []  # Store frames for the GIF

        # Initialize Pygame screen
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        pygame.display.set_caption('Bug Simulation')

    def render_grid(self, grid):
        """Render the grid (NumPy array) onto the Pygame screen."""
        self.screen.fill((255, 255, 255))  # Fill the screen with white

        # Loop through the NumPy array and display each cell
        for x in range(self.arenasize):
            for y in range(self.arenasize):
                # Color cells based on their value (can be customized)

                color = (255, 255, 255) if grid[x, y] == 0 else (0, 255, 0)  # Default: white for empty, green for occupied
                pygame.draw.rect(self.screen, color, pygame.Rect(y * self.cell_size, x * self.cell_size, self.cell_size, self.cell_size))

    def capture_frame(self):
        """Capture the screen as an image and store it in the frames list."""
        frame = pygame.surfarray.array3d(pygame.display.get_surface())  # Capture the screen
        frame = np.transpose(frame, (1, 0, 2))  # Transpose to correct orientation (OpenCV uses BGR instead of RGB)
        frame_image = Image.fromarray(frame)  # Convert to PIL image
        self.frames.append(frame_image)  # Add the frame to the frames list

    def create_gif_from_grids(self, metagridstate):
        """Generate the GIF from the list of grid states."""
        # Render each grid state and capture a frame
        for i, gridstate in enumerate(metagridstate):
            for grid in gridstate:
                self.render_grid(grid)  # Render each grid state
                self.capture_frame()  # Capture the frame
            self.frames[0].save(f'gengifs/Gen{i}.gif', save_all=True, append_images=self.frames[1:], duration=100, loop=0)
            self.frames.clear()
        # Save the GIF

        # Quit pygame after creating the gif
        pygame.quit()
