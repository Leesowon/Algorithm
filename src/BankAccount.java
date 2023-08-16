public class BankAccount {
    private int bankCode;
    private int account;
    private String owner;
    private int balance;
    private boolean isDormant;
    private int accountPw = 11111;

    void inquiry(){}
    void deposit(){}
    void withdraw(){}
    void heldInDormant(){}
    public void changePW(int pw){
        this.accountPw = pw;
    }

    BankAccount(){} // 기본 생성자
    BankAccount(int bankCode, int account, String owner, int balance, boolean isDormant, int accountPw){
        this.bankCode = bankCode;
        this.account = account;
    }

    public int getBankCode() {
        return bankCode;
    }

    public int getAccount() {
        return account;
    }

    public String getOwner() {
        return owner;
    }

    public int getBalance() {
        return balance;
    }

    public boolean isDormant() {
        return isDormant;
    }

    public int getAccountPw() {
        return accountPw;
    }
}
