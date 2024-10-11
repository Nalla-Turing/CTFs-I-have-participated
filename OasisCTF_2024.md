# It all starts with a flag
It all started with challenge that asked me to add the flag it has given. So began my first ever CTF.
Ready PLayer?
.
.
.
.
*Goooooo*
<br><br><br>

## A rcoky start
`The game has finally loaded! Yet, as you start to play, a sinking realization dawns: you've been led into a trap. The virus has ensnared you in a loop, wasting precious time. The game is rigged to stall your progress. To save OASIS, you must break free of this digital decoy and bypass the virusâ€™s stalling tactics. Sometimes, you need to overflow the memory's expectations to find a way out.The game is broken; you can't shoot. However, only if you get a score of 100 or more can you get the flag.`
As the name suggests it was indeed a rocky start :(
    
<br><br>

## Comma Separated virus
`Victory comes not from playing the game, but from outwitting it. Yet, even as you break free, you realize the virus has hidden itself deep within the OASIS database. Thousands—maybe millions—of data fragments fill the screen. Somewhere among them, the virus lies dormant, waiting to strike again. It’s time to sift through the noise and identify the hidden threat. Using the basics of machine learning, perform exploratory data analysis to try and figure out a pattern. Can you find the virus among the data?`

This one was easy. Going to the link gave us csv file.
I tried different pattern and quickly found that we had to remove all the blanks and filter TUNE column in descending

flag `OASIS{TROJAN}`

<br><br>

## Mo-sike
`You’ve uncovered the truth: it was a Trojan all along. Disguised as an integral part of the OASIS, the virus has been feeding vital information to IOI, undermining the system from within. Now, with its cover blown, you must track the data trails left behind by the Trojan before it can do any more damage. These data trails are in the form of a file containing a sequence of color names, each representing a piece of a larger mosaic. This mosaic forms a square grid, and when the squares are correctly arranged, they reveal a hidden image of a video game character. Your task is to decipher the relationship between the color list and the grid, reconstructing the image by placing each colored square in its correct position. The challenge lies in ensuring that the final arrangement reveals the intended character, with no visual discrepancies.. Follow the breadcrumbs and uncover its next move.Flag format: OASIS{nameofcharacter_nameofgame} in lowercase`

Ok so on clicking the file we get a text fle with the name of colour squares in the mosaic.
So i make code to print the mosaic blocks, to get an idea what it looks like
But the blocks are way too big

The code looked something like this and yes i took help of chatgpt due time constraints

    import tkinter as tk

    def create_mosaic(color_list, grid_size=56):
        # Create a new Tkinter window
        window = tk.Tk()
        window.title("Mosaic Grid")

        # Calculate the size of each block
        window_width = window.winfo_screenwidth()
        window_height = window.winfo_screenheight()
        block_size = min(window_width, window_height) // grid_size

        # Create a canvas for drawing the mosaic
        canvas = tk.Canvas(window, width=grid_size * block_size, height=grid_size * block_size)
        canvas.pack()

        # Loop through the grid and create each block
        for row in range(grid_size):
            for col in range(grid_size):
                color = color_list[row * grid_size + col].strip().lower()
                x1, y1 = col * block_size, row * block_size
                x2, y2 = x1 + block_size, y1 + block_size
                canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

        # Start the Tkinter event loop
     window.mainloop()

    # Example string of colors, repeat to ensure enough colors for the grid
    color_string = """
    red green blue yellow cyan magenta purple orange brown pink lime teal navy olive gray white
    """
    # Split the color string into a list
    color_list = color_string.split() * 313  # Repeat the list to get enough colors for the 56x56 grid

    # Create the mosaic
    create_mosaic(color_list)
The blocks are visible

A lot of yellow and red
Can it be packman or perhaps the original mario and super mario bros??
Nope

Wait a minute !!!!
I know this pattern!!!!
This is that  stupid pokemon....missingo

flag `OASIS{missingno_pokemon}`

<br><br>

## I am Optimus Prime
As you set out to warn the OASIS community about the Trojan's infiltration, your efforts are abruptly interrupted. Mechanoids, armed and dangerous, have been dispatched by IOI to stop you. These mechanical enforcers close in, their metallic limbs glinting in the digital light. It's time to fight back and escape their relentless assault. Can you outmaneuver these foes and stay alive? https://blogpost.oasis.cryptonite.live

This was the prompt, on going to the said link I reach the website that looked something like this

![Blogpost challenge](/Photo%20one.png)

Since it is one of those webpage challenge my first instint was to go into inspect element and search for if I can find any functionality to the save button??? Did't find anything

So i went to that discord and the hin that was given said something about `"robot-only" no no zone`.
On chatgpting It turns out in webpages there are some areas that are restricted for most people. To keep web crawlers away from this areas, developers add sections telling which area is prohibited.

Following on that I add `/robots.txt` to the url and got into a page giving this output
    User-agent: *
    Disallow: /hiddenFlag

Meaning the /hiddenFlag area is prohibited for everyone, so that means I will need tp try somnething in the console to get the flag output.

So I searched how do we usually get access to this kind of area????? 

It tells me to use different https methods to test the effects but there are so many https method? which one do I use??? 
To check this I use `curl -X OPTIONS -i https://blogpost.oasis.cryptonite.live`
and get this
    HTTP/2 400
    cache-control: public, max-age=0, must-revalidate
    content-type: text/html; charset=utf-8
    date: Thu, 10 Oct 2024 18:00:58 GMT
    server: Vercel
    strict-transport-security: max-age=63072000
    x-vercel-cache: MISS
    x-vercel-id: bom1::iad1::cntpm-1728583258673-75fa10664b80
    content-length: 13

    Invalid token

The token is missing, so to find I take a wild guess and find it in cookies and found something very interetsing
`user_token:"f308d3f1-7f1a-4e8d-a370-6347ea545322"`

Using this I use the options method again
Now all i need is to check POST, PATCH methods
and then it got me the flag using options again
flag `OASIS{r0b0t5_4nd_m37h0d5_4r3_pr3tty_c00l!}`    
