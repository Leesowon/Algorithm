public class SavingAccount extends BankAccount{
    int sayAccount;

    public static void main(String[] args) {
        BankAccount account = new BankAccount();
//        account.changePW(12345);
        System.out.println(account.getAccountPw());
    }
}
