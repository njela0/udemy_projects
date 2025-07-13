from turtle import Turtle

class Snake():
    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        """Creates a three segments long snake."""
        for _ in range(3):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            self.snake_segments.append(new_segment)

        for index, segment in enumerate(self.snake_segments):
            if index < len(self.snake_segments) - 1:
                x_cor = segment.xcor()
                y_cor = segment.ycor()

                self.snake_segments[index + 1].teleport(x_cor - 20, y_cor)


    def move(self):
        """Moves the snake forwards."""
        for segment_num in range((len(self.snake_segments) - 1), 0, -1):
            x_cor_new = self.snake_segments[segment_num - 1].xcor()
            y_cor_new = self.snake_segments[segment_num - 1].ycor()

            self.snake_segments[segment_num].goto(x_cor_new, y_cor_new)

        self.snake_segments[0].forward(20)


    def turn_left(self):
        """Turns the snake left."""
        self.snake_segments[0].left(90)


    def turn_right(self):#
        """Turns the snake right."""
        self.snake_segments[0].right(90)