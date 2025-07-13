from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake():
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        """Creates a three segments long snake."""
        new_segment = Turtle()
        new_segment.shape("circle")
        new_segment.color("brown1")
        new_segment.penup()
        self.snake_segments.append(new_segment)

        for _ in range(2):
            self.grow()

        for index, segment in enumerate(self.snake_segments):
            if index < len(self.snake_segments) - 1:
                x_cor = segment.xcor()
                y_cor = segment.ycor()

                self.snake_segments[index + 1].teleport(x_cor - 20, y_cor)

    def grow(self):
        """Adds another segment to the end of the snake."""
        new_segment = Turtle()
        new_segment.shape("circle")
        new_segment.color("yellowgreen")
        new_segment.penup()
        self.snake_segments.append(new_segment)


    def move(self):
        """Moves the snake forwards."""
        for segment_num in range((len(self.snake_segments) - 1), 0, -1):
            x_cor_new = self.snake_segments[segment_num - 1].xcor()
            y_cor_new = self.snake_segments[segment_num - 1].ycor()

            self.snake_segments[segment_num].goto(x_cor_new, y_cor_new)

        self.snake_head.forward(20)


    def turn_right(self):
        """Turns the snake right"""
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)


    def turn_up(self):
        """Turns the snake upwards."""
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)


    def turn_left(self):
        """Turns the snake left"""
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)


    def turn_down(self):#
        """Turns the snake downwards."""
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
