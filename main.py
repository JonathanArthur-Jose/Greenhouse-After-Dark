#initialize the user's Garden Points and Noise Marks
garden_points = 50
noise_marks = 0 

#create a function to display the current statistics of the user
player_name = input("Enter your name: ")
print(f"Player: {player_name}")
def display_stats(garden_points, noise_marks):
    print(f"Current Garden Points: {garden_points}")
    #lets evalute the user's score based on garden points
    #if the user has less than 50 garden points, print a message to encourage them to keep going
    if garden_points < 50:
        print("You are not yet ready to win the game. You need at least 50 Garden Points to win. Try Again!")
    print(f"Current Noise Marks: {noise_marks}")
    if noise_marks > 5:
            print("YOU MIGHT WANT TO BE MORE QUIET!")
  
#Create an adventure Sim
# First Let's Display the title of the sim
print("=====================================================")
print("             LET THE ADVENTURE BEGIN                 ")
print("=====================================================")

print("") #THIS PROVIDES A BLANK LINE BETWEEN EACH "PRINT" 
print("INTRODUCTION: Greenhouse After Dark")# LETS PRINT THE OUT THE INTRODUCTION TO THE SIM
print("") 
print("DATE: 11/18/2189")
print("TIME: 2:15 AM")

print("")
print("LOCATION: The Greenhouse")
print("")
input("\nPress Enter to continue...")
#NOW LETS PRINT OUT MANY LINES OF TEXT WITH ONLY ONE PRINT STATEMENT
print("_" * 100)
print("""
You are halfway through your first overnight maintenance shift when your wrist monitor vibrates.
""")# i am making a print statement that will print out the text in the triple quotes.  
input("\nPress Enter to continue...")

print("_" * 100)
print("""
"OXYGEN OUTPUT FALLING. GREENHOUSE SECTOR 7 REQUIRES IMMEDIATE ATTENTION!"
""")

input("\nPress Enter to continue...")
print("_" * 100)
print("""
The crew is asleep. Beneath the station, Vespara turns slowly past the observation windows.
There is nothing breathable down there. 
Until morning, everyone aboard Eden’s Wake depends on what grows behind one greenhouse door.
""")

input("\nPress Enter to continue...")
# NOW LETS PRINT OUT THE REST OF THE TEXT
print("_" * 100)
print("""
Condensation streaks the inside of the glass. Through it, you see overturned pots, wilted flowers, and the corner of a fertilizer bag disappearing beneath a workbench. You wait for whatever took it to come out. It doesn’t.
""")

input("\nPress Enter to continue...")
# NOW LETS PRINT OUT THE REST OF THE TEXT
print("_" * 100)
print("""
The night-shift botanist is missing. Her coat still hangs beside the entrance. On the greenhouse computer, the instruction KEEP ALL GROW LIGHTS ON has been crossed out in grease pencil. Beneath it, in the botanist’s handwriting, are six words.
""")

input("\nPress Enter to continue...")
# NOW LETS PRINT OUT THE REST OF THE TEXT
print("_" * 100)
print("""

THAT IS WHAT STARTED THE WHOLE THING!
""")

input("\nPress Enter to continue...")
# NOW LETS PRINT OUT THE REST OF THE TEXT
print("_" * 100)
print("""
Under the lamps, a black vine has wound itself around an irrigation pipe. Pale flowers lean out of their bed. Broad silver leaves hang across the walkway, their undersides lined with tiny hooked spines. Fresh soil lies in a neat pile beneath a ventilation grate. Someone has left handwritten notes at the workstations. The last one is taped over the intercom.

Keep your footsteps soft. Silence your wrist monitor. If a flower turns toward you, stop moving. Whatever you hear from the ventilation shaft, do not answer.

The door seals behind you. Somewhere among the plants, the fertilizer bag rustles again.

Then your wrist monitor begins to beep.

""")

input("\nPress Enter to continue...")
# NOW LETS PRINT OUT THE REST OF THE TEXT
print("_" * 100)

print("\n\n THIS IS THE END OF THE INTRODUCTION TO THE SIM. MORE CONTENT TO FOLLOW. \n\n")

input("\nPress Enter to END SIMULATION INTRODUCTION...")
print("_" * 100)
#--------------------------------------------------------------------------------------
#NOW PRINT OUT THE GAME DIRECTIONS
print("GAME DIRECTIONS:")
print("""
Start with 100 Garden Points and 0 Noise Marks. Garden Points measure how much of the oxygen garden can still support the crew. Noise Marks count disturbances that reveal your position to the plants.
""")

input("\nPress Enter to continue...")
# NOW LETS PRINT OUT THE REST OF THE TEXT
print("_" * 100)
print("""
Play all 10 scenarios in order. Read the scene and its night-shift note, pick A, B, or C, then read only the outcome for your choice.
A lasting repair earns +5 Garden Points, a partial fix earns +3, and a damaging decision costs −4. Add one Noise Mark only when the outcome says Noise +1. Keep both totals through the final scenario.
At the end, you win with at least 24 Garden Points and no more than 2 Noise Marks. Otherwise, read the losing conclusion. The station’s emergency reserve gives you time to make all ten decisions.
""")

#input("\nPress Enter to continue...")
# NOW LETS PRINT OUT THE REST OF THE TEXT
#print("_" * 100)
#print(f"Garden Points: {garden_points}")
#print(f"Noise Marks: {noise_marks}")

#THIS WILL TAKE THE USER'S CHOICE AND STORE IT AS A VARIABLE CALLED USER_CHOICE
print("Scenario 1 — Something Heard You")
print("""
The pale flower nearest the entrance turns toward your wrist. Its stem lengthens with each beep, slowly lifting itself over the edge of the planter.
A much larger shadow shifts behind it.
Your monitor has a silent-alert setting. Reaching it will take a few seconds.
Night-shift note — “Movement is easiest to hide when nothing can hear where it starts.”
""")
display_stats(garden_points, noise_marks)
user_choice = input("Please enter your choice (A, B, or C): ")
print("A. Hold still and carefully switch the monitor to silent alerts.")
print("B. Press the monitor into your sleeve until the alert finishes.")
print("C. Shout for the botanist and run toward the computer.")
if user_choice.upper() == "A":
    garden_points += 5 
    noise_marks += 0
    print("""
    You chose option A. +5 Garden Points!
    The beeping stops. The flower searches the empty air, then settles. The larger shadow remains behind the planting bed.
    """)
elif user_choice.upper() == "B":
    garden_points += 3
    noise_marks += 1
    print("""
    You chose option B. +3 Garden Points!
    The sound becomes faint enough to slow the flower. You slip past, but its stem has already pulled several seedlings from their tray.
    """)
elif user_choice.upper() == "C":
    garden_points -= 4
    noise_marks += 2
    print("""
    You chose option C. −4 Garden Points!
    Flowers stretch across the aisle toward your voice. Something heavy moves with them, striking a shelf and blocking your easiest route back.
    """)
else:
    print("Invalid choice. Please enter A, B, or C.")



# scenario 2
print("Scenario 2 — The Wrong Instructions")
print("""
The computer recommends increasing the light over the black vine. Beneath the brightest lamp, its coils are crushing a water pipe. In a shadow behind the planter, another section grows loose and healthy.
A small opaque cover sits beside the bed.
Night-shift note — “Blackvine grows in darkness. Light makes it grip whatever supports it. Shade the entire runner before touching the pipe.”
""")
display_stats(garden_points, noise_marks)
user_choice = input("Please enter your choice (A, B, or C): ")
print("A. Increase the lamp brightness, following the computer’s recommendation.")
print("B. Fit the opaque cover over the vine and its exposed runners.")
print("C. Wrap a dark cloth around the most tightly wound section.")
if user_choice.upper() == "A":
    garden_points -= 4
    noise_marks += 2
    print("""
    You chose option A. -4 Garden Points!
    The vine contracts sharply. A pipe connection splits, sending water across the floor and reducing irrigation pressure.
    """)
elif user_choice.upper() == "B":
    garden_points += 5
    noise_marks += 0
    print("""
    You chose option B. +5 Garden Points!
    The coils gradually loosen. Water moves through the pipe again, and the vine begins opening its folded leaves.
    """)
elif user_choice.upper() == "C":
    garden_points += 3
    noise_marks += 1
    print("""
    You chose option C. +3 Garden Points!
    That section releases enough pressure for a trickle of water, but the uncovered runners keep gripping the equipment.
    """)
else:
    print("Invalid choice. Please enter A, B, or C.")



# scenario 3
print("Scenario 3 — The Silver Passage")
print("""
The shortest route to the supply cabinet passes beneath broad silver leaves. Your light catches tiny hooks along their undersides. A scrap of the botanist’s sleeve hangs from one.
You spot a long planting tool beside the walkway.
Night-shift note — “Silverhook catches anything dragged against its spines. Support the stem from above and lift slowly. Never pull caught fabric straight back.”
""")
display_stats(garden_points, noise_marks)
user_choice = input("Please enter your choice (A, B, or C): ")
print("A. Take the narrow maintenance route around the bed.")
print("B. Push through and pull free if anything catches.")
print("C. Use the planting tool to lift the stems into their overhead supports.")
if user_choice.upper() == "A":
    garden_points += 3
    noise_marks += 0
    print("""
    You chose option A. +3 Garden Points!
    You reach the cabinet safely, though the detour delays work on the failing plants. The main walkway remains blocked.
    """)
elif user_choice.upper() == "B":
    garden_points -= 4
    noise_marks += 2
    print("""
    You chose option B. -4 Garden Points!
    A hook catches your sleeve. Your struggle shakes the whole bed, tears several leaves, and draws a pale flower toward your breathing.
    """)
elif user_choice.upper() == "C":
    garden_points += 5
    noise_marks += 0
    print("""
    You chose option C. +5 Garden Points!
    You clear the passage without touching the hooked undersides. The route stays open for the rest of your work.
    """)
else:
    print("Invalid choice. Please enter A, B, or C.")



# scenario 4
print("Scenario 4 — The Fertilizer Thief")
print("""
Behind the supply cabinet, you find the missing fertilizer bag.
A small six-legged creature is chewing a pellet. It deposits fine, dark material beside a root, then reaches for another. Several smaller creatures wait inside a service tunnel.
The creature notices you and freezes.
Night-shift note — “Soil diggers process the fertilizer before the plants can use it safely. Leave measured portions. They will carry away everything you give them.”
""")
display_stats(garden_points, noise_marks)
print("A. Leave one measured portion at the tunnel and secure the remaining bag.")
print("B. Chase the creatures away and pour raw fertilizer into the beds.")
print("C. Collect some processed soil and place it around the weakest plant.")
user_choice = input("Please enter your choice (A, B, or C): ")

if user_choice.upper() == "A":
    garden_points += 5
    noise_marks += 0
    print("""
    You chose option A. +5 Garden Points!
    The diggers resume their work, spreading processed nutrients around the roots while the main supply stays protected.
    """)
elif user_choice.upper() == "B":
    garden_points -= 4
    noise_marks += 2
    print("""
    You chose option B. -4 Garden Points!
    Concentrated pellets damage the delicate roots. The diggers retreat, leaving the remaining fertilizer unprocessed.
    """)
elif user_choice.upper() == "C":
    garden_points += 3
    noise_marks += 0
    print("""
    You chose option C. +3 Garden Points!
    That plant improves, but the other beds still need a reliable supply of nutrients.
    """)
else:
    print("Invalid choice. Please enter A, B, or C.")


# scenario 5
print("Scenario 5 — The Voice in the Shaft")
print("""
“Please. I’m hurt.”
The voice comes through the ventilation grille beside your head.
“Come closer.”
It sounds like the botanist, but the words repeat with exactly the same pauses. Beneath the grille, you find a second note pressed into damp soil.
Night-shift note — “The hollowstalk copies voices. Its hunting tendril follows a reply through the duct. It carries the same sweet smell as the unopened flowers. Stay away from the opening.”
""")
display_stats(garden_points, noise_marks)
print("A. Whisper that you are coming and look inside.")
print("B. Remain silent and close the local duct shutter using the lever beside the wall.")
print("C. Keep silent and retreat around the far side of the planting beds.")
user_choice = input("Please enter your choice (A, B, or C): ")

if user_choice.upper() == "A":
    garden_points -= 4
    noise_marks += 2
    print("""
    You chose option A. -4 Garden Points!
    A dark tendril snaps through the grille toward your voice. You stumble back, knocking over a nutrient container as it sweeps the floor.
    """)
elif user_choice.upper() == "B":
    garden_points += 5
    noise_marks += 0
    print("""
    You chose option B. +5 Garden Points!
    The shutter isolates the side duct while leaving the main ventilation route open. Something presses against the metal, then withdraws.
    """)
elif user_choice.upper() == "C":
    garden_points += 3
    noise_marks += 0
    print("""
    You chose option C. +3 Garden Points!
    You avoid the tendril, but the open duct remains a hazard near the control station.
    """)
else:
    print("Invalid choice. Please enter A, B, or C.")


# scenario 6
print("Scenario 6 — A Hand Behind the Glass")
print("""
A hand moves behind the irrigation-room window.
The botanist is inside, wearing an emergency breathing mask. A blackvine runner has grown around the sliding door mechanism. She points toward a blackout curtain hanging beside the frame.
You draw a circle on the fogged glass. She draws a square beside it and points at the curtain again.
Night-shift note — “The irrigation door has a manual release. Shade the runner first. The motor will damage the pipe if it pulls against a tightened vine.”
""")
display_stats(garden_points, noise_marks)
print("A. Cover the whole runner, wait for it to loosen, and use the manual release.")
print("B. Activate the powered emergency opening.")
print("C. Shade one section and ease the door open just far enough for her to pass.")
user_choice = input("Please enter your choice (A, B, or C): ")

if user_choice.upper() == "A":
    garden_points += 5
    noise_marks += 0
    print("""
    You chose option A. +5 Garden Points!
    The door opens. The botanist steps out and shows you which pipe supplies the shared root beds before retreating to the protected service alcove.
    """)
elif user_choice.upper() == "B":
    garden_points -= 4
    noise_marks += 2
    print("""
    You chose option B. -4 Garden Points!
    The motor tears the runner from its support, damaging a nearby water connection. The botanist squeezes through the gap, but irrigation pressure drops further.
    """)
elif user_choice.upper() == "C":
    garden_points += 3
    noise_marks += 0
    print("""
    You chose option C. +3 Garden Points!
    You free the botanist, though the remaining runner keeps the door mechanism partly trapped. She moves to the service alcove to recover.
    """)
else:
    print("Invalid choice. Please enter A, B, or C.")


# scenario 7
print("Scenario 7 — Choosing the Right Neighbors")
print("""
At the central planting bench, you find a field sketch and a failed experiment.
In the failed bed, silverhook leaves have caught the pale flowers’ stems. Beside it, a healthy sample has pale flowers above an enclosed blackvine root chamber.
Night-shift note — “Pale flowers need upper light and shed nutrient-rich husks. Blackvine uses those husks in a dark lower bed. Keep silverhook separate. Leave a passage for the soil diggers.”
""")
display_stats(garden_points, noise_marks)
print("A. Keep the flowers and vine in separate beds and transfer a handful of husks.")
print("B. Put silverhook between the flowers and vine to provide shade.")
print("C. Place the flowers above a fully shaded vine chamber, with a husk channel and access for the diggers.")
user_choice = input("Please enter your choice (A, B, or C): ")

if user_choice.upper() == "A":
    garden_points += 3
    noise_marks += 0
    print("""
    You chose option A. +3 Garden Points!
    The vine receives a small feeding, but continued care will require someone to transfer the nutrients manually.
    """)
elif user_choice.upper() == "B":
    garden_points -= 4
    noise_marks += 2
    print("""
    You chose option B. -4 Garden Points!
    The flowers turn toward a distant pump, dragging their stems across the hooks. Several blossoms tear away.
    """)
elif user_choice.upper() == "C":
    garden_points += 5
    noise_marks += 0
    print("""
    You chose option C. +5 Garden Points!
    Light reaches the flowers, nutrients reach the vine, and the diggers maintain the shared soil. Oxygen output begins recovering.
    """)
else:
    print("Invalid choice. Please enter A, B, or C.")


# scenario 8
print("Scenario 8 — The Sweet Smell")
print("""
The air beside the central bed smells increasingly sweet.
Behind a hanging screen, a tall hollowstalk has wrapped itself around a nutrient return line. Its open mouth resembles a flower until the inside contracts.
In the planter below it, the soil is almost dry. A disconnected drip hose lies just out of reach.
Night-shift note — “A dry hollowstalk searches beyond its enclosure. Restore the marked drip line from behind the barrier. When the scent fades and the mouth closes, lower the containment screen.”
""")
display_stats(garden_points, noise_marks)
print("A. Strike the stalk with a tool until it releases the pipe.")
print("B. Reconnect the marked hose with the long tool, wait behind the barrier, and lower the screen when the mouth closes.")
print("C. Lower the screen immediately and keep your distance.")
user_choice = input("Please enter your choice (A, B, or C): ")

if user_choice.upper() == "A":
    garden_points -= 4
    noise_marks += 2
    print("""
    You chose option A. -4 Garden Points!
    The impact brings its tendril around toward you. You escape behind the screen, but it tears the return line loose as it follows.
    """)
elif user_choice.upper() == "B":
    garden_points += 5
    noise_marks += 0
    print("""
    You chose option B. +5 Garden Points!
    Water reaches the dry roots. The tendril withdraws, the smell fades, and the screen keeps the plant inside its enclosure.
    """)
elif user_choice.upper() == "C":
    garden_points += 3
    noise_marks += 0
    print("""
    You chose option C. +3 Garden Points!
    The barrier limits the plant’s reach, but the thirsty stalk continues pulling against the nutrient line.
    """)
else:
    print("Invalid choice. Please enter A, B, or C.")


# scenario 9
print("Scenario 9 — Air for the Crew")
print("""
The greenhouse oxygen gauge climbs, but your wrist monitor still reports a shortage in the sleeping quarters.
The delivery damper is nearly closed.
Its powered test lever would open it instantly. Beside it is a manual wheel with a padded grip.
Night-shift note — “Open gradually. A sudden draft bends the pale flowers into the grille. Watch the greenhouse and crew-side gauges together.”
""")
display_stats(garden_points, noise_marks)
print("A. Slowly turn the manual wheel until both gauges begin rising.")
print("B. Open the damper a little and leave it there.")
print("C. Pull the powered test lever.")
user_choice = input("Please enter your choice (A, B, or C): ")

if user_choice.upper() == "A":
    garden_points += 5
    noise_marks += 0
    print("""
    You chose option A. +5 Garden Points!
    Fresh air moves into the station without disturbing the plants. The crew-side warning changes from critical to recovering.
    """)
elif user_choice.upper() == "B":
    garden_points += 3
    noise_marks += 0
    print("""
    You chose option B. +3 Garden Points!
    Some oxygen reaches the crew, but the restricted opening prevents full delivery.
    """)
elif user_choice.upper() == "C":
    garden_points -= 4
    noise_marks += 2
    print("""
    You chose option C. -4 Garden Points!
    The damper slams open. A sudden draft bends flowers against the grille, obstructing the airflow you were trying to restore.
    """)
else:
    print("Invalid choice. Please enter A, B, or C.")


# scenario 10
print("Scenario 10 — The Morning Cycle")
print("""
At 5:59 a.m., the computer prepares to restore its original daytime program.
Every grow lamp will switch on. The fertilizer dispenser will empty a full tray. The greenhouse speakers will play the morning announcement.
You have one final decision.
Night-shift note — “Check what the system will do after you leave. Save the settings before the countdown ends.”
""")
display_stats(garden_points, noise_marks)
print("A. Delay the morning cycle for one hour and leave instructions for the day crew.")
print("B. Accept the original program because it is labeled ‘recommended.’")
print("C. Save separate lighting zones, measured fertilizer portions, the hollowstalk drip schedule, and silent alerts.")
user_choice = input("Please enter your choice (A, B, or C): ")

if user_choice.upper() == "A":
    garden_points += 3
    noise_marks += 0
    print("""
    You chose option A. +3 Garden Points!
    You gain time, but the harmful settings remain stored and still need to be replaced.
    """)
elif user_choice.upper() == "B":
    garden_points -= 4
    noise_marks += 2
    print("""
    You chose option B. -4 Garden Points!
    Lights flood the vine beds, the dispenser rattles, and the flowers turn toward the announcement speakers. The repaired garden begins to struggle again.
    """)
elif user_choice.upper() == "C":
    garden_points += 5
    noise_marks += 0
    print("""
    You chose option C. +5 Garden Points!
    The flowers receive light while the vines remain shaded. Water and nutrients reach the correct beds. The morning cycle begins quietly.
    """)
else:
    print("Invalid choice. Please enter A, B, or C.")

    # Final results
display_stats(garden_points, noise_marks)

if garden_points >= 50 and noise_marks <= 5:
    print("\nYOU WIN!")
    print("The Morning Handoff")
    print("""
At 6:04 a.m., the needle on the crew-side oxygen gauge climbs above
the grease-pencil mark. For the first time tonight, you see clear
glass where someone wiped away the condensation hours ago. Beyond
it, a crew member walks past carrying coffee, unaware that the air
reaching her bunk nearly stopped.

The botanist joins you at the observation window. She has a strip
of black vine caught in her bootlace and a maintenance report to
fill out. She writes "oxygen delivery restored," then pauses at
the line for missing supplies.

At your feet, the smallest digger backs out of the tunnel, tugging
the empty scoop behind it. The scoop is too wide for the grate.
It turns the scoop sideways, pulls it through, and heads back
underground.

You take the pencil and write, "One scoop returned. Leave it by
the grate."
""")

else:
    print("\nGAME OVER")
    print("One Bed Left")
    print("""
At 6:04 a.m., your wrist monitor vibrates with the evacuation order.
""")

    # Explain each reason the player lost.
    if garden_points < 50:
        print("""
The surviving beds can't produce enough oxygen for the crew.
""")

    if noise_marks >= 5:
        print("""
The sound-seeking flowers have stretched across the delivery grille,
dragging hooked silver leaves with them. Clearing those hooks will
take longer than the reserve allows.
""")

print("""
Emergency lights guide everyone to the shuttle. Its cabin has
enough oxygen to hold the crew while Eden's Wake shuts down the
failing sector. From the shuttle window, you watch the greenhouse
lamps go out one row at a time.

The botanist straps a small planter into the seat beside yours.
A single pale flower grows on top. Below it, inside an opaque
sample box, a black vine has already put down one white root.

Something under the seat scratches twice. A chewed fertilizer
pellet rolls against your boot.

You pick it up, find the little hole beside the root, and quietly
put it where it belongs.
""")