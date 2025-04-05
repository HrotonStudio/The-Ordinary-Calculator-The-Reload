import java.time.LocalDateTime;

public class log {
    public static void info(String level, String msg, String file) {
        LocalDateTime now = LocalDateTime.now();
        String wait_time = now.toString();
        String time = wait_time.substring(0, wait_time.length() - 6);
        String f_time = time.replace("T", " ");
        if (f_time.endsWith(".")) {
            String final_time = f_time + "000";
            String final_file = String.format("%-24s", file);
            if (level == "I") {
                System.out.println("\033[94m" + final_time + " " + "\033[92m" + level + " " + "\033[90m" + final_file + "\033[92m" + msg + "\033[0m");
            } else if (level == "E") {
                System.out.println("\033[94m" + final_time + " " + "\033[31m" + level + " " + "\033[90m" + final_file + "\033[31m" + msg + "\033[0m");
            } else if (level == "W") {
                System.out.println("\033[94m" + final_time + " " + "\033[33m" + level + " " + "\033[90m" + final_file + "\033[33m" + msg + "\033[0m");
            } else if (level == "D") {
                System.out.println("\033[94m" + final_time + " " + "\033[90m" + level + " " + "\033[90m" + final_file + "\033[90m" + msg + "\033[0m");
            } else if (level == "F") {
                System.out.println("\033[94m" + final_time + " " + "\033[35m" + level + " " + "\033[90m" + final_file + "\033[35m" + msg + "\033[0m");
            } else if (level == "C") {
                System.out.println("\033[94m" + final_time + " " + "\033[35m" + level + " " + "\033[90m" + final_file + "\033[35m" + msg + "\033[0m");
            }

        } else {
            String final_time = f_time;
            String final_file = String.format("%-24s", file);
            if (level == "I") {
                System.out.println("\033[94m" + final_time + " " + "\033[92m" + level + " " + "\033[90m" + final_file + "\033[92m" + msg + "\033[0m");
            } else if (level == "E") {
                System.out.println("\033[94m" + final_time + " " + "\033[31m" + level + " " + "\033[90m" + final_file + "\033[31m" + msg + "\033[0m");
            } else if (level == "W") {
                System.out.println("\033[94m" + final_time + " " + "\033[33m" + level + " " + "\033[90m" + final_file + "\033[33m" + msg + "\033[0m");
            } else if (level == "D") {
                System.out.println("\033[94m" + final_time + " " + "\033[90m" + level + " " + "\033[90m" + final_file + "\033[90m" + msg + "\033[0m");
            } else if (level == "F") {
                System.out.println("\033[94m" + final_time + " " + "\033[35m" + level + " " + "\033[90m" + final_file + "\033[35m" + msg + "\033[0m");
            } else if (level == "C") {
                System.out.println("\033[94m" + final_time + " " + "\033[35m" + level + " " + "\033[90m" + final_file + "\033[35m" + msg + "\033[0m");
                
            }
        }
    }
}
