package Day23.Game;

public abstract class Character {
    protected int hp;
    protected int mp;
    protected WeaponBehavior weapon; // Association(Aggregation)


    public void info() {
        System.out.printf("""
                체력:%d
                지능:%d
                """, hp, mp);
    }
    public void setWeapon(WeaponBehavior weapon) {
        this.weapon = weapon;
    }

    public final void performWeapon(){
        weapon.useWeapon();
    }
}
