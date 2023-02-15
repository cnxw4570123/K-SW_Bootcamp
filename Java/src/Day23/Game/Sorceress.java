package Day23.Game;

public class Sorceress extends Character{
    public Sorceress() {
        hp = 300;
        mp = 550;
    }
    @Override
    public void info() {
        System.out.printf("""
                체력:%d
                지능:%d
                """, hp, mp);
    }
}
