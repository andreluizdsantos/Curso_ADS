//Andre Luiz dos Santos

import java.io.*;

public class Forca
{
	public static void main(String args[])
	{
		try	
		{
			int op = 0;//variavel que recebe opcao
			BufferedReader b = new BufferedReader (new InputStreamReader ( System.in ));//declaracao e inicializacao do objeto
			Funcao f = new Funcao();//constroi variavel f que recebe a funcao do jogo
			do
  			{
				System.out.println("\t\t**Jogo da Forca**\n\n1-Novo Jogo\n0-Sair");//imprime o menu
				op = Integer.parseInt(b.readLine());//leitura da opcao
				f.Criar();//chama o metodo criar
				switch(op)
				{
					case 1:
						f.Jogo(b);//chama o metodo jogo com a variavel objeto
						break;
					case 0:
	      				break;
	      			default:
	      				break;
	      		}
			}while(op != 0);//faca enquanto a opcao for diferente de 0
		}
		catch (IOException e)
		{
  			System.out.println ("Erro na entrada dos dados");
		}
	}
}