class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = [[] for _ in range(101)]
        for id, score in items:
            scores[id].append(score)

        res = []
        for i, score in enumerate(scores):
            score.sort(reverse=True)
            top_five = score[:5]
            if len(top_five):
                res.append([i, sum(top_five) // len(top_five)])

        return res
