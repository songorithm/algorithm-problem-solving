// MORDOR
// Jaekyoung Kim(rlakim5521@naver.com)

import java.util.Scanner;

class minRMQ {
	int n;
	int[] rangeMin;
	
	public minRMQ(int[] array) {
		n = array.length;
		rangeMin = new int[4*n];
		init(array, 0, n-1, 1);
	}
	
	private int init(int[] array, int left, int right, int node) {
		if(left == right) {
			rangeMin[node] = array[left];
			return rangeMin[node];
		}
		
		int mid = (left + right) / 2;
		int leftMin = init(array, left, mid, node*2);
		int rightMin = init(array, mid+1, right, node*2+1);
		rangeMin[node] = Math.min(leftMin, rightMin);
		return rangeMin[node];
	}
	
	public int query(int left, int right) {
		return _query(left, right, 1, 0, n-1);
	}
	
	private int _query(int left, int right, int node, int nodeLeft, int nodeRight) {
		if(right < nodeLeft || nodeRight < left) {
			return Integer.MAX_VALUE;
		}
		if(left <= nodeLeft && nodeRight <= right) {
			return rangeMin[node];
		}
		int mid = (nodeLeft + nodeRight) / 2;
		return Math.min(_query(left,right,node*2,nodeLeft,mid), _query(left,right,node*2+1,mid+1,nodeRight));
	}
}

class maxRMQ {
	int n;
	int[] rangeMax;
	
	public maxRMQ(int[] array) {
		n = array.length;
		rangeMax = new int[4*n];
		init(array, 0, n-1, 1);
	}
	
	private int init(int[] array, int left, int right, int node) {
		if(left == right) {
			rangeMax[node] = array[left];
			return rangeMax[node];
		}
		
		int mid = (left + right) / 2;
		int leftMin = init(array, left, mid, node*2);
		int rightMin = init(array, mid+1, right, node*2+1);
		rangeMax[node] = Math.max(leftMin, rightMin);
		return rangeMax[node];
	}
	
	public int query(int left, int right) {
		return _query(left, right, 1, 0, n-1);
	}
	
	private int _query(int left, int right, int node, int nodeLeft, int nodeRight) {
		if(right < nodeLeft || nodeRight < left) {
			return Integer.MIN_VALUE;
		}
		if(left <= nodeLeft && nodeRight <= right) {
			return rangeMax[node];
		}
		int mid = (nodeLeft + nodeRight) / 2;
		return Math.max(_query(left,right,node*2,nodeLeft,mid), _query(left,right,node*2+1,mid+1,nodeRight));
	}
}

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int cases = sc.nextInt();
		while(cases-- > 0) {
			// Input
			int N = sc.nextInt();
			int Q = sc.nextInt();
			sc.nextLine();
			int [] h = new int[N];
			for (int iter = 0; iter < N; iter++) {
				h[iter] = sc.nextInt();
			}
			sc.nextLine();
			minRMQ min = new minRMQ(h);
			maxRMQ max = new maxRMQ(h);
			while(Q-- > 0) {
				int a = sc.nextInt();
				int b = sc.nextInt();
				// Output
				System.out.println(max.query(a, b) - min.query(a, b));
				sc.nextLine();
			}
		}
	}
}
