# TODO: This will become automated in a CI workflow
import pickle

with open("../token.pickle", "rb") as f:
    API_TOKEN = pickle.load(f)

with open("../token.pickle", "wb") as f:
    pickle.dump(API_TOKEN, f)


with open("../issues.pickle", "rb") as f:
    API_TOKEN = pickle.load(f)

with open("../issues.pickle", "wb") as f:
    pickle.dump(issues, f)

final_contribs = all_contribs_dict_up
with open("all_contribs.pickle", "wb") as f:
    pickle.dump(all_contribs_dict_up, f)
