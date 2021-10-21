/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package teste;

/**
 *
 * @author Santos
 */
public class Teste {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int i;
        String palavras = "palavra";
        char palavrac[] = new char[7];
        palavras.split(palavras);
        palavrac = palavras.toCharArray();
        System.out.println(palavras);
        for(i = 0; i < palavrac.length; i ++){
            System.out.println(palavrac[i]);
        }
    }
    
}
