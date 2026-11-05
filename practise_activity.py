marks = [98, 92, 64, 81, 79]
subjects = ["math", "physics", "english", "biology", "history"]

results = {mark: count for mark, count in zip(subjects, marks)}
print("The results: ", results)
