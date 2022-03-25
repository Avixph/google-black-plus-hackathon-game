import json

def make_guess(request):
    game = request.get_json()

    for turn in game['history']:
        histories = turn['guess']
        if turn['result'] == 'lower':
            if game['maximum'] >= histories:
                game['maximum'] = histories - 1
        if turn['result'] == 'higher':
            if game['minimum'] <= histories:
                game['minimum'] = histories + 1

    guess = (game['minimum'] + game['maximum']) // 2
    return json.dumps(guess)
