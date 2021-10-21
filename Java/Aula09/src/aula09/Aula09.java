/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aula09;

/**
 *
 * @author Santos
 */
public class Aula09 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
    
        Pessoa[] p  = new Pessoa[2];
        Livro[] l = new Livro[3];
     
        p[0] = new Pessoa("Pedro", 22, "M");
        p[1] = new Pessoa("Mari", 25, "F");
        
        l[0] = new Livro("Aprendendo Java", "José da Silva", 300, p[0]);
        l[1] = new Livro("POO para Iniciantes", "Pedro Paulo", 500, p[1]);
        l[2] = new Livro("Java Avançado", "Maria Candido", 800, p[0]);
        
        System.out.println("Descrição: " + l[0].detalhes());
        System.out.println("Descrição: " + l[1].detalhes());
        System.out.println("Descrição: " + l[2].detalhes());
    }
}