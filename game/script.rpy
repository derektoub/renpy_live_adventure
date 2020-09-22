# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ch = Character("Charles")
define cu = Character("Cheolsu")
define da = Character("David")
define dr = Character("Drew")
define j = Character("Jimmy")
define uh = Character("Unspeakable Horror")
define s = Character("Sesshomaru")
define y = Character("Yeonghui")
define u = Character("Usagi")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene beach

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music "audio/cute music.mp3"

    show unspeakable_horror
    show usagi at right behind unspeakable_horror
    show jimmy at left behind unspeakable_horror
    show charles at right

    # These display lines of dialogue.

    uh "You know what's coming right?"

    uh "The time has finally come..."

    menu:
        uh "What will you do?"

        "Breakdance":
            uh "You've made a terrible mistake"

        "Run away":
            uh "Wait for me baby!"
    # This ends the game.

    return
