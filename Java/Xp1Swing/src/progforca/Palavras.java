package progforca;

//Andre Luiz dos Santos

public class Palavras
{
	private int i = 0;//contador letra
	public char charac;//variavel para comparacao
	public int a = 12;//implementador
	public char erro[] = new char[6];//vetor para armazenar letras nao presentes na palavra
	public int x[] = new int[a];//vetor que recebe todas as quantidades de letras das palavras
	public char palavra[][] = new char[14][a];//vetor de letras das palavras
	public char confere[][] = new char[14][a];//vetor para comparar e receber letras das palavras
	
	public void Criar()//metodo para criar a lista de palavras do jogo
	{
		x[0]=6;//quantidade de letras
		for(i = 0; i < x[0]; i ++)//for para inicializar o vetor que serve para a compara��o
		{
			confere[i][0] = '_';//inicializacao com um caracter que representa espaco no jogo
		}
		palavra[0][0] = 'c';//inicializa o vetor palavra
		palavra[1][0] = 'l';
		palavra[2][0] = 'a';
		palavra[3][0] = 's';
		palavra[4][0] = 's';
		palavra[5][0] = 'e';
		
		x[1]=6;
		for(i = 0; i < x[1]; i ++)
		{
			confere[i][1] = '_';
		}
		palavra[0][1] = 'm';
		palavra[1][1] = 'e';
		palavra[2][1] = 't';
		palavra[3][1] = 'o';
		palavra[4][1] = 'd';
		palavra[5][1] = 'o';
		
		x[2]=13;
		for(i = 0; i < x[2]; i ++)
		{
			confere[i][2] = '_';
		}
		palavra[0][2] = 'm';
		palavra[1][2] = 'o';
		palavra[2][2] = 'd';
		palavra[3][2] = 'i';
		palavra[4][2] = 'f';
		palavra[5][2] = 'i';
		palavra[6][2] = 'c';
		palavra[7][2] = 'a';
		palavra[8][2] = 'd';
		palavra[9][2] = 'o';
		palavra[10][2] = 'r';
		palavra[11][2] = 'e';
		palavra[12][2] = 's';
		
		x[3]=12;
		for(i = 0; i < x[3]; i ++)
		{
			confere[i][3] = '_';
		}
		palavra[0][3] = 'p';
		palavra[1][3] = 'o';
		palavra[2][3] = 'l';
		palavra[3][3] = 'i';
		palavra[4][3] = 'm';
		palavra[5][3] = 'o';
		palavra[6][3] = 'r';
		palavra[7][3] = 'f';
		palavra[8][3] = 'i';
		palavra[9][3] = 's';
		palavra[10][3] = 'm';
		palavra[11][3] = 'o';
		
		x[4]=7;
		for(i = 0; i < x[4]; i ++)
		{
			confere[i][4] = '_';
		}
		palavra[0][4] = 'h';
		palavra[1][4] = 'e';
		palavra[2][4] = 'r';
		palavra[3][4] = 'a';
		palavra[4][4] = 'n';
		palavra[5][4] = 'c';
		palavra[6][4] = 'a';
		
		x[5]=6;
		for(i = 0; i < x[5]; i ++)
		{
			confere[i][5] = '_';
		}
		palavra[0][5] = 'o';
		palavra[1][5] = 'b';
		palavra[2][5] = 'j';
		palavra[3][5] = 'e';
		palavra[4][5] = 't';
		palavra[5][5] = 'o';
		
		x[6]=8;
		for(i = 0; i < x[6]; i ++)
		{
			confere[i][6] = '_';
		}
		palavra[0][6] = 'a';
		palavra[1][6] = 't';
		palavra[2][6] = 'r';
		palavra[3][6] = 'i';
		palavra[4][6] = 'b';
		palavra[5][6] = 'u';
		palavra[6][6] = 't';
		palavra[7][6] = 'o';
		
		x[7]=7;
		for(i = 0; i < x[7]; i ++)
		{
			confere[i][7] = '_';
		}
		palavra[0][7] = 't';
		palavra[1][7] = 'h';
		palavra[2][7] = 'r';
		palavra[3][7] = 'e';
		palavra[4][7] = 'a';
		palavra[5][7] = 'd';
		palavra[6][7] = 's';
		
		x[8]=12;
		for(i = 0; i < x[8]; i ++)
		{
			confere[i][8] = '_';
		}
		palavra[0][8] = 'c';
		palavra[1][8] = 'o';
		palavra[2][8] = 'n';
		palavra[3][8] = 's';
		palavra[4][8] = 't';
		palavra[5][8] = 'r';
		palavra[6][8] = 'u';
		palavra[7][8] = 't';
		palavra[8][8] = 'o';
		palavra[9][8] = 'r';
		palavra[10][8] = 'e';
		palavra[11][8] = 's';
		
		x[9]=14;
		for(i = 0; i < x[9]; i ++)
		{
			confere[i][9] = '_';
		}
		palavra[0][9] = 'e';
		palavra[1][9] = 'n';
		palavra[2][9] = 'c';
		palavra[3][9] = 'a';
		palavra[4][9] = 'p';
		palavra[5][9] = 's';
		palavra[6][9] = 'u';
		palavra[7][9] = 'l';
		palavra[8][9] = 'a';
		palavra[9][9] = 'm';
		palavra[10][9] = 'e';
		palavra[11][9] = 'n';
		palavra[12][9] = 't';
		palavra[13][9] = 'o';
		
		x[10]=7;
		for(i = 0; i < x[10]; i ++)
		{
			confere[i][10] = '_';
		}
		palavra[0][10] = 'g';
		palavra[1][10] = 'e';
		palavra[2][10] = 't';
		palavra[3][10] = 't';
		palavra[4][10] = 'e';
		palavra[5][10] = 'r';
		palavra[6][10] = 's';

		x[11]=7;
		for(i = 0; i < x[11]; i ++)
		{
			confere[i][11] = '_';
		}
		palavra[0][11] = 's';
		palavra[1][11] = 'e';
		palavra[2][11] = 't';
		palavra[3][11] = 't';
		palavra[4][11] = 'e';
		palavra[5][11] = 'r';
		palavra[6][11] = 's';

	}//fim do metodo criar
}//fim da classe palavra
	