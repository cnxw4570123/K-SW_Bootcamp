package Day23.Game;

public class Bow implements WeaponBehavior{
    @Override
    public void useWeapon() {
        System.out.println("활을 사용해 화살을 날립니다.");
    }
}
