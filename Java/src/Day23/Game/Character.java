package Day23.Game;

public abstract class Character {
    protected int hp;
    protected int mp;
    protected WeaponBehavior weapon; // Association(Aggregation)


    abstract void info();
    public void setWeapon(WeaponBehavior weapon) {
        this.weapon = weapon;
    }

    public final void performWeapon(){
        weapon.useWeapon();
    }
}
