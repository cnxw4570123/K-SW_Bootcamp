package Day23.Game;

public class Barbarian extends Character{
    public Barbarian() {
        hp = 1000;
        mp = 150;
    }

    @Override
    void info() {
        System.out.printf("""
                체력:%d
                지능:%d
                """, hp, mp);
    }
}
