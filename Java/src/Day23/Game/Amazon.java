package Day23.Game;

public class Amazon extends Character{
    public Amazon() {
        hp = 700;
        mp = 250;
    }

    @Override
    void info() {
        System.out.printf("""
                체력:%d
                지능:%d
                """, hp, mp);
    }
}
