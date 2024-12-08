class MemoryManager:
    def __init__(self, frames):
        self.frames = frames
        self.memory = []
        self.page_faults = 0
        self.page_hits = 0
        self.access_count = {}

    def access_page(self, page):
        # Update access frequency
        self.access_count[page] = self.access_count.get(page, 0) + 1

        if page in self.memory:
            # Page hit
            self.page_hits += 1
        else:
            # Page fault
            self.page_faults += 1
            if len(self.memory) < self.frames:
                self.memory.append(page)
            else:
                # Adaptive replacement: Decide between LRU and MFU
                lru_page = min(self.memory, key=lambda x: self.access_count[x])
                mfu_page = max(self.memory, key=lambda x: self.access_count[x])

                # Example switch: Use LRU if total faults are even, MFU otherwise
                replacement = lru_page if self.page_faults % 2 == 0 else mfu_page
                self.memory.remove(replacement)
                self.memory.append(page)

        # Prefetch: Add the next page if not already in memory
        predicted_page = page + 1
        if predicted_page not in self.memory and len(self.memory) < self.frames:
            self.memory.append(predicted_page)

    def simulate(self, reference_sequence):
        for page in reference_sequence:
            self.access_page(page)

    def get_metrics(self):
        total_accesses = self.page_faults + self.page_hits
        hit_ratio = self.page_hits / total_accesses
        avg_memory_access_time = (self.page_faults * 100 + self.page_hits * 1) / total_accesses
        return {
            "Page Faults": self.page_faults,
            "Hit Ratio": hit_ratio,
            "Average Memory Access Time": avg_memory_access_time
        }

# Example usage
reference_sequence = [2, 3, 1, 5, 2, 4, 1, 3, 5, 2]
frames = 3

memory_manager = MemoryManager(frames)
memory_manager.simulate(reference_sequence)
metrics = memory_manager.get_metrics()

print("Metrics:", metrics)
