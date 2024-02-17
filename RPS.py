# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
def player(prev_play, opponent_history=[], play_history={}):
    hist= 5
    if not prev_play:
        prev_play= 'R'
    opponent_history.append(prev_play)
    opponent_response= random.choice(['R', 'P', 'S'])

    last_few = "".join(opponent_history[-hist:])

    if len(opponent_history)> hist+1:
        past_play= "".join(opponent_history[-hist-1:])
        play_history[past_play]=play_history.get(past_play, 0) + 1
        # print(play_history)
        # print(opponent_history)

    if len(last_few)==hist:
        possible_outcome={}
        combinations= [last_few+k for k in ['R', 'P', 'S']]
        for c in combinations:
            possible_outcome[c]= play_history.get(c, 0)
        opponent_response= max(possible_outcome, key= possible_outcome.get)[-1]
        # print(possible_outcome)
        # print(possible_outcome)
    
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[opponent_response] 
