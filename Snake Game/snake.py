from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_blocks = []
        self.create_snake()
        self.head = self.snake_blocks[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_block(position)

    def add_block(self, position):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        self.snake_blocks.append(new_block)

    def extend(self):
        self.add_block(position=self.snake_blocks[-1].position())

    def move(self):
        for blocks in range(len(self.snake_blocks) - 1, 0, -1):
            new_x = self.snake_blocks[blocks - 1].xcor()
            new_y = self.snake_blocks[blocks - 1].ycor()
            self.snake_blocks[blocks].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for block in self.snake_blocks:
            block.goto(1000, 1000)
        self.snake_blocks.clear()
        self.create_snake()
        self.head = self.snake_blocks[0]
