package Pokemon;

import java.util.Scanner;

public class Poke_main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true){
            System.out.print("num of pokemon instances  : " + Pokemon.getCount()+"\n1) generate new pokemon 2) quit: ");
            byte menu = sc.nextByte();
            if (menu == 2)
                break;
            else{
                System.out.print("1) Pickachu 2) Ggoboogi 3) Pairi : ");
                menu = sc.nextByte();
                sc.nextLine();
                System.out.print("Input Player Name: ");
                String owner = sc.nextLine();
                System.out.print("Input Skill List(Separate with '/'): ");
                String skill_list = sc.nextLine();

                Pokemon p = switch (menu){ // Upcasting each instance
                    case 1 -> {
                        yield new Pickachu(owner, skill_list);
                    }
                    case 2 ->{
                        yield new Ggoboogi(owner, skill_list);
                    }
                    case 3 ->{
                        yield new Pairi(owner, skill_list);
                    }
                    default -> {
                        System.out.println("Choose one among menu");
                        yield null;
                    }
                };

                if (p == null) continue;

                System.out.print("1) attack: ");
                byte info_atk = sc.nextByte();
                if (info_atk == 1){
                    p.info();
                    System.out.println("Select skill number: ");
                    menu = sc.nextByte();
                    try{
                        p.attack(menu);
                    }catch (IndexOutOfBoundsException e){
                        e.printStackTrace();
                    }
                } else{
                    System.out.println("There's no allocation for " + info_atk);
                }
            }
        }
        System.out.println("END");
    }
}
