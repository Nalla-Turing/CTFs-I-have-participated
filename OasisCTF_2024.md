# It all starts with a flag
It all started with challenge that asked me to add the flag it has given. So began my first ever CTF.
Ready PLayer?
.
.
.
.
*Goooooo*
<br><br><br>

##
<br><br>

## Knock Knock
`At last, the key darts towards the door, a keyhole materializes, and the door swings open. Author’s Note: I don’t know about you, but I was definitely growing tired of this key. You find yourself standing at the entrance of a labyrinth. The only way out is to navigate through the labyrinth itself. However, the entrance is guarded by an image recognition system. A QR code is pasted on the wall beside it. Your task is clear: bypass the system to gain entry.`


This challenge gives me a QR code but it is dirty.
I have seen this challenge. 
All thsoe Games Theory and spending time with matpat came handy.

I edit the qr and briighten upand increase contrast the qr unless it is clear
Scanning I get the flag

Flag `OASIS{qu3u3r_r3c0v3r3r}`
<br><br>

## MICROSOFT StrongEdge
`Upon repairing the QR code, you scan it and discover it contains a file. As you meticulously sift through its contents, nothing of value seems to emerge. The mystery deepens—where could the next clue be hidden?`
This give us  pptx file with the first slide hvaing some file in it.

I take the text and run it on ROT13 decryptior and get the flag

flag `OASIS{r0t4t0r_0f_pp75}`

<br><br>

## Quench your thrust
`How could the IOI overlook such a critical flaw? You now possess administrative privileges! Surveying your surroundings, you notice the monitor displaying a series of commands accessible only to the admin. However, another security measure is in place—it’s encrypted, and only the true admin knows the key. Can you crack this encryption scheme?`

Ok this was kinda confusing.......
We get a text file with some form of cipher but no matter what cipher I use... It doesn't work.
Using the hint I learn about in popular cipher you can find the cipher by trying to find the most frequently coming up letters.
This is called `Frequency Analysys`

Using this i find that `Y Q Z J` are repeating. So wit that information
I get some words forming up...!!!!!!!

So using that an almighty chatgpt I find the decrypted text.
    AS THE PROTAGONIST STUMBLED INTO THE HEART OF THE IOIS TRAP THE WALLS AROUND HIM FLICKERED WITH SCORCHING HEAT A MASSIVE IMPENETRABLE FIREWALL ROARED IN EVERY DIRECTION CUTTING OFF HIS ESCAPE THE IOI HAD ANTICIPATED HIS INFILTRATION AND THIS WAS THEIR FINAL GAMBIT TO STOP HIM BUT ARTEMIS HAD LEFT HIM WITH A GIFT A COMPUTER TERMINAL IN THE CENTER OF THE CHAMBER THE SCREEN BLINKED TO LIFE AWAITING INPUT WITH A FLASH OF INSPIRATION HE REALISED WHAT HE NEEDED TO DO ADMIN PRIVILEGES HAD BEEN UNLOCKED THE COMMANDS HE EGGSECUTED HERE COULD DISMANTLE THE FIREWALL AND ALLOW HIM TO REACH THE HEART OF THE VIRUS IF HE FOLLOWED THE CORRECT ORDER THE LIST OF ADMIN COMMANDS APPEARED ON THE SCREEN ADMIN COMMAND LIST FIREWALL BYPASS 1 VERIFY THE CURRENT STATUS OF THE FIREWALL SCANNING FOR VULNERABILITIES IN THE DEFENSE SYSTEMS
    2 DISABLE THE FIREWALLS AUTOREPAIR MECHANISM WHICH REGENERATES ANY BREACHED SECTIONS
    3 DISPLAY ALL ACTIVE FIREWALL LAYERS THIS REVEALS THE NUMBER OF DEFENSIVE LAYERS AND THEIR RESPECTIVE CONFIGURATIONS
    4 MANUALLY DISABLE THE THIRD FIREWALL LAYER WHICH HAS BEEN IDENTIFIED AS THE STRONGEST BARRIER PROTECTING THE CORE
    5 SCAN FOR MALICIOUS PATTERNS THAT MIGHT BE HIDDEN INSIDE THE FIREWALL CODE THIS HELPS NEUTRALISE ANY TRAPS LAID BY IOI
    6 ISOLATE THE SIGNATURE FILE USED BY IOI TO SUSTAIN THE FIREWALLS INTEGRITY
    7 OVERRIDE THE FIREWALLS ENCRYPTION WITH THE HIGHEST LEVEL ADMIN PRIVILEGES BREAKING IOIS CONTROL OVER IT
    8 EGGSECUTE A COMPLETE SHUTDOWN OF ALL FIREWALL LAYERS LEAVING THE SYSTEM UNPROTECTED FOR A BRIEF MOMENT
    9 RESET THE ACCESS CONTROLS TO OASIS GATEWAYS ALLOWING UNRESTRICTED MOVEMENT THROUGH THE SERVERS THE TERMINAL BEEPED WITH EACH SUCCESSFUL COMMAND EGGSECUTION AND THE HEAT AROUND HIM BEGAN TO FADE WITH EVERY FIREWALL LAYER DEACTIVATED THE PATH FORWARD BECAME CLEARER HE WAS ALMOST THROUGH ONLY ONE FINAL COMMAND TO DISABLE THE LAST OF IOIS TRAPS AND HE WOULD HAVE ACCESS TO THE VIRUS CONTROLS THE FATE OF THE OASIS WAS NOW IN HIS HANDS
    HTTPS://KATB.IN/YXNZORQJ

flag `oasis{fr3qu3nt_j4!l_br34k1ng_m4k3s_!`t_t00_3asy_fr}


<br><br>

## Stairway to Heaven
`The ground beneath you trembles as Tetris blocks rain from the shadows, cascading down like a storm. At first, panic sets in, but then you realize: these blocks aren’t meant to crush you—they’re your escape. Each piece, carefully arranged, could form a staircase to the control room floating above in the void. It’s time to use them strategically and rise to safety. Stack the blocks and find your way out!`

This challenge gives an executable file `./game`
Running that in wsl gives this
![message](/Message.png)

I tried to convert this into text as i read somwhere that you can actually convert your test into an image file
And i get the code that gives me the text on convertinf it

Flag `OASIS{v34y_f4ncy_AN5I}`
<br><br>

## Heads up,Tails Down
`Finally, you step into the admin control room. Decay has overtaken the space—screens flicker, panels glitch, and virus-riddled code runs rampant across every surface. The system is on the brink of collapse. You sit at the central terminal, but it's unresponsive, frozen by the infection. It’s up to you to repair the system and revive the decaying screens. Only then can you regain control.` 

OK so opening the url, you get a png file that is cracked.Easy I will use a png fixer aaaaaand it's not working ofcoursee.
So i try to find it's meta data using exiftools.

OK it says unknown file type.
On googling it turns i will need to change it's hex code to make it png file.

I used a hex editor online to do it
OK so the first 8 bytes needs to `89 50 4E 47 0D 0A 1A 0A` as it determines the type of the file we have
And changing the next files showing IDHD chunk as `00 00 00 0D 49 48 44 52` with some modification

We get the flag

Flag `OASIS{h34d_c4rr135}`
<br><br>

## A rcoky start
`The game has finally loaded! Yet, as you start to play, a sinking realization dawns: you've been led into a trap. The virus has ensnared you in a loop, wasting precious time. The game is rigged to stall your progress. To save OASIS, you must break free of this digital decoy and bypass the virusâ€™s stalling tactics. Sometimes, you need to overflow the memory's expectations to find a way out.The game is broken; you can't shoot. However, only if you get a score of 100 or more can you get the flag.`
As the name suggests it was indeed a rocky start :(

We started directlt working on the game code. We installed ghidra and started looking for the machine assembly code.
It tooks us 5 hours of endless grinf that led us to nowhere.....

Then we read the prompt multiple times
Huhhh it talks about overflowing the memory!!!!!!

Wait we are still able to add our name?? what if i try to spam
`MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM`
![Username](/Screen.png)



Huh???? The score went to 70.... Less gooo progresss
![Score](/Score.png)

hmmmmmmm.... Wait a second !!!! 70 is the ASCII of M...
Then spamming d instead of M I got it to score 100 and got the flag.

Flag `OASIS{D0DG3_4LL_TH3_R0CK5_0R_N07}`

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
