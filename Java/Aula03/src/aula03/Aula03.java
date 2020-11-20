package aula03;

public class Aula03 {
    public static void main(String[] args) {
        Caneta c1 = new Caneta();
        c1.modelo = "Esferográfica";
        c1.cor = "azul";
        //c1.ponta = 0.5f;
        c1.destampar();
        c1.status();
        c1.rabiscar();
        Caneta c2 = new Caneta();
        c2.modelo = "Tinteiro";
        c2.cor = "Preta";
        c2.carga = 100;
        c2.tampar();
        c2.status();
        c2.rabiscar();
    }
    
}
