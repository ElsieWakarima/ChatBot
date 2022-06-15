import random
R_EATING="I don't  eat anything because I am a bot obviously"
R_ADVICE= "I offer the best advise I can"
def unknown():
    response=['Could you re-phrase that?','...','sounds about right','What does that mean?'][random.randrange(4)]
    return response