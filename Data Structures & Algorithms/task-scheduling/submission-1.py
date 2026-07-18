class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        clock = 0
        window = []
        heapq.heapify(window)

        for key in cnt.keys():
            cnt[key] = (0, cnt[key])

        while len(cnt.keys()):
            # add to window with latest increment
            for key in cnt.keys():
                available_time, count = cnt[key]
                if available_time <= clock:
                    heapq.heappush(window, (-abs(count), key))
            # process window for most prevalent
            if len(window):
                curr_count, curr_letter = heapq.heappop(window)
                curr_count += 1
                curr_time = clock + n + 1
                if curr_count == 0: # letter used up
                    del cnt[curr_letter]
                else:
                    cnt[curr_letter] = (curr_time, curr_count) # add letter back into list
            window = []
            heapq.heapify(window)
            clock += 1
            

        return clock