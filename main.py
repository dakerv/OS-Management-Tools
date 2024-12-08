import I.Osystem as Osystem
import memoryManagementSystem
import integratedSystem

def main():
  
    io_manager = Osystem()
    memory_manager = memoryManagementSystem(frames=3)
    unified_system = integratedSystem(io_manager, memory_manager)
    
   
    unified_system.add_request("Disk", "R1", 0, 20, [2, 3, 1, 5])
    unified_system.add_request("Printer", "R2", 10, 25, [1, 4, 2, 3])
    unified_system.run()
    

    performance = unified_system.evaluate_performance()
    print("Performance Metrics:", performance)

if __name__ == "__main__":
    main()
