package Day16;

public class Node {
    public String data;
    public Node link;

    public Node(){
    }

    public Node(String data){
        this.data = data;
        this.link = null;
    }

    @Override
    public String toString() {
        return "해당 노드의 데이터는 "+ this.data +"입니다";
    }
}
