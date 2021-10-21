/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package xp1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 * @author Santos
 */
public class XP1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        int i = 0;//contador coluna
	int j = 0;//contador linha
	int cont = 0;//contador erros
	int contr = 0;//contador se ja tem um erro
	int contx = 0;//contador acertos por tentativa
	int contf = 0;//contador acertos total
	char palavo[] = new char[6];
	char palavc[] = new char[6];
	char charac;
	//Random x = new Random();
	//j = x.nextInt(11);
	for(i = 0; i < 6; i ++)
	{
		palavc[i] = '_';
	}
	palavo[0] = 'c';
	palavo[1] = 'l';
	palavo[2] = 'a';
	palavo[3] = 's';
	palavo[4] = 's';
	palavo[5] = 'e';
	i=6;
	String auxChar = new String();
	try	
	{
		BufferedReader b = new BufferedReader (new InputStreamReader ( System.in ));
		System.out.println ("\t    *Forca*");
		System.out.println ("\n\t  __________");
		System.out.println ("\t  |        |");
		System.out.println ("\t  |        |");
		System.out.println ("\t           |");
		System.out.println ("\t           |");
		System.out.println ("\t           |");
		System.out.println ("\t___________|_");
		System.out.println ("\nSobre JAVA com: "+i+" letras");
		do
		{
			System.out.println ("\nDigite uma letra:");
			auxChar = b.readLine();
			charac = auxChar.charAt(0);
			contx = 0;
			for(i = 0; i < 6; i ++)
			{
				if(charac==palavo[i])
				{
					palavc[i] = charac;
					contx +=1;
					contf +=1;
					System.out.print (palavc[i]);
				}
				else
				{
					System.out.print (palavc[i]);
				}
			}
			if(contx==0||contr !=0)
			{
				if(contx==0)
				{
					cont+=1;
				}
				switch(cont)
				{
					case 1:
						System.out.println ("\n\t  __________");
						System.out.println ("\t  |        |");
						System.out.println ("\t ( )       |");
						System.out.println ("\t           |");
						System.out.println ("\t           |");
						System.out.println ("\t           |");
						System.out.println ("\t___________|_");
						contr =1;
						break;
					case 2:
						System.out.println ("\n\t  __________");
						System.out.println ("\t  |        |");
						System.out.println ("\t ( )       |");
						System.out.println ("\t  |        |");
						System.out.println ("\t           |");
						System.out.println ("\t           |");
						System.out.println ("\t___________|_");
						break;
					case 3:
						System.out.println ("\n\t  __________");
						System.out.println ("\t  |        |");
						System.out.println ("\t ( )       |");
						System.out.println ("\t /|        |");
						System.out.println ("\t           |");
						System.out.println ("\t           |");
						System.out.println ("\t___________|_");
						break;
					case 4:
						System.out.println ("\n\t  __________");
						System.out.println ("\t  |        |");
						System.out.println ("\t ( )       |");
						System.out.println ("\t /|\\       |");
						System.out.println ("\t           |");
						System.out.println ("\t           |");
						System.out.println ("\t___________|_");
						break;
					case 5:
						System.out.println ("\n\t  __________");
						System.out.println ("\t  |        |");
						System.out.println ("\t ( )       |");
						System.out.println ("\t /|\\       |");
						System.out.println ("\t /         |");
						System.out.println ("\t           |");
						System.out.println ("\t___________|_");
						break;
					case 6:
						System.out.println ("\n\t  __________");
						System.out.println ("\t  |        |");
						System.out.println ("\t ( )       |");
						System.out.println ("\t /|\\       |");
						System.out.println ("\t / \\       |");
						System.out.println ("\t           |");
						System.out.println ("\t___________|_");
						System.out.println ("\tVoce perdeu!\n");
						break;
				}
			}
			else
			{
				if(contr==0)
				{
					System.out.println ("\n\t  __________");
					System.out.println ("\t  |        |");
					System.out.println ("\t  |        |");
					System.out.println ("\t           |");
					System.out.println ("\t           |");
					System.out.println ("\t           |");
					System.out.println ("\t___________|_");
				}
			}
			if(contf == 6)
				System.out.println ("\tVoce venceu!\n");
		}while(contf<6&&cont<6);
	}
	catch (IOException e)
	{
  		System.out.println ("Erro na entrada dos dados");
        }      
    }    
}
