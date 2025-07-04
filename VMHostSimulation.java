import java.util.*;

class VirtualMachine {
    int id;
    int requiredCpu;
    public VirtualMachine(int id, int requiredCpu) {
        this.id = id;
        this.requiredCpu = requiredCpu;
    }
}

class CloudHost {
    int id;
    int totalCpu;
    int usedCpu = 0;
    List<Integer> deployedVMs = new ArrayList<>();
    public CloudHost(int id, int totalCpu) {
        this.id = id;
        this.totalCpu = totalCpu;
    }
    public boolean canHost(VirtualMachine vm) {
        return (usedCpu + vm.requiredCpu) <= totalCpu;
    }
    public void deployVM(VirtualMachine vm) {
        usedCpu += vm.requiredCpu;
        deployedVMs.add(vm.id);
        System.out.println("VM " + vm.id + " deployed to Host " + id +
                " | CPU used: " + usedCpu + "/" + totalCpu);
    }
}

public class VMHostSimulation {
    public static void main(String[] args) {
        // Step 1: Create Hosts
        List<CloudHost> hosts = new ArrayList<>();
        hosts.add(new CloudHost(1, 8));
        hosts.add(new CloudHost(2, 8));
        // Step 2: Create VMs
        List<VirtualMachine> vms = new ArrayList<>();
        vms.add(new VirtualMachine(101, 2));
        vms.add(new VirtualMachine(102, 3));
        vms.add(new VirtualMachine(103, 4));
        vms.add(new VirtualMachine(104, 2));
        vms.add(new VirtualMachine(105, 5));
        // Step 3: Allocate VMs to Hosts
        System.out.println("--- VM Allocation Started ---\n");
        for (VirtualMachine vm : vms) {
            boolean allocated = false;
            for (CloudHost host : hosts) {
                if (host.canHost(vm)) {
                    host.deployVM(vm);
                    allocated = true;
                    break;
                }
            }
            if (!allocated) {
                System.out.println("VM " + vm.id + " could NOT be deployed due to insufficient CPU.");
            }
        }
        System.out.println("\n--- VM Allocation Finished ---");
    }
}