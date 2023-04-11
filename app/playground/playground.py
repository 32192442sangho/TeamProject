import csv
import os

ansforposition = ['ad carry', 'support', 'ad carry', 'jungle', 'top', 'jungle', 'mid', 'mid', 'support', 'mid', 'mid',
                  'ad carry', 'jungle', 'top', 'mid', 'ad carry', 'top', 'mid', 'ad carry', 'support', 'ad carry',
                  'jungle', 'ad carry', 'mid', 'top', 'mid', 'support', 'jungle', 'ad carry', 'jungle', 'jungle',
                  'support', 'ad carry', 'jungle', 'mid', 'top', 'support', 'mid', 'top', 'ad carry', 'jungle', 'mid',
                  'ad carry', 'mid', 'top', 'jungle', 'top', 'jungle', 'top', 'mid', 'support', 'jungle', 'top',
                  'support', 'ad carry', 'ad carry', 'ad carry', 'support', 'support', 'top', 'support', 'support',
                  'mid', 'top', 'ad carry', 'jungle', 'mid', 'support', 'mid', 'mid', 'top', 'top', 'support',
                  'support', 'ad carry', 'top', 'mid', 'top', 'ad carry', 'top', 'mid', 'ad carry', 'jungle', 'mid',
                  'jungle', 'ad carry', 'support', 'ad carry', 'support', 'jungle', 'mid', 'top', 'ad carry', 'mid',
                  'support', 'top', 'top', 'support', 'top', 'top', 'ad carry', 'mid', 'support', 'jungle', 'mid',
                  'mid', 'support', 'jungle', 'ad carry', 'top', 'ad carry', 'support', 'jungle', 'mid', 'ad carry',
                  'ad carry', 'top', 'jungle', 'support', 'ad carry', 'ad carry', 'ad carry', 'ad carry', 'mid', 'top',
                  'ad carry', 'jungle', 'ad carry', 'support', 'ad carry', 'mid', 'support', 'ad carry', 'top', 'mid',
                  'ad carry', 'jungle', 'top', 'ad carry', 'mid', 'ad carry', 'top', 'jungle', 'jungle', 'ad carry',
                  'support', 'top', 'ad carry', 'top', 'support', 'support', 'top', 'support', 'ad carry', 'ad carry',
                  'mid', 'support', 'mid', 'ad carry', 'top', 'support', 'mid', 'jungle', 'support', 'ad carry', 'top',
                  'top', 'support', 'support', 'mid', 'support', 'support', 'ad carry', 'ad carry', 'mid', 'support',
                  'support', 'ad carry', 'support', 'mid', 'support', 'mid', 'jungle', 'ad carry', 'top', 'mid',
                  'ad carry', 'support', 'mid', 'ad carry', 'support', 'ad carry', 'ad carry', 'support', 'ad carry',
                  'top', 'jungle', 'mid', 'support', 'top', 'mid', 'mid', 'ad carry', 'support', 'support', 'ad carry',
                  'mid', 'support', 'top', 'mid', 'ad carry', 'support', 'top', 'mid', 'top', 'ad carry', 'jungle',
                  'support', 'support', 'ad carry', 'top', 'top', 'jungle', 'support', 'ad carry', 'support', 'mid',
                  'top', 'support', 'jungle', 'top', 'top', 'support', 'jungle', 'mid', 'jungle', 'ad carry', 'top',
                  'mid', 'support', 'jungle', 'ad carry', 'support', 'top', 'mid', 'mid', 'jungle', 'support', 'jungle',
                  'support', 'ad carry', 'top', 'top', 'mid', 'support', 'top', 'support', 'top', 'jungle', 'support',
                  'top', 'jungle', 'jungle', 'jungle', 'ad carry', 'mid', 'support', 'ad carry', 'top', 'jungle',
                  'support', 'ad carry', 'mid', 'mid', 'jungle', 'support', 'top', 'mid', 'top', 'mid', 'jungle', 'mid',
                  'jungle', 'mid', 'top', 'top', 'ad carry', 'mid', 'jungle', 'support', 'mid', 'ad carry', 'ad carry',
                  'support', 'jungle', 'mid', 'jungle', 'mid', 'top', 'mid', 'top', 'support', 'ad carry', 'top',
                  'jungle', 'support', 'jungle', 'mid', 'jungle', 'top', 'jungle', 'ad carry', 'jungle', 'jungle',
                  'ad carry', 'support', 'ad carry', 'top', 'support', 'support', 'support', 'top', 'jungle', 'mid',
                  'ad carry', 'support', 'mid', 'top', 'ad carry', 'mid', 'ad carry', 'jungle', 'support', 'mid',
                  'support', 'ad carry', 'support', 'support', 'support', 'jungle', 'top', 'ad carry', 'top', 'support',
                  'jungle', 'mid', 'top', 'ad carry', 'support', 'jungle', 'ad carry', 'support', 'support', 'ad carry',
                  'jungle', 'support', 'mid', 'ad carry', 'mid', 'ad carry', 'support', 'jungle', 'support', 'top',
                  'jungle', 'top', 'jungle', 'ad carry', 'support', 'ad carry', 'support', 'support', 'jungle', 'top',
                  'ad carry', 'mid', 'mid', 'top', 'jungle', 'mid', 'top', 'top', 'mid', 'ad carry', 'support', 'mid',
                  'support', 'mid', 'ad carry', 'support', 'top', 'top', 'mid', 'top', 'mid', 'jungle', 'mid',
                  'support', 'top', 'top', 'jungle', 'ad carry', 'support', 'mid', 'support', 'top', 'ad carry', 'top',
                  'mid', 'ad carry', 'jungle', 'support', 'support', 'mid', 'top', 'mid', 'ad carry', 'support',
                  'jungle', 'support', 'ad carry', 'support', 'support', 'mid', 'top', 'jungle', 'mid', 'top',
                  'ad carry', 'top', 'support', 'ad carry', 'jungle', 'support', 'top', 'mid', 'ad carry', 'support',
                  'jungle', 'support', 'top', 'ad carry', 'top', 'ad carry', 'jungle', 'support', 'ad carry', 'mid',
                  'jungle', 'top', 'top', 'jungle', 'mid', 'support', 'mid', 'ad carry', 'jungle', 'top', 'ad carry',
                  'ad carry', 'top', 'ad carry', 'top', 'top', 'support', 'top', 'ad carry', 'jungle', 'jungle', 'mid',
                  'top', 'jungle', 'mid', 'support', 'ad carry', 'jungle', 'jungle', 'ad carry', 'ad carry', 'mid',
                  'top', 'ad carry', 'mid', 'ad carry', 'support', 'ad carry', 'ad carry', 'top', 'support', 'jungle',
                  'mid', 'mid', 'ad carry', 'support', 'ad carry', 'support', 'jungle', 'jungle', 'top', 'jungle',
                  'ad carry', 'support', 'ad carry', 'top', 'jungle', 'support', 'jungle', 'top', 'mid', 'support',
                  'mid', 'top', 'support', 'top', 'support', 'top', 'mid', 'top', 'support', 'mid', 'support', 'top',
                  'jungle', 'support', 'ad carry', 'ad carry', 'jungle', 'support', 'mid', 'top', 'support', 'mid',
                  'mid', 'top', 'support', 'top', 'mid', 'mid', 'top', 'ad carry', 'top', 'support', 'ad carry',
                  'jungle', 'top', 'mid', 'top', 'top', 'jungle', 'mid', 'mid', 'ad carry', 'support', 'top', 'mid',
                  'support', 'jungle', 'support', 'ad carry', 'jungle', 'jungle', 'top', 'ad carry', 'support',
                  'support', 'mid', 'support', 'jungle', 'ad carry', 'jungle', 'ad carry', 'jungle', 'support', 'mid',
                  'jungle', 'jungle', 'mid', 'top', 'ad carry', 'support', 'top', 'ad carry', 'jungle', 'mid',
                  'support', 'mid', 'jungle', 'support', 'ad carry', 'support', 'support', 'ad carry', 'ad carry',
                  'top', 'support', 'jungle', 'support', 'mid', 'support', 'jungle', 'jungle', 'ad carry', 'top',
                  'support']
print(ansforposition)
print(len(ansforposition))

which_team = ['p', 'p', 'b', 'p', 'b', 'p', 'p', 'b', 'p', 'p', 'b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b', 'p', 'p',
              # 21
              'p', 'b', 'b', 'p', 'p', 'p', 'p', 'p', 'b', 'p', 'p', 'b', 'p', 'p', 'b', 'p', 'b', 'p', 'p', 'p', 'p',
              # 42
              'p', 'b', 'p', 'p', 'b', 'b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b', 'p', 'p', 'p', 'p', 'b', 'p',
              # 63
              'p', 'b', 'b', 'b', 'b', 'p', 'b', 'b', 'p', 'b', 'p', 'p', 'b', 'p', 'p', 'b', 'p', 'b', 'b', 'b', 'b',
              # 84
              'b', 'p', 'b', 'b', 'p', 'p', 'p', 'p', 'b', 'p', 'b', 'b', 'p', 'b', 'b', 'p', 'b', 'p', 'p', 'b', 'b',
              # 105
              'b', 'b', 'b', 'b', 'b', 'p', 'p', 'p', 'p', 'b', 'p', 'p', 'b', 'p', 'b', 'p', 'p', 'b', 'p', 'p',
              'b',
              # 126
              'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b', 'b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p',
              # 147
              'p', 'b', 'b', 'b', 'b', 'p', 'b', 'b', 'b', 'b', 'p', 'p', 'b', 'p', 'b', 'p', 'b', 'b', 'b', 'b',
              'b',
              # 168
              'p', 'p', 'p', 'b', 'p', 'b', 'b', 'p', 'p', 'b', 'p', 'b', 'b', 'p', 'b', 'p', 'b', 'p', 'b', 'b', 'b',
              # 189
              'p', 'p', 'b', 'p', 'p', 'b', 'p', 'b', 'b', 'p', 'b', 'p', 'b', 'b', 'b', 'p', 'p', 'b', 'p', 'b',
              'b',
              # 210
              'b', 'b', 'b', 'b', 'p', 'b', 'b', 'b', 'p', 'p', 'b', 'p', 'p', 'p', 'b', 'b', 'b', 'b', 'b', 'b', 'p',
              # 231
              'b', 'b', 'p', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'p', 'b', 'b', 'p', 'b', 'p', 'p', 'b', 'p', 'p',
              # 252
              'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'p', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'p',
              # 273
              'b', 'b', 'b', 'b', 'b', 'b', 'b', 'p', 'p', 'b', 'b', 'b', 'b', 'p', 'p', 'b', 'p', 'b', 'p', 'b', 'b',
              # 294
              'p', 'p', 'b', 'b', 'b', 'b', 'p', 'b', 'b', 'b', 'p', 'b', 'b', 'p', 'p', 'b', 'p', 'b', 'p', 'b', 'p',
              # 315
              'b', 'b', 'p', 'b', 'b', 'p', 'p', 'b', 'b', 'b', 'b', 'p', 'p', 'b', 'b', 'p', 'b', 'b', 'p', 'p', 'b',
              # 336
              'p', 'b', 'p', 'p', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'p', 'p', 'p', 'p', 'p', 'p', 'b', 'p',
              # 357
              'b', 'b', 'p', 'b', 'p', 'p', 'p', 'p', 'p', 'b', 'p', 'p', 'p', 'b', 'p', 'p', 'p', 'p', 'b', 'p', 'b',
              # 378
              'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b', 'p', 'b', 'p', 'b', 'p', 'b', 'b', 'p', 'p', 'b', 'b', 'p', 'b',
              # 399
              'p', 'p', 'p', 'p', 'b', 'b', 'p', 'p', 'b', 'p', 'p', 'p', 'b', 'p', 'b', 'p', 'p', 'p', 'p', 'p', 'b',
              # 420
              'b', 'b', 'p', 'b', 'p', 'b', 'p', 'b', 'b', 'p', 'b', 'p', 'p', 'b', 'p', 'p', 'p', 'p', 'p', 'p', 'p',
              # 441
              'b', 'p', 'b', 'p', 'p', 'p', 'p', 'p', 'b', 'p', 'p', 'p', 'p', 'b', 'b', 'b', 'b', 'b', 'p', 'p', 'b',
              # 462
              'p', 'p', 'p', 'b', 'p', 'b', 'p', 'p', 'p', 'p', 'p', 'p', 'b', 'b', 'b', 'p', 'b', 'p', 'p', 'b', 'p',
              # 483
              'p', 'p', 'p', 'b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b', 'p', 'p', 'p', 'p', 'p', 'p', 'b',
              # 504
              'p', 'b', 'b', 'p', 'b', 'p', 'p', 'p', 'p', 'b', 'p', 'p', 'b', 'p', 'b', 'p', 'p', 'p', 'b', 'p', 'p',
              # 525
              'b', 'p', 'b', 'p', 'p', 'p', 'p', 'b', 'b', 'p', 'p', 'p', 'p', 'b', 'p', 'p', 'p', 'p', 'b', 'p', 'p',
              # 546
              'b', 'p', 'p', 'p', 'b', 'p', 'p', 'p', 'p', 'p', 'b', 'b', 'b', 'p', 'b', 'b', 'p', 'b', 'p', 'b', 'b',
              # 567
              'b', 'b', 'p', 'b', 'p', 'b', 'p', 'b', 'p', 'b', 'p', 'b', 'b', 'p', 'b', 'b', 'b', 'b', 'b', 'b', 'p',
              # 588
              'b', 'b', 'p', 'p', 'b', 'b', 'b', 'b', 'p', 'b', 'b', 'b', 'b', 'b', 'b', 'b']  # 604
# 56, 110, 150, 200, 242, 276, 310, 370, 439, 484, 520, 555, 604
print(which_team)
print(len(which_team))

ansforwhatspell = [['heal', 'flash'], ['barrier', 'flash'], ['cleanse', 'flash'], ['smite', 'flash'],
                   ['flash', 'teleport'], ['smite', 'flash'], ['teleport', 'flash'], ['ghost', 'ignite'],
                   ['barrier', 'flash'], ['teleport', 'flash'], ['ghost', 'ignite'], ['heal', 'flash'],
                   ['smite', 'flash'], ['teleport', 'ignite'], ['teleport', 'flash'], ['heal', 'flash'],
                   ['teleport', 'ignite'], ['teleport', 'flash'], ['cleanse', 'flash'], ['barrier', 'flash'],
                   ['heal', 'flash'], ['smite', 'flash'], ['cleanse', 'flash'], ['ghost', 'ignite'],
                   ['teleport', 'ignite'], ['teleport', 'flash'], ['barrier', 'flash'], ['smite', 'flash'],
                   ['heal', 'flash'], ['smite', 'flash'], ['smite', 'flash'], ['barrier', 'flash'],
                   ['cleanse', 'flash'], ['smite', 'flash'], ['teleport', 'flash'], ['flash', 'teleport'],
                   ['barrier', 'flash'], ['ghost', 'ignite'], ['teleport', 'ignite'], ['heal', 'flash'],
                   ['smite', 'flash'], ['teleport', 'flash'], ['heal', 'flash'], ['ghost', 'ignite'],
                   ['teleport', 'ignite'], ['smite', 'flash'], ['flash', 'teleport'], ['smite', 'flash'],
                   ['teleport', 'ignite'], ['teleport', 'flash'], ['barrier', 'flash'], ['smite', 'flash'],
                   ['teleport', 'ignite'], ['barrier', 'flash'], ['heal', 'flash'], ['heal', 'flash'],
                   ['exhaust', 'flash'], ['heal', 'flash'], ['heal', 'flash'], ['ignite', 'flash'], ['heal', 'flash'],
                   ['ignite', 'flash'], ['flash', 'teleport'], ['ignite', 'flash'], ['exhaust', 'flash'],
                   ['smite', 'flash'], ['teleport', 'flash'], ['ignite', 'flash'], ['flash', 'teleport'],
                   ['teleport', 'flash'], ['teleport', 'flash'], ['ignite', 'flash'], ['ignite', 'flash'],
                   ['heal', 'flash'], ['flash', 'cleanse'], ['teleport', 'flash'], ['flash', 'teleport'],
                   ['ignite', 'flash'], ['exhaust', 'flash'], ['ignite', 'flash'], ['teleport', 'flash'],
                   ['exhaust', 'flash'], ['smite', 'flash'], ['teleport', 'flash'], ['smite', 'flash'],
                   ['flash', 'cleanse'], ['ignite', 'flash'], ['exhaust', 'flash'], ['heal', 'flash'],
                   ['smite', 'flash'], ['flash', 'teleport'], ['ignite', 'flash'], ['exhaust', 'flash'],
                   ['flash', 'teleport'], ['ignite', 'flash'], ['teleport', 'flash'], ['ignite', 'flash'],
                   ['ignite', 'flash'], ['teleport', 'flash'], ['ignite', 'flash'], ['exhaust', 'flash'],
                   ['flash', 'teleport'], ['heal', 'flash'], ['smite', 'flash'], ['teleport', 'flash'],
                   ['teleport', 'flash'], ['ignite', 'flash'], ['smite', 'flash'], ['exhaust', 'flash'],
                   ['teleport', 'flash'], ['cleanse', 'flash'], ['ignite', 'flash'], ['smite', 'flash'],
                   ['teleport', 'flash'], ['heal', 'flash'], ['cleanse', 'flash'], ['ghost', 'teleport'],
                   ['smite', 'flash'], ['ignite', 'flash'], ['heal', 'flash'], ['cleanse', 'flash'],
                   ['cleanse', 'flash'], ['heal', 'flash'], ['teleport', 'flash'], ['ghost', 'teleport'],
                   ['heal', 'flash'], ['smite', 'flash'], ['cleanse', 'flash'], ['ignite', 'flash'],
                   ['cleanse', 'flash'], ['teleport', 'flash'], ['ignite', 'flash'], ['cleanse', 'flash'],
                   ['ghost', 'teleport'], ['ignite', 'flash'], ['heal', 'flash'], ['smite', 'flash'],
                   ['ghost', 'teleport'], ['cleanse', 'flash'], ['teleport', 'flash'], ['cleanse', 'flash'],
                   ['ghost', 'teleport'], ['smite', 'flash'], ['smite', 'flash'], ['cleanse', 'flash'],
                   ['ignite', 'flash'], ['ghost', 'teleport'], ['cleanse', 'flash'], ['teleport', 'flash'],
                   ['ignite', 'flash'], ['ignite', 'flash'], ['ignite', 'flash'], ['flash', 'ignite'],
                   ['ghost', 'flash'], ['ghost', 'flash'], ['ignite', 'flash'], ['ignite', 'flash'],
                   ['teleport', 'flash'], ['flash', 'heal'], ['ignite', 'flash'], ['flash', 'ignite'],
                   ['ignite', 'flash'], ['flash', 'smite'], ['ignite', 'flash'], ['ghost', 'flash'],
                   ['ignite', 'flash'], ['ignite', 'flash'], ['ignite', 'flash'], ['flash', 'ignite'],
                   ['teleport', 'flash'], ['flash', 'ignite'], ['ignite', 'flash'], ['flash', 'heal'],
                   ['ghost', 'flash'], ['ignite', 'flash'], ['flash', 'ignite'], ['flash', 'ignite'],
                   ['ghost', 'flash'], ['flash', 'ignite'], ['ignite', 'flash'], ['ignite', 'flash'],
                   ['teleport', 'flash'], ['smite', 'flash'], ['flash', 'heal'], ['ignite', 'flash'],
                   ['teleport', 'flash'], ['ghost', 'flash'], ['ignite', 'flash'], ['ignite', 'flash'],
                   ['flash', 'heal'], ['flash', 'ignite'], ['ghost', 'flash'], ['flash', 'heal'], ['flash', 'ignite'],
                   ['ghost', 'flash'], ['ignite', 'teleport'], ['smite', 'flash'], ['ignite', 'flash'],
                   ['flash', 'ignite'], ['ignite', 'flash'], ['ignite', 'flash'], ['ignite', 'flash'],
                   ['cleanse', 'flash'], ['heal', 'flash'], ['flash', 'ghost'], ['flash', 'heal'], ['ignite', 'flash'],
                   ['flash', 'ghost'], ['teleport', 'flash'], ['ignite', 'flash'], ['cleanse', 'flash'],
                   ['heal', 'flash'], ['teleport', 'flash'], ['ignite', 'flash'], ['ghost', 'teleport'],
                   ['cleanse', 'flash'], ['smite', 'flash'], ['heal', 'flash'], ['flash', 'ghost'], ['flash', 'heal'],
                   ['teleport', 'flash'], ['ghost', 'teleport'], ['flash', 'smite'], ['flash', 'ghost'],
                   ['cleanse', 'flash'], ['heal', 'flash'], ['ignite', 'flash'], ['teleport', 'flash'],
                   ['heal', 'flash'], ['smite', 'flash'], ['ghost', 'teleport'], ['teleport', 'flash'],
                   ['heal', 'flash'], ['flash', 'smite'], ['ignite', 'flash'], ['smite', 'flash'], ['cleanse', 'flash'],
                   ['teleport', 'flash'], ['ignite', 'flash'], ['heal', 'flash'], ['smite', 'flash'],
                   ['cleanse', 'flash'], ['ignite', 'flash'], ['barrier ', 'flash'], ['flash', 'ghost'],
                   ['exhaust', 'flash'], ['smite', 'flash'], ['ignite', 'flash'], ['smite', 'flash'],
                   ['ignite', 'flash'], ['heal', 'flash'], ['flash', 'teleport'], ['barrier ', 'flash'],
                   ['flash', 'ghost'], ['ignite', 'flash'], ['barrier ', 'flash'], ['ignite', 'flash'],
                   ['barrier ', 'flash'], ['smite', 'flash'], ['ignite', 'flash'], ['barrier ', 'flash'],
                   ['smite', 'flash'], ['smite', 'flash'], ['smite', 'flash'], ['heal', 'flash'], ['flash', 'ghost'],
                   ['ignite', 'flash'], ['heal', 'flash'], ['barrier ', 'flash'], ['smite', 'flash'],
                   ['ignite', 'flash'], ['heal', 'flash'], ['exhaust', 'flash'], ['flash', 'ghost'], ['smite', 'flash'],
                   ['ignite', 'flash'], ['teleport ', 'ghost'], ['flash', 'teleport'], ['teleport ', 'ghost'],
                   ['flash', 'teleport'], ['smite', 'flash'], ['flash', 'teleport'], ['smite', 'flash'],
                   ['flash', 'teleport'], ['teleport ', 'ghost'], ['teleport ', 'ghost'], ['flash', 'ghost'],
                   ['flash', 'teleport'], ['smite', 'flash'], ['ignite', 'flash'], ['flash', 'teleport'],
                   ['flash', 'ghost'], ['flash', 'ghost'], ['heal', 'flash'], ['smite', 'flash'], ['flash', 'teleport'],
                   ['smite', 'flash'], ['flash', 'teleport'], ['teleport ', 'ghost'], ['flash', 'teleport'],
                   ['flash', 'ignite'], ['heal', 'flash'], ['flash', 'ghost'], ['teleport ', 'ghost'],
                   ['smite', 'flash'], ['heal', 'flash'], ['smite', 'flash'], ['flash', 'teleport'], ['smite', 'flash'],
                   ['teleport ', 'ghost'], ['flash', 'smite'], ['heal', 'flash'], ['flash', 'smite'],
                   ['flash', 'smite'], ['barrier', 'flash'], ['ignite', 'flash'], ['heal', 'flash'],
                   ['flash', 'teleport'], ['ignite', 'flash'], ['ignite', 'flash'], ['flash', 'ignite'],
                   ['flash', 'teleport'], ['flash', 'smite'], ['exhaust', 'flash'], ['heal', 'flash'],
                   ['ignite', 'flash'], ['ignite', 'flash'], ['flash', 'teleport'], ['heal', 'flash'],
                   ['exhaust', 'flash'], ['barrier', 'flash'], ['flash', 'smite'], ['ignite', 'flash'],
                   ['ignite', 'flash'], ['flash', 'ignite'], ['heal', 'flash'], ['flash', 'ignite'],
                   ['ignite', 'flash'], ['flash', 'ignite'], ['flash', 'smite'], ['ghost', 'flash'], ['heal', 'flash'],
                   ['ghost', 'flash'], ['ignite', 'flash'], ['flash', 'smite'], ['exhaust', 'flash'],
                   ['ghost', 'flash'], ['heal', 'flash'], ['ignite', 'flash'], ['flash', 'smite'], ['barrier', 'flash'],
                   ['flash', 'ignite'], ['flash', 'ignite'], ['barrier', 'flash'], ['flash', 'smite'],
                   ['ignite', 'flash'], ['ignite', 'flash'], ['heal', 'flash'], ['exhaust', 'flash'],
                   ['barrier', 'flash'], ['ignite', 'flash'], ['flash', 'smite'], ['flash', 'ignite'],
                   ['flash', 'teleport'], ['flash', 'smite'], ['flash', 'teleport'], ['flash', 'smite'],
                   ['barrier', 'flash'], ['flash', 'ignite'], ['barrier', 'flash'], ['ignite', 'flash'],
                   ['ignite', 'flash'], ['smite', 'flash'], ['barrier', 'flash'], ['ghost', 'flash'],
                   ['ignite', 'flash'], ['teleport', 'flash'], ['ghost', 'teleport'], ['smite', 'flash'],
                   ['teleport', 'flash'], ['barrier', 'flash'], ['barrier', 'flash'], ['teleport', 'flash'],
                   ['ghost', 'flash'], ['ignite', 'flash'], ['ignite', 'flash'], ['ignite', 'flash'],
                   ['ignite', 'flash'], ['ghost', 'flash'], ['ignite', 'flash'], ['barrier', 'flash'],
                   ['ghost', 'teleport'], ['ignite', 'flash'], ['barrier', 'flash'], ['teleport', 'flash'],
                   ['flash', 'smite'], ['ignite', 'flash'], ['ignite', 'flash'], ['ghost', 'teleport'],
                   ['barrier', 'flash'], ['smite', 'flash'], ['ghost', 'flash'], ['ignite', 'flash'],
                   ['ignite', 'flash'], ['ignite', 'flash'], ['barrier', 'flash'], ['ghost', 'flash'],
                   ['ghost', 'teleport'], ['teleport', 'flash'], ['ghost', 'flash'], ['smite', 'flash'],
                   ['ignite', 'flash'], ['ignite', 'flash'], ['ignite', 'flash'], ['barrier', 'flash'],
                   ['teleport', 'flash'], ['ghost', 'flash'], ['ignite', 'flash'], ['smite', 'flash'],
                   ['ignite', 'flash'], ['heal', 'flash'], ['ignite', 'flash'], ['ignite', 'flash'],
                   ['ignite', 'flash'], ['barrier', 'flash'], ['flash', 'smite'], ['teleport', 'flash'],
                   ['ghost', 'teleport'], ['heal', 'flash'], ['barrier', 'flash'], ['ignite', 'flash'],
                   ['ghost', 'flash'], ['smite', 'flash'], ['ignite', 'flash'], ['barrier', 'flash'],
                   ['teleport', 'flash'], ['ghost', 'flash'], ['ignite', 'flash'], ['smite', 'flash'],
                   ['flash', 'ignite'], ['ghost', 'flash'], ['heal', 'flash'], ['ghost', 'flash'], ['heal', 'flash'],
                   ['smite', 'flash'], ['flash', 'ignite'], ['flash', 'cleanse'], ['teleport', 'flash'],
                   ['smite', 'flash'], ['ghost', 'teleport'], ['ghost', 'flash'], ['smite', 'flash'],
                   ['teleport', 'flash'], ['flash', 'ignite'], ['teleport', 'flash'], ['heal', 'flash'],
                   ['smite', 'flash'], ['ghost', 'teleport'], ['heal', 'flash'], ['flash', 'cleanse'],
                   ['ghost', 'flash'], ['heal', 'flash'], ['ghost', 'flash'], ['ghost', 'flash'], ['flash', 'ignite'],
                   ['ghost', 'teleport'], ['flash', 'cleanse'], ['smite', 'flash'], ['smite', 'flash'],
                   ['teleport', 'flash'], ['ghost', 'flash'], ['smite', 'flash'], ['teleport', 'flash'],
                   ['flash', 'ignite'], ['heal', 'flash'], ['smite', 'flash'], ['smite', 'flash'], ['flash', 'cleanse'],
                   ['heal', 'flash'], ['teleport', 'flash'], ['ghost', 'flash'], ['heal', 'flash'],
                   ['teleport', 'flash'], ['flash', 'cleanse'], ['ignite', 'flash'], ['ghost', 'flash'],
                   ['heal', 'flash'], ['flash', 'ignite'], ['ignite', 'flash'], ['smite', 'flash'],
                   ['teleport', 'flash'], ['teleport', 'flash'], ['ghost', 'flash'], ['ignite', 'flash'],
                   ['ghost', 'flash'], ['ignite', 'flash'], ['smite', 'flash'], ['smite', 'flash'], ['flash', 'ignite'],
                   ['smite', 'flash'], ['ghost', 'flash'], ['ignite', 'flash'], ['ghost', 'flash'],
                   ['teleport', 'ghost'], ['smite', 'flash'], ['ghost', 'flash'], ['smite', 'flash'],
                   ['flash', 'ignite'], ['ignite', 'flash'], ['ignite', 'flash'], ['teleport', 'flash'],
                   ['flash', 'ignite'], ['ignite', 'flash'], ['teleport', 'ghost'], ['ignite', 'flash'],
                   ['flash', 'ignite'], ['ignite', 'flash'], ['flash', 'ignite'], ['ghost', 'flash'],
                   ['teleport', 'flash'], ['flash', 'ghost'], ['teleport', 'flash'], ['smite', 'flash'],
                   ['flash', 'ghost'], ['flash', 'cleanse'], ['ghost', 'flash'], ['flash', 'smite'], ['flash', 'heal'],
                   ['ignite', 'ghost'], ['teleport', 'flash'], ['flash', 'ghost'], ['ignite', 'ghost'],
                   ['teleport', 'flash'], ['flash', 'teleport'], ['flash', 'ghost'], ['teleport', 'flash'],
                   ['ignite', 'ghost'], ['ignite', 'ghost'], ['flash', 'teleport'], ['flash', 'cleanse'],
                   ['teleport', 'flash'], ['flash', 'ghost'], ['flash', 'cleanse'], ['smite', 'flash'],
                   ['teleport', 'flash'], ['ignite', 'ghost'], ['flash', 'teleport'], ['teleport', 'flash'],
                   ['flash', 'smite'], ['ignite', 'ghost'], ['teleport', 'flash'], ['flash', 'cleanse'],
                   ['flash', 'ghost'], ['teleport', 'flash'], ['ignite', 'ghost'], ['barrier', 'flash'],
                   ['smite', 'flash'], ['ignite', 'flash'], ['flash', 'heal'], ['smite', 'flash'], ['smite', 'flash'],
                   ['flash', 'ignite'], ['flash', 'heal'], ['ignite', 'flash'], ['barrier', 'flash'],
                   ['ignite', 'flash'], ['ignite', 'flash'], ['smite', 'flash'], ['flash', 'heal'], ['smite', 'flash'],
                   ['flash', 'heal'], ['smite', 'flash'], ['ignite', 'flash'], ['ignite', 'flash'], ['smite', 'flash'],
                   ['smite', 'flash'], ['ignite', 'flash'], ['ignite', 'teleport'], ['flash', 'heal'],
                   ['ignite', 'flash'], ['ignite', 'teleport'], ['flash', 'heal'], ['smite', 'flash'],
                   ['ignite', 'flash'], ['ignite', 'flash'], ['ignite', 'flash'], ['smite', 'flash'],
                   ['barrier', 'flash'], ['flash', 'heal'], ['ignite', 'flash'], ['barrier', 'flash'],
                   ['flash', 'heal'], ['flash', 'heal'], ['flash', 'ignite'], ['ignite', 'flash'], ['smite', 'flash'],
                   ['barrier', 'flash'], ['ignite', 'flash'], ['ignite', 'flash'], ['smite', 'flash'],
                   ['smite', 'flash'], ['flash', 'heal'], ['flash', 'ignite'], ['ignite', 'flash']]

a = 0
for i in range(0, 56):
    a += 1
    if which_team[i] == 'b':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['flash', 'teleport'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['ghost', 'ignite'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['cleanse', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['heal', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
    elif which_team[i] == 'p':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['teleport', 'ignite'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['teleport', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['heal', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['barrier', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
print(a)
a = 0
for i in range(56, 110):
    a += 1
    if which_team[i] == 'b':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['teleport', 'flash'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['teleport', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['exhaust', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['ignite', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
    elif which_team[i] == 'p':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['ignite', 'flash'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['flash', 'teleport'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['flash', 'cleanse'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['heal', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
print(a)
a = 0
for i in range(110, 150):
    a += 1
    if which_team[i] == 'b':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['teleport', 'flash'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['ignite', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['heal', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['ignite', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
    elif which_team[i] == 'p':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['ghost', 'teleport'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['teleport', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['cleanse', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['ignite', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
print(a)
a = 0
for i in range(150, 200):
    a += 1
    if which_team[i] == 'b':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['ignite', 'flash'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['ignite', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['ghost', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['ignite', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
    elif which_team[i] == 'p':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['ignite', 'teleport'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['flash', 'smite'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['teleport', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['flash', 'heal'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['flash', 'ignite'])
        else:
            ansforwhatspell.append(['error', i])
print(a)
a = 0
for i in range(200, 242):
    a += 1
    if which_team[i] == 'b':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['teleport', 'flash'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['ignite', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['cleanse', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['heal', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
    elif which_team[i] == 'p':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['ghost', 'teleport'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['flash', 'smite'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['ignite', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['flash', 'heal'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['flash', 'ghost'])
        else:
            ansforwhatspell.append(['error', i])
print(a)
a = 0
for i in range(242, 276):
    a += 1
    if which_team[i] == 'b':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['barrier ', 'flash'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['special', i])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['heal', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['ignite', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
    elif which_team[i] == 'p':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['flash', 'teleport'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['exhaust', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['heal', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['ignite', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
print(a)
a = 0
######특수!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

for i in range(276, 310):
    a += 1
    if which_team[i] == 'b':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['teleport ', 'ghost'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['flash', 'teleport'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['flash', 'ghost'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['heal', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
    elif which_team[i] == 'p':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['flash', 'ignite'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['flash', 'teleport'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['flash', 'ghost'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['ignite', 'flash'])
        else:
            ansforwhatspell.append(['error', i])

for i in range(310, 370):
    a += 1
    if which_team[i] == 'b':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['ghost', 'flash'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['flash', 'smite'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['exhaust', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['heal', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['ignite', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
    elif which_team[i] == 'p':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['flash', 'teleport'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['flash', 'smite'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['ignite', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['barrier', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['flash', 'ignite'])
        else:
            ansforwhatspell.append(['error', i])
print(a)
a = 0
for i in range(370, 439):
    a += 1
    if which_team[i] == 'b':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['ghost', 'teleport'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['flash', 'smite'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['ignite', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['heal', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['ignite', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
    elif which_team[i] == 'p':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['barrier', 'flash'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['teleport', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['ghost', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['ignite', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
print(a)
a = 0
for i in range(439, 484):
    a += 1
    if which_team[i] == 'b':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['ghost', 'teleport'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['teleport', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['heal', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['barrier', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
    elif which_team[i] == 'p':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['ghost', 'flash'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['teleport', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['flash', 'cleanse'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['flash', 'ignite'])
        else:
            ansforwhatspell.append(['error', i])
print(a)
a = 0
for i in range(484, 520):
    a += 1
    if which_team[i] == 'b':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['teleport', 'ghost'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['ignite', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['heal', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['ghost', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
    elif which_team[i] == 'p':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['flash', 'ignite'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['teleport', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['ghost', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['ignite', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
print(a)
a = 0
for i in range(520, 555):
    a += 1
    if which_team[i] == 'b':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['flash', 'teleport'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['teleport', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['ghost', 'flash'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['flash', 'heal'])
        else:
            ansforwhatspell.append(['error', i])
    elif which_team[i] == 'p':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['teleport', 'flash'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['flash', 'smite'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['ignite', 'ghost'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['flash', 'cleanse'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['flash', 'ghost'])
        else:
            ansforwhatspell.append(['error', i])
print(a)
a = 0
for i in range(555, 604):
    a += 1
    if which_team[i] == 'b':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['flash', 'ignite'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['ignite', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['flash', 'heal'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['ignite', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
    elif which_team[i] == 'p':
        if ansforposition[i] == 'top':
            ansforwhatspell.append(['ignite', 'teleport'])
        elif ansforposition[i] == 'jungle':
            ansforwhatspell.append(['smite', 'flash'])
        elif ansforposition[i] == 'mid':
            ansforwhatspell.append(['ignite', 'flash'])
        elif ansforposition[i] == 'ad carry':
            ansforwhatspell.append(['flash', 'heal'])
        elif ansforposition[i] == 'support':
            ansforwhatspell.append(['barrier', 'flash'])
        else:
            ansforwhatspell.append(['error', i])
print(a)
print(ansforwhatspell)
print(len(ansforwhatspell))

# 없음1,있음2,중간에 사용3,없다 생김4,없다 생긴걸 사용5
'''
ans_spell_used = [
    [3,3],
[3,3],
[2,1],
[4,3],
[3,2],
[2,1],
[2,3],
[1,3],
[3,1],
[1,1],
[3,1],
    [3,3],
[2,2],
[2,1],
[2,1],
[1,1],
[1,2],
[1,1],
[3,1],
[3,1],
[1,1],
[1,1],
    [1,1],
[1,3],
[1,1],
[1,1],
[1,1],
[2,1],
[3,1],
[2,2],
[2,1],
[3,2],
[2,1],
    [3,3],
[3,2],
[1,1],
[1,2],
[1,1],
[1,1],
[1,1],
[3,1],
[1,3],
[3,1],
[1,1],
    [1,3],
[3,1],
[1,2],
[1,1],
[1,1],
[1,1],
[1,1],
[1,4],
[1,2],
[5,1],
[1,1],
    [3,3],
[1,3],
[1,3],
[1,1],
[3,2],
[1,1],
[1,1],
[2,1],
[1,2],
[1,1],
[2,2],
    [1,1],
[1,3],
[1,1],
[1,2],
[1,1],
[1,1],
[3,3],
[1,2],
[2,1],
[1,1],
[1,1],
[1,1],
[1,1],
[2,2],
[1,1],
[2,1],
[3,3],
[1,1],
[3,1],
[2,3],
[3,3],
[3,3],
[1,1],
[1,1],
[1,2],
[1,1],
[1,1],
[1,1],
[1,3],
[1,1],
[2,1],
[3,1],
[1,1],
[3,5],
[1,1],
[1,1],
[1,1],
[3,3],
[1,1],
[1,1],
[1,2],
[3,1],
[3,4],
[2,1],
[3,3],
[3,3],
[3,1],
[1,2],
[1,1],
[3,1],
[1,1],
[1,1],
[1,1],
[3,1],
[1,1],
[1,1],
[1,2],
[1,3],
[2,1],
[1,2],
[3,1],
[1,1],
[3,3],
[1,1],
[2,1],
[1,1],
[2,3],
[2,1],
[3,3],
[1,1],
[5,1],
[3,2],
[2,1],
[2,1],
[3,1],
[1,3],
[2,2],
[3,3],
[1,3],
[2,1],
[2,1],
[2,2],
[1,1],
[1,1],
[2,2],
[2,2],
[3,2],
[1,3],
[1,1],
[3,3],
[1,1],
[1,3],
[1,1],
[2,2],
[1,1],
[1,1],
[3,4],
[3,1],
[1,1],
[1,3],
[1,1],
[2,2],
[1,3],
[1,3],
[1,1],
[3,3],
[3,3],
[1,1],
[1,1],
[2,5],
[3,1],
[1,1],
[1,1],
[3,1],
[1,1],
[1,1],
[1,3],
[1,1],
[1,1],
[2,1],
[1,2],
[2,2],
[3,3],
[2,1],
[3,1],
[3,3],
[3,1],
[1,3],
[1,3],
[1,2],
[3,2],
[3,3],
[2,2],
[3,1],
[3,3],
[3,1],
[2,2],
[3,3],
[1,1],
[1,1],
[1,1],
[1,1],
[1,3],
[3,3],
[2,3],
[1,1],
[1,1],
[5,1],
[1,1],
[2,1],
[5,1],
[3,1],
[1,1],
[1,1],
[1,3],
[1,1],
[3,3],
[1,1],
[1,1],
[1,3],
[1,3],
[1,1],
[1,1],
[2,2],
[1,4],
[2,1],
[3,1],
[3,5],
[5,1],
[1,2],
[3,2],
[2,1],
[1,2],
[1,3],
[2,2],
[1,1],
[2,2],
[1,1],
[3,3],
[3,3],
[2,3],
[1,1],
[3,1],
[3,3],
[1,1],
[1,2],
[5,1],
[1,1],
[1,1],
[1,5],
[2,1],
[4,1],
[4,1],
[3,3], #260
[2,1],
[2,1],
[3,1],
[3,1],
[2,2],
[1,3],
[2,1],
[2,2],
[3,2],
[2,2],
[1,2],
[3,3],
[1,5],
[1,1],
[3,3],
[1,2],
[2,3],
[3,3],
[1,1],
[1,1],
[2,1],
[1,2],
[1,1],
[1,1],
[1,3],
[1,1],
[3,3],
[3,1],
[3,3],
[1,1],
[3,1],
[1,1],
[1,3],
[3,1],
[1,1],
[1,1],
[1,1],
[1,1],  # 298
[1,1],
[1,1],
[1,5],
[1,3],
[2,3],
[3,3],
[3,2],
[1,1],
[3,1],
[1,1],
[3,2],
[1,1],
[3,1],
[2,1],
[1,1],
[1,4],
[3,2],
[3,2],
[3,1],
[1,1],
[1,3],     # 319
[1,1],
[1,1],
[2,2],
[1,4],
[3,3],
[1,1],
[3,2],
[2,2],
[2,1],
[2,2],
[3,1],
[3,3],
[3,1],
[3,3], # 333
[3,3],
[3,3],
[1,3],
[1,1],
[1,1],
[2,4],
[1,5],
[1,1],
[2,1],
[3,1],
[3,3],
[3,3],
[3,2],
[1,3],
[1,2], # 348
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
[,],
]
'''
lineordone = ['line', 'line', 'line', 'line', 'line', 'line', 'line', 'line', 'line', 'line', 'line', 'line', 'line',
              'line', 'line', 'line', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done',
              'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done',
              'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done',
              'done', 'done', 'done', 'line', 'line', 'line', 'line', 'line', 'line', 'line', 'line', 'line', 'line',
              'line', 'line', 'line', 'line', 'line', 'line', 'line', 'line', 'line', 'line', 'line', 'line', 'line',
              'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done',
              'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done', 'done',
              'done', 'done', 'done', 'done', 'done', 'done']
t = 23
a = 24
b = 55
"""
for i in range(t):
    lineordone.append('line')
for i in range(b-a+1):
    lineordone.append('done')

print(len(lineordone))
print(lineordone)
"""
# 우리팀 탑,정글,미드,봇,서폿  상대팀 탑,정글,미드,봇,서폿
near = [['n', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ]

'''
for i in range(604):
    near.append(['','','','','','','','','',''])
print(near)
'''

'''
for i, j in enumerate(ans):
    re_higlightls[i]['line'] = j
print(re_higlightls)
'''
