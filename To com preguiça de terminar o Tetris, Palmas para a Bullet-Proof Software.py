import pygame
import random

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

SHAPES = [
    [[1, 1, 1, 1]],

    [[1, 1],
     [1, 1]],

    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 1, 1],
     [1, 1, 0]],

    [[1, 1, 0],
     [0, 1, 1]],

    [[1, 1, 1],
     [0, 0, 1]],

    [[1, 1, 1],
     [1, 0, 0]]
]

COLORS = [CYAN, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED]

class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.score = 0
        self.game_over = False

    def new_piece(self):
        """Generate a new random tetromino piece."""
        shape = random.choice(SHAPES)
        color = random.choice(COLORS)
        piece = {
            'shape': shape,
            'color': color,
            'x': GRID_WIDTH // 2 - len(shape[0]) // 2,
            'y': 0
        }
        return piece

    def draw_piece(self, piece):
        """Draw the current tetromino piece."""
        shape = piece['shape']
        color = piece['color']
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, color, pygame.Rect((piece['x'] + x) * BLOCK_SIZE, (piece['y'] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, BLACK, pygame.Rect((piece['x'] + x) * BLOCK_SIZE, (piece['y'] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 2)

    def draw_grid(self):
        """Draw the grid."""
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, cell, pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(self.screen, BLACK, pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 2)

    def check_collision(self, piece):
        """Check collision between the piece and the grid."""
        shape = piece['shape']
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if (piece['x'] + x < 0 or piece['x'] + x >= GRID_WIDTH or
                        piece['y'] + y >= GRID_HEIGHT or
                        self.grid[piece['y'] + y][piece['x'] + x]):
                        return True
        return False
#Esse é o pior Tetris da HISTÓRIA
    def drop_piece(self):
        """Drop the piece to the lowest possible position."""
        while not self.check_collision(self.current_piece):
            self.current_piece['y'] += 1
        self.current_piece['y'] -= 1

    def merge_piece(self):
        """Merge the piece with the grid."""
        shape = self.current_piece['shape']
        color = self.current_piece['color']
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if self.current_piece['y'] + y >= GRID_HEIGHT - 1 or self.grid[self.current_piece['y'] + y + 1][self.current_piece['x'] + x]:
                        self.grid[self.current_piece['y'] + y][self.current_piece['x'] + x] = color
                    else:
                        self.grid[self.current_piece['y'] + y][self.current_piece['x'] + x] = 0

    def remove_filled_rows(self):
        """Remove filled rows from the grid."""
        new_grid = [row for row in self.grid if 0 not in row]
        num_removed_rows = GRID_HEIGHT - len(new_grid)
        if num_removed_rows > 0:
            self.grid = [[0] * GRID_WIDTH for _ in range(num_removed_rows)] + new_grid
            self.score += num_removed_rows * 100

    def draw(self):
        """Draw the game screen."""
        self.screen.fill(BLACK)
        self.draw_grid()
        self.draw_piece(self.current_piece)
        self.draw_score()
        pygame.display.flip()
#BTW, se tu clicar espaço o bloco desaparece automaticamente.
    def draw_score(self):
        """Draw the score on the screen."""
        font = pygame.font.Font(None, 24)
        text = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(text, (10, 10))

    def run(self):
        """Run the game loop."""
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.current_piece['x'] -= 1
                        if self.check_collision(self.current_piece):
                            self.current_piece['x'] += 1
                    if event.key == pygame.K_RIGHT:
                        self.current_piece['x'] += 1
                        if self.check_collision(self.current_piece):
                            self.current_piece['x'] -= 1
                    if event.key == pygame.K_DOWN:
                        self.current_piece['y'] += 1
                        if self.check_collision(self.current_piece):
                            self.current_piece['y'] -= 1
                    if event.key == pygame.K_SPACE:
                        self.drop_piece()
                    if event.key == pygame.K_UP:
                        self.rotate_piece()

            self.current_piece['y'] += 1
            if self.check_collision(self.current_piece):
                self.current_piece['y'] -= 1
                self.merge_piece()
                self.remove_filled_rows()
                self.current_piece = self.next_piece
                self.next_piece = self.new_piece()
                if self.check_collision(self.current_piece):
                    self.game_over = True
            self.draw()
            self.clock.tick(5)

        self.screen.fill(BLACK)
        font = pygame.font.Font(None, 36)
        text = font.render(f"Game Over! Score: {self.score}", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()

    def rotate_piece(self):
        """Rotate the current piece clockwise."""
        shape = self.current_piece['shape']
        rotated_shape = [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0]) - 1, -1, -1)]
        if not self.check_collision({'shape': rotated_shape, 'x': self.current_piece['x'], 'y': self.current_piece['y']}):
            self.current_piece['shape'] = rotated_shape

if __name__ == "__main__":
    game = Tetris()
    game.run()
