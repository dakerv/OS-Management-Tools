class UnifiedSystem:
    def __init__(self, io_manager, memory_manager):
        self.io_manager = io_manager
        self.memory_manager = memory_manager
        self.requests = []

    def add_request(self, device_name, request_id, arrival, duration, memory_references):
        self.io_manager.add_request(device_name, request_id, arrival, duration)
        self.requests.append({"id": request_id, "memory_references": memory_references})

    def run(self):
        print("Starting Unified Subsystem Simulation...")
   
        self.io_manager.run()
        print("Completed I/O Management")
        

        for req in self.requests:
            print(f"Processing Memory for Request {req['id']}")
            self.memory_manager.simulate(req['memory_references'])

    def evaluate_performance(self):
   
        io_metrics = self.io_manager.calculate_metrics()
        memory_metrics = self.memory_manager.get_metrics()

  
        total_throughput = len(self.io_manager.completed) / self.io_manager.global_time
        avg_response_time = sum(req['End'] - req['Start'] for req in self.io_manager.completed) / len(self.io_manager.completed)
        overall_utilization = {
            "I/O Utilization": io_metrics,
            "Memory Hit Ratio": memory_metrics["Hit Ratio"],
        }
        return {
            "Total Throughput": total_throughput,
            "Average Response Time": avg_response_time,
            "Overall Utilization": overall_utilization,
        }