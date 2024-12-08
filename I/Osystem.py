import heapq
from collections import deque

class Device:
    def __init__(self, name):
        self.name = name
        self.queue = deque()
        self.time = 0
        self.utilization = 0

    def add_request(self, request):
        self.queue.append(request)

    def process_requests(self, global_time):
        if self.queue:
            request = self.queue.popleft()
            start_time = max(global_time, self.time)
            end_time = start_time + request['duration']
            self.time = end_time
            self.utilization += request['duration']
            return {
                "Device": self.name,
                "Request_ID": request['id'],
                "Start": start_time,
                "End": end_time
            }
        return None

class IOManager:
    def __init__(self):
        self.devices = {}
        self.completed = []
        self.global_time = 0

    def add_device(self, device_name):
        self.devices[device_name] = Device(device_name)

    def add_request(self, device_name, request_id, arrival, duration):
        request = {"id": request_id, "arrival": arrival, "duration": duration}
        heapq.heappush(self.devices[device_name].queue, (arrival, request))

    def run(self):
        while any(device.queue for device in self.devices.values()):
            for device in self.devices.values():
                result = device.process_requests(self.global_time)
                if result:
                    self.completed.append(result)
                    self.global_time = result["End"]

    def calculate_metrics(self):
        total_time = sum(
            [max(self.global_time - device.time, 0) for device in self.devices.values()]
        )
        utilization = {device.name: device.utilization / total_time * 100 for device in self.devices.values()}
        return utilization

# Example usage
io_manager = IOManager()
io_manager.add_device("Disk")
io_manager.add_device("Printer")

io_manager.add_request("Disk", "R1", 0, 20)
io_manager.add_request("Printer", "R2", 10, 25)
io_manager.add_request("Printer", "R3", 5, 15)

io_manager.run()
metrics = io_manager.calculate_metrics()

print("Completed Requests Timeline:", io_manager.completed)
print("Device Utilization:", metrics)
