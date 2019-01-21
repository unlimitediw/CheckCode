#include<iostream>
#include<vector>
#include<unordered_map>

using namespace std;

class Solution {
public:
	vector<int> twoSum(vector<int>& nums, int target) {
		vector<int> res;
		unordered_map<int, int> h;
		for (int i = 0; i < nums.size(); ++i) {
			const auto it = h.find(target - nums.at(i));
			if (it != h.cend()) {
				res.push_back(it->second);
				res.push_back(i);
				break;
			}
			h[nums.at(i)] = i;
		}
		return res;
	}

	ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
	{
		vector<int> carryVector = turnToVector(l1, l2);
		carryOn(carryVector);
		return buildNode(carryVector);
	}

	vector<int> turnToVector(ListNode* l1, ListNode* l2)
	{
		vector<int> returnVector;
		int sum = 0;
		while (!((l1 == nullptr) && (l2 == nullptr)))
		{
			if (l1 != nullptr) {
				sum += l1->val;
				l1 = l1->next;
			}
			if (l2 != nullptr) {
				sum += l2->val;
				l2 = l2->next;
			}
			returnVector.push_back(sum);
			sum = 0;
		}
		return returnVector;
	}

	void carryOn(vector<int> &turn) {
		for (int i = 0; i < turn.size(); i++) {
			if (turn[i] >= 10) {
				turn[i] = turn[i] - 10;
				if (i + 1 >= turn.size()) turn.push_back(1);
				else turn[i + 1] += 1;
			}
		}
	}

	ListNode* buildNode(vector<int> result)
	{
		ListNode *head{ nullptr }, *tail{ nullptr };
		for (int i : result) {
			if (head != nullptr) {
				tail->next = new ListNode(i);
				tail = tail->next;
			}
			else {
				head = new ListNode(i);
				tail = head;
			}
		}
		return head;
	}
};