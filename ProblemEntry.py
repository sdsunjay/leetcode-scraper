class ProblemEntry:
    def __init__(self, problem_id, title, url_link, tags, acceptance, difficulty, frequency):
        self.problem_id = problem_id
        self.title = title
        self.url_link = url_link
        self.tags = tags  # This will be a list of strings
        self.acceptance = acceptance
        self.difficulty = difficulty
        self.frequency = frequency

    def __repr__(self):
        return f"ProblemEntry(probelm_id={self.id}, title={self.title}, url_link={self.url_link}, tags={self.tags}, acceptance={self.acceptance}, difficulty={self.difficulty}, frequency={self.frequency})"
