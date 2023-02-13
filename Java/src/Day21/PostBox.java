package Day21;

public class PostBox<T> {
    private T item;

    public PostBox() {
    }

    public PostBox(T item) {
        this.item = item;
    }

    public T getItem() {
        return item;
    }

    public void setItem(T item) {
        this.item = item;
    }
}
