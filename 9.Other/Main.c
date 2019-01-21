/* Question 2
#include<stdint.h>
#include<stdio.h>

typedef struct student {
	char name[50];
	int age;
	double GPA;
	char gradeLevel[50];
} student;

void showInfo(student zero) {
	printf("Information for ");
	printf(zero.name);
	printf(":\n	name: ");
	printf(zero.name);
	printf("\n	age: ");
	printf("%d", zero.age);
	printf("\n	GPA: ");
	printf("%.1f", zero.GPA);
	printf("\n	gradeLevel: ");
	printf(zero.gradeLevel);
	printf("\n");
}

void main() {
	student students[15] = { { "Lancelot",25,4.0,"master" },
	{ "Gawaine", 18, 3.8, "freshman" },
	{ "Geraint", 19, 3.4, "freshman" },
	{ "Gareth", 19, 3.5, "freshman" },
	{ "Galahad", 20, 3.2, "Sophomore" },
	{ "Gaheris", 19, 3.8, "Sophomore" },
	{ "Ganis", 20, 3.6, "Sophomore" },
	{ "Bedivere", 21, 3.2, "Sophomore" },
	{ "Kay", 23, 3.3, "Junior" },
	{ "Lamorak", 22, 3.7, "Junior" },
	{ "Percivale", 21, 3.8, "Junior" },
	{ "Tristan", 22, 3.8, "Junior" },
	{ "Dagonet", 23, 3.1, "Senior" },
	{ "Mordered", 22, 2.9, "Senior" },
	{ "Ector", 23, 4.0, "Senior" } };
	for (int i = 0; i < 15; i++) {
		showInfo(students[i]);
	}
	// I need system("pause") to show in my visual studio. You will not need it on codechef.
	//system("pause");
}
*/

#include<stdint.h>
#include<stdio.h>
#include<stdlib.h>

void showInfo(int studentId, char names[15][50], int* ages, double* GPAs, char gradeLevels[15][50]) {
	printf("Information for ");
	printf("%s:\n	name: ",names[studentId]);
	printf("%s", names[studentId]);
	printf("\n	age: ");
	printf("%d", ages[studentId]);
	printf("\n	GPA: ");
	printf("%.1f", GPAs[studentId]);
	printf("\n	gradeLevel: ");
	printf("%s", gradeLevels[studentId]);
	printf("\n");
}

void main() {
	char names[15][50] = { "Lancelot", "Gawaine","Geraint","Gareth","Galahad","Gaheris","Ganis",
		"Bedivere","Kay", "Lamorak","Percivale", "Tristan","Dagonet","Mordered", "Ector" };
	int ages[15] = { 25,18,19,19,20,19,20,21,23,22,21,22,23,22,23 };
	double GPAs[15] = { 4.0,3.8,3.4,3.5,3.2,3.8,3.6,3.2,3.3,3.7,3.8,3.8,3.1,2.9,4.0 };
	char gradeLevels[15][50] = { "master", "freshman" ,"freshman" ,"freshman","Sophomore" ,"Sophomore" ,"Sophomore" ,"Sophomore",
		"Junior" ,"Junior" ,"Junior" ,"Junior" ,"Senior" ,"Senior" ,"Senior" };
	for (int i = 0; i < 15; i++) {
		showInfo(i, names, ages, GPAs, gradeLevels);
	}
}
