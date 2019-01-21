#include "20181022.h"

#include<iostream>
using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

Solution thisSolution;


int main() {


	// leetcode 1
	cout << "leetcode No.1 problem:" << endl;
	vector<int> intList = vector<int>();
	for (int i = 0; i < 10; i++) {
		intList.push_back(i);
	}
	vector<int> res = thisSolution.twoSum(intList, 5);
	for (int i = 0; i < res.size(); i++) {
		cout << res.at(i) << endl;
	}
	cout << "problem finished." << endl << endl;

	// leetcode 2
	cout << "leetcode No.2 problem:" << endl;
	ListNode node1 = ListNode(2);
	ListNode node2 = ListNode(5);
	ListNode resNode = *thisSolution.addTwoNumbers(&node1, &node2);
	cout << "problem finished." << endl << endl;
	

	system("pause");
}