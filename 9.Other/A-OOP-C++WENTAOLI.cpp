#include<iostream>
#include<vector>
#include<regex>
#include<set>
#include<unordered_set>
using namespace std;


class Student
{
public:
	string StudentFirstName;
	string StudentLastName;
	string StudentGNoss;

	Student(string SFN, string SLN, string SGN) {
		StudentFirstName = SFN;
		StudentLastName = SLN;
		StudentGNoss = SGN;
	}

	string getSFN() {
		return StudentFirstName;
	}

	string getSLN() {
		return StudentLastName;
	}

	string getSGN() {
		return StudentGNoss;
	}
};

//Student manager
class StudentManager
{
public:
	vector<Student> students;
	unordered_set<string> IDset;

	void insert(string SFN, string SLN, string SGN) {
		if (IDset.find(SGN) != IDset.end()) {
			cout << SGN << endl;
			IDset.insert(SGN);
			Student student = Student(SFN, SLN, SGN);
			students.push_back(student);
		}
		else {
			printf("warning: SGN duplicated!\n");
		}
	}

	// override
	void insert(Student student) {
		if (IDset.find(student.getSGN()) == IDset.end()) {
			IDset.insert(student.getSGN());
			students.push_back(student);
		}
		else {
			printf("warning: SGN duplicated!\n");
			cout <<"duplicated GNoss: " <<student.getSGN() << endl;
		}
	}

	// The find ID method without regex
	Student findStudent(string GNoss) {
		for (int i = 0; i < students.size(); i++) {
			if (students[i].getSGN() == GNoss) {
				return students[i];
			}
		}
		cout << "ID NOT FOUND!";
	}

	vector<Student> findStudents(string GNoss) {
		vector<Student> res;
		for (int i = 0; i < students.size(); i++) {
			string a = students[i].getSGN();
			regex b(GNoss);
			if (regex_match(a, b)) {
				res.push_back(students[i]);
			}
		}
		return res;
	}

	void removeStudents(string GNoss) {
		for (int i = 0; i < students.size(); i++) {
			string a = students[i].getSGN();
			regex b(GNoss);
			if (regex_match(a, b)) {
				students.erase(students.begin() + i);
				i -= 1;
			}
		}
	}

	void studentMatchCheck() {
		for (int i = 0; i < students.size(); i++) {
			Student curStudent = students[i];
			for (int j = i + 1; j < students.size(); j++) {
				// forward
				string a = students[j].getSFN();
				regex b(students[i].getSFN());
				string c = students[j].getSLN();
				regex d(students[i].getSLN());
				// backward
				string e = students[i].getSFN();
				regex f(students[j].getSFN());
				string g = students[i].getSLN();
				regex h(students[j].getSLN());
				if (regex_match(a, b) | regex_match(c, d)| regex_match(e,f) | regex_match(g,h)) {
					cout << "Match: (" << a << " " << c << ") (" << students[i].getSFN() << " " << students[i].getSLN() << ")" << endl;
				}
			}
		}
	}
};


int main() {
	StudentManager studentManager;
	// test cases
	Student a = Student("Tajea", "Shen", "G35");
	Student b = Student("Innovation", "Shen", "G36");
	Student c = Student("Soo", "Ya", "G33");
	Student d = Student("Byun", "Wei", "G32");
	Student e = Student("So.+", "Money", "G31");
	Student f = Student("hero.+", "Sao", "G44");
	Student g = Student("heroMarine", "MoneyNone", "G45");
	Student h = Student("Innovation", "ShenLuBu", "G49");
	Student i = Student("Arthur", "ExCalliber", "G99");
	Student j = Student("Mordred", "ExClarent", "G30");
	Student k = Student("MordredFaker", "ExClarent", "G30");
	// Mission 1: Insert new students a-k
	studentManager.insert(a);
	studentManager.insert(b);
	studentManager.insert(c);
	studentManager.insert(d);
	studentManager.insert(e);
	studentManager.insert(f);
	studentManager.insert(g);
	studentManager.insert(h);
	studentManager.insert(i);
	studentManager.insert(j);
	studentManager.insert(k);
	// insert k is rejected due to duplicate G ID
	printf("\nInsertion complete.\n\n");
	vector<Student> p = studentManager.findStudents("G3.");
	// print all students with GNoss in G3. regex format
	cout << "G3. students:" << endl;
	for (Student student : p) {
		cout << student.getSFN().c_str() << endl;
	}
	printf("\nStudent finding complete.\n\n");
	// check match
	studentManager.studentMatchCheck();
	printf("\nStudent matching complete.\n\n");
	// Remove student checking
	cout << "Before removing." << endl;
	vector<Student> G3 = studentManager.findStudents("G3.");
	for (Student student : G3) {
		cout << "Finding G3.: " << student.getSFN() << " " << student.getSLN() << endl;
	}
	// Remove all G3. regex student
	studentManager.removeStudents("G3.");
	cout << "After removing." << endl;
	vector<Student> G3aft = studentManager.findStudents("G3.");
	for (Student student : G3aft) {
		cout << "Finding G3.: " << student.getSFN() << " " << student.getSLN() << endl;
	}
	system("pause");
}

