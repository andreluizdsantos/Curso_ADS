//Andre Luiz dos Santos
import java.util.*;
import java.io.*;

public class Funcao extends Palavras
{
	private int i = 0;
	public int cont = 0;//contador de erros
	public int contr = 0;//contador de erro auxiliar
	public int contx = 0;//contador acertos por tentativa
	public int contf = 0;//contador acertos total
	private String auxChar = new String();//Sting para receber a letra digitada
	Random random = new Random(3);//funcao random para dar numeros aleatoriamente apartir de uma semente
	int j = random.nextInt(9);//inicia a variavel j com um numero aleatorio
	
	public void Jogo(BufferedReader b)//metodo jogo � chamado com uma variavel objeto
	{
		try	//teste
		{
			
			j = random.nextInt(9);
			System.out.println ("\t\t    *Forca*");
			System.out.println ("\n\t\t  __________");
			System.out.println ("\t\t  |        |");
			System.out.println ("\t\t           |");
			System.out.println ("\t\t           |");
			System.out.println ("\t\t           |");
			System.out.println ("\t\t           |");
			System.out.println ("\t\t           |");
			System.out.println ("\t\t___________|__");
			System.out.println ("\nPalavra sobre JAVA com: "+x[j]+" letras");
			cont = 0;//reseta contador erros para nova palavra
			contr = 0;//reseta contador se ja tem um erro para nova palavra
			contx = 0;//reseta contador acertos por tentativa para nova palavra
			contf = 0;//reseta contador acertos total para nova palavra
			do
			{
				System.out.println ("\nDigite uma letra:");
				auxChar = b.readLine();//leitura da letra digitada
				charac = auxChar.charAt(0);//convercao de String para char
				contx = 0;//inicia e reinicia contador de acertos por tentativa
				
				for(i = 0; i < x[j]; i ++)//for de zero ate a quantidade de letras da palavra
				{
					if(charac == palavra[i][j])//se a letra digitada for igual a uma das letras da palavra
					{
						if(confere[i][j] != charac)//para nao repitir acerto de uma mesma letra.
						{
							confere[i][j] = charac;//o vetor de caracteres recebera na mesma posicao a letra digitada
							contx +=1;//contador de acertos por tentativa recebe o valor dele mais um
							contf +=1;//contador acertos total recebe o valor dele mais um.
						}//fim do se
					}//fim do se
				}//fim do for
				if(contx==0||contr !=0)//se acerto igual a zero "ou" se o contador de erro auxiliar for diferente de 0
				{
					if(contx==0)//se nao teve nenhum acerto
					{
						erro[cont] = charac;//vetor de caracter recebe a letra digitada que nao tem na palavra
						cont+=1;//aumenta o contador de erros
					}//fim do se
					switch(cont)
					{
						case 1://caso seja o primeiro erro
							System.out.println ("\n\t\t  __________");
							System.out.println ("\t\t  |        |");
							System.out.println ("\t\t ( )       |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t___________|__");
							contr =1;//contador de erro auxiliar recebe 1.
							break;
						case 2://caso seja o segundo erro
							System.out.println ("\n\t\t  __________");
							System.out.println ("\t\t  |        |");
							System.out.println ("\t\t ( )       |");
							System.out.println ("\t\t  |        |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t___________|__");
							break;
						case 3://caso seja o terceiro erro
							System.out.println ("\n\t\t  __________");
							System.out.println ("\t\t  |        |");
							System.out.println ("\t\t ( )       |");
							System.out.println ("\t\t /|        |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t___________|__");
							break;
						case 4://caso seja o quarto erro
							System.out.println ("\n\t\t  __________");
							System.out.println ("\t\t  |        |");
							System.out.println ("\t\t ( )       |");
							System.out.println ("\t\t /|\\       |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t___________|__");
							break;
						case 5://caso seja o quinto erro
							System.out.println ("\n\t\t  __________");
							System.out.println ("\t\t  |        |");
							System.out.println ("\t\t ( )       |");
							System.out.println ("\t\t /|\\       |");
							System.out.println ("\t\t /         |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t___________|__");
							break;
						case 6://caso seja o sexto e ultimo erro
							System.out.println ("\n\t\t  __________");
							System.out.println ("\t\t  |        |");
							System.out.println ("\t\t ( )       |");
							System.out.println ("\t\t /|\\       |");
							System.out.println ("\t\t / \\       |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t           |");
							System.out.println ("\t\t___________|__");
							System.out.println ("\t\t Voce perdeu!\n");
							System.out.print ("A palavra e: \t\t");
							for(i = 0; i < x[j]; i ++)//for para imprimir a palavra completa
							{
								System.out.print (palavra[i][j]+" ");//imprime caracter por caracter
							}//fim do for
							break;
					}//fim do switch
				}//fim do se
				else//se acerto nao igual a zero "ou" se o contador de erro auxiliar nao for diferente de 0
				{
					if(contr==0)//caso na haja nenhum erro
					{
						System.out.println ("\n\t\t  __________");
						System.out.println ("\t\t  |        |");
						System.out.println ("\t\t           |");
						System.out.println ("\t\t           |");
						System.out.println ("\t\t           |");
						System.out.println ("\t\t           |");
						System.out.println ("\t\t           |");
						System.out.println ("\t\t___________|__");
					}//fim do se
				}//fim do senao
				if(contf == x[j])//se o contador de acertos totais for igual a quantidade de letras da palavra
					System.out.println ("\t\t Voce venceu!\n");
				if(cont<6)//se a quantidade de erros total for menor que 6 
				{
					System.out.print ("\nA palavra e: \t\t");
					for(i = 0; i < x[j]; i ++)//for para imprimir as letras acertadas
					{
						System.out.print (confere[i][j]+" ");//imprime caracter por caracter do vetor confere
					}//fim do for
				}//fim do se
				if(contr !=0)//se contador de erro auxiliar
				{
					System.out.print ("\n\nNao tem a(s) letra(s): \t");
					for(i = 0; i < cont; i ++)//for para imprimir as letras erradas
					{
						System.out.print (erro[i]+" ");//imprime caracter por caracter
					}//fim do for
				}//fim do se
				System.out.println ("\n");//pula linha
				
			}while(contf<x[j]&&cont<6);//fazer enquanto o contador de acertos for menor que a que a quantidade de letras "e" o contador de erros for menor que 6
			
		}//fim da teste
		catch (IOException e)//se erro no teste
		{
  			System.out.println ("Erro na entrada dos dados");
		}
	}//fim do metodo jogo
}//fim da classe funcao