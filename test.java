public class Test {
    public static void main(String[] args) {
        String query = "SELECT * FROM users WHERE id = " + userInput;
        Statement stmt = connection.createStatement();
        stmt.executeQuery(query);
    }
}