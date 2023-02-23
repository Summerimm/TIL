public class Menu {
    // Field
    String name;
    int cost;
    String category;

    // Constructor
    Menu(String name, int cost, String category){
        this.name = name;
        this.cost = cost;
        this.category = category;
    }

    // Method
    public void printMenuName(){
        System.out.println("메뉴 이름: " + name);
        System.out.println("메뉴 가격: " + cost + "원");
        System.out.println("카테고리: " + category);
    }

    public void addMenu(){

    }
}
