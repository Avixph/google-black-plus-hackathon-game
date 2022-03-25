import json
from google.cloud import firestore


def save_result(request):
    # All result reports should be in JSON form
    result = request.get_json()

    # Reported result data is the request payload
    contest_round = result['contest_round']
    outcome = result['outcome']
    moves = result['moves']
    questioner = result['questioner']
    secret = result['secret']

    # Look up contest_round random ID to be sure this is a genuine report
    rounds = firestore.Client().collection('rounds')
    this_round = rounds.document(contest_round).get()

    if not this_round.exists:
        return '404'  # Not found - no such contest_round was ever asked for
    if secret != this_round.to_dict().get('secret'):
        return '403'  # Forbidden - they don't know the shared secret

    # Update results with data from this new run
    rounds.document(contest_round).collection('runs').add({
        'outcome': outcome,
        'moves': moves,
        'questioner': questioner,
    })

    # Acknowledge a successful report
    return '201'  # Created (a new contest run entry)
