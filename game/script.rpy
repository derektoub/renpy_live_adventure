# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ch = Character("Eric")
define cu = Character("Cheolsu")
define da = Character("Pichael")
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

    python:
        characters = [
            'Unspeakable Horror',
            'Sesshomaru',
            'Usagi',
            'Charles',
            'Cheolsu',
            'David',
            'Jimmy',
            'Yeonghui',
            'Drew'
        ]
        love_meter = {name: 0 for name in characters}

    jump concert

    scene bg beach

    # jump concert

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
    $ num_attacks = 0

    while boss_health > 0 and player_health > 0:

        call boss_attack(num_attacks=num_attacks)

        $ num_attacks += 1

        show bg beach with Dissolve(1)

        menu:

            "Choose a spell"

            "Airflares":
                $ boss_health -= 10
                $ boss_health = max(boss_health, 0)
                play sound "audio/hell yeah.mp3"
                uh "oh damn"

            "Throw water":
                $ boss_health -= 99
                $ boss_health = max(boss_health, 0)
                play sound "audio/water splash.mp3"
                uh "That felt good baby!"

            "Ultimate attack":
                $ boss_health -= 1
                $ boss_health = max(boss_health, 0)
                play music "audio/filthyfrank sad piano.mp3"
                play sound "audio/crying.mp3"
                uh "What did you just do to me??"
        if boss_health > 0:
            uh "Heh, I still have [boss_health]/100 health"
        else:
            uh "Woo, you got me this time!"

    if boss_health == 0:
        uh "I think I'm starting to like you ;)"
        hide unspeakable_horror
        with moveouttop
        $ lover = 'Unspeakable Horror'
        $ love_meter[lover] += 1
        "Congrats, Unspeakable Horror's love meter increased to [love_meter[Unspeakable Horror]]!"
    elif player_health == 0:
        uh "I was hoping for better"

    uh "Let's do it again tomorrow?"

    label concert:
        scene bg concert with Dissolve(1)

        play music "audio/alcohaulin ass.mp3"

        show david at right with moveintop:
            yalign .5 subpixel True

            parallel:
                rotate 0
                linear 2 rotate 360
                repeat
            # parallel:
            #     xalign .5
            #     linear 3.0 xalign .75
            #     linear 6.0 xalign .25
            #     linear 3.0 xalign .5
            #     repeat

            # parallel:
            #     alpha 1.0 zoom 1.0
            #     linear .75 zoom .9
            #     linear .75 zoom 1.0
            #     repeat

        show charles at left with moveinleft:
            yalign .5 subpixel True

            parallel:
                xalign .5
                linear 3.0 xalign .75
                linear 6.0 xalign .25
                linear 3.0 xalign .5
                repeat

            parallel:
                alpha 1.0 zoom 1.0
                linear .75 zoom .9
                linear .75 zoom 1.0
                repeat

            parallel:
                rotate 0
                linear 0.25 rotate 360
                repeat

        da "You ready to play Pichael?"

        ch "One minute I need to finish breakdancing"

        "Pichael does airflares while Eric and the band play"

        "He flies off the stage and into the crowd"

        play music "audio/sleepytime gorilla museum.mp3"

        "The audience is shocked when he turns into a vegetable"

        "Several innocent bystanders also transform into various foods"

        da "Eric, even though you are a vegetable, you're still pretty cute ;)"

        da "I'll do whatever it takes to turn you back"

        ch "..."

        menu:

            "Choose a spell"

            "Try setting up a cooking show":
                play sound "audio/cute music.mp3"
                ch "whoa what did you just do???"

                ch "I feel like time just skipped"

                da "*crying*"

                ch "Why are you crying nothing happened?"

                jump good_path


            "Bring him to the nearest volcano":
                play sound "audio/water splash.mp3"
                play music "audio/khrushchev trap.mp3"
                ch "That felt good baby! But I'm still a vegetable"
                show unspeakable_horror
                with moveinleft
                uh "Hey fancy meeting you here!"

            "Eat the eggplant audience members":
                play music "audio/brutaldubstep.mp3"
                da "Cool now I'm an eggplant"
                "They lived happily ever after..."

    label good_path:

        scene bg cafe

        show drew with moveinright

        show david with moveintop

        show charles with moveinbottom

        dr "You seriously thought I would just let you be together?"

        ch "Yes.."

        dr "You best be ready to dance, young man"

        ch "Oh boy"

        menu:

            "Airflares":
                "rick always wins"

            "Windmills":
                "rick always wins"

            "Toprock":
                "You turn back into a vegetable"



#         Rick is Pichael's dad
#  · Reply · Pin · 2m
# Michael J Block
# Rick says you can't be with Pichael unless you beat me at a breakdancing competition
#  · Reply · Pin · 2m
# Michael J Block
# So Eric accepts the challenge
#  · Reply · Pin · 2m
# Michael J Block
# Eric learned from his former accident, and tricks Rick into making the mistake he formerly made



    return

    label boss_attack(num_attacks=0):

        if num_attacks == 0:
            play music "audio/sleepytime gorilla museum.mp3"
        elif num_attacks == 1:
            play music "audio/prokofiev.mp3"

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

        uh "ULTIMATE ATTACK"

        $ player_health -= 10

        $ player_health = max(player_health, 0)

        "you only have [player_health]/100 health left"

        hide magic

        return
    # This ends the game.


