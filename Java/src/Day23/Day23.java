package Day23;

import Day23.Game.Axe;
import Day23.Game.Barbarian;
import Day23.Game.Bow;
import Day23.Game.Sorceress;

// diablo v0.5
public class Day23 {
    public static void main(String[] args) {
        Barbarian b1 = new Barbarian();
        Axe berserker = new Axe();
        Sorceress s1 = new Sorceress();
        Bow windForce = new Bow();
        s1.setWeapon(windForce);
        s1.performWeapon();

        b1.setWeapon(berserker);
        b1.performWeapon();

        s1.setWeapon(new Axe());
        s1.performWeapon();
        s1.info();
        b1.setWeapon(()-> System.out.println("신오브를 사용해 라이트닝 볼트를 시전합니다."));
        b1.performWeapon();
    }
}
