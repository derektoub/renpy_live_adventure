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

    scene bg beach

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music "audio/cute music.mp3"

    # show unspeakable_horror:
    #     xalign 0.3 yalign 0.7
    #     linear 1.0 xalign 0.4 yalign 0.6
    #     linear 1.0 xalign 0.3 yalign 0.7
    show unspeakable_horror:
        # parallel:
        linear 1.0 xalign 0.0
        linear 1.0 xalign 1.0
        repeat
        # parallel:
        #     linear 0 yalign 1.3
        #     linear 1.3 yalign 0.0
        #     repeat

    with zoomin
    show usagi at right behind unspeakable_horror
    with move
    # show jimmy at left behind unspeakable_horror
    show charles at right
    with move

    # These display lines of dialogue.

    uh "You know what's coming right?"

    uh "The time has finally come..."
    $ boss_health = 100
    $ player_health = 100
    $ current_song = "cute"

    while boss_health > 0 and player_health > 0:

        call boss_attack(boss_taunt="ULTIMATE ATTACK")

        show bg beach with Dissolve(1)

        menu:

            "Choose a spell"

            "Airflares":
                $ boss_health -= 10
                $ boss_health = max(boss_health, 0)
                play sound "audio/hell yeah.mp3"
                uh "You've made a terrible mistake"

            "Throw water":
                $ boss_health -= 99
                $ boss_health = max(boss_health, 0)
                uh "That felt good baby!"

            "Ultimate attack":
                $ boss_health -= 1
                $ boss_health = max(boss_health, 0)
                play music "audio/filthyfrank sad piano.mp3"
                play sound "audio/crying.mp3"
                $ current_song = "sad"
                uh "What did you just do to me??"

        uh "Heh, I still have [boss_health]/100 health"

    if boss_health == 0:
        uh "I think I'm starting to like you ;)"
        uh "I lost this time.."
        hide unspeakable_horror
        with moveouttop
    elif player_health == 0:
        uh "I was hoping for better"

    uh "Let's do it again tomorrow?"

    return

    label boss_attack(boss_taunt=""):

        if current_song != "dubstep":
            play music "audio/brutaldubstep.mp3"
            $ current_song = "dubstep"

        show bg ominoustrees with Dissolve(1)

        show magic with Dissolve(1):
            yalign .5 subpixel True

            parallel:
                xalign .5
                linear 3.0 xalign .75
                linear 6.0 xalign .25
                linear 3.0 xalign .5
                repeat

            parallel:
                alpha 1.0 zoom 1.0
                linear .75 alpha .5 zoom .9
                linear .75 alpha 1.0 zoom 1.0
                repeat

            parallel:
                rotate 0
                linear 5 rotate 360
                repeat

        uh "[boss_taunt]"

        $ player_health -= 10

        $ player_health = max(player_health, 0)

        "you only have [player_health]/100 health left"

        hide magic

        return
    # This ends the game.


