import tkinter as tk
import itertools as IT  # avoiding double loops
import ConnectFour  # the game API
import pygame

class GameScreen(tk.Tk):
    def __init__(self):
        super().__init__()
      
        self.title("Connect Four v1.0")
        self._rows = 6
        self._cols = 7
        #put the window in the center
        self.app_height=700
        self.app_width=800
        self.screenWidth=self.winfo_screenwidth()
        self.screenHeight=self.winfo_screenheight()
        self.x=(self.screenWidth/2)-(self.app_width/2)
        self.y=(self.screenHeight/2)-(self.app_height/2)
        self.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')

        # create the top canvas for the game board
        canvas= tk.Canvas(self, bg="#13005A")
        self.create_board(canvas)
        canvas.pack(fill=tk.BOTH, expand=True)

        # create the bottom frame for the game state
        frame = tk.Frame(self)
        self.text1 = tk.Label(
            frame,
            bd=1,
            text="Round 1",
            relief=tk.RAISED,
            bg="lightgrey",
            fg="black")
        self.text2 = tk.Label(
            frame,
            bd=1,
            text="Black's turn",
            relief=tk.RAISED,
            bg="lightgrey",
            fg="black")
        self.text3 = tk.Label(
            frame,
            bd=1,
            text="Undecided",
            relief=tk.RAISED,
            bg="lightgrey",
            fg="black")
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        self.text1.grid(row=1, column=0, sticky=tk.E + tk.W)
        self.text2.grid(row=1, column=1, sticky=tk.E + tk.W)
        self.text3.grid(row=1, column=2, sticky=tk.E + tk.W)
        frame.pack(side=tk.BOTTOM, fill=tk.X)

        # create new game
        self.game = ConnectFour.Game()

    def create_board(self, canvas):
        """Create a new empty board with circle shapes for discs"""
        self.board = [[None] * self._cols for _ in range(self._rows)]
        self.buttons = [[None] * self._cols for _ in range(self._rows)]
        for i, j in IT.product(range(self._rows), range(self._cols)):
            self.board[self._rows - 1 - i][j] = L = tk.Canvas(
                canvas,
                bg="#13005A",
                height=100,
                width=100,
                relief="raised",
                highlightthickness=0)
            padding = 2
            id = self.buttons[self._rows - 1 - i][j] = L.create_oval(
                (padding, padding, 80 + padding, 80 + padding),
                outline="black",
                fill="lightgrey")
            width = L.winfo_reqwidth()
            height = L.winfo_reqheight()
            L.configure(width=width, height=height)

            canvas.rowconfigure(i, weight=1)
            canvas.columnconfigure(j, weight=1)
            L.grid(
                row=i,
                column=j,
                padx=3,
                pady=3,
                sticky=tk.E +
                tk.W +
                tk.N +
                tk.S)
            L.bind('<Button-1>', lambda e, id=id, j=j: self.on_click(e, id, j))

    def on_click(self, event, id, j):
        """Column j was clicked. The method that actually preform the moves."""
        pygame.mixer.init()
        pygame.mixer.music.load("music/mixkit-gaming-lock-2848.wav")
        pygame.mixer.music.play(loops=1)
        player = self.game.turn
        player_color = "black" if self.game.turn == 'X' else "white"
        next_player_color = "white" if self.game.turn == 'X' else "black"
        try:
            self.game.move(j)
            self.text3.config(text="Undecided".format(j))
        except ConnectFour.FullColumn as e:
            self.text3.config(text="Column {} is full".format(j))
            return

        i = self.game.col_size[j] - 1
        self.board[i][j].itemconfig(
            id, fill=player_color, tags="{}".format(player))
        self.text1.config(text="Round {}".format(self.game.round))
        self.text2.config(text="{}'s turn".format(next_player_color))
        if self.game.winner in ["X", "Y"]:
            self.text3.config(text="{} has won!".format(player_color))
            self.text2.config(text="The End")
            pygame.mixer.init()
            pygame.mixer.music.load("music/mixkit-arcade-game-opener-222.wav")
            pygame.mixer.music.play(loops=0)
            self.canva = tk.Canvas(self,width= 900, height= 800,bg="black",bd=0,highlightcolor="black",highlightbackground="black")
            
            self.img1=tk.PhotoImage(file="./imgs/1000_F_230211192_R64ABnxLSLCUQjDnwzZFvws6F0JJvFOC.png")
            self.canva.create_image(400,250,image=self.img1)
            self.canva.place(x=0,y=0)
            if self.game.winner=='X':
                    self.canva2 = tk.Canvas(self,width= 900, height= 150,bg="black",bd=0,highlightcolor="black",highlightbackground="black")
                    self.img2=tk.PhotoImage(file="./imgs/final1.png")
                    self.canva2.create_image(400,100,image=self.img2)
                    self.canva2.place(x=0,y=500)
            if self.game.winner=='Y':
                    self.canva3 = tk.Canvas(self,width= 900, height= 150,bg="black",bd=0,highlightcolor="black",highlightbackground="black")
                    self.img3=tk.PhotoImage(file="./imgs/final2.png")
                    self.canva3.create_image(400,100,image=self.img3)
                    self.canva3.place(x=0,y=500)
        if self.game.winner == 'D':
            self.text1.config(text="Round 42")
            self.text2.config(text="The End")
            self.text3.config(text="Draw")
            for i, j in IT.product(range(self._rows), range(self._cols)):
                self.board[i][j].unbind("<Button-1>")

    def flash_discs(self, discs, winner, altcolor):
        """Alternate color of given discs"""
        for disc in discs:
            row = disc[0]
            col = disc[1]
            self.board[row][col].itemconfig(
                self.buttons[row][col], fill=altcolor)

        self.after(250, self.flash_discs, discs, altcolor, winner)


root = GameScreen()
root.mainloop()