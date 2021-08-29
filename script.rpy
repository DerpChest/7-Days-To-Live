#( I see you snooping around the code! ͡° ͜ʖ ͡° Don't get too nosy.)
#Intizile images
init:
    image bedroom = im.Scale("images/bedroom.png", 1920,1080)
    image docOffice = im.Scale("images/doctorsOffice.png", 1920,1080)
    image Schoolcampus = im.Scale("images/schoolCampus.png", 1920,1080)
    image schoolHallway = im.Scale("images/schoolHallway.png", 1920,1080)
    image ArcadePlace = im.Scale("images/arcadebg.jpg", 1920,1080)
    image Black = im.Scale("images/black.jpg", 1920,1080)
    image mommy = im.Scale("images/mommy.png", 710,1000)
    image mommySad = im.Scale("images/mommySad.png", 710,1000)
    image mommyTriggered = im.Scale("images/mommyTriggered.png", 710,1000)
    image Crush = im.Scale("images/yourCrush.png", 710,1000)
    image CrushSad = im.Scale("images/yourCrushSad.png", 710,1000)
    image CrushTriggered = im.Scale("images/yourCrushTriggered.png", 710,1000)
    image bullyph = im.Scale("images/bullyplaceholder.jpg", 710,1000)
    image Dr = im.Scale("images/Doctorhappy.png", 710,1000)
    image DrSad = im.Scale("images/Doctorsad.png", 710,1000)
    image bff = im.Scale("images/bffHappy.png", 710,1000)
    image bffsad = im.Scale("images/bffSad.png", 710,1000)
    image bffMeh = im.Scale("images/bffMeh.png", 710,1000)
    image bullyHappy = im.Scale("images/BullyHappy.png", 1000,1000)
    image bullySad = im.Scale("images/BullySad.png", 1000,1000)
    image DanielNormal = im.Scale("images/DanielNormal.png", 1000,1000)
    image DanielMad = im.Scale("images/DanielMad.png", 1000,1000)
    image Heaven = im.Scale("images/Heaven.jpg", 1920,1080)
    image EileenConcerned = im.Scale("images/eileen concerned.png", 320,720)
    image EileenHappy = im.Scale("images/eileen happy.png", 320,720)
    image Nikkibedroom = im.Scale("images/nikkisbedroom.png", 1920,1080)
    image CabinBg = im.Scale("images/cabinbg.png", 1920,1080)
    image Car = im.Scale("images/insidethecar.png", 1920,1080)
    image airport = im.Scale("images/airbortbg.jpg", 1920,1080)
#declare characters
define Mom = Character("Mom")
define Dr = Character("Dr. Green")
define bully = Character("Chester")
define Crush = Character("Nikki")
define BestFriend = Character("Blake")
define Crowd = Character("Literally Everyone")
define Eileen = Character("Eileen")
define NikkiDad = Character("Nikki's Dad")
define Daniel = Character("Daniel")
define FakeProtag = Character("'[playerName]'")
#The Game Starts here
label start:
    #Asking the player for there name
    $ playerName = renpy.input("What is your name")
    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName = "Player"

    define Protag = Character("[playerName]")
    jump Prolouge

label Prolouge:
    "Prolouge: Sunday"
    #Changes Background
    scene bedroom
    play music "happyday.mp3"
    #show Mom
    show mommy
    #Start Mom script
    Mom "Wake Up Honey! It's time for church! So dress up nicely!"
    "You make some weird coughing sound and you twitch."
    "Are you ok?"
    "You do the same thing again"
    "Again"
    "Again"
    #This is the 69th line of my game
    "And again"
    hide mommy
    show mommySad
    Mom "It sounds bad!"
    Mom "We are going to have to cancel church today."
    Mom "Let me visit your doctor"
    hide mommySad
    #with squares
    scene docOffice
    show DrSad
    play music "Kevin MacLeod Sad Trio.mp3"
    Dr "So um, I have some good news, and some bad news."
    Dr "The bad news is."
    Dr "Well,"
    Dr "How do i explain this without causing any drama?"
    Dr "Let's just say that..."
    Dr "You have MERE days to live."
    Dr "You are diagnosed with 7daystoliveitis"
    Dr "It is a type of cancer that completely destroys your body in a week."
    hide DrSad
    show Dr
    Dr "But the good news is that this day does not count, so it starts tommorow."
    "Mom starts bawling."
    hide Dr
    show mommySad
    Mom "But do you have a cure?"
    hide mommySad
    show DrSad
    Dr "Sadfully, we don’t have a cure."
    Dr "So here is your Doctor's note."
    hide Dr
    show mommySad
    Mom "Looks Like starting tomorrow, you are going to have to say goodbye to all of your friends at school."
    hide DrSad
    hide mommySad
    jump Act1
label Act1:
    $ count = 0
    $ bfTALK = True
    $ bullyTALK = True
    scene Schoolcampus
    with squares
    menu Saygoodbye:
        "Who should i say goodbye to first?"
        "My best friend" if bfTALK:
            $ bfTALK = False
            jump bf

        "The Bully" if bullyTALK:
            $ bullyTALK = False
            jump bully

    label bf:
        if count < 2:
            $ count += 1
            show bff
            BestFriend "Hi Pal!"
            Protag "Hey, so i got some bad news."
            hide bff
            show bffsad
            BestFriend "What?"
            Protag "I acutally got {b}7 Days to Live{/b}, Which means i have a week to live"
            BestFriend "Man, Well i wish you goodbye."
            hide bffsad
        if count == 2:
            jump crush
        else:
            jump Saygoodbye


    label bully:
        if count < 2:
            $ count += 1
            show bullyHappy
            bully "Hey! Are you ready for another beating?"
            Protag "Before you beat me up, i actually have a reare disease named '7daystoliveitis', which means i have {b}7 Days to Live{/b}"
            hide bullyHappy
            show bullySad
            bully "Damn, That stinks, i'm actually sorry. I won't beat you up."
            bully "Welp, See you in Class."
            hide bullySad
        if count == 2:
            jump crush
        else:
            jump Saygoodbye

    label crush:
        scene schoolHallway
        stop music
        play music "happyday.mp3"
        Protag "Man, i have been trying to admit to my crush for {b}7 YEARS{/b}!"
        $ renpy.pause(1.5)
        show Crush
        Crush "Hi there!"
        Protag "So um, there is something i have to say to you."
        $ renpy.pause(3.0)
        Protag "I actually have a crush on you."
        python:
            import random
            n = random.randint(1,100000)
        if n == 1:
            $ raise Exception("This is an Easter Egg, Tell me on GameJolt Right Now if you find this screen.")
        else:
            hide Crush
            show CrushTriggered
            Crush "EW! I don't want to be near a hobbit!"
            hide CrushTriggered
            show bffMeh
            BestFriend "What the heck Nikki!"
            BestFriend "He has 7daystoliveitis!"
            BestFriend "and your just treating him like trash!"
            hide bffMeh
            show CrushTriggered
            Crush "WOW! IM {b}TERRIBLY{/b} SORRY!"
            Crush "Just because he asked me out, that does not mean i have to accept"
            hide CrushTriggered
            show bffMeh
            BestFriend "Just because you want your Ex to give you gifts everyday, that does not mean he has to"
            hide bffMeh
            show CrushSad
            Crowd "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!"
            hide CrushSad
            "Nikki runs away crying."
            show bff
            Protag "Thanks for being there for me!"
            BestFriend "Your welcome!"
            hide bff
            show bffMeh
            BestFriend "She was always whiney."
            BestFriend "I can't belive you have a crush on the worst girl in school!"
            hide bffMeh
            show bff
            BestFriend "How about we both go to the arcade tommorow?"
            BestFriend "Is that cool?"
            menu ArcadeChoice:
                "Yeah sure!":
                    BestFriend "Ok! That's cool! Meet you tommorow"
                    jump Act2
                "No thanks!":
                    BestFriend "Its ok! I understand"
                    hide bff
                    scene Black
                    "2 days later."
                    jump Act3
label Act2:
    scene black
    "Day 2: Tuesday"
    scene ArcadePlace
    show bff
    BestFriend "I can't wait to play something in our favorite Arcade!"
    $ renpy.pause(2.5)
    BestFriend "How about we play this pong game!"
    #This is where the pong game is
    jump ponggame
    label ponggame:
        init python:

            class PongDisplayable(renpy.Displayable):

                def __init__(self):

                    renpy.Displayable.__init__(self)

                    # The sizes of some of the images.
                    self.PADDLE_WIDTH = 12
                    self.PADDLE_HEIGHT = 95
                    self.PADDLE_X = 240
                    self.BALL_WIDTH = 15
                    self.BALL_HEIGHT = 15
                    self.COURT_TOP = 129
                    self.COURT_BOTTOM = 650

                    # Some displayables we use.
                    self.paddle = Solid("#ffffff", xsize=self.PADDLE_WIDTH, ysize=self.PADDLE_HEIGHT)
                    self.ball = Solid("#ffffff", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT)

                    # If the ball is stuck to the paddle.
                    self.stuck = True

                    # The positions of the two paddles.
                    self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
                    self.computery = self.playery

                    # The speed of the computer.
                    self.computerspeed = 380.0

                    # The position, delta-position, and the speed of the
                    # ball.
                    self.bx = self.PADDLE_X + self.PADDLE_WIDTH + 10
                    self.by = self.playery
                    self.bdx = .5
                    self.bdy = .5
                    self.bspeed = 350.0

                    # The time of the past render-frame.
                    self.oldst = None

                    # The winner.
                    self.winner = None

                def visit(self):
                    return [ self.paddle, self.ball ]

                # Recomputes the position of the ball, handles bounces, and
                # draws the screen.
                def render(self, width, height, st, at):

                    # The Render object we'll be drawing into.
                    r = renpy.Render(width, height)

                    # Figure out the time elapsed since the previous frame.
                    if self.oldst is None:
                        self.oldst = st

                    dtime = st - self.oldst
                    self.oldst = st

                    # Figure out where we want to move the ball to.
                    speed = dtime * self.bspeed
                    oldbx = self.bx

                    if self.stuck:
                        self.by = self.playery
                    else:
                        self.bx += self.bdx * speed
                        self.by += self.bdy * speed

                    # Move the computer's paddle. It wants to go to self.by, but
                    # may be limited by it's speed limit.
                    cspeed = self.computerspeed * dtime
                    if abs(self.by - self.computery) <= cspeed:
                        self.computery = self.by
                    else:
                        self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

                    # Handle bounces.

                    # Bounce off of top.
                    ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
                    if self.by < ball_top:
                        self.by = ball_top + (ball_top - self.by)
                        self.bdy = -self.bdy


                    # Bounce off bottom.
                    ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
                    if self.by > ball_bot:
                        self.by = ball_bot - (self.by - ball_bot)
                        self.bdy = -self.bdy



                    # This draws a paddle, and checks for bounces.
                    def paddle(px, py, hotside):

                        # Render the paddle image. We give it an 800x600 area
                        # to render into, knowing that images will render smaller.
                        # (This isn't the case with all displayables. Solid, Frame,
                        # and Fixed will expand to fill the space allotted.)
                        # We also pass in st and at.
                        pi = renpy.render(self.paddle, width, height, st, at)

                        # renpy.render returns a Render object, which we can
                        # blit to the Render we're making.
                        r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                        if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                            hit = False

                            if oldbx >= hotside >= self.bx:
                                self.bx = hotside + (hotside - self.bx)
                                self.bdx = -self.bdx
                                hit = True

                            elif oldbx <= hotside <= self.bx:
                                self.bx = hotside - (self.bx - hotside)
                                self.bdx = -self.bdx
                                hit = True

                            if hit:
                                self.bspeed *= 1.10

                    # Draw the two paddles.
                    paddle(self.PADDLE_X, self.playery, self.PADDLE_X + self.PADDLE_WIDTH)
                    paddle(width - self.PADDLE_X - self.PADDLE_WIDTH, self.computery, width - self.PADDLE_X - self.PADDLE_WIDTH)

                    # Draw the ball.
                    ball = renpy.render(self.ball, width, height, st, at)
                    r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                                  int(self.by - self.BALL_HEIGHT / 2)))

                    # Check for a winner.
                    if self.bx < -50:
                        self.winner = "Blake"

                        # Needed to ensure that event is called, noticing
                        # the winner.
                        renpy.timeout(0)

                    elif self.bx > width + 50:
                        self.winner = "[playerName]"
                        renpy.timeout(0)

                    # Ask that we be re-rendered ASAP, so we can show the next
                    # frame.
                    renpy.redraw(self, 0)

                    # Return the Render object.
                    return r

                # Handles events.
                def event(self, ev, x, y, st):

                    import pygame

                    # Mousebutton down == start the game by setting stuck to
                    # false.
                    if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                        self.stuck = False

                        # Ensure the pong screen updates.
                        renpy.restart_interaction()

                    # Set the position of the player's paddle.
                    y = max(y, self.COURT_TOP)
                    y = min(y, self.COURT_BOTTOM)
                    self.playery = y

                    # If we have a winner, return him or her. Otherwise, ignore
                    # the current event.
                    if self.winner:
                        return self.winner
                    else:
                        raise renpy.IgnoreEvent()

        screen pong():

            default pong = PongDisplayable()

            add pong

            if pong.stuck:
                text _("Click to Begin"):
                    xalign 0.5
                    ypos 50
                    size 40

        label play_pong:

            window hide  # Hide the window and  quick menu while in pong
            $ quick_menu = False

            call screen pong

            $ quick_menu = True
            window show



        if _return == "Blake":

            BestFriend "I win!"

        else:


            BestFriend "No Fair."


            return
    "But on that same day."
    scene Nikkibedroom
    show CrushTriggered
    Crush "This dude is ruining all of my fame."
    Crush "Just because he has 7daystoliveitis does not mean he deserves all of the attetion!"
    Crush "Maybe i am going to expose him..."
    Crush "Maybe he is faking the disease,"
    Crush "My plan is going to be so perfect!"
    Crush "Everyone is going to hate him!"
    Crush "He is going to d-"
    NikkiDad "Sweethart!"
    NikkiDad "Are you doing your homework?"
    hide CrushTriggered
    show CrushSad
    Crush "I am dad."
    jump Act3


label Act3:
    scene black
    "Day 3: Wednesday"
    Mom "Wake up, Wake up!"
    scene bedroom
    with fade
    show mommy
    Protag "What is it mom?"
    Mom "We are going on a trip to Tennessee!"
    Protag "Ok, thats cool!"
    Mom "Let's go to the airport now!"
    Protag "Ok, ok."
    scene Car
    with squares
    Protag "What are we even going to do there"
    Mom "We are going to go to a cabin!"
    Mom "With 90's movies from my time!"
    Protag "ok."
    $ renpy.pause(5)
    Mom "Ok, We are here"
    scene Black
    "But in Nikki's house..."
    "Again."
    scene Nikkibedroom
    show Crush
    Crush "Ok so Daniel."
    Crush "So i have this enemy na-"
    hide Crush
    show DanielNormal
    Daniel "Do you have any snacks in here?"
    hide DanielNormal
    show CrushTriggered
    Crush "Uh no, even if i had them, i'm not giving them to you."
    hide CrushTriggered
    show DanielMad
    Daniel "Well you payed me 15$ to be here."
    hide DanielMad
    show CrushTriggered
    Crush "WELL I'M NOT GIVING YOU SNACKS!"
    Crush "SO SHUT UP BLONDY"
    hide CrushTriggered
    show DanielMad
    Daniel "I'M NOT BLOND!"
    Daniel "I JUST DYED MY HAIR YELLOW AND YOU KNOW THAT!"
    NikkiDad "Is everything alright?"
    Crush "Yeah, we're ok."
    hide DanielMad
    show Crush
    Crush "Ok, so this is easy."
    Crush "Just make a text to speech program that mimics the voice of the guy that 'has' 7daystoliveitis."
    Daniel "But why do you need that?"
    Crush "That's not important."
    Daniel "Well ok."
    Daniel "Off to buy a new science textbook for me with my 15$!"
    Crush "Don't forget that program!"
    Daniel "Ok."
    scene black
    jump Act4

label Act4:
    "Day 4: Thursday"
    scene CabinBg
    show mommy
    Mom "It sure is cozy in here!"
    Protag "It sure is."
    Mom "Ooo! This looks like a good movie! A bugs life!"
    Mom "I LOVED this movie when i was your age!"
    Mom "It was about..."
    Mom "Blah blah blah blah blah blah"
    Mom "blah blah blah"
    Mom "blah blah."
    hide mommy
    scene black
    "But in Nikki's house..."
    "Once again."
    scene Nikkibedroom
    show Crush
    Crush "Did you get that program done?"
    Daniel "Yes, because i am a genius!"
    Crush "yeah yeah, let me see it"
    "Nikki puts the hard drive onto her computer."
    FakeProtag "{font=FakeProtag.ttf} HELLO WORLD!{/font}"
    Crush "Perfect!"
    Crush "Thanks!"
    hide Crush
    show DanielNormal
    Daniel "Yeah, ok."
    "Daniel leaves"
    hide DanielNormal
    show Crush
    Crush "Ok so i will make an audio recording of the fake text to speech voice!"
    Crush "and people with belive it!"
    Crush "Everybody is going to hate him!"
    Crush "My plan is going to be perfect!"
    hide Crush
    scene black

label Act5:
    "Act 5: Friday"
    scene Schoolcampus
    show Crush
    Crush "Guys Guys!! Look!"
    Crush "I overheared him saying something 5 days ago!"
    Crush "Let me just get the recording!"
    FakeProtag "{font=FakeProtag.ttf} MY PLAN OF FAKING 7DAYSTOLIVEITIS IS WORKING! {/font}"
    FakeProtag "{font=FakeProtag.ttf} I  AM NOW THE MOST POPULAR KID IN SCHOOL!! {/font}"
    hide Crush
    show bffsad
    BestFriend "I can't belive he did this!"
    hide bffsad
    show bullySad
    bully "That is a very crappy thing to do!"
    hide bullySad
    show CrushTriggered
    Crush "How about we get revenge on him tommorow!"
    Crowd "YEAH!!!"
    

label Act6:

label Act7:
    return


