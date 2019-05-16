import json
import os

class User:
  @staticmethod
  def current():
    here = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(here, '../data/current_user.json')) as current_user:
      return json.load(current_user)

