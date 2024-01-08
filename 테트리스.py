import tkinter as tk
import random

class Tetris:
    def __init__(self, master):
        self.master = master
        self.master.title("Tetris")
        self.master.geometry("300x600")
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Down>", self.move_down)
        self.master.bind("<Up>", self.rotate_piece)

        self.canvas = tk.Canvas(self.master, width=300, height=600, bg="white")
        self.canvas.pack()

        self.board = [[0] * 10 for _ in range(20)]
        self.current_shape = self.get_random_shape()
        self.current_position = [0, 4]

        self.draw()

        self.update()

    def draw(self):
        self.canvas.delete("all")
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] != 0:
                    self.canvas.create_rectangle(
                        col * 30,
                        row * 30,
                        (col + 1) * 30,
                        (row + 1) * 30,
                        fill="blue",
                        outline="black",
                    )

        for block in self.current_shape:
            x, y = block
            x += self.current_position[0]
            y += self.current_position[1]
            self.canvas.create_rectangle(
                y * 30,
                x * 30,
                (y + 1) * 30,
                (x + 1) * 30,
                fill="blue",
                outline="black",
            )

    def move_left(self, event):
        if self.is_valid_move(self.current_shape, [self.current_position[0], self.current_position[1] - 1]):
            self.current_position[1] -= 1
            self.draw()

    def move_right(self, event):
        if self.is_valid_move(self.current_shape, [self.current_position[0], self.current_position[1] + 1]):
            self.current_position[1] += 1
            self.draw()

    def move_down(self, event):
        if self.is_valid_move(self.current_shape, [self.current_position[0] + 1, self.current_position[1]]):
            self.current_position[0] += 1
            self.draw()

    def rotate_piece(self, event):
        rotated_shape = list(map(lambda x: (-x[1], x[0]), self.current_shape))
        if self.is_valid_move(rotated_shape, self.current_position):
            self.current_shape = rotated_shape
            self.draw()

    def is_valid_move(self, shape, position):
        for block in shape:
            x, y = block
            x += position[0]
            y += position[1]
            if x < 0 or x >= 20 or y < 0 or y >= 10 or self.board[x][y] != 0:
                return False
        return True

    def get_random_shape(self):
        shapes = [
            [(0, 0), (0, 1), (0, 2), (0, 3)],  # I-shape
            [(0, 0), (0, 1), (0, 2), (1, 2)],  # L-shape
            [(0, 0), (0, 1), (0, 2), (-1, 2)],  # J-shape
            [(0, 0), (0, 1), (1, 0), (1, 1)],  # O-shape
            [(0, 0), (0, 1), (1, 1), (1, 2)],  # Z-shape
        ]
        return random.choice(shapes)

    def update(self):
        if self.is_valid_move(self.current_shape, [self.current_position[0] + 1, self.current_position[1]]):
            self.current_position[0] += 1
            self.draw()
        else:
            self.place_piece()
            self.check_lines()
            self.current_shape = self.get_random_shape()
            self.current_position = [0, 4]

        self.master.after(500, self.update)

    def place_piece(self):
        for block in self.current_shape:
            x, y = block
            x += self.current_position[0]
            y += self.current_position[1]
            self.board[x][y] = 1

    def check_lines(self):
        lines_to_remove = []
        for i in range(len(self.board)):
            if all(self.board[i]):
                lines_to_remove.append(i)

        for line in lines_to_remove:
            del self.board[line]
            self.board.insert(0, [0] * 10)

        self.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = Tetris(root)
    root.mainloop()
