from django.apps import AppConfig


class FormsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'form'
#
# from random import shuffle
#
# players = ['altai', 'bolot', 'abdulla', 'diana', 'jony', 'anvar', 'erlan', 'adilet']
#
#
#
# def play(players):
#     shuffle(players)
#     result = []
#     while True:
#         if players:
#             player1 = players.pop()
#             player2 = players.pop()
#             result.append({player1: player2})
#         else:
#             break
#
#     return result
#
# print(play(players))

