import java.util.*;

class Task {
    int id;
    int executionTime; // in milliseconds

    public Task(int id, int executionTime) {
        this.id = id;
        this.executionTime = executionTime;
    }

    public void execute() {
        System.out.println("Executing Task ID: " + id + " | Time required: " + executionTime + "ms");
        try {
            Thread.sleep(executionTime); // simulate execution delay
        } catch (InterruptedException e) {
            System.out.println("Task execution interrupted.");
        }
        System.out.println("Task ID: " + id + " completed.\n");
    }
}

class CloudServer {
    Queue<Task> taskQueue = new LinkedList<>();

    public void submitTask(Task task) {
        taskQueue.add(task);
        System.out.println("Task ID " + task.id + " submitted to cloud.");
    }

    public void executeAllTasks() {
        System.out.println("\n--- Cloud Execution Started ---\n");
        while (!taskQueue.isEmpty()) {
            Task task = taskQueue.poll();
            task.execute();
        }
        System.out.println("--- Cloud Execution Finished ---");
    }
}

public class SimpleCloudSimulator {
    public static void main(String[] args) {
        CloudServer cloud = new CloudServer();

        // Create some sample tasks
        Task task1 = new Task(1, 1000); // 1 second
        Task task2 = new Task(2, 1500); // 1.5 seconds
        Task task3 = new Task(3, 500);  // 0.5 seconds

        // Submit tasks to cloud
        cloud.submitTask(task1);
        cloud.submitTask(task2);
        cloud.submitTask(task3);

        // Execute all tasks (FCFS)
        cloud.executeAllTasks();
    }
}
