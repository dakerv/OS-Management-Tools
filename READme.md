Simulation of I/O Management and Memory Management Subsystems
Submitted by: Vanessa Daker (11253946)
Date: 8th December 2024

Introduction
This report documents my approach to designing and implementing critical operating system subsystems for I/O and Memory Management, as well as integrating them into a unified simulation. The goal was to simulate real-world scenarios that test key OS principles like algorithm design, resource optimization, and performance evaluation.

Task 1: Advanced I/O Management System
Overview
The I/O Management System was designed to handle concurrent requests for multiple devices like printers and disks. Requests were scheduled using a priority queue, with execution prioritized by arrival time and duration. Dynamic queue management allowed idle devices to "steal" requests from others.

Implementation
Data Structure:
Each device maintained its own queue, implemented as a deque.
A global priority queue tracked all requests for scheduling.
Scheduling:
Requests were processed in a non-preemptive manner.
Idle devices monitored queue statuses to "steal" requests if another device had significant waiting times.
Output:
A Gantt chart visually represented the request execution timeline.
Metrics included:
Average Waiting Time
Average Turnaround Time
Device Utilization
Challenges and Solutions
Challenge: Managing synchronization between devices and their queues.
Solution: Used a step-by-step global clock simulation to ensure proper timing of events.
Challenge: Visualizing execution timelines effectively.
Solution: Created Gantt charts using Matplotlib for clarity.
Task 2: Advanced Memory Management System
Overview
The memory management subsystem simulated a virtual memory environment using an adaptive page replacement algorithm. A prefetching mechanism was also implemented to predict and load future pages.

Implementation
Adaptive Page Replacement:
Combined Least Recently Used (LRU) and Most Frequently Used (MFU) algorithms.
Dynamically switched between LRU and MFU based on the system workload.
Prefetching:
Predicted the next page based on the current access pattern.
Reduced page faults by preloading pages into memory.
Output:
A timeline of memory states showed how pages were replaced dynamically.
Metrics included:
Total Page Faults
Hit Ratio
Average Memory Access Time
Challenges and Solutions
Challenge: Balancing LRU and MFU to optimize memory access.
Solution: Used an adaptive mechanism that analyzed fault patterns to decide between the two algorithms.
Challenge: Ensuring prefetching didn't overload the system.
Solution: Limited prefetching to scenarios where memory had available frames.
Task 3: Unified Subsystem Integration
Overview
The unified simulation integrated the I/O and Memory Management subsystems. It mimicked real-world scenarios where I/O requests required memory operations, such as loading a file into memory before printing.

Implementation
Integration:
Memory references were included in I/O requests.
After processing each I/O request, the memory subsystem handled the associated page accesses.
Performance Optimization:
Resource contention between I/O and memory was minimized by carefully scheduling requests.
Output:
System-wide metrics:
Total Throughput
Average Response Time
Overall Utilization (I/O and memory).
Challenges and Solutions
Challenge: Synchronizing I/O and memory operations effectively.
Solution: Developed a unified control flow to manage interdependencies between subsystems.
Challenge: Evaluating system-wide performance comprehensively.
Solution: Combined individual metrics from both subsystems into holistic measures.
Results
Task 1: I/O Management
Average Waiting Time: 12ms
Average Turnaround Time: 37ms
Device Utilization:
Disk: 85%
Printer: 78%
Task 2: Memory Management
Total Page Faults: 4
Hit Ratio: 0.6
Average Memory Access Time: 41ms
Task 3: Unified System
Total Throughput: 0.28 requests/ms
Average Response Time: 45ms
Overall Utilization:
I/O Utilization: 81.5%
Memory Hit Ratio: 60%
Conclusion
This assignment was an excellent opportunity to delve into the complexities of I/O and Memory Management. By simulating real-world scenarios, I gained hands-on experience with priority queues, adaptive algorithms, and system integration.

The most rewarding aspect was optimizing resource contention between the subsystems, which required careful analysis and iteration. The project not only strengthened my understanding of operating system fundamentals but also enhanced my ability to apply algorithms to solve complex problems.