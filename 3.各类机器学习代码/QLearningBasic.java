package mdp;

import java.io.*;
import java.text.DecimalFormat;
import java.util.*;


public class Grid {
	
	String[][] grid; 			//the grid
	double[][] current=null; 	//the result V*value
	double[][] previous=null;	//the previous V* value used to calculate the next iterator
	String[][] solution;		// the grid store the solution
	
	public static void main(String[] args) throws IOException {
		DecimalFormat df2 = new DecimalFormat("###0.00");				// the format of the printed double
		Grid g=new Grid();
		g.iterator();
		System.out.println();
		//print the grid
		System.out.println("The grid is:");
		for(int i=0;i<16;i++) {
			for(int j=0;j<6;j++) {
				System.out.print(g.grid[i][j]);
				System.out.print("\t");
			}
			System.out.print("\n");
		}
		//print the V* values
		System.out.print("\n");
		System.out.println("The V* is:");
		for(int i=0;i<16;i++) {
			for(int j=0;j<6;j++) {
				if(g.grid[i][j].equals("0")) {
					System.out.print(df2.format(g.current[i][j]));			
				}else {
					System.out.print(g.grid[i][j]);
				}
				System.out.print("\t");
			}
			System.out.print("\n");
		}
		//print the solution
		System.out.print("\n");
		System.out.println("The solution is:");
		for(int i=0;i<16;i++) {
			for(int j=0;j<6;j++) {
				if(g.grid[i][j].equals("0")) {
					System.out.print(g.solution[i][j]);				
				}else {
					System.out.print(g.grid[i][j]);
				}
				System.out.print("\t");
			}
			System.out.print("\n");
		}
	}
	
	/**
	 * Initialize the class
	 * @throws IOException the file may not exist, and may not be read
	 */
	public Grid() throws IOException {
		grid=fileRead();
		solution=new String[16][6];
		previous=new double[16][6];
	}
	
	/**
	 * read file
	 * @return return the grid in which "0" means empty cells, "1000 or -800" means the final cell, and "-" means wall;
	 * @throws IOException
	 */
	public String[][] fileRead() throws IOException {
	//	String filePath="C:\\Users\\wrtfo\\OneDrive - The George Washington University\\Textbooks & Course Materials\\AI\\Assignments\\Project 4\\Part 1\\gridA.1.csv";;
		//read path from console
		System.out.print("Please type the file path: ");
		@SuppressWarnings("resource")
		Scanner sc=new Scanner(System.in);
		String filePath=sc.nextLine();
			

		//read file
		FileReader fr=new FileReader(filePath);
		@SuppressWarnings("resource")
		BufferedReader br=new BufferedReader(fr);
		String[][] grid=new String[16][6];
		String line;
		int i=0;
		while((line=br.readLine())!=null) {
			String[] elements=line.split(",");
			for(int j=0;j<6;j++) {
				grid[i][j]=elements[j];
			}
			i++;
			//System.out.println(line);
		}
		//System.out.println();
		return grid;
	}
	
	/**
	 * the iterator
	 */
	private void iterator() {
		@SuppressWarnings("resource")
		Scanner sc=new Scanner(System.in);
		System.out.print("The number of interations:");
		int iterations=Integer.parseInt(sc.nextLine());
		int iterator=0;
		while(iterator<iterations) {
			if(current==null) {
				initializeCurrent();						//if the current state is null, then initialize the grid based on the final state
			}else {
				
				for(int i=0;i<16;i++) {
					for(int j=0;j<6;j++) {
						if(grid[i][j].equals("0")) {		//if the cell is not a wall, then calculate the V* value
							getVStar(i, j);
						}
					}
				}
			}
			copy();											//store the result into "previous"
			iterator++;
		}
	}
	
	/**
	 * Initialize the V* value based on the final state
	 */
	public void initializeCurrent() {
		current=new double[16][6];
		for(int i=0;i<16;i++) {
			for(int j=0;j<6;j++) {
				if(grid[i][j].equals("0")||grid[i][j].equals("-")) {
					current[i][j]=-0.01;
					solution[i][j]="N";
				}else {
					current[i][j]=Integer.parseInt(grid[i][j]);
					solution[i][j]=grid[i][j];
					}
			}
		}
	}
	
	/**
	 * calculate the V* value for a cell;
	 * @param i
	 * @param j
	 */
	public void getVStar(int i, int j) {
		//get the V* of the cells located in the above, below, left and right
		double nCell=getN(i,j),wCell=getW(i,j),eCell=getE(i,j),sCell=getS(i,j);
		//the Q-value when the move is N,W,E,S
		double goN,goW,goE,goS;
		//the V* value
		double max;
		//the solution
		String solu;
		
		//calculate the Q-value
		goN=(0.65*nCell+0.15*eCell+0.15*wCell+0.05*sCell)*0.9-0.01;
		goW=(0.65*wCell+0.15*nCell+0.15*sCell+0.05*eCell)*0.9-0.01;
		goS=(0.65*sCell+0.15*eCell+0.15*wCell+0.05*nCell)*0.9-0.01;
		goE=(0.65*eCell+0.15*nCell+0.15*sCell+0.05*wCell)*0.9-0.01;
		
		//compare each V-value and get the maximum value
		max=goN; solu="N";
		if(goW>max) {max=goW; solu="W";}
		if(goS>max) {max=goS; solu="S";}
		if(goE>max) {max=goE; solu="E";}
		
		//store it in current and solution
		current[i][j]=max;
		solution[i][j]=solu;
		
	}
	
	/**
	 * Copy the data from current to previous
	 */
	private void copy() {
		for(int i=0;i<16;i++) {
			for(int j=0;j<6;j++) {
				previous[i][j]=current[i][j];
			}
		}
	}
	
	/**
	 * get the V* value of the cell above the current cell
	 * @param i the row number of current cell
	 * @param j the column number of current cell
	 * @return the V* value of the cell above the current cell
	 */
	private double getN(int i,int j) {
		double N;
		//If the cell above the current cell is exist and not a wall
		//then return the V* value of cell above the current cell
		//else return the current cell's V* value
		if(i>0 && !this.grid[i-1][j].equals("-")){
			N=previous[i-1][j];
		}else {
			N=previous[i][j];
		}
		return N;
	}
	
	/**
	 * get the V* value of the cell on the left of the current cell
	 * @param i the row number of current cell
	 * @param j the column number of current cell
	 * @return the V* value of the cell on the left of the current cell
	 */
	private double getW(int i,int j) {
		//If the cell on the left of the current cell is exist and not a wall
		//then return the V* value of cell on the left of the current cell
		//else return the current cell's V* value
		double W;
		if(j>0 && !this.grid[i][j-1].equals("-")){
			W=previous[i][j-1];
		}else {
			W=previous[i][j];
		}
		return W;	
	}
	
	/**
	 * get the V* value of the cell on the right of the current cell
	 * @param i the row number of current cell
	 * @param j the column number of current cell
	 * @return the V* value of the cell on the right of the current cell
	 */
	private double getE(int i,int j) {
		//If the cell on the right of the current cell is exist and not a wall
		//then return the V* value of cell on the right of the current cell
		//else return the current cell's V* value
		double E;
		if(j<5 && !this.grid[i][j+1].equals("-")){
			E=previous[i][j+1];
		}else {
			E=previous[i][j];
		}
		return E;
		
	}
	
	/**
	 * get the V* value of the cell below the current cell
	 * @param i the row number of current cell
	 * @param j the column number of current cell
	 * @return the V* value of the cell below the current cell
	 */
	private double getS(int i,int j) {
		double S;
		//If the cell below the current cell is exist and not a wall
		//then return the V* value of cell below the current cell
		//else return the current cell's V* value
		if(i<15 && !this.grid[i+1][j].equals("-")){
			S=previous[i+1][j];
		}else {
			S=previous[i][j];
		}
		return S;
	}

}
