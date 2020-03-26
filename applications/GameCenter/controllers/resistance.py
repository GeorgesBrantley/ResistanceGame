# -*- coding: utf-8 -*-
import time
import json



# Resistance Home
def ResistanceHome():
    gameID=request.vars.gameID
    return dict(test="Create/Join Game Buttons",gameID=gameID)

# Create Game
def ResistanceCreate():
    
    return dict(test="Creating Game")

# Join Game
def ResistanceJoin():
    
    return dict(test="Join Game")


# Game Page
def ResistancePlay():
    # Artifacts:
    # Leader Turn Order
    # Leader Selection
    # Team (Hover)
    # Select Team Members if Leader
    # Voting on Team (Trigger?)
    return dict(test="Game")


# Results
def ResistanceResults():
    # Who Won
    # Who Lost
    # Teams
    return dict(test="Finished Game")
