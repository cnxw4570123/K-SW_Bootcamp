import java.sql.*;
import java.util.List;

public class day29 {
    private static PreparedStatement pstmt;
    private static Connection conn;
    public static int insertSql() throws SQLException {
        class book{
            int id;
            String title;
            String publisher;
            String author;

            public book(int id, String title, String publisher, String author) {
                this.id = id;
                this.title = title;
                this.publisher = publisher;
                this.author = author;
            }

            public int getId() {
                return id;
            }

            public String getPublisher() {
                return publisher;
            }

            public String getAuthor() {
                return author;
            }

            public String getTitle() {
                return title;
            }
        }
        book b1 = new book(0, "harry Potter", "Bloomsbury", "J. K. Rowling");
        book b2 = new book(1, "The Lord of the Rings", "Allen & Unwin", "J. R. R. Tolkein");
        book b3 = new book(2, "Pride and Prejudice", "T. Egerton Kingdom", "Jane Austen");
        List<book> bookList = List.of(b1, b2, b3);

        conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/bookdb", "root", "12152294");

        return bookList.stream().mapToInt(book -> {
            try {
                pstmt = conn.prepareStatement("insert into book(id, title, publisher, author) values(?, ?, ?, ?)");
                pstmt.setInt(1,book.getId());
                pstmt.setString(2,book.getTitle());
                pstmt.setString(3,book.getPublisher());
                pstmt.setString(4,book.getAuthor());
                return pstmt.executeUpdate();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }).reduce(0, Integer::sum);
    }
    public static void main(String[] args) {
        System.out.println("JDBC Start");

        try (Connection conn = DriverManager.
                getConnection("jdbc:mysql://127.0.0.1:3306/bookdb?useSSL=false&serverTimeZone=Asia/Seoul", "root", "12152294")
        ) {
            if(conn != null){
//                System.out.println(insertSql());
                String sql = "select * from book";
                pstmt = conn.prepareStatement(sql);
                ResultSet rs = pstmt.executeQuery();

                while (rs.next()){
                    System.out.printf("%-2d\t %-20s\t %-20s\t %s\n", rs.getInt(1), rs.getString(2), rs.getString(3), rs.getString(4));
                }
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
